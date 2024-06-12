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
		border: 1px solid var(--accent-color);
		background-color: var(--secondary-dark-color);
		color: var(--accent-color);
		min-height: 1.15em;
	}
</style>
