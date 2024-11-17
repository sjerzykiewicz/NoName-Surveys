export default function formatDate(isoString: string): string {
	return new Date(isoString).toLocaleString();
}
