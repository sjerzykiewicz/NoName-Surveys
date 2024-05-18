<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { beforeUpdate } from 'svelte';

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

<div class="choice-area">
	<div class="slider">
		<input
			class="range"
			type="range"
			step="1"
			min={$questions[questionIndex].choices[0]}
			max={$questions[questionIndex].choices[1]}
			name={questionIndex.toString()}
			disabled
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
	.choice-area {
		display: flex;
		flex-flow: column;
		align-items: center;
		justify-content: center;
		margin-left: 2.25em;
	}

	@media screen and (max-width: 767px) {
		.choice-area {
			font-size: 1em;
		}
	}
</style>
