export function formatDateTime(isoString: string): string {
	return new Date(isoString).toLocaleString();
}

export function formatDate(isoString: string): string {
	return new Date(isoString).toLocaleDateString();
}
