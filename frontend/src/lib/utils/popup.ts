import { delay } from './delay';

export async function popup(id: string) {
	const element = document.getElementById(id);
	element!.classList.add('visible');
	await delay(1500);
	element!.classList.remove('visible');
}
