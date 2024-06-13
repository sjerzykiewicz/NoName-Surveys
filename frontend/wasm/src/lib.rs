use num_bigint_dig::algorithms::div_rem;
use num_bigint_dig::{BigUint, RandomBits};
use num_traits::{One, Zero};
use rand::Rng;
use rsa::pkcs1::{
    DecodeRsaPrivateKey, DecodeRsaPublicKey, EncodeRsaPrivateKey, EncodeRsaPublicKey,
};
use rsa::traits::{PrivateKeyParts, PublicKeyParts};
use rsa::{RsaPrivateKey, RsaPublicKey};
use sha2::Digest;
use wasm_bindgen::prelude::*;

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
pub fn get_keypair() -> Result<KeyPair, JsValue> {
    let mut rng = rand::thread_rng();
    let bits = 2048;

    let priv_key = match RsaPrivateKey::new(&mut rng, bits) {
        Ok(key) => key,
        Err(_) => return Err(JsValue::from_str("Failed to generate a key.")),
    };

    let pub_key = RsaPublicKey::from(&priv_key);

    let private_pem = match priv_key.to_pkcs1_pem(rsa::pkcs1::LineEnding::LF) {
        Ok(k) => k,
        Err(_) => return Err(JsValue::from_str("Failed to export private key.")),
    };
    let public_pem = match pub_key.to_pkcs1_pem(rsa::pkcs1::LineEnding::LF) {
        Ok(k) => k,
        Err(_) => return Err(JsValue::from_str("Failed to export public key.")),
    };

    Ok(KeyPair {
        private_key: private_pem.to_string(),
        public_key: public_pem,
    })
}

#[wasm_bindgen]
pub struct Ring {
    pub_keys: Vec<RsaPublicKey>,
    priv_key: RsaPrivateKey,
    priv_key_index: u32,
    bit_length: u32,
    num_keys: usize,
    q_value: BigUint,
    permutation: BigUint,
}

#[wasm_bindgen]
impl Ring {
    pub fn new(
        pub_keys: Vec<String>,
        priv_key: String,
        priv_key_index: u32,
        bit_length: u32,
    ) -> Result<Ring, JsValue> {
        let num_keys = pub_keys.len();
        let q_value = BigUint::one() << ((bit_length as usize) - 1);

        let mut keys = Vec::new();

        for key in &pub_keys {
            let rsa_key = match RsaPublicKey::from_pkcs1_pem(&key) {
                Ok(k) => k,
                Err(_) => return Err(JsValue::from_str("Public key could not be processed.")),
            };
            keys.push(rsa_key);
        }

        let priv_key = match RsaPrivateKey::from_pkcs1_pem(&priv_key) {
            Ok(k) => k,
            Err(_) => return Err(JsValue::from_str("Private key could not be processed.")),
        };

        Ok(Ring {
            pub_keys: keys,
            priv_key,
            priv_key_index,
            bit_length,
            num_keys,
            q_value: q_value.into(),
            permutation: BigUint::default(),
        })
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
        let mut signatures: Vec<BigUint> = vec![BigUint::zero(); n];
        let z = self.priv_key_index;
        let u: BigUint = rng.sample(RandomBits::new(self.q_value.bits()));
        let mut v = self.compute_e(&u);
        let mut sign_str: Vec<String> = Vec::new();

        for i in z..(n as u32) {
            signatures[i as usize] = rng.sample(RandomBits::new(self.q_value.bits()));
            let e = self.compute_g(
                &signatures[i as usize],
                self.pub_keys[i as usize].e(),
                self.pub_keys[i as usize].n(),
            );
            let x = v ^ e;
            v = self.compute_e(&x);
        }

        sign_str.push(v.to_string());

        for i in 0..z {
            signatures[i as usize] = rng.sample(RandomBits::new(self.q_value.bits()));
            let e = self.compute_g(
                &signatures[i as usize],
                self.pub_keys[i as usize].e(),
                self.pub_keys[i as usize].n(),
            );
            let x = v ^ e;
            v = self.compute_e(&x);
        }

        let x = v ^ u;
        let priv_big = self.compute_g(&x, &self.priv_key.d(), &self.priv_key.n());

        for i in 0..z {
            sign_str.push(signatures[i as usize].to_string());
        }
        sign_str.push(priv_big.to_string());
        for i in z..(n as u32) {
            sign_str.push(signatures[i as usize].to_string());
        }
        sign_str
    }

    #[wasm_bindgen]
    pub fn compute_y0(&self, public_key: String, private_key: String) -> Result<String, JsValue> {
        let mut hasher = sha2::Sha384::new();
        hasher.update(public_key.as_bytes());
        let pub_key_hashed = hasher.finalize();

        let priv_key = match RsaPrivateKey::from_pkcs1_pem(&private_key) {
            Ok(k) => k,
            Err(_) => return Err(JsValue::from_str("Private key could not be processed.")),
        };

        let y0 = BigUint::from_bytes_be(&pub_key_hashed).modpow(priv_key.d(), priv_key.n());

        Ok(y0.to_string())
    }
}
