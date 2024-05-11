<script lang="ts">
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import { page } from '$app/stores';
	import type { PageData } from './$types';

	export let data: PageData;

	let isCopied: boolean = false;

	function copyCode(): void {
		if (window.isSecureContext) {
			navigator.clipboard.writeText(data.code);
			isCopied = true;
		} else {
			alert('The code could not be copied due to an insecure connection.');
		}
	}
</script>

<Header>
	<div class="title">Survey created successfully.</div>
</Header>

<Content>
	<div class="content">
		<h2>Access code:</h2>
		<h1>{data.code}</h1>
		<a href="/{data.code}/fill" title="Go to fill page">
			<img
				src="https://api.qrserver.com/v1/create-qr-code/?data={$page.url.origin}/{data.code}/fill"
				alt="QR Code"
			/>
		</a>
	</div>
</Content>

<Footer>
	<button title="Copy code" class="save" on:click={copyCode}
		><i class="material-symbols-rounded">content_copy</i>
		{#if isCopied}
			Copied!
		{:else}
			Copy
		{/if}</button
	>
</Footer>

<style>
	.content {
		text-align: center;
		text-shadow: 0px 4px 4px var(--shadow-color);
		color: var(--text-color);
		font-weight: bold;
	}

	h2 {
		margin: 0em;
		font-size: 3em;
		cursor: default;
	}

	h1 {
		margin: 0em;
		margin-bottom: 0.25em;
		font-size: 7em;
		cursor: text;
	}

	img {
		width: 50%;
	}

	@media screen and (max-width: 767px) {
		h2 {
			font-size: 2em;
		}

		h1 {
			font-size: 3.5em;
		}
	}
</style>
