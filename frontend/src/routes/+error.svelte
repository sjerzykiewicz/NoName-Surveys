<script lang="ts">
	import { page } from '$app/stores';
	import Tx from 'sveltekit-translate/translate/tx.svelte';

	$: errorMessage =
		typeof $page.error!.message === 'string'
			? $page.error!.message
			: typeof $page.error!.message === 'undefined'
				? 'Unknown error' // @ts-expect-error message is not necessarily a string
				: typeof $page.error!.message.detail === 'string' // @ts-expect-error message is not necessarily a string
					? $page.error!.message.detail
					: 'Unknown error';
</script>

{#if $page.error}
	<div>
		<h1><Tx text="error" />: <span>{$page.status}</span></h1>
		<h2><Tx text="Message" />: <span>{errorMessage}</span></h2>
		<p><Tx text="error_message" /></p>
	</div>
{/if}

<style>
	div {
		text-align: center;
		color: var(--text-color-1);
		font-size: 1em;
		padding: 2em;
		margin: 2em;
		background-color: var(--secondary-color-2);
		border: 1px solid var(--error-color-1);
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--shadow-color-1);
		text-shadow: 0px 4px 4px var(--shadow-color-1);
		font-weight: 700;
		cursor: default;
		transition:
			0.2s,
			outline 0s;
	}

	span {
		color: var(--error-color-1);
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
