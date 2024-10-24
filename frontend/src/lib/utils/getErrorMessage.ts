export function getErrorMessage(detail: string | { msg: string }[]): string {
	if (typeof detail === 'string') return detail;
	else return detail[0].msg;
}
