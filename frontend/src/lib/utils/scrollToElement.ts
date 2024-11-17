export function scrollToElement(selector: string) {
	const element = document.querySelector(selector) as HTMLElement;

	if (element) {
		element.scrollIntoView({ behavior: 'smooth', block: 'center' });
	}
}

export function scrollToElementById(id: string) {
	const element = document.getElementById(id) as HTMLElement;

	if (element) {
		element.scrollIntoView({ behavior: 'smooth', block: 'center' });
	}
}
