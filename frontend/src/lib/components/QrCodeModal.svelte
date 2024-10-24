<script lang="ts">
	import Modal from '$lib/components/Modal.svelte';
	import QrCode from '$lib/components/QrCode.svelte';
	import noname_black from '$lib/assets/noname_black.png';
	import { page } from '$app/stores';
	import { copy } from '$lib/utils/copy';
	import { popup } from '$lib/utils/popup';
	import { errorModalContent, isErrorModalHidden, M } from '$lib/stores/global';

	export let isHidden: boolean = true;
	export let title: string;
	export let surveyCode: string;

	async function handleCopy(str: string, id: string) {
		if (copy(str)) {
			popup(id);
		} else {
			$errorModalContent = 'Could not copy due to an insecure connection.';
			$isErrorModalHidden = false;
		}
	}

	let innerWidth: number;
	let innerHeight: number;
</script>

<svelte:window bind:innerWidth bind:innerHeight />

<Modal icon="qr_code_2" {title} bind:isHidden width={innerWidth > $M && innerHeight > $M ? 30 : 20}>
	<div slot="content" class="content">
		<span class="survey-code">{surveyCode}</span>
		<a href="/fill?code={surveyCode}" title="Fill out the survey" class="qr-code">
			<QrCode
				code={surveyCode}
				codeSize={innerWidth > $M && innerHeight > $M ? 360 : 260}
				codeMargin={3}
				image={noname_black}
				imageMargin={6}
			/>
		</a>
	</div>
	<button
		title="Copy the link"
		class="save popup"
		on:click={() => handleCopy($page.url.origin + '/fill?code=' + surveyCode, 'link-popup')}
		><i class="material-symbols-rounded">content_copy</i>Copy Link
		<span class="popup-text top" id="link-popup">Copied!</span></button
	>
	<button
		title="Copy the code"
		class="save popup"
		on:click={() => handleCopy(surveyCode, 'code-popup')}
		><i class="material-symbols-rounded">content_copy</i>Copy Code
		<span class="popup-text top" id="code-popup">Copied!</span></button
	>
</Modal>

<style>
	.popup .popup-text {
		--tooltip-width: 4em;
	}

	.content {
		display: inherit;
		flex-flow: inherit;
		justify-content: inherit;
		align-items: inherit;
	}

	.survey-code {
		display: block;
		width: 7em;
		padding-bottom: 0.25em;
		font-size: 4em;
		font-weight: 700;
		cursor: text;
	}

	.qr-code {
		padding-bottom: 1em;
	}
</style>
