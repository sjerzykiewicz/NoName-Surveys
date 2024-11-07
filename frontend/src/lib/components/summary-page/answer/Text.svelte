<script lang="ts">
	export let data: { answer: string; details: string };
</script>

<div class="choice-area display">
	<div title="Question details" class="details">
		{data.details}
	</div>
	<div title="Answer" class="text-area display">
		{data.answer}
	</div>
</div>

<style>
	.text-area {
		border: 1px solid var(--accent-color-1);
		background-color: var(--secondary-color-2);
		color: var(--accent-color-1);
		min-height: 1.15em;
		transition:
			0.2s,
			outline 0s;
	}
</style>
