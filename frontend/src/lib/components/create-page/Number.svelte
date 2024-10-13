<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { beforeUpdate } from 'svelte';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';

	export let questionIndex: number;

	let innerWidth: number;
	let placeholder: Array<string>;

	beforeUpdate(() => {
		if (innerWidth <= 767) {
			placeholder = ['Enter min...', 'Enter max...'];
		} else {
			placeholder = ['Enter minimum value...', 'Enter maximum value...'];
		}
	});
</script>

<svelte:window bind:innerWidth />

<div
	class="choice-area slider"
	in:slide={{ delay: 200, duration: 200, easing: cubicInOut }}
	out:slide={{ duration: 200, easing: cubicInOut }}
>
	<div class="limits">
		<label>
			Minimum
			<input
				title="Enter minimum value"
				class="limit-input"
				type="number"
				name={questionIndex.toString()}
				autocomplete="off"
				placeholder={placeholder[0]}
				bind:value={$questions[questionIndex].choices[0]}
				on:keydown|once={() => ($questions[questionIndex].choices[0] = '')}
			/></label
		>
		<label>
			Maximum
			<input
				title="Enter maximum value"
				class="limit-input"
				type="number"
				name={questionIndex.toString()}
				autocomplete="off"
				placeholder={placeholder[1]}
				bind:value={$questions[questionIndex].choices[1]}
				on:keydown|once={() => ($questions[questionIndex].choices[1] = '')}
			/></label
		>
	</div>
</div>

<style>
	label {
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	@media screen and (max-width: 767px) {
		.limit-input {
			width: 6em;
		}
	}
</style>
