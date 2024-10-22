import OAuth from 'oauth-1.0a';
import CryptoJS from 'crypto-js';
import { env } from '$env/dynamic/private';

export const getOAuthInstance = () => {
	return new OAuth({
		consumer: {
			key: env.AUTH_USOS_ID as string,
			secret: env.AUTH_USOS_SECRET as string
		},
		signature_method: 'HMAC-SHA1',
		hash_function(base_string: string, key: string) {
			return CryptoJS.HmacSHA1(base_string, key).toString(CryptoJS.enc.Base64);
		}
	});
};
