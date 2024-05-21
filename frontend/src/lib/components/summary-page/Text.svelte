<script lang="ts">
	export let data: { answer: string; details: string };
</script>

<div class="choice-area">
	<div title="Details" class="details">
		{data.details}
	</div>
	<div title="Answer" class="text-area">
		{data.answer}
	</div>
</div>

<style>
	.choice-area {
		padding-left: 2.3em;
	}

	.text-area {
		background-color: var(--secondary-dark-color);
		padding: 0.25em;
		border: 2px solid var(--accent-color);
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--shadow-color);
		font-size: 1.25em;
		font-weight: bold;
		color: var(--accent-color);
		width: fit-content;
		max-width: 100%;
		cursor: default;
		overflow: hidden;
		overflow-wrap: break-word;
		margin-right: 0.5em;
	}

	@media screen and (max-width: 767px) {
		.choice-area,
		.details,
		.text-area {
			font-size: 1em;
		}
	}
</style>
