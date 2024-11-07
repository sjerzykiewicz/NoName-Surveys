<script lang="ts">
	import Modal from '$lib/components/global/Modal.svelte';
	import { warningModalContent, isWarningModalHidden } from '$lib/stores/global';
	import { onMount } from 'svelte';

	export let hide: () => void = () => ($isWarningModalHidden = true);

	onMount(() => {
		function handleEnter(event: KeyboardEvent) {
			if (!$isWarningModalHidden && event.key === 'Enter') {
				event.preventDefault();
				hide();
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
	zIndex={12}
	bind:isHidden={$isWarningModalHidden}
	{hide}
>
	<div slot="content" class="content">{$warningModalContent}</div>
	<button title="Ok" class="save" on:click={hide}
		><i class="symbol">done</i>OK</button
	>
</Modal>

<style>
	.save i {
		font-variation-settings: 'wght' 700;
	}
</style>
