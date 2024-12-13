export function setContrast(): string {
	const colorContrast = localStorage.getItem('colorContrast') || 'medium';

	if (colorContrast === 'medium') {
		document.documentElement.dataset.colorContrast = 'medium';
	} else {
		document.documentElement.dataset.colorContrast = 'high';
	}

	return colorContrast;
}
