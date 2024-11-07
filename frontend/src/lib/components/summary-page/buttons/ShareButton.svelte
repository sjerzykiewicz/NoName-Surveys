<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
</script>

<button
	title="Share survey results"
	class="footer-button"
	class:save={$page.route.id === '/surveys/[surveysPage]/[code]/access/[accessPage]'}
	on:click={() =>
		goto('/surveys/' + $page.params.surveysPage + '/' + $page.params.code + '/access/0')}
>
	<i class="material-symbols-rounded">share</i>Share
</button>
