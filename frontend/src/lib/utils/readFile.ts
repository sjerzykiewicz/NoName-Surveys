export function readFile(fileInput: HTMLInputElement | null): Promise<string> {
	const fileReader = new FileReader();
	const file = fileInput?.files?.[0];
	return new Promise<string>((resolve, reject) => {
		if (!file) {
			reject('No file selected');
			return;
		}

		fileReader.readAsText(file);
		fileReader.onload = (e) => {
			const fileData = e.target?.result;
			const text = fileData as string;
			resolve(text);
		};

		fileReader.onerror = () => {
			reject('Error reading file');
		};
	});
}

export function readBinaryFile(fileInput: HTMLInputElement | null): Promise<Uint8Array> {
	const fileReader = new FileReader();
	const file = fileInput?.files?.[0];
	return new Promise<Uint8Array>((resolve, reject) => {
		if (!file) {
			reject('No file selected');
			return;
		}

		fileReader.readAsArrayBuffer(file);
		fileReader.onload = (e) => {
			const fileData = e.target?.result as ArrayBuffer;
			const byteArray = new Uint8Array(fileData);
			resolve(byteArray);
		};

		fileReader.onerror = () => {
			reject('Error reading file');
		};
	});
}
