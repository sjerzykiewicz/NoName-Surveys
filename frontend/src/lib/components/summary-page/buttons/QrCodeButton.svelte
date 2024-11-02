<script lang="ts">
	export let isModalHidden: boolean = true;
</script>

<button title="View QR code" class="footer-button" on:click={() => (isModalHidden = false)}>
	<i class="material-symbols-rounded">qr_code_2</i>Code
</button>
