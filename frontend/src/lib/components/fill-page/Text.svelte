<script lang="ts">
	import { questions } from '$lib/stores/fill-page';
	import { answers } from '$lib/stores/fill-page';
	export let questionIndex: number;
	let value: string;
</script>

<div class="choice-area">
	<div class="details">
		{$questions[questionIndex].choices[0]}
	</div>
	<textarea
		class="details-area"
		required={$questions[questionIndex].required}
		name={$questions[questionIndex].question}
		placeholder="Enter your answer..."
		bind:value
		on:change={() => ($answers[questionIndex].choices[0] = value)}
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
		background-color: #1a1a1a;
		border: 1px solid #999999;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		padding: 0.3em;
	}

	.details-area {
		flex: 1;
		background-color: #1a1a1a;
		padding: 0.5em;
		border: 1px solid #999999;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		cursor: text;
		color: #eaeaea;
		width: 80%;
		height: 5em;
		resize: none;
	}

	@media screen and (max-width: 767px) {
		.choice-area,
		.details-area {
			font-size: 1em;
		}
	}
</style>
