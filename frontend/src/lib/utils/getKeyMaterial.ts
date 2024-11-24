export default async function getKeyMaterial(passphrase: string) {
	const encoder = new TextEncoder();
	return crypto.subtle.importKey('raw', encoder.encode(passphrase), 'PBKDF2', false, [
		'deriveBits',
		'deriveKey'
	]);
}
