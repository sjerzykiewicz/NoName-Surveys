<script lang="ts">
	export let goBack: () => void = () => {
		history.back();
	};
</script>

<button title="Go back" class="footer-button" on:click={goBack}
	><i class="symbol">undo</i>Back</button
>
