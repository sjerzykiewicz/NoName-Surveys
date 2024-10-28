<script lang="ts">
	import Modal from '$lib/components/Modal.svelte';
	import { warningModalContent, isWarningModalHidden } from '$lib/stores/global';
	import { onMount } from 'svelte';

	onMount(() => {
		function handleEnter(event: KeyboardEvent) {
			if (!$isWarningModalHidden && event.key === 'Enter') {
				event.preventDefault();
				$isWarningModalHidden = true;
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
	textColor="var(--warning-color)"
	borderColor="var(--warning-color)"
	zIndex={12}
	bind:isHidden={$isWarningModalHidden}
>
	<div slot="content" class="content">{$warningModalContent}</div>
	<button title="Ok" class="save" on:click={() => ($isWarningModalHidden = true)}
		><i class="material-symbols-rounded">done</i>OK</button
	>
</Modal>
