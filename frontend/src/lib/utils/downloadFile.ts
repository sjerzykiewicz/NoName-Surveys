export function downloadFile(filename: string, type: string, content: Uint8Array) {
	const blob = new Blob([content], { type: type });

	const element = document.createElement('a');
	element.href = URL.createObjectURL(blob);
	element.setAttribute('download', filename);

	element.style.display = 'none';
	document.body.appendChild(element);

	element.click();

	document.body.removeChild(element);
	URL.revokeObjectURL(element.href);
}
