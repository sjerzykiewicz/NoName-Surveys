<script lang="ts">
	import Modal from '$lib/components/global/Modal.svelte';
	import { successModalContent, isSuccessModalHidden } from '$lib/stores/global';
	import { onMount } from 'svelte';

	export let hide: () => void = () => ($isSuccessModalHidden = true);

	onMount(() => {
		function handleEnter(event: KeyboardEvent) {
			if (!$isSuccessModalHidden && event.key === 'Enter') {
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
	icon="check_circle"
	title="Success"
	--text-color="var(--accent-color-1)"
	--border-color="var(--accent-color-1)"
	--z-index="12"
	bind:isHidden={$isSuccessModalHidden}
	{hide}
>
	<div slot="content" class="content">{$successModalContent}</div>
	<button title="Ok" class="done" on:click={hide}><i class="symbol">done</i>OK</button>
</Modal>
