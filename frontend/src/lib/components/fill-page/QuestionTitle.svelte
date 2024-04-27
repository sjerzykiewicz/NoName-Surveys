<script lang="ts">
	export let questionNumber: number;
	export let question: string;
</script>

<div class="question-area">
	<div class="index">{questionNumber}.</div>
	<div title="Question title" class="question-title">
		{question}
	</div>
</div>

<style>
	.question-area {
		display: flex;
		flex-flow: row;
		align-items: center;
		margin-bottom: 1em;
		font-size: 1.25em;
		font-weight: normal;
		font-family: 'Jura';
		color: #eaeaea;
	}

	.question-title {
		flex: 1;
		background-color: #1a1a1a;
		padding: 0.25em;
		border: 1px solid #999999;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		cursor: text;
		overflow: hidden;
		margin-right: 0.5em;
	}

	.index {
		margin-right: 0.3em;
		font-size: 1.1em;
		cursor: default;
		width: 1.4em;
		text-align: right;
	}
</style>
