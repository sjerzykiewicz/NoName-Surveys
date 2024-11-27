<script lang="ts">
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';
	import { PassphraseErrorEnum } from '$lib/entities/PassphraseErrorEnum';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let error: PassphraseErrorEnum;
	export let passphrase: string;
	export let passphraseConfirm: string;

	function errorMessage() {
		switch (error) {
			case PassphraseErrorEnum.Empty:
				return $t('error_empty_passphrase');
			case PassphraseErrorEnum.ConfirmNotMatching:
				return $t('error_passphrase_confirm_no_match');
		}
	}

	$: checkPassphraseError = () => {
		switch (error) {
			case PassphraseErrorEnum.Empty:
				return passphrase === '';
			case PassphraseErrorEnum.ConfirmNotMatching:
				return passphrase !== passphraseConfirm;
		}
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
