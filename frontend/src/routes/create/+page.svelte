<script lang="ts">
</script>

<div class="header">
	<form id="form" method="POST">
		<div class="input" contenteditable></div>
	</form>
</div>
<div class="content"></div>
<div class="footer">
	<button class="footer-button" type="button" form="form">Back</button>
	<button class="footer-button" type="button" form="form">Preview</button>
	<button class="footer-button" type="submit" form="form">Save</button>
</div>

<style>
	.header {
		padding: 0.5em 1em 0.5em 0.5em;
		border-bottom: 1px solid #eaeaea;
		font-size: 24px;
		font-weight: bold;
		font-family: 'Jura';
		color: #eaeaea;
	}

	.header .input {
		background-color: #1a1a1a;
		padding: 0.25em;
		border: 1px solid #eaeaea;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		cursor: text;
		width: fit-content;
		max-width: 100%;
	}

	.header .input[contenteditable]:empty::before {
		content: 'Enter survey title...';
		color: #eaeaea40;
	}

	.content {
		flex: 1;
	}

	.footer {
		padding: 0.75em;
		border-top: 1px solid #eaeaea;
	}

	.footer-button {
		background-color: #4a4a4a;
		margin-left: 0.5em;
		padding: 0.25em;
		border: 1px solid #eaeaea;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		width: fit-content;
		font-size: 16px;
		font-weight: normal;
		font-family: 'Jura';
		color: #eaeaea;
		cursor: pointer;
		transition: background-color 0.5s;
		float: right;
	}

	.footer-button:hover {
		background-color: #1a1a1a;
	}
</style>
