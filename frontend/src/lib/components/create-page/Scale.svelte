<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';

	export let questionIndex: number;
</script>

<div class="choice-area scale" transition:slide={{ duration: 200, easing: cubicInOut }}>
	{#each $questions[questionIndex].choices as choice}
		<div title={choice} class="choice scale">
			<input type="radio" disabled name={questionIndex.toString()} />
			<div class="choice-input display scale">
				{choice}
			</div>
		</div>
	{/each}
</div>

<style>
	.choice-area {
		justify-content: space-between;
		width: calc(86% - 2.25em);
	}

	.choice {
		padding: 0em;
	}

	.choice-input {
		background-color: var(--secondary-color-1);
		color: var(--text-color-3);
		cursor: default;
		transition:
			0.2s,
			outline 0s;
	}

	.choice-input:hover {
		background-color: var(--secondary-color-1);
	}

	input[type='radio'] {
		cursor: default;
	}
</style>
