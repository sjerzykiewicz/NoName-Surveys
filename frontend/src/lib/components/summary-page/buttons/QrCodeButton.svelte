<script lang="ts">
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);
	export let isModalHidden: boolean = true;
</script>

<button title={$t('view_qr')} class="footer-button" on:click={() => (isModalHidden = false)}>
	<i class="symbol">qr_code_2</i><Tx text="code"></Tx>
</button>
