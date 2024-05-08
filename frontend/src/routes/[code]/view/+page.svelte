<script lang="ts">
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

<div class="content">
	<h2>Survey created successfully.</h2>
	<h2>Access code:</h2>
	<h1>{data.code}</h1>
	<button class="save" on:click={copyCode}
		><i class="material-symbols-rounded">content_copy</i>Copy</button
	>
	{#if isCopied}
		<h2>Copied!</h2>
	{/if}
</div>

<style>
	.content {
		text-align: center;
		text-shadow: 0px 4px 4px var(--shadow-color);
		color: var(--text-color);
		font-weight: bold;
	}

	h2 {
		font-size: 3em;
		cursor: default;
	}

	h1 {
		margin: 0em;
		font-size: 7em;
		cursor: text;
	}

	.save {
		margin: auto;
		margin-top: 1em;
		font-size: 2em;
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
