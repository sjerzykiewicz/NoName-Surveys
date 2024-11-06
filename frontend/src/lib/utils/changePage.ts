import { goto } from '$app/navigation';
import { delay } from './delay';

export async function changePage(pathname: string, page: number) {
	await delay(100);
	await goto(pathname.substring(0, pathname.lastIndexOf('/') + 1) + page, {
		keepFocus: true,
		noScroll: true
	});
}
