<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
</script>

<button
	title="View possible respondents"
	class="footer-button"
	class:save={$page.route.id === '/surveys/[surveysPage]/[code]/respondents/[respondentsPage]'}
	on:click={() =>
		goto('/surveys/' + $page.params.surveysPage + '/' + $page.params.code + '/respondents/0')}
>
	<i class="symbol">group</i>Respondents
</button>
