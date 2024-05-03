<script lang="ts">
	import { title } from '$lib/stores/create-page';
</script>

<div title="Enter survey title" class="title-input" contenteditable bind:textContent={$title}>
	{$title}
</div>

<style>
	.title-input {
		font-size: 1.5em;
		font-weight: bold;
		margin: 0em;
	}

	.title-input[contenteditable]:empty::before {
		content: 'Enter survey title...';
		color: var(--text-dark-color);
	}

	@media screen and (max-width: 767px) {
		.title-input {
			font-size: 1.25em;
		}
	}
</style>
