<script lang="ts">
	import { title } from '$lib/stores/create-page';

	export let titleError: boolean;

	$: checkTitleError = () => {
		const t = $title;
		return titleError && (t === null || t === undefined || t.length === 0);
	};
</script>

<div title="Enter survey title" class="title-input" contenteditable bind:textContent={$title}>
	{$title}
</div>
{#if checkTitleError()}
	<p title="Error" class="error">
		<i class="material-symbols-rounded">error</i>Please enter survey title.
	</p>
{/if}

<style>
	.title-input {
		font-size: 1.5em;
		font-weight: bold;
		margin: 0em;
		width: calc(100% - 0.5em);
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
