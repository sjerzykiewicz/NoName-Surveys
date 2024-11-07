<script lang="ts">
	export let data: { answer: number; min_value: number; max_value: number };
</script>

<div class="choice-area display slider">
	<div title="Answer" class="choice slider">
		<input
			class="limit-input"
			type="number"
			autocomplete="off"
			value={data.answer.toFixed(2)}
			disabled
		/>
	</div>
	<div class="limits">
		<div title="Minimum value" class="limit">{data.min_value}</div>
		<div title="Maximum value" class="limit">{data.max_value}</div>
	</div>
</div>

<style>
	.limit-input {
		color: var(--accent-color-1);
		border: 1px solid var(--accent-color-1);
		width: 100%;
		cursor: default;
		transition:
			0.2s,
			outline 0s;
	}
</style>
