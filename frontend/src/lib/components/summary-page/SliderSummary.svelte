<script lang="ts">
	export let data: { answers: number[]; min_value: number; max_value: number };

	let avg = (data.answers.reduce((a, b) => a + b, 0) / data.answers.length).toFixed(2);
</script>

<div class="choice-area display slider">
	<div class="choice slider">
		<div title="Average" class="limit">{avg}</div>
	</div>
	<div title="Average" class="slider-area">
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
		<div title="Maximum value" class="limit">{data.max_value}</div>
	</div>
</div>

<style>
	.choice .limit {
		color: var(--accent-color);
	}
</style>
