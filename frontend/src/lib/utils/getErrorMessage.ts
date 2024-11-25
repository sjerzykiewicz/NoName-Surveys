export function getErrorMessage(detail: string | { msg: string }[]): string {
	if (typeof detail === 'string') return detail;
	if (Array.isArray(detail) && detail.length > 0) {
		if (typeof detail[0] === 'string') return detail[0];
		if (detail[0] && typeof detail[0].msg === 'string') return detail[0].msg;
	}
	return 'Something went wrong';
}
