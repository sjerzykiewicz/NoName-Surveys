<script lang="ts">
	import type { PageData } from './$types';
	import QrCode from '$lib/components/QrCode.svelte';
	import { copyCode } from '$lib/utils/copyCode';
	import Content from '$lib/components/Content.svelte';
	import { delay } from '$lib/utils/delay';
	import { cubicInOut } from 'svelte/easing';
	import { fade } from 'svelte/transition';

	export let data: PageData;

	let isCopyPopupVisible: boolean = false;
	let innerWidth: number;

	function calculateSize(width: number): number {
		if (width < 768) {
			return 300;
		}
		return 400;
	}
</script>

<svelte:window bind:innerWidth />

<Content>
	<h2 id="title">Survey created successfully.</h2>
	<h2>Access code:</h2>
	<h1>{data.code}</h1>
	<button
		title="Copy the code"
		class="save popup"
		on:click={async () => {
			copyCode(data.code);
			isCopyPopupVisible = true;
			await delay(2000);
			isCopyPopupVisible = false;
		}}
		><i class="material-symbols-rounded">content_copy</i>Copy
		{#if isCopyPopupVisible}
			<span class="popup-text left" transition:fade={{ duration: 200, easing: cubicInOut }}
				>Copied!</span
			>
		{/if}</button
	>
	<a href="/fill?code={data.code}" title="Fill out the survey" class="qr-code">
		<QrCode code={data.code} size={calculateSize(innerWidth)} />
	</a>
</Content>

<style>
	.popup .popup-text.left {
		--tooltip-width: 4em;
		font-size: 0.75em;
	}

	h2#title {
		border-bottom: 1px solid var(--border-color);
		padding: 0.25em 0em 0.5em;
	}

	h2,
	h1 {
		color: var(--text-color);
		text-align: center;
		text-shadow: 0px 4px 4px var(--shadow-color);
		font-weight: bold;
	}

	h2 {
		margin: 0em;
		padding-top: 0.5em;
		font-size: 3em;
		cursor: default;
	}

	h1 {
		margin: 0em;
		font-size: 7em;
		cursor: text;
	}

	.save {
		font-size: 2em;
		margin: 0.5em auto;
	}

	.qr-code {
		display: flex;
		margin: 2em auto;
		width: fit-content;
	}

	@media screen and (max-width: 767px) {
		h2 {
			font-size: 2em;
		}

		h1 {
			font-size: 3.5em;
		}

		.save {
			font-size: 1.5em;
		}
	}
</style>
