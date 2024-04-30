<script lang="ts">
	import { title } from '$lib/stores/create-page';
</script>

<div title="Enter survey title" class="title-input" contenteditable bind:textContent={$title}>
	{$title}
</div>

<style>
	.title-input {
		flex: 1;
		background-color: var(--secondary-color);
		padding: 0.25em;
		border: 1px solid var(--border-color);
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--box-shadow-color);
		font-size: 1.5em;
		font-weight: bold;
		font-family: 'Jura';
		color: var(--text-color);
		cursor: text;
		overflow: hidden;
	}

	.title-input[contenteditable]:empty::before {
		content: 'Enter survey title...';
		color: var(--text-color-transparent);
	}

	@media screen and (max-width: 767px) {
		.title-input {
			font-size: 1.25em;
		}
	}
</style>
