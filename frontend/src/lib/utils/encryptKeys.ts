import getKeyMaterial from './getKeyMaterial';
import keyFromMaterial from './keyFromMaterial';

export default async function encryptKeys(contents: string, password: string) {
	const keyMaterial = await getKeyMaterial(password);
	const salt = crypto.getRandomValues(new Uint8Array(16));
	const key = await keyFromMaterial(keyMaterial, salt);

	const enc = new TextEncoder();
	const encoded = enc.encode(contents);

	const iv = crypto.getRandomValues(new Uint8Array(12));
	const encrypted = await crypto.subtle.encrypt({ name: 'AES-GCM', iv }, key, encoded);
	const ciphertext = new Uint8Array(encrypted);

	return { salt, iv, ciphertext };
}
