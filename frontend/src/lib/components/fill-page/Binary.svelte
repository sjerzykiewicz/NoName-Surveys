<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';

	export let questionIndex: number;
</script>

<div class="choice-area">
	<label
		class="choice"
		class:selected={$answers[questionIndex].choices[0] === $questions[questionIndex].choices[0]}
	>
		<input
			type="radio"
			name={questionIndex.toString()}
			on:change={() => {
				$answers[questionIndex].choices[0] = $questions[questionIndex].choices[0];
			}}
		/>
		<i class="material-symbols-rounded">thumb_up</i>
		<div title="Select your answer" class="choice-in">
			{$questions[questionIndex].choices[0]}
		</div>
	</label>
	<label
		class="choice"
		class:selected={$answers[questionIndex].choices[0] === $questions[questionIndex].choices[1]}
	>
		<input
			type="radio"
			name={questionIndex.toString()}
			on:change={() => {
				$answers[questionIndex].choices[0] = $questions[questionIndex].choices[1];
			}}
		/>
		<i class="material-symbols-rounded">thumb_down</i>
		<div title="Select your answer" class="choice-in">
			{$questions[questionIndex].choices[1]}
		</div>
	</label>
</div>

<style>
	.choice-area {
		display: flex;
		flex-flow: row;
		align-items: center;
		justify-content: space-evenly;
		width: calc(86% - 2.25em);
		margin-left: 2.25em;
	}

	.choice {
		flex-flow: column;
		text-align: center;
		margin-bottom: 0em;
		padding: 0em 0.5em;
		cursor: pointer;
	}

	.choice-in {
		margin: 0.5em 0em 0em 0em;
		width: fit-content;
		max-width: 11em;
		overflow-wrap: break-word;
	}

	.selected .choice-in,
	.selected .choice-in:hover {
		background-color: var(--secondary-dark-color);
		border: 2px solid var(--accent-color);
		color: var(--accent-color);
		font-weight: bold;
	}

	input {
		appearance: none;
		position: relative;
		top: 1.5em;
		margin: 0em;
		height: 1.5em;
		width: 1.5em;
	}

	i {
		font-size: 1.25em;
	}

	.selected i {
		color: var(--accent-color);
		font-variation-settings:
			'FILL' 1,
			'GRAD' 200;
	}

	@media screen and (max-width: 767px) {
		.choice-in,
		i {
			font-size: 1.5em;
		}

		.choice-in {
			max-width: 5em;
		}
	}
</style>
