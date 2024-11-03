<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
</script>

<button
	title="View survey summary"
	class="footer-button"
	class:save={$page.route.id === '/surveys/[surveysPage]/[code]'}
	on:click={() => goto('/surveys/' + $page.params.surveysPage + '/' + $page.params.code)}
>
	<i class="material-symbols-rounded">bar_chart</i>Summary
</button>
