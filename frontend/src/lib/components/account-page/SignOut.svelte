<script lang="ts">
	import { signOut } from '$lib/utils/signOut';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);
</script>

<div class="sign-buttons">
	<button title={$t('sign_out')} class="sign-out" on:click={signOut}
		><i class="symbol">logout</i><Tx text="sign_out" />
	</button>
</div>

<style>
	.sign-buttons {
		display: flex;
		justify-content: flex-start;
		padding-top: 0.5em;
		padding-bottom: 0.5em;
		font-size: 1.5em;
	}

	@media screen and (max-width: 768px) {
		.sign-buttons {
			font-size: 1.25em;
		}
	}
</style>
