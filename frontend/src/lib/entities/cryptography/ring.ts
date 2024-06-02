import { createHash, randomBytes } from 'crypto';

export class Ring {
	keys: string[];
	bitLength: number;
	numKeys: number;
	qValue: bigint;
	permutation: bigint;

	constructor(keys: string[], bitLength: number = 2048) {
		this.keys = keys;
		this.bitLength = bitLength;
		this.numKeys = keys.length;
		this.qValue = BigInt(1) << BigInt(bitLength - 1);
		this.permutation = BigInt(0);
	}

	sign(m: string, z: number): (bigint | null)[] {
		this._computePermutation(m);
		const s: (bigint | null)[] = new Array(this.numKeys).fill(null);
		const u: bigint = this._randomBelow(this.qValue);
		let c: bigint = this._computeE(u);
		let v: bigint = c;

		const firstRange: number[] = Array.from({ length: this.numKeys - z - 1 }, (_, i) => i + z + 1);
		const secondRange: number[] = Array.from({ length: z }, (_, i) => i);
		const wholeRange: number[] = [...firstRange, ...secondRange];

		for (const i of wholeRange) {
			s[i] = this._randomBelow(this.qValue);
			const e: bigint = this._computeG(s[i], this.keys[i].e, this.keys[i].n);
			v = this._computeE(v ^ e);
			if ((i + 1) % this.numKeys === 0) {
				c = v;
			}
		}

		s[z] = this._computeG(v ^ u, this.keys[z].d, this.keys[z].n);
		return [c, ...s];
	}

	private _computeE(x: bigint): bigint {
		const encodedMessage = Buffer.from(`${x}${this.permutation}`, 'utf-8');
		const hash = createHash('sha384').update(encodedMessage).digest('hex');
		return BigInt(`0x${hash}`);
	}

	private _computeG(x: bigint, e: bigint, n: bigint): bigint {
		const quotient = x / n;
		const remainder = x % n;
		const upperLimit = (BigInt(1) << BigInt(this.bitLength)) - BigInt(1);

		if ((quotient + BigInt(1)) * n <= upperLimit) {
			return quotient * n + this.modPow(remainder, e, n);
		} else {
			return x;
		}
	}

	private _computePermutation(message: string): void {
		const encodedMessage = Buffer.from(message, 'utf-8');
		const hash = createHash('sha384').update(encodedMessage).digest('hex');
		this.permutation = BigInt(`0x${hash}`);
	}

	modPow(base: bigint, exponent: bigint, modulus: bigint): bigint {
		if (modulus === BigInt(1)) return BigInt(0);
		let result = BigInt(1);
		base = base % modulus;
		while (exponent > 0) {
			if (exponent % BigInt(2) === BigInt(1)) {
				result = (result * base) % modulus;
			}
			exponent = exponent >> BigInt(1);
			base = (base * base) % modulus;
		}
		return result;
	}

	private _randomBelow(n: bigint): bigint {
		let r: bigint;
		do {
			r = BigInt(`0x${randomBytes(this.bitLength / 8).toString('hex')}`);
		} while (r >= n);
		return r;
	}

	hash(message: string): string {
		return createHash('sha384').update(message).digest('hex');
	}
}
