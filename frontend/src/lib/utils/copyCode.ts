export function copyCode(code: string): void {
	if (window.isSecureContext) {
		navigator.clipboard.writeText(code);
	} else {
		alert('The code could not be copied due to an insecure connection.');
	}
}
