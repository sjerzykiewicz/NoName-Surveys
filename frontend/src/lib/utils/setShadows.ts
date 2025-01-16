export function setShadows(): string {
	const shadows = localStorage.getItem('shadows') || 'on';

	if (shadows === 'on') {
		document.documentElement.dataset.shadows = 'on';
	} else {
		document.documentElement.dataset.shadows = 'off';
	}

	return shadows;
}
