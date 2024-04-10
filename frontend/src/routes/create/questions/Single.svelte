<script lang="ts">
	export let index: number;
	index += 1;
</script>

<div class="question-area">
	<span class="index">{index}.</span>
	<form method="POST">
		<span class="question-input" contenteditable></span>
	</form>
</div>

<style>
	.question-area {
		display: flex;
		flex-flow: row;
		align-items: baseline;
		margin-bottom: 0.5em;
		width: fit-content;
		max-width: 100%;
		font-size: 1.25em;
		font-weight: normal;
		font-family: 'Jura';
		color: #eaeaea;
	}

	.question-input {
		background-color: #1a1a1a;
		padding: 0.25em;
		border: 1px solid #eaeaea;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		width: fit-content;
		max-width: 100%;
		cursor: text;
	}

	.question-input[contenteditable]:empty::before {
		content: 'Enter question...';
		color: #eaeaea40;
	}

	.index {
		font-size: 1.25em;
		margin-right: 10px;
		cursor: default;
	}
</style>
