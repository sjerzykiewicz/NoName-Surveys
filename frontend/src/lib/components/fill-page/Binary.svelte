<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';

	export let questionIndex: number;
</script>

<div class="choice-area display">
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
		<div title="Select your answer" class="choice-input display">
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
		<div title="Select your answer" class="choice-input display">
			{$questions[questionIndex].choices[1]}
		</div>
	</label>
</div>

<style>
	.choice-area {
		display: flex;
		flex-flow: row;
		align-items: center;
		justify-content: space-around;
		margin-left: 2.25em;
		width: calc(100% - 4.5em);
	}

	.choice {
		flex-flow: column;
		text-align: center;
		margin-top: -0.5em;
		margin-bottom: 0em;
		cursor: pointer;
	}

	.choice-input {
		margin: 0.5em 0em 0em 0em;
		max-width: 12em;
		overflow-wrap: break-word;
	}

	.selected .choice-input,
	.selected .choice-input:hover {
		background-color: var(--secondary-dark-color);
		border: 1px solid var(--accent-color);
		color: var(--accent-color);
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
		font-size: 1em;
	}

	.selected i {
		color: var(--accent-color);
		font-variation-settings:
			'FILL' 1,
			'GRAD' 200;
	}

	@media screen and (max-width: 767px) {
		.choice-input {
			max-width: 6em;
		}
	}
</style>
