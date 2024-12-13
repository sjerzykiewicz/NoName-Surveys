export default async function keyFromMaterial(keyMaterial: CryptoKey, salt: Uint8Array) {
	return crypto.subtle.deriveKey(
		{
			name: 'PBKDF2',
			salt,
			iterations: 500000,
			hash: 'SHA-512'
		},
		keyMaterial,
		{ name: 'AES-GCM', length: 256 },
		true,
		['encrypt', 'decrypt']
	);
}
