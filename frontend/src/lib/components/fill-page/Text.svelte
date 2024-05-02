<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';
	export let questionIndex: number;
	let value: string;
</script>

<div class="choice-area">
	<div class="details">
		{$questions[questionIndex].choices[0]}
	</div>
	<textarea
		class="details-area"
		name={$questions[questionIndex].question}
		placeholder="Enter your answer..."
		bind:value
		on:change={() => ($answers[questionIndex].choices[0] = value)}
	/>
</div>

<style>
	.choice-area {
		padding-left: 2.3em;
	}

	.details {
		display: flex;
		align-items: center;
		flex-flow: row;
		margin-bottom: 0.5em;
		background-color: var(--secondary-color);
		border: 1px solid var(--border-color);
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--box-shadow-color);
		padding: 0.3em;
	}

	.details-area {
		flex: 1;
		background-color: var(--secondary-color);
		padding: 0.5em;
		border: 1px solid var(--border-color);
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--box-shadow-color);
		cursor: text;
		color: var(--text-color);
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
