<div class="input" contenteditable></div>

<style>
	.input {
		flex: 1;
		background-color: #1a1a1a;
		padding: 0.25em;
		border: 1px solid #eaeaea;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		font-size: 1.5em;
		font-weight: bold;
		font-family: 'Jura';
		color: #eaeaea;
		cursor: text;
		overflow: hidden;
	}

	.input[contenteditable]:empty::before {
		content: 'Enter survey title...';
		color: #eaeaea40;
	}
</style>
