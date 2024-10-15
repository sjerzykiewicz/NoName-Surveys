<script lang="ts">
	import { page } from '$app/stores';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
</script>

{#if $page.error}
	<div>
		<h1><Tx text="error"></Tx>: <span>{$page.status}</span></h1>
		<h2><Tx text="Message"></Tx>: <span>{$page.error.message}</span></h2>
		<p><Tx text="error_message"></Tx></p>
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

	@media screen and (max-width: 767px) {
		div {
			margin: 1em;
			padding: 1em;
		}
	}
</style>
