<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';

	export let questionIndex: number;

	let value: number = Math.round(
		(parseFloat($questions[questionIndex].choices[0]) +
			parseFloat($questions[questionIndex].choices[1])) /
			2
	);
</script>

<div
	class="choice-area display slider"
	in:slide={{ duration: 200, easing: cubicInOut }}
	out:slide={{ delay: 200, duration: 200, easing: cubicInOut }}
>
	<div class="choice slider">
		<input
			title="Selected value"
			class="limit-input"
			type="number"
			autocomplete="off"
			min={$questions[questionIndex].choices[0]}
			max={$questions[questionIndex].choices[1]}
			name={questionIndex.toString()}
			bind:value
		/>
	</div>
	<div class="limits">
		<div title="Minimum value" class="limit">{$questions[questionIndex].choices[0]}</div>
		<div title="Maximum value" class="limit">{$questions[questionIndex].choices[1]}</div>
	</div>
</div>

<style>
	.limit-input {
		color: var(--accent-color);
		border: 1px solid var(--accent-color);
		width: 15em;
	}

	@media screen and (max-width: 767px) {
		.limit-input {
			width: 10em;
		}
	}
</style>
