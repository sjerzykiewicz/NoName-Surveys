<script lang="ts">
	import { page } from '$app/stores';
	import type { PageData } from './$types';
	import QrCode from '$lib/components/QrCode.svelte';
	import { copyCode } from '$lib/utils/copyCode';

	export let data: PageData;

	let url: string = $page.url.origin + '/fill?code=' + data.code;

	let isCopied: boolean = false;

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
	<button
		title="Copy code"
		class="save"
		on:click={() => {
			copyCode(data.code);
			isCopied = true;
		}}
		><i class="material-symbols-rounded">content_copy</i>
		{isCopied ? 'Copied!' : 'Copy'}</button
	>
	<a href="/fill?code={data.code}" title="Fill out the survey" class="qr-code">
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
