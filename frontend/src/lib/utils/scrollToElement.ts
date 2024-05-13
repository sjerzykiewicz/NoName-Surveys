export function scrollToElement(selector: string) {
	const element = document.querySelector(selector) as HTMLElement;

	if (element) {
		element.scrollIntoView({ behavior: 'smooth' });
	}
}
