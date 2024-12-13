export function setScheme(): string {
	const colorScheme = localStorage.getItem('colorScheme') || 'dark';

	if (colorScheme === 'dark') {
		document.documentElement.dataset.colorScheme = 'dark';
	} else {
		document.documentElement.dataset.colorScheme = 'light';
	}

	return colorScheme;
}
