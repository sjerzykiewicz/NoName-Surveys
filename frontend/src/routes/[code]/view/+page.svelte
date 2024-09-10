<script lang="ts">
	import type { PageData } from './$types';
	import QrCode from '$lib/components/QrCode.svelte';
	import { copyCode } from '$lib/utils/copyCode';
	import Content from '$lib/components/Content.svelte';

	export let data: PageData;

	let isCopied: boolean = false;
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
		class="save"
		on:click={() => {
			copyCode(data.code);
			isCopied = true;
		}}
		><i class="material-symbols-rounded">content_copy</i>
		{isCopied ? 'Copied!' : 'Copy'}</button
	>
	<a href="/fill?code={data.code}" title="Fill out the survey" class="qr-code">
		<QrCode code={data.code} size={calculateSize(innerWidth)} />
	</a>
</Content>

<style>
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
