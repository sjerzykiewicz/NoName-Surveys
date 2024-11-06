<script lang="ts">
    import ShareButton from '$lib/components/summary-page/buttons/ShareButton.svelte';
    import RespondentsButton from '$lib/components/summary-page/buttons/RespondentsButton.svelte';
    import AnswersButton from '$lib/components/summary-page/buttons/AnswersButton.svelte';
    import SummaryButton from '$lib/components/summary-page/buttons/SummaryButton.svelte';
    import QrCodeButton from '$lib/components/summary-page/buttons/QrCodeButton.svelte';
    import Back from '$lib/components/global/Back.svelte';

    export let isOwnedByUser: boolean;
    export let usesCryptographicModule: boolean;
    export let isModalHidden: boolean = true;
</script>

{#if isOwnedByUser}
	<ShareButton />
{/if}
{#if usesCryptographicModule}
	<RespondentsButton />
{/if}
<div class="footer-button-group">
	<div class="footer-button-group">
		<AnswersButton />
		<SummaryButton />
	</div>
	<div class="footer-button-group">
		<QrCodeButton bind:isModalHidden />
		<Back />
	</div>
</div>
