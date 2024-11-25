export function copy(str: string): boolean {
	if (window.isSecureContext) {
		navigator.clipboard.writeText(str);
		return true;
	}
	return false;
}
