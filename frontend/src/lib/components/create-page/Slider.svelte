<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { MOBILE_DEVICE_BREAKPOINT } from '$lib/stores/global';
	import { afterUpdate, beforeUpdate } from 'svelte';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';

	export let questionIndex: number;

	let innerWidth: number;
	let placeholder: Array<string>;

	let value: number = Math.round(
		(parseFloat($questions[questionIndex].choices[0]) +
			parseFloat($questions[questionIndex].choices[1])) /
			2
	);

	beforeUpdate(() => {
		if (innerWidth <= $MOBILE_DEVICE_BREAKPOINT) {
			placeholder = ['Enter min...', 'Enter max...'];
		} else {
			placeholder = ['Enter minimum value...', 'Enter maximum value...'];
		}
	});

	afterUpdate(() => {
		value = Math.round(
			(parseFloat($questions[questionIndex].choices[0]) +
				parseFloat($questions[questionIndex].choices[1])) /
				2
		);
	});
</script>

<svelte:window bind:innerWidth />

<div
	class="choice-area slider"
	in:slide={{ delay: 200, duration: 200, easing: cubicInOut }}
	out:slide={{ duration: 200, easing: cubicInOut }}
>
	<div class="slider-area">
		<input
			class="range"
			type="range"
			step="1"
			min={$questions[questionIndex].choices[0]}
			max={$questions[questionIndex].choices[1]}
			name={questionIndex.toString()}
			disabled
			bind:value
		/>
	</div>
	<div class="limits">
		<input
			title="Enter minimum value"
			class="limit-input"
			type="number"
			name={questionIndex.toString()}
			autocomplete="off"
			placeholder={placeholder[0]}
			bind:value={$questions[questionIndex].choices[0]}
			on:keydown|once={() => ($questions[questionIndex].choices[0] = '')}
		/>
		<input
			title="Enter maximum value"
			class="limit-input"
			type="number"
			name={questionIndex.toString()}
			autocomplete="off"
			placeholder={placeholder[1]}
			bind:value={$questions[questionIndex].choices[1]}
			on:keydown|once={() => ($questions[questionIndex].choices[1] = '')}
		/>
	</div>
</div>

<style>
	@media screen and (max-width: 767px) {
		.limit-input {
			width: 6em;
		}
	}
</style>
