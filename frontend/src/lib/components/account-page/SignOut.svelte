<script lang="ts">
	import { signOut } from '$lib/utils/signOut';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	let isSignOutButtonDisabled: boolean = false;
</script>

<div class="sign-buttons">
	<button
		title={$t('sign_out')}
		class="sign-out"
		disabled={isSignOutButtonDisabled}
		on:click={async () => {
			isSignOutButtonDisabled = true;
			await signOut();
			isSignOutButtonDisabled = false;
		}}
		><i class="symbol">logout</i><Tx text="sign_out" />
	</button>
</div>

<style>
	.sign-buttons {
		display: flex;
		justify-content: flex-start;
		padding-top: 1em;
		padding-bottom: 1em;
		font-size: 1.5em;
		border-top: 1px solid var(--border-color-1);
	}

	@media screen and (max-width: 768px) {
		.sign-buttons {
			font-size: 1.25em;
		}
	}
</style>
