<script lang="ts">
	import { questions } from '$lib/components/fill-page/stores';
	export let questionIndex: number;
</script>

<div class="choice-area">
	<div class="details">
		{$questions[questionIndex].choices[0]}
	</div>
	<input
		class="text-area"
		type="textarea"
		required={$questions[questionIndex].required}
		name={$questions[questionIndex].question}
	/>
</div>

<style>
	.choice-area {
		font-size: 1em;
		font-weight: normal;
		font-family: 'Jura';
		color: #eaeaea;
		width: 86%;
		padding-left: 2.3em;
	}

	.details {
		display: flex;
		align-items: center;
		flex-flow: row;
		margin-bottom: 0.5em;
	}

	.text-area {
		flex: 1;
		background-color: #1a1a1a;
		padding: 0.5em;
		border: 1px solid #999999;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		cursor: text;
		color: #eaeaea;
	}
</style>
