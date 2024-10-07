<script lang="ts">
	import Modal from '$lib/components/Modal.svelte';
	import QrCode from '$lib/components/QrCode.svelte';
	import noname_black from '$lib/assets/noname_black.png';
	import { page } from '$app/stores';
	import { copy } from '$lib/utils/copy';
	import { popup } from '$lib/utils/popup';
	import { MOBILE_DEVICE_BREAKPOINT } from '$lib/stores/global';

	export let isHidden: boolean = true;
	export let title: string;
	export let surveyCode: string;

	async function handleCopy(str: string, id: string) {
		if (copy(str)) {
			popup(id);
		}
	}

	let innerWidth: number;
	let innerHeight: number;

	const MODAL_BREAKPOINT = 707;
</script>

<svelte:window bind:innerWidth bind:innerHeight />

<Modal
	icon="qr_code_2"
	{title}
	bind:isHidden
	width={innerWidth > $MOBILE_DEVICE_BREAKPOINT && innerHeight > MODAL_BREAKPOINT ? 30 : 20}
>
	<div slot="content" class="content">
		<span class="survey-code">{surveyCode}</span>
		<a href="/fill?code={surveyCode}" title="Fill out the survey" class="qr-code">
			{#if !isHidden}
				<QrCode
					code={surveyCode}
					codeSize={innerWidth > $MOBILE_DEVICE_BREAKPOINT && innerHeight > MODAL_BREAKPOINT
						? 360
						: 260}
					codeMargin={3}
					image={noname_black}
					imageMargin={6}
				/>
			{/if}
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
