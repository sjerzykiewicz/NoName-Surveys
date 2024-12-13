export function toggleContrast(colorContrast: string): string {
	if (colorContrast === 'medium') {
		document.documentElement.dataset.colorContrast = 'high';
		localStorage.setItem('colorContrast', 'high');
	} else {
		document.documentElement.dataset.colorContrast = 'medium';
		localStorage.setItem('colorContrast', 'medium');
	}

	return document.documentElement.dataset.colorContrast;
}
