const keys = [
	'ArrowDown',
	'ArrowLeft',
	'ArrowRight',
	'ArrowUp',
	'End',
	'Home',
	'PageDown',
	'PageUp',
	'Backspace',
	'Delete'
];

export function limitInput(e: KeyboardEvent, str: string, limit: number) {
	if (str.length >= limit && !keys.includes(e.key)) {
		e.preventDefault();
	}
}
