use wasm_bindgen::prelude::*;
use rsa::{RsaPrivateKey, RsaPublicKey};
use rsa::pkcs1::{EncodeRsaPrivateKey, EncodeRsaPublicKey};
use zeroize::Zeroizing;

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
