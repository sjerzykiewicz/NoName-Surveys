export function getErrorMessage(detail: string | { msg: string }[]): string {
	return typeof detail === 'string'
		? detail
		: typeof detail === 'undefined'
			? 'Something went wrong'
			: typeof detail[0].msg === 'string'
				? detail[0].msg
				: 'Something went wrong';
}
