<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
</script>

<button
	title="View individual answers"
	class="footer-button"
	class:save={$page.route.id === '/surveys/[surveysPage]/[code]/answers/[answersPage]'}
	on:click={() =>
		goto('/surveys/' + $page.params.surveysPage + '/' + $page.params.code + '/answers/0')}
>
	<i class="material-symbols-rounded">mail</i>Answers
</button>
