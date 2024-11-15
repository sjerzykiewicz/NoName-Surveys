<script lang="ts">
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	export let goBack: () => void = () => {
		history.back();
	};
</script>

<button title="Go back" class="footer-button" on:click={goBack}
	><i class="symbol">undo</i><Tx text="back"></Tx></button
>
