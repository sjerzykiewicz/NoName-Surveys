<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);
</script>

<button
	title={$t('view_individual_answers')}
	class="footer-button"
	class:save={$page.route.id === '/surveys/[surveysPage]/[code]/answers/[answersPage]'}
	on:click={() =>
		goto('/surveys/' + $page.params.surveysPage + '/' + $page.params.code + '/answers/0')}
>
	<i class="symbol">mail</i><Tx text="answers" />
</button>
