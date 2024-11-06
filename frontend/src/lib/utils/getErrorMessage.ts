export function getErrorMessage(detail: string | { msg: string }[]): string {
	return typeof detail === 'string'
		? detail
		: detail[0].msg === 'string'
			? detail[0].msg
			: 'Something went wrong';
}
