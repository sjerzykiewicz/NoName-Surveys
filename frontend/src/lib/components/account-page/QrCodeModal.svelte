<script lang="ts">
	import Modal from '$lib/components/global/Modal.svelte';
	import QrCode from '$lib/components/global/QrCode.svelte';
	import { page } from '$app/stores';
	import { copy } from '$lib/utils/copy';
	import { popup } from '$lib/utils/popup';
	import { errorModalContent, isErrorModalHidden, M } from '$lib/stores/global';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let isHidden: boolean = true;
	export let title: string;
	export let id: string;

	async function handleCopy(str: string, id: string) {
		if (copy(str)) {
			popup(id);
		} else {
			$errorModalContent = $t('no_copy_insecure_connection');
			$isErrorModalHidden = false;
		}
	}

	function handleEnter(event: KeyboardEvent) {
		if (!isHidden && event.key === 'Enter') {
			event.preventDefault();
			event.stopImmediatePropagation();
			isHidden = true;
		}
	}

	let innerWidth: number;
	let innerHeight: number;
</script>

<svelte:window bind:innerWidth bind:innerHeight />
<svelte:body on:keydown={handleEnter} />

<Modal
	icon="qr_code_2"
	{title}
	bind:isHidden
	--width={innerWidth > $M && innerHeight > $M ? '30em' : '20em'}
>
	<div slot="content" class="content">
		<span class="scan"><Tx text="scan_to_join" /></span>
		<a href="/account" title={$t('scan_to_join')}>
			<QrCode
				href={$page.url.toString()}
				{id}
				codeSize={innerWidth > $M && innerHeight > $M ? 360 : 260}
				codeMargin={3}
				imageMargin={6}
			/>
		</a>
	</div>
	<button
		title={$t('copy_link_title')}
		class="save popup"
		on:click={() => handleCopy($page.url.toString(), 'link-popup')}
		><i class="symbol">link</i><Tx text="copy_link" />
		<span class="popup-text top" id="link-popup"><Tx text="copied" /></span></button
	>
</Modal>

<style>
	.popup .popup-text {
		--tooltip-width: 6em;
	}

	.content {
		display: inherit;
		flex-flow: inherit;
		justify-content: inherit;
		align-items: inherit;
		padding-bottom: 1em;
	}

	.scan {
		padding-bottom: 0.75em;
		font-size: 1.75em;
	}
</style>
