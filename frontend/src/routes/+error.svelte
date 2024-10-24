<script lang="ts">
	import { page } from '$app/stores';
	import Tx from 'sveltekit-translate/translate/tx.svelte';

	let errorMessage: string = '';
	if (typeof $page.error!.message === 'string') errorMessage = $page.error!.message;
	// @ts-expect-error message is not necessarily a string
	else errorMessage = $page.error!.message.detail;
</script>

{#if $page.error}
	<div>
		<h1><Tx text="error"></Tx>: <span>{$page.status}</span></h1>
		<h2><Tx text="Message"></Tx>: <span>{errorMessage}</span></h2>
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
		background-color: var(--secondary-dark-color);
		border: 1px solid var(--error-color);
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--shadow-color);
		text-shadow: 0px 4px 4px var(--shadow-color);
		cursor: default;
	}

	span {
		color: var(--error-color);
	}

	p {
		font-size: 1.5em;
	}

	@media screen and (max-width: 768px) {
		div {
			margin: 1em;
			padding: 1em;
			font-size: 0.8em;
		}
	}
</style>
