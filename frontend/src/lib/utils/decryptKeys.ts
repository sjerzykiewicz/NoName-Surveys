import getKeyMaterial from './getKeyMaterial';
import keyFromMaterial from './keyFromMaterial';

export default async function decryptKeys(
	ciphertext: Uint8Array,
	password: string,
	salt: Uint8Array,
	iv: Uint8Array
) {
	const keyMaterial = await getKeyMaterial(password);
	const key = await keyFromMaterial(keyMaterial, salt);

	const decrypted = await crypto.subtle.decrypt({ name: 'AES-GCM', iv }, key, ciphertext);
	return new Uint8Array(decrypted);
}
