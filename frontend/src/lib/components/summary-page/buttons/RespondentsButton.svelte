<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);
</script>

<button
	title={$t('view_respondents')}
	class="footer-button"
	class:save={$page.url.pathname.includes('respondents')}
	on:click={() =>
		goto('/surveys/' + $page.params.surveysPage + '/' + $page.params.code + '/respondents/0')}
>
	<i class="symbol">group</i><Tx text="respondents" />
</button>
