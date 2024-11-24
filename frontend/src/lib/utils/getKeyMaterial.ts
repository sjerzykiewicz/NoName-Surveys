export default async function getKeyMaterial(password: string) {
	const encoder = new TextEncoder();
	return crypto.subtle.importKey('raw', encoder.encode(password), 'PBKDF2', false, [
		'deriveBits',
		'deriveKey'
	]);
}
