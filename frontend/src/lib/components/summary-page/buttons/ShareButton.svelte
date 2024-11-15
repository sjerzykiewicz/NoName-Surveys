<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
</script>

<button
	title="Share survey results"
	class="footer-button"
	class:save={$page.route.id === '/surveys/[surveysPage]/[code]/access/[accessPage]'}
	on:click={() =>
		goto('/surveys/' + $page.params.surveysPage + '/' + $page.params.code + '/access/0')}
>
	<i class="symbol">share</i><Tx text="share"></Tx>
</button>
