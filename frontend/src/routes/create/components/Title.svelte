<div>
	<form method="POST">
		<div class="input" contenteditable></div>
	</form>
</div>

<style>
	.input {
		background-color: #1a1a1a;
		padding: 0.25em;
		border: 1px solid #eaeaea;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		width: fit-content;
		max-width: 100%;
		font-size: 1.5em;
		font-weight: bold;
		cursor: text;
	}

	.input[contenteditable]:empty::before {
		content: 'Enter survey title...';
		color: #eaeaea40;
	}
</style>
