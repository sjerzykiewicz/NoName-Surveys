<script lang="ts">
	export let data: { answer: string; choices: string[] };
</script>

<div class="choice-area">
	<div title="Answer" class="select">{data.answer}</div>
</div>

<style>
	.choice-area {
		padding-left: 2.3em;
	}

	.select {
		background-color: var(--secondary-dark-color);
		padding: 0.25em;
		border: 2px solid var(--accent-color);
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--shadow-color);
		font-size: 1.25em;
		cursor: default;
		font-weight: bold;
		color: var(--accent-color);
		width: fit-content;
		max-width: 100%;
		transition: 0.2s;
	}
	@media screen and (max-width: 767px) {
		.select {
			font-size: 1em;
		}
	}
</style>
