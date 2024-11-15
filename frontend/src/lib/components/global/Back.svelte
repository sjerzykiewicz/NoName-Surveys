<script lang="ts">
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let goBack: () => void = () => {
		history.back();
	};
</script>

<button title={$t('back_title')} class="footer-button" on:click={goBack}
	><i class="symbol">undo</i><Tx text="back"></Tx></button
>
