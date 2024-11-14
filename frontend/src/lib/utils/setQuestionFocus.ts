export default function setQuestionFocus(index: number) {
	const matches = document.querySelectorAll('.question .question-area .input-container .input');
	(matches.item(index) as HTMLElement).focus();
}
