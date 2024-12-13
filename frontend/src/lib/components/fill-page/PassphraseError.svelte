<script lang="ts">
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';
	import type KeyPair from '$lib/entities/KeyPair';
	import { PassphraseErrorEnum } from '$lib/entities/PassphraseErrorEnum';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let error: PassphraseErrorEnum;
	export let keyPair: KeyPair | null;

	function errorMessage() {
		return $t('passphrase_file_decryption_failed');
	}

	$: checkPassphraseError = () => {
		return error === PassphraseErrorEnum.DecryptionFailed && keyPair === null;
	};
</script>

{#if checkPassphraseError()}
	<p title={$t('error')} class="error" transition:slide={{ duration: 200, easing: cubicInOut }}>
		<i class="symbol">error</i>
		{#key [$t, error]}
			{errorMessage()}
		{/key}
	</p>
{/if}

<style>
	.error {
		font-size: 0.8em;
	}
</style>
