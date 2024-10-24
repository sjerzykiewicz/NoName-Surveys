<script lang="ts">
	import Tx from 'sveltekit-translate/translate/tx.svelte';

	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	async function signOut() {
		try {
			await fetch('/api/oauth/sign-out', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				}
			});
			location.reload();
		} catch (error) {
			console.error('OAuth sign-out failed:', error);
		}
	}
</script>

<div class="sign-buttons">
	<button title={$t('account_sign_out')} class="sign-out" on:click={() => signOut()}
		><i class="material-symbols-rounded">logout</i><Tx text="account_sign_out"></Tx>
	</button>
</div>

<style>
	.sign-buttons {
		display: flex;
		flex-flow: row;
		align-items: center;
		justify-content: center;
		padding-top: 1.5em;
		padding-bottom: 1.5em;
		font-size: 1.75em;
	}

	@media screen and (max-width: 768px) {
		.sign-buttons {
			font-size: 1.25em;
		}
	}
</style>
