export function downloadFile(filename: string, type: string, content: string) {
	const blob = new Blob([content], { type: type + ';charset=utf-8;' });
	downloadBlob(blob, filename);
}

export function downloadBinaryFile(filename: string, content: Uint8Array) {
	const blob = new Blob([content], { type: 'application/octet-stream' });
	downloadBlob(blob, filename);
}

function downloadBlob(blob: Blob, filename: string) {
	const element = document.createElement('a');
	element.href = URL.createObjectURL(blob);
	element.setAttribute('download', filename);

	element.style.display = 'none';
	document.body.appendChild(element);

	element.click();

	document.body.removeChild(element);
	URL.revokeObjectURL(element.href);
}
