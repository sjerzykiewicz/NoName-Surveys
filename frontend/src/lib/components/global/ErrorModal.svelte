<script lang="ts">
	import Modal from '$lib/components/global/Modal.svelte';
	import { errorModalContent, isErrorModalHidden } from '$lib/stores/global';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let hide: () => void = () => ($isErrorModalHidden = true);

	function handleEnter(event: KeyboardEvent) {
		if (!$isErrorModalHidden && event.key === 'Enter') {
			event.preventDefault();
			hide();
			event.stopImmediatePropagation();
		}
	}
</script>

<svelte:body on:keydown={handleEnter} />

<Modal
	icon="error"
	title={$t('error')}
	--text-color="var(--error-color-1)"
	--border-color="var(--error-color-1)"
	--z-index="12"
	bind:isHidden={$isErrorModalHidden}
	{hide}
>
	<div slot="content" class="content">{$errorModalContent}</div>
	<button title="Ok" class="done" on:click={hide}><i class="symbol">done</i>OK</button>
</Modal>
