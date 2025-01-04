<script lang="ts">
	import { page } from '$app/stores';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	$: errorMessage = (() => {
		const { error } = $page;
		if (!error) return $t('unknown_error');
		if (typeof error.message === 'string') return error.message; // @ts-expect-error message is not necessarily a string
		if (error.message && typeof error.message.detail === 'string') return error.message.detail;
		if (error.message && typeof error.message.message === 'string') return error.message.message;
		return $t('unknown_error');
	})();
</script>

{#if $page.error}
	<div>
		<h1><Tx text="error" />: <span>{$page.status}</span></h1>
		<h2><Tx text="message" />: <span>{errorMessage}</span></h2>
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
		transition: 0.2s;
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
