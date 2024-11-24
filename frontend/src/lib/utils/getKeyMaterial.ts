export default async function getKeyMaterial(password: string) {
	const encoder = new TextEncoder();
	return crypto.subtle.importKey('raw', encoder.encode(password), 'PKDF2', false, [
		'deriveBits',
		'deriveKey'
	]);
}
