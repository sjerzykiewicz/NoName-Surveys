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
	textColor="var(--accent-color-1)"
	borderColor="var(--accent-color-1)"
	zIndex={12}
	bind:isHidden={$isSuccessModalHidden}
	{hide}
>
	<div slot="content" class="content">{$successModalContent}</div>
	<button title="Ok" class="save" on:click={hide}><i class="symbol">done</i>OK</button>
</Modal>
