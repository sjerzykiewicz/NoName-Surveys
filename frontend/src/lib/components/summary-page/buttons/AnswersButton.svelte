<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
</script>

<button
	title="View individual answers"
	class="footer-button"
	class:save={$page.url.pathname.includes('answers')}
	on:click={() =>
		goto('/surveys/' + $page.params.surveysPage + '/' + $page.params.code + '/answers')}
>
	<i class="material-symbols-rounded">mail</i>Answers
</button>
