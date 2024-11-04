use getrandom::Error;
use num_bigint::{BigUint, RandBigInt};
use num_traits::{One, Zero};
use pem::{encode, parse, Pem};
use sha3::{
    digest::{ExtendableOutput, Update, XofReader},
    Digest, Sha3_256, Sha3_384, Shake256,
};
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
const R_HEX: &[u8; 448] = b"F65B7EA7706034A2\
                            8A29B9436AF161BB\
                            F3632483671C60AE\
                            E9B1A6A496FFF904\
                            FCB09731B6C6E16B\
                            551CEC2C063910B0\
                            4E40795D4BEB474D\
                            B762E28CC923AE40\
                            FDBAF05BF7501D03\
                            14C3CBE4BAD7329D\
                            D473BDF441E7B8B3\
                            87B402CD0BE7DC53\
                            4FA6D3C039BDAD13\
                            3F59DC899FD570A6\
                            67C453D08150A35C\
                            F5E845087BD9ACFA\
                            8333343375E8EE52\
                            965A84C699C59DFE\
                            F852EFB96023BEF0\
                            FFB2F99C53AC2D94\
                            CD2969764698B8DD\
                            E401DA6AA6BDB3B0\
                            3B5506D287090F8E\
                            852C05EC0BDB3C0C\
                            4FBEC1A4AB9FE141\
                            E8A7C9EADB17D335\
                            921B673615A7FC0C\
                            92384946B9AB6452";
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
    fingerprint: String,
}

#[wasm_bindgen]
impl KeyPair {
    pub fn get_public_key(&self) -> String {
        self.public_key.clone()
    }

    pub fn get_private_key(&self) -> String {
        self.private_key.clone()
    }

    pub fn get_fingerprint(&self) -> String {
        self.fingerprint.clone()
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

    let private_pem = encode(&Pem::new("PRIVATE KEY", priv_key.to_string().as_bytes()));
    let public_pem = encode(&Pem::new("PUBLIC KEY", pub_key.to_string().as_bytes()));

    let mut hasher = Sha3_256::new();
    Digest::update(&mut hasher, public_pem.to_string().as_bytes());
    let h = hasher.finalize();
    let print = format!("{:x}", h);

    KeyPair {
        private_key: private_pem,
        public_key: public_pem,
        fingerprint: print,
    }
}

// h1 : {0,1}* -> Zq/Z
fn h1(x: &String) -> BigUint {
    // hash to {0,1}^384
    let mut hasher = Sha3_384::new();
    Digest::update(&mut hasher, x.as_bytes());
    let h = hasher.finalize();
    let int = BigUint::from_bytes_be(&h);

    let q: BigUint = BigUint::parse_bytes(Q_HEX, 16).unwrap();

    // reduce mod q
    int.modpow(&BigUint::one(), &q)
}

// h2 : {0,1}* -> <g>
fn h2(x: &String) -> BigUint {
    // hash to {0,1}^2176
    let mut hasher = Shake256::default();
    hasher.update(x.as_bytes());
    let mut reader = hasher.finalize_xof();
    let mut result = [0u8; 2176];
    reader.read(&mut result);
    let int = BigUint::from_bytes_be(&result);

    // reduce mod (p-1) -> element of Z(p-1)/Z
    let p: BigUint = BigUint::parse_bytes(P_HEX, 16).unwrap();
    let int = int % (&p - BigUint::one());

    // add 1 -> element of Z*p
    let int: BigUint = int + BigUint::one();

    // i^r is an element of <g>
    let r: BigUint = BigUint::parse_bytes(R_HEX, 16).unwrap();
    int.modpow(&r, &p)
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

    let pub_keys: Vec<Pem> = match pub_keys.iter().map(|k| parse(k)).collect() {
        Ok(pk) => pk,
        Err(_) => return Err(JsValue::from_str("Could not convert public key pem")),
    };

    let pub_keys: Vec<String> = match pub_keys
        .iter()
        .map(|k| String::from_utf8(k.contents().to_vec()))
        .collect()
    {
        Ok(pk) => pk,
        Err(_) => return Err(JsValue::from_str("Could not convert pem data to string")),
    };

    let y: Vec<BigUint> = match pub_keys.iter().map(|k| k.parse::<BigUint>()).collect() {
        Ok(y) => y,
        Err(_) => return Err(JsValue::from_str("Invalid public key format")),
    };

    let priv_key = match parse(priv_key) {
        Ok(k) => k,
        Err(_) => return Err(JsValue::from_str("Could not convert private key pem")),
    };

    let priv_key = match String::from_utf8(priv_key.contents().to_vec()) {
        Ok(k) => k,
        Err(_) => return Err(JsValue::from_str("Could not convert pem data to string")),
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
    let mut sum_c_i = BigUint::zero();
    let mut prod_y_i_c_i = BigUint::one();

    for i in 0..index {
        c[i as usize] = rng.gen_biguint_below(&q);
        sum_c_i += &c[i as usize];
        prod_y_i_c_i *= &y[i as usize].modpow(&c[i as usize], &p);
    }

    for i in index + 1..n as u32 {
        c[i as usize] = rng.gen_biguint_below(&q);
        sum_c_i += &c[i as usize];
        prod_y_i_c_i *= &y[i as usize].modpow(&c[i as usize], &p);
    }

    sum_c_i %= &q;

    let g_to_r = g.modpow(&r, &p);
    let h_to_r = h.modpow(&r, &p);

    let for_hash: String = keys_concatenated
        + &y0.to_string()
        + &m
        + &((&g_to_r * &prod_y_i_c_i) % &p).to_string()
        + &((&h_to_r * &y0.modpow(&sum_c_i, &p)) % &p).to_string();

    let hash_val: BigUint = h1(&for_hash);

    c[index as usize] = if hash_val >= sum_c_i {
        hash_val - sum_c_i
    } else {
        &q - sum_c_i + hash_val
    };

    let prod: BigUint = (&c[index as usize] * pk) % &q;

    let s = if r >= prod { r - prod } else { &q - prod + r };

    let mut sig: Vec<String> = Vec::new();
    sig.push(y0.to_string());
    sig.push(s.to_string());

    for i in 0..n {
        sig.push(c[i as usize].to_string());
    }

    Ok(sig)
}
