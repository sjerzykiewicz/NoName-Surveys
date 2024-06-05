use rand::Rng;
use rsa::{RsaPrivateKey, RsaPublicKey};
use sha2::{Sha384, Digest};
use num_bigint::{BigUint, RandBigInt};
use num_traits::One;
use std::str::FromStr;

#[wasm_bindgen]
pub struct Ring {
    keys: Vec<RsaPublicKey>,
    bit_length: usize,
    num_keys: usize,
    q_value: BigUint,
    permutation: BigUint,
}

#[wasm_bindgen]
impl Ring {
    pub fn new(keys: Vec<RsaPublicKey>, bit_length: usize) -> Ring {
        let num_keys = keys.len();
        let q_value = BigUint::one() << (bit_length - 1);

        Ring {
            keys,
            bit_length,
            num_keys,
            q_value,
            permutation: BigUint::zero(),
        }
    }

    fn compute_permutation(&mut self, message: &str) {
        let mut hasher = Sha384::new();
        hasher.update(message.as_bytes());
        let result = hasher.finalize();
        self.permutation = BigUint::from_bytes_be(&result);
    }

    fn compute_E(&self, x: &BigUint) -> BigUint {
        let input = format!("{}{}", x, self.permutation);
        let mut hasher = Sha384::new();
        hasher.update(input.as_bytes());
        BigUint::from_bytes_be(&hasher.finalize())
    }

    fn compute_g(&self, x: &BigUint, e: &BigUint, n: &BigUint) -> BigUint {
        let (quotient, remainder) = (x / n, x % n);
        let result = remainder.modpow(e, n);
        if (quotient + 1u8) * n <= (BigUint::one() << self.bit_length) - 1u8 {
            quotient * n + result
        } else {
            x.clone()
        }
    }

    pub fn sign(&mut self, m: &str, z: usize) -> Vec<BigUint> {
        self.compute_permutation(m);
        let mut s: Vec<BigUint> = vec![BigUint::zero(); self.num_keys];
        let mut rng = rand::thread_rng();
        let u: BigUint = rng.gen_biguint(self.bit_length - 1);
        let mut c: BigUint = self.compute_E(&u);
        let mut v = c.clone();

        let mut whole_range: Vec<usize> = ((z + 1)..self.num_keys).collect();
        whole_range.extend(0..z);

        for i in whole_range {
            s[i] = rng.gen_biguint(self.bit_length - 1);
            let e = self.compute_g(&s[i], &self.keys[i].e().unwrap().to_biguint().unwrap(), &self.keys[i].n().to_biguint().unwrap());
            v = self.compute_E(&(v ^ e));
            if (i + 1) % self.num_keys == 0 {
                c = v.clone();
            }
        }

        // Assuming that self.keys[z] is a private key (RsaPrivateKey)
        // If not, you will need to pass the private key separately
        let priv_key = RsaPrivateKey::new(&mut rng, self.bit_length).expect("Failed to generate private key");
        s[z] = self.compute_g(&(v ^ u), &priv_key.d().to_biguint().unwrap(), &priv_key.n().to_biguint().unwrap());

        let mut result = vec![c];
        result.extend(s);
        result
    }
}

#[wasm_bindgen]
trait ToBigUint {
    fn to_biguint(&self) -> Option<BigUint>;
}

#[wasm_bindgen]
impl ToBigUint for rsa::BigUint {
    fn to_biguint(&self) -> Option<BigUint> {
        BigUint::from_str(&self.to_string()).ok()
    }
}

#[wasm_bindgen]
impl ToBigUint for rsa::RsaPrivateKey {
    fn to_biguint(&self) -> Option<BigUint> {
        Some(self.n().to_biguint().unwrap())
    }
}

#[wasm_bindgen]
pub fn compute_y0() -> BigUint {

}
