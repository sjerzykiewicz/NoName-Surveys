export function toggleScheme(colorScheme: string): string {
	if (colorScheme === 'dark') {
		document.documentElement.dataset.colorScheme = 'light';
		localStorage.setItem('colorScheme', 'light');
	} else {
		document.documentElement.dataset.colorScheme = 'dark';
		localStorage.setItem('colorScheme', 'dark');
	}

	return document.documentElement.dataset.colorScheme;
}
