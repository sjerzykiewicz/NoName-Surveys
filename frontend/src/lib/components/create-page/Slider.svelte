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
			on:beforeinput|once={() => ($questions[questionIndex].choices[0] = '')}
		/>
		<input
			title="Enter maximum value"
			class="limit-input"
			type="number"
			name={questionIndex.toString()}
			autocomplete="off"
			placeholder={placeholder[1]}
			bind:value={$questions[questionIndex].choices[1]}
			on:beforeinput|once={() => ($questions[questionIndex].choices[1] = '')}
		/>
	</div>
</div>

<style>
	.choice-area {
		display: flex;
		flex-flow: column;
		align-items: center;
		justify-content: center;
		font-size: 1.25em;
		margin-left: 2.25em;
	}

	.slider {
		display: flex;
		align-items: center;
		justify-content: center;
		width: calc(100% - 2.25em);
		margin-top: 0.5em;
		margin-bottom: 1em;
		margin-right: 2.25em;
	}

	.range {
		appearance: none;
		width: 100%;
		height: 0.5em;
		border-radius: 0.5em;
		background: var(--border-color);
		outline: none;
		opacity: 1;
	}

	.range::-webkit-slider-thumb {
		appearance: none;
		width: 1.5em;
		height: 1.5em;
		border-radius: 1.5em;
		background: var(--text-color);
		cursor: default;
	}

	.range::-moz-range-thumb {
		appearance: none;
		width: 1.5em;
		height: 1.5em;
		border-radius: 1.5em;
		background: var(--text-color);
		cursor: default;
	}

	.limits {
		display: flex;
		align-items: center;
		justify-content: space-between;
		width: calc(100% - 2.25em);
		margin-right: 2.25em;
	}

	.limit-input {
		background-color: var(--secondary-dark-color);
		padding: 0.25em;
		border: 1px solid var(--border-color);
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--shadow-color);
		font-size: 1em;
		font-weight: normal;
		color: var(--text-color);
		text-align: center;
		cursor: text;
		overflow: hidden;
		width: 12em;
	}

	.limit-input::placeholder {
		color: var(--text-dark-color);
	}

	@media screen and (max-width: 767px) {
		.choice-area {
			font-size: 1em;
		}

		.limit-input {
			width: 6em;
		}
	}
</style>
