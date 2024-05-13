<script lang="ts">
	import { page } from '$app/stores';
	import type { PageData } from './$types';
	import QrCode from '$lib/components/QrCode.svelte';

	export let data: PageData;

	let url: string = $page.url.origin + '/' + data.code + '/fill';

	let isCopied: boolean = false;

	function copyCode(): void {
		if (window.isSecureContext) {
			navigator.clipboard.writeText(data.code);
			isCopied = true;
		} else {
			alert('The code could not be copied due to an insecure connection.');
		}
	}

	let innerWidth: number;
	function calculateSize(width: number): number {
		if (width < 768) {
			return 300;
		} else {
			return 400;
		}
	}
</script>

<svelte:window bind:innerWidth />

<div class="content">
	<h2>Survey created successfully.</h2>
	<h2>Access code:</h2>
	<h1>{data.code}</h1>
	<button title="Copy code" class="save" on:click={copyCode}
		><i class="material-symbols-rounded">content_copy</i>
		{#if isCopied}
			Copied!
		{:else}
			Copy
		{/if}</button
	>
	<a href="/{data.code}/fill" title="Go to fill page" class="qr-code">
		<QrCode data={url} size={calculateSize(innerWidth)} />
	</a>
</div>

<style>
	.content {
		text-align: center;
		text-shadow: 0px 4px 4px var(--shadow-color);
		color: var(--text-color);
		font-weight: bold;
	}

	h2 {
		margin: 0.5em 0em;
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
