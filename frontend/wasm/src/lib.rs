/*
    First attempt at LRS implementation. This implementation is not confirmed to be secure and is only for testing and demonstration purposes.
*/

use num_bigint::{BigUint, RandBigInt};
use num_traits::{One, Zero};
use sha2::Digest;
use wasm_bindgen::prelude::*;

// cyclic group parameters
// from RFC 5114
// 2048-bit p, 256-bit q
// G = {g^n mod p | n < q}
const P_HEX: &[u8; 512] = b"87A8E61DB4B6663CFFBBD19C65195999\
                            8CEEF608660DD0F25D2CEED4435E3B00\
                            E00DF8F1D61957D4FAF7DF4561B2AA30\
                            16C3D91134096FAA3BF4296D830E9A7C\
                            209E0C6497517ABD5A8A9D306BCF67ED\
                            91F9E6725B4758C022E0B1EF4275BF7B\
                            6C5BFC11D45F9088B941F54EB1E59BB8\
                            BC39A0BF12307F5C4FDB70C581B23F76\
                            B63ACAE1CAA6B7902D52526735488A0E\
                            F13C6D9A51BFA4AB3AD8347796524D8E\
                            F6A167B5A41825D967E144E514056425\
                            1CCACB83E6B486F6B3CA3F7971506026\
                            C0B857F689962856DED4010ABD0BE621\
                            C3A3960A54E710C375F26375D7014103\
                            A4B54330C198AF126116D2276E11715F\
                            693877FAD7EF09CADB094AE91E1A1597";
const Q_HEX: &[u8; 64] = b"8CF83642A709A097\
                            B447997640129DA2\
                            99B1A47D1EB3750B\
                            A308B0FE64F5FBD3";
const G_HEX: &[u8; 512] = b"3FB32C9B73134D0B2E77506660EDBD48\
                            4CA7B18F21EF205407F4793A1A0BA125\
                            10DBC15077BE463FFF4FED4AAC0BB555\
                            BE3A6C1B0C6B47B1BC3773BF7E8C6F62\
                            901228F8C28CBB18A55AE31341000A65\
                            0196F931C77A57F2DDF463E5E9EC144B\
                            777DE62AAAB8A8628AC376D282D6ED38\
                            64E67982428EBC831D14348F6F2F9193\
                            B5045AF2767164E1DFC967C1FB3F2E55\
                            A4BD1BFFE83B9C80D052B985D182EA0A\
                            DB2A3B7313D3FE14C8484B1E052588B9\
                            B7D2BBD2DF016199ECD06E1557CD0915\
                            B3353BBB64E0EC377FD028370DF92B52\
                            C7891428CDC67EB6184B523D1DB246C3\
                            2F63078490F00EF8D647D148D4795451\
                            5E2327CFEF98C582664B4C0F6CC41659";

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
    let prime: BigUint = BigUint::parse_bytes(P_HEX, 16).unwrap();
    let order: BigUint = BigUint::parse_bytes(Q_HEX, 16).unwrap();
    let generator: BigUint = BigUint::parse_bytes(G_HEX, 16).unwrap();

    let mut rng = rand::thread_rng();
    let priv_key = rng.gen_biguint_below(&order);
    let pub_key = generator.modpow(&priv_key, &prime);

    KeyPair {
        private_key: priv_key.to_string(),
        public_key: pub_key.to_string(),
    }
}

// h1 : {0,1}* -> Zq
// k = 384 >= log2(q) + 128
// hash to {0,1}^k, reduce mod q
// TODO - first version, might change in future
fn h1(x: &String) -> BigUint {
    let mut hasher = sha2::Sha384::new();
    hasher.update(x.as_bytes());
    let h = hasher.finalize();
    let int = BigUint::from_bytes_be(&h);

    let q: BigUint = BigUint::parse_bytes(Q_HEX, 16).unwrap();

    int.modpow(&BigUint::one(), &q)
}

