<script lang="ts">
	import Modal from '$lib/components/global/Modal.svelte';
	import { warningModalContent, isWarningModalHidden } from '$lib/stores/global';
	import { onMount } from 'svelte';
	import { downloadFile } from '$lib/utils/downloadFile';

	export let isExportButtonVisible: boolean = false;
	export let emails: string[] = [];
	export let width: number = 20;

	onMount(() => {
		function handleEnter(event: KeyboardEvent) {
			if (!$isWarningModalHidden && event.key === 'Enter') {
				event.preventDefault();
				$isWarningModalHidden = true;
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
	title="Warning"
	textColor="var(--warning-color-1)"
	borderColor="var(--warning-color-1)"
	{width}
	zIndex={12}
	bind:isHidden={$isWarningModalHidden}
>
	<div slot="content" class="content">{$warningModalContent}</div>
	{#if isExportButtonVisible}
		<button
			title="Export invalid emails"
			class="export"
			on:click={() => downloadFile('invalid-emails.csv', emails.join(';\n'))}
			><i class="symbol">file_save</i>Export</button
		>
	{/if}
	<button title="Ok" class="save" on:click={() => ($isWarningModalHidden = true)}
		><i class="symbol">done</i>OK</button
	>
</Modal>

<style>
	.export i {
		margin-right: 0.15em;
	}

	.save i {
		font-variation-settings: 'wght' 700;
	}
</style>
