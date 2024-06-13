export function handleNewLine(event: KeyboardEvent) {
	if (event.key === 'Enter') {
		event.preventDefault();
		document.execCommand('insertLineBreak');
	}
}
