export function copy(str: string): boolean {
	if (window.isSecureContext) {
		navigator.clipboard.writeText(str);
		return true;
	}
	alert('Could not copy due to an insecure connection.');
	return false;
}
