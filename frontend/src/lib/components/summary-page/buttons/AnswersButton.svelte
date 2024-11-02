<script lang="ts">
	import { goto } from '$app/navigation';

	export let code: string;
</script>

<button
	title="View individual answers"
	class="footer-button"
	on:click={() => goto('/' + code + '/summary/answers')}
>
	<i class="material-symbols-rounded">mail</i>Answers
</button>
