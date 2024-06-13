<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';

	export let questionIndex: number;
</script>

<div
	class="choice-area scale"
	in:slide={{ delay: 200, duration: 200, easing: cubicInOut }}
	out:slide={{ duration: 200, easing: cubicInOut }}
>
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
		background-color: var(--secondary-color);
		color: var(--text-dark-color);
		cursor: default;
	}

	.choice-input:hover {
		background-color: var(--secondary-color);
	}

	input[type='radio'] {
		cursor: default;
	}
</style>
