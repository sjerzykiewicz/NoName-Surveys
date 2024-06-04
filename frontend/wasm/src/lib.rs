use wasm_bindgen::prelude::*;

// import Javascript's alert method to Rust
#[wasm_bindgen]
extern "C" {
    fn alert(s: &str);
}

// export Rust function greet to be used in JS/TS, the same function signature will be used in JS/TS
#[wasm_bindgen]
pub fn greet(str: &str) {
    alert(&format!("Hello, {}!", str));
}
