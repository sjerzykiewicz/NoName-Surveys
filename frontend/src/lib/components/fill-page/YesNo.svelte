<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';

	export let questionIndex: number;
</script>

<div class="choice-area">
	<button
		title="Select your answer"
		class="choice-binary"
		class:selected={$answers[questionIndex].choices[0] === $questions[questionIndex].choices[0]}
		on:click={() => {
			$answers[questionIndex].choices[0] = $questions[questionIndex].choices[0];
		}}
	>
		<i class="material-symbols-rounded">thumb_up</i>{$questions[questionIndex].choices[0]}
	</button>
	<button
		title="Select your answer"
		class="choice-binary"
		class:selected={$answers[questionIndex].choices[0] === $questions[questionIndex].choices[1]}
		on:click={() => {
			$answers[questionIndex].choices[0] = $questions[questionIndex].choices[1];
		}}
	>
		<i class="material-symbols-rounded">thumb_down</i>{$questions[questionIndex].choices[1]}
	</button>
</div>

<style>
	.choice-area {
		display: flex;
		flex-flow: row;
		align-items: center;
		justify-content: space-around;
		font-size: 1em;
		font-weight: normal;
		font-family: 'Jura';
		color: var(--text-color);
		width: calc(86% - 2.25em);
		margin-left: 2.25em;
	}

	.choice-binary {
		display: flex;
		background-color: var(--primary-color);
		padding: 0.25em;
		border: 1px solid var(--border-color);
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--box-shadow-color);
		font-size: 1.25em;
		font-family: 'Jura';
		color: var(--text-color);
		cursor: pointer;
		transition: 0.2s;
	}

	.choice-binary:hover {
		background-color: var(--secondary-color);
	}

	.choice-binary.selected,
	.choice-binary.selected:hover {
		background-color: var(--accent-color);
	}

	.choice-binary:active,
	.choice-binary.selected:active {
		background-color: var(--border-color);
	}

	i {
		font-size: 1.15em;
		margin-right: 0.15em;
	}

	@media screen and (max-width: 767px) {
		.choice-binary,
		i {
			font-size: 1em;
		}
	}
</style>
