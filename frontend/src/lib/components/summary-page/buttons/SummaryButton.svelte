<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
</script>

<button
	title="View the summary"
	class="footer-button"
	class:save={$page.route.id === '/surveys/[surveysPage]/[code]'}
	on:click={() => goto('/surveys/' + $page.params.surveysPage + '/' + $page.params.code)}
>
	<i class="symbol">bar_chart</i><Tx text="summary"></Tx>
</button>
