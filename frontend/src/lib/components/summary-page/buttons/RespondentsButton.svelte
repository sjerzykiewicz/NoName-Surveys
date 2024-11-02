<script lang="ts">
	import { goto } from '$app/navigation';

	export let code: string;
</script>

<button
	title="View possible respondents"
	class="footer-button"
	on:click={() => goto('/' + code + '/summary/respondents/0')}
>
	<i class="material-symbols-rounded">group</i>Respondents
</button>