// h2 : {0,1}* -> <g>
// TODO - this is a naive version and will be replaced by a different hash
fn h2(x: &String) -> BigUint {
    let p: BigUint = BigUint::parse_bytes(P_HEX, 16).unwrap();
    let g: BigUint = BigUint::parse_bytes(G_HEX, 16).unwrap();

    g.modpow(&h1(x), &p)
}

#[wasm_bindgen]

pub fn linkable_ring_signature(
    m: String,
    pub_keys: Vec<String>,
    priv_key: String,
    index: u32,
) -> Result<Vec<String>, JsValue> {
    let p: BigUint = BigUint::parse_bytes(P_HEX, 16).unwrap();
    let q: BigUint = BigUint::parse_bytes(Q_HEX, 16).unwrap();
    let g: BigUint = BigUint::parse_bytes(G_HEX, 16).unwrap();

    let y: Vec<BigUint> = match pub_keys.iter().map(|k| k.parse::<BigUint>()).collect() {
        Ok(y) => y,
        Err(_) => return Err(JsValue::from_str("Invalid public key format")),
    };

    let pk: BigUint = match priv_key.parse::<BigUint>() {
        Ok(pk) => pk,
        Err(_) => return Err(JsValue::from_str("Invalid private key format")),
    };

    // TODO - concatenation of keys is not an ideal method, some encoding will be used in future
    let keys_concatenated = pub_keys.join("");

    let h = h2(&keys_concatenated);
    let y0 = h.modpow(&pk, &p);

    let mut rng = rand::thread_rng();
    let r = rng.gen_biguint_below(&q);

    let n = pub_keys.len();
    let mut c: Vec<BigUint> = vec![BigUint::zero(); n];
    let mut s: Vec<BigUint> = vec![BigUint::zero(); n];
    let mut z_1: Vec<BigUint> = vec![BigUint::zero(); n];
    let mut z_2: Vec<BigUint> = vec![BigUint::zero(); n];
    let mut sum_c_i = BigUint::zero();

    for i in 0..index {
        s[i as usize] = rng.gen_biguint_below(&q);
        c[i as usize] = rng.gen_biguint_below(&q);
        sum_c_i += &c[i as usize];
        z_1[i as usize] =
            (g.modpow(&s[i as usize], &p) * y[i as usize].modpow(&c[i as usize], &p)) % &p;
        z_2[i as usize] = (h.modpow(&s[i as usize], &p) * y0.modpow(&c[i as usize], &p)) % &p;
    }

    z_1[index as usize] = g.modpow(&r, &p);
    z_2[index as usize] = h.modpow(&r, &p);

    for i in index + 1..n as u32 {
        s[i as usize] = rng.gen_biguint_below(&q);
        c[i as usize] = rng.gen_biguint_below(&q);
        sum_c_i += &c[i as usize];
        z_1[i as usize] =
            (g.modpow(&s[i as usize], &p) * y[i as usize].modpow(&c[i as usize], &p)) % &p;
        z_2[i as usize] = (h.modpow(&s[i as usize], &p) * y0.modpow(&c[i as usize], &p)) % &p;
    }

    let z_1_concatenated = z_1.iter().map(|x| x.to_string()).collect::<String>();
    let z_2_concatenated = z_2.iter().map(|x| x.to_string()).collect::<String>();

    let for_hash: String =
        keys_concatenated + &y0.to_string() + &m + &z_1_concatenated + &z_2_concatenated;

    let hash_val: BigUint = h1(&for_hash);

    sum_c_i = sum_c_i % &q;

    c[index as usize] = if hash_val >= sum_c_i {
        hash_val - sum_c_i
    } else {
        &q - sum_c_i + hash_val
    };

    let prod: BigUint = (&c[index as usize] * pk) % &q;

    s[index as usize] = if r >= prod { r - prod } else { &q - prod + r };

    let mut sig: Vec<String> = Vec::new();
    sig.push(y0.to_string());

    for i in 0..n {
        sig.push(s[i as usize].to_string());
    }

    for i in 0..n {
        sig.push(c[i as usize].to_string());
    }

    Ok(sig)
}
