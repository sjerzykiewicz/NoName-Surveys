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
	export let surveyCode: string;

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
		<span class="survey-code">{surveyCode}</span>
		<a href="/fill?code={surveyCode}" title={$t('fill_survey')}>
			<QrCode
				href={$page.url.origin + '/fill?code=' + surveyCode}
				id={surveyCode}
				codeSize={innerWidth > $M && innerHeight > $M ? 360 : 260}
				codeMargin={3}
				imageMargin={6}
			/>
		</a>
	</div>
	<button
		title={$t('copy_link_title')}
		class="save popup"
		on:click={() => handleCopy($page.url.origin + '/fill?code=' + surveyCode, 'link-popup')}
		><i class="symbol">link</i><Tx text="copy_link" />
		<span class="popup-text top" id="link-popup"><Tx text="copied" /></span></button
	>
	<button
		title={$t('copy_code_title')}
		class="save popup"
		on:click={() => handleCopy(surveyCode, 'code-popup')}
		><i class="symbol">content_copy</i><Tx text="copy_code" />
		<span class="popup-text top" id="code-popup"><Tx text="copied" /></span></button
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

	.survey-code {
		display: block;
		width: 7em;
		padding-bottom: 0.25em;
		font-size: 4em;
		font-weight: 700;
		cursor: text;
	}
</style>
