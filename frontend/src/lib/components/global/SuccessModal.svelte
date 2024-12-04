<script lang="ts">
	import Modal from '$lib/components/global/Modal.svelte';
	import { successModalContent, isSuccessModalHidden } from '$lib/stores/global';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let hide: () => void = () => ($isSuccessModalHidden = true);

	function handleEnter(event: KeyboardEvent) {
		if (!$isSuccessModalHidden && event.key === 'Enter') {
			event.preventDefault();
			event.stopImmediatePropagation();
			hide();
		}
	}
</script>

<svelte:body on:keydown={handleEnter} />

<Modal
	icon="check_circle"
	title={$t('success')}
	--text-color="var(--accent-color-1)"
	--border-color="var(--accent-color-1)"
	--z-index="12"
	bind:isHidden={$isSuccessModalHidden}
	{hide}
>
	<div slot="content" class="content">{$successModalContent}</div>
	<button title="Ok" class="done" on:click={hide}><i class="symbol">done</i>OK</button>
</Modal>
