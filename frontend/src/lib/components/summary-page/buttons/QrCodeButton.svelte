<script lang="ts">
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	export let isModalHidden: boolean = true;
</script>

<button title="View QR code" class="footer-button" on:click={() => (isModalHidden = false)}>
	<i class="symbol">qr_code_2</i><Tx text="code"></Tx>
</button>
