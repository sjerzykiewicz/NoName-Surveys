<script lang="ts">
	import { page } from '$app/stores';
</script>

{#if $page.error}
	<div>
		<h1>Error: <span>{$page.status}</span></h1>
		<h2>Message: <span>{$page.error.message}</span></h2>
		<p>Something went wrong, please contact with the administrator.</p>
	</div>
{/if}

<style>
	div {
		text-align: center;
		color: var(--text-color);
		font-size: 1em;
		padding: 2em;
		margin: 2em;
		border: 1px solid var(--border-color);
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--shadow-color);
	}
	span {
		color: var(--error-color);
	}

	p {
		font-size: 1.5em;
	}
</style>
