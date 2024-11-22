<script lang="ts">
	import Modal from '$lib/components/global/Modal.svelte';
	import { warningModalContent, isWarningModalHidden } from '$lib/stores/global';
	import { onMount } from 'svelte';
	import { downloadFile } from '$lib/utils/downloadFile';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';
	import Tx from 'sveltekit-translate/translate/tx.svelte';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let isExportButtonVisible: boolean = false;
	export let emails: string[] = [];
	export let hide: () => void = () => ($isWarningModalHidden = true);

	onMount(() => {
		function handleEnter(event: KeyboardEvent) {
			if (!$isWarningModalHidden && event.key === 'Enter') {
				event.preventDefault();
				hide();
				event.stopImmediatePropagation();
			}
		}

		document.body.addEventListener('keydown', handleEnter);

		return () => {
			document.body.removeEventListener('keydown', handleEnter);
		};
	});
</script>

<Modal
	icon="warning"
	title={$t('warning')}
	--text-color="var(--warning-color-1)"
	--border-color="var(--warning-color-1)"
	--width="var(--width-warning)"
	--z-index="12"
	bind:isHidden={$isWarningModalHidden}
	{hide}
>
	<div slot="content" class="content">{$warningModalContent}</div>
	{#if isExportButtonVisible}
		<button
			title={$t('export_invalid_emails')}
			class="export"
			on:click={() => downloadFile('invalid-emails.csv', 'text/csv', emails.join(';\n'))}
			><i class="symbol">file_save</i><Tx text="export" /></button
		>
	{/if}
	<button title="Ok" class="done" on:click={() => ($isWarningModalHidden = true)}
		><i class="symbol">done</i>OK</button
	>
</Modal>

<style>
	.export i {
		margin-right: 0.15em;
	}
</style>
