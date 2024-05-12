<script lang="ts">
	export let data: { answers: number[]; min_value: number; max_value: number };

	let avg = (data.answers.reduce((a, b) => a + b, 0) / data.answers.length).toFixed(2);
</script>

<div class="choice-area">
	<div class="slider">
		<input
			class="range"
			type="range"
			step="1"
			min={data.min_value}
			max={data.max_value}
			value={avg}
			disabled
		/>
	</div>
	<div class="limits">
		<div title="Minimum value" class="limit">{data.min_value}</div>
		<div title="Average answer" class="current-value">{avg}</div>
		<div title="Maximum value" class="limit">{data.max_value}</div>
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
		cursor: default;
	}

	.range:hover {
		background: var(--border-color);
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

	.range::-webkit-slider-thumb:hover {
		background: var(--text-color);
	}

	.range::-moz-range-thumb:hover {
		background: var(--text-color);
	}

	.range::-webkit-slider-thumb:active {
		cursor: default;
	}

	.range::-moz-range-thumb:active {
		cursor: default;
	}

	.limits {
		display: flex;
		align-items: center;
		justify-content: space-between;
		width: 100%;
	}

	.limit {
		text-shadow: 0px 4px 4px var(--shadow-color);
		font-size: 1.25em;
		font-weight: bold;
		color: var(--text-color);
		cursor: default;
		margin-left: 2em;
	}

	.current-value {
		background-color: var(--secondary-dark-color);
		padding: 0.25em;
		border: 2px solid var(--accent-color);
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--shadow-color);
		font-size: 1.25em;
		font-weight: bold;
		color: var(--accent-color);
		cursor: default;
		overflow: hidden;
		width: fit-content;
		margin-left: 2em;
		text-align: center;
	}

	@media screen and (max-width: 767px) {
		.choice-area,
		.limit,
		.current-value {
			font-size: 1em;
		}
	}
</style>
