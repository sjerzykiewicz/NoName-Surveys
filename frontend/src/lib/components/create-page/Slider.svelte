<script lang="ts">
	import { questions } from '$lib/stores/create-page';

	export let questionIndex: number;
</script>

<div class="choice-area">
	<div class="slider">
		<input
			class="range"
			type="range"
			step="1"
			min={$questions[questionIndex].choices[0]}
			max={$questions[questionIndex].choices[1]}
			name={$questions[questionIndex].question}
			disabled
		/>
	</div>
	<div class="limits">
		<input
			title="Enter minimum value"
			class="limit-input"
			type="number"
			name={$questions[questionIndex].question}
			autocomplete="off"
			placeholder="Enter min..."
			bind:value={$questions[questionIndex].choices[0]}
		/>
		<input
			title="Enter maximum value"
			class="limit-input"
			type="number"
			name={$questions[questionIndex].question}
			autocomplete="off"
			placeholder="Enter max..."
			bind:value={$questions[questionIndex].choices[1]}
		/>
	</div>
</div>

<style>
	.choice-area {
		display: flex;
		flex-flow: column;
		align-items: center;
		justify-content: center;
	}

	.slider {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 100%;
		margin-top: 0.5em;
		margin-bottom: 1em;
	}

	.range {
		appearance: none;
		width: 100%;
		height: 0.5em;
		border-radius: 0.5em;
		background: var(--border-color);
		outline: none;
		opacity: 1;
		margin-left: 2.75em;
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
		width: 100%;
	}

	.limit-input {
		background-color: var(--secondary-dark-color);
		padding: 0.25em;
		border: 1px solid var(--border-color);
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--shadow-color);
		font-size: 1.25em;
		font-weight: normal;
		color: var(--text-color);
		text-align: center;
		cursor: text;
		overflow: hidden;
		width: 6.5em;
		margin-left: 1.75em;
	}

	.limit-input::placeholder {
		color: var(--text-dark-color);
	}

	@media screen and (max-width: 767px) {
		.choice-area,
		.limit-input {
			font-size: 1em;
		}

		.limit-input {
			margin-left: 2.25em;
		}
	}
</style>
