export function readFile(fileInput: HTMLInputElement | null): Promise<Uint8Array> {
	const fileReader = new FileReader();
	const file = fileInput?.files?.[0];
	return new Promise<Uint8Array>((resolve, reject) => {
		if (!file) {
			reject('No file selected');
			return;
		}

		fileReader.readAsArrayBuffer(file);
		fileReader.onload = (e) => {
			const fileData = e.target?.result as Uint8Array;
			const byteArray = new Uint8Array(fileData);
			resolve(byteArray);
		};

		fileReader.onerror = () => {
			reject('Error reading file');
		};
	});
}
