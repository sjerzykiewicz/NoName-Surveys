export function copyCode(code: string): boolean {
	if (window.isSecureContext) {
		navigator.clipboard.writeText(code);
		return true;
	}
	alert('The code could not be copied due to an insecure connection.');
	return false;
}
