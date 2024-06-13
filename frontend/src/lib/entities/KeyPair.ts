export default class KeyPair {
	privateKey: string;
	publicKey: string;
	constructor(privateKey: string, publicKey: string) {
		this.privateKey = privateKey;
		this.publicKey = publicKey;
	}
}
