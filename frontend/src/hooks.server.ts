import type { Handle } from '@sveltejs/kit';

export const handle: Handle = async ({ event, resolve }) => {
	const sessionCookie = event.cookies.get('user_session');

	if (sessionCookie) {
		event.locals.user = JSON.parse(sessionCookie);
	}

	const response = await resolve(event);

	return response;
};
