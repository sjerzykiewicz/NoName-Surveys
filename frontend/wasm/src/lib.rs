use rsa::traits::{PrivateKeyParts, PublicKeyParts};
use sha2::Digest;
use wasm_bindgen::prelude::*;
use rsa::{RsaPrivateKey, RsaPublicKey};
use rsa::pkcs1::{EncodeRsaPrivateKey, EncodeRsaPublicKey, DecodeRsaPrivateKey, DecodeRsaPublicKey};
use num_bigint_dig::algorithms::div_rem;
use num_bigint_dig::{BigUint, RandomBits};
use num_traits::One;
use rand::Rng;

// import Javascript's alert method to Rust
#[wasm_bindgen]
extern "C" {
    fn alert(s: &str);
}

#[wasm_bindgen]
pub struct KeyPair {
    private_key: String,
    public_key: String,
}

#[wasm_bindgen]
impl KeyPair {
    pub fn get_public_key(&self) -> String {
        self.public_key.clone()
    }

    pub fn get_private_key(&self) -> String {
        self.private_key.clone()
    }
}

#[wasm_bindgen]
pub fn get_keypair() -> KeyPair {
    let mut rng = rand::thread_rng();
    let bits = 2048;
    let priv_key = RsaPrivateKey::new(&mut rng, bits).expect("failed to generate a key");
    let pub_key = RsaPublicKey::from(&priv_key);
    let private_pem = priv_key.to_pkcs1_pem(rsa::pkcs1::LineEnding::LF).expect("failed to convert to pem");
    let public_pem = pub_key.to_pkcs1_pem(rsa::pkcs1::LineEnding::LF).expect("failed to convert to pem");

    return KeyPair {
        private_key: private_pem.to_string(),
        public_key: public_pem,
    };
}

#[wasm_bindgen]
pub struct Ring {
    pub_keys: Vec<RsaPublicKey>,
    priv_key : RsaPrivateKey,
    priv_key_index: u32,
    bit_length: u32,
    num_keys: usize,
    q_value: BigUint,
    permutation: BigUint,
}

#[wasm_bindgen]
impl Ring {
    pub fn new(pub_keys: Vec<String>, priv_key: String, priv_key_index: u32, bit_length: u32) -> Ring {
        let num_keys = pub_keys.len();
        let q_value = BigUint::one() << ((bit_length as usize) - 1);

        let mut keys = Vec::new();

        for key in &pub_keys {
            let rsa_key = RsaPublicKey::from_pkcs1_pem(&key).unwrap();
            keys.push(rsa_key);
        }

        let priv_key = RsaPrivateKey::from_pkcs1_pem(&priv_key).unwrap();

        Ring {
            pub_keys: keys,
            priv_key,
            priv_key_index,
            bit_length,
            num_keys,
            q_value: q_value.into(),
            permutation: BigUint::default(),
        }
    }

    fn compute_permutation(&mut self, message: &str) {
        let mut hasher = sha2::Sha384::new();
        hasher.update(message.as_bytes());
        let result = hasher.finalize();
        self.permutation = BigUint::from_bytes_be(&result);
    }

    fn compute_e(&self, x: &BigUint) -> BigUint {
        let input = format!("{}{}", x, self.permutation);
        let mut hasher = sha2::Sha384::new();
        hasher.update(input.as_bytes());
        BigUint::from_bytes_be(&hasher.finalize())
    }

    fn compute_g(&self, x: &BigUint, e: &BigUint, n: &BigUint) -> BigUint {
        let (quotient, remainder) = div_rem(x, n);
        let result = remainder.modpow(e, n);
        let n_quotient = quotient.clone();
        if (n_quotient + 1u8) * n <= (BigUint::one() << self.bit_length as usize) - 1u8 {
            quotient * n + result
        } else {
            x.clone()
        }
    }

    #[wasm_bindgen]
    pub fn sign(&mut self, message: &str) -> Vec<String> {
        let mut rng = rand::thread_rng();
        self.compute_permutation(message);
        let n = self.num_keys;
        let mut signatures: Vec<BigUint> = Vec::new();
        let z = self.priv_key_index;
        let u: BigUint = rng.sample(RandomBits::new(self.q_value.bits()));
        let new_val = self.compute_e(&u);
        let mut c = new_val.clone();
        let mut v = new_val.clone();

        for i in z..(n as u32) {
            let sig:BigUint = rng.sample(RandomBits::new(self.q_value.bits()));
            signatures.push(sig.clone());
            let e = self.compute_g(&sig, self.pub_keys[i as usize].e(), self.pub_keys[i as usize].n());
            v = self.compute_e(&(v.clone() ^ e.clone())).clone();
            c = v.clone();
        }
        for i in 0..z {
            let sig:BigUint = rng.sample(RandomBits::new(self.q_value.bits()));
            signatures.push(sig.clone());
            let e = self.compute_g(&sig, self.pub_keys[i as usize].e(), self.pub_keys[i as usize].n());
            v = self.compute_e(&(v.clone() ^ e.clone())).clone();
        }

        let priv_big = self.compute_g(&(v.clone() ^ u.clone()), &self.priv_key.d(), &self.priv_key.n());

        let mut sign_str: Vec<String> = Vec::new();
        sign_str.push(c.to_string());
        for i in 0..z {
            sign_str.push(signatures[i as usize].to_string());
        }
        sign_str.push(priv_big.to_string());
        for i in z..(n as u32) {
            sign_str.push(signatures[i as usize].to_string());
        }

        sign_str
    }

}
