<script lang="ts">
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';
	import type KeyPair from '$lib/entities/KeyPair';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let error: boolean;
	export let keyPair: KeyPair | null;

	function errorMessage() {
		return $t('incorrect_passphrase');
	}

	$: checkPassphraseError = () => {
		return error && keyPair === null;
	};
</script>

{#if checkPassphraseError()}
	<p title={$t('error')} class="error" transition:slide={{ duration: 200, easing: cubicInOut }}>
		<i class="symbol">error</i>
		{#key $t}
			{errorMessage()}
		{/key}
	</p>
{/if}

<style>
	.error {
		font-size: 0.8em;
	}
</style>
