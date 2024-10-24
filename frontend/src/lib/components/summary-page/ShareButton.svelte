<script lang="ts">
	import { goto } from '$app/navigation';

	export let code: string;
</script>

<button
	title="Share survey results"
	class="footer-button"
	on:click={() => goto('/' + code + '/summary/access')}
>
	<i class="material-symbols-rounded">share</i>Share
</button>
