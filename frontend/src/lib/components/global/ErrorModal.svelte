<script lang="ts">
	import Modal from '$lib/components/global/Modal.svelte';
	import { errorModalContent, isErrorModalHidden } from '$lib/stores/global';
	import { onMount } from 'svelte';

	onMount(() => {
		function handleEnter(event: KeyboardEvent) {
			if (!$isErrorModalHidden && event.key === 'Enter') {
				event.preventDefault();
				$isErrorModalHidden = true;
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
	icon="error"
	title="Error"
	textColor="var(--error-color-1)"
	borderColor="var(--error-color-1)"
	zIndex={12}
	bind:isHidden={$isErrorModalHidden}
>
	<div slot="content" class="content">{$errorModalContent}</div>
	<button title="Ok" class="save" on:click={() => ($isErrorModalHidden = true)}
		><i class="symbol">done</i>OK</button
	>
</Modal>

<style>
	.save i {
		font-variation-settings: 'wght' 700;
	}
</style>
