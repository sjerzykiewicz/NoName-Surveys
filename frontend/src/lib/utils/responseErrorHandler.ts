import { error } from '@sveltejs/kit';

export const responseErrorHandler = async (response: Response) => {
	if (response.status === 400) {
		const body = await response.json();
		alert(body.detail);
	} else if (response.status === 422) {
		const body = await response.json();
		alert(body.detail[0].msg);
	} else {
		error(response.status, response.statusText);
	}
};
