export function toggleShadows(shadows: string): string {
	if (shadows === 'on') {
		document.documentElement.dataset.shadows = 'off';
		localStorage.setItem('shadows', 'off');
	} else {
		document.documentElement.dataset.shadows = 'on';
		localStorage.setItem('shadows', 'on');
	}

	return document.documentElement.dataset.shadows;
}
