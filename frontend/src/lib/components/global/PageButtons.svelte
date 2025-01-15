<script lang="ts">
	import { page } from '$app/stores';
	import { changePage } from '$lib/utils/changePage';
	import { ENTRIES_PER_PAGE } from '$lib/stores/global';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);
	export let numEntries: number;

	let pageInput: HTMLInputElement;

	$: currentPage = parseInt($page.url.pathname.substring($page.url.pathname.lastIndexOf('/') + 1));
	$: minPage = 0;
	$: maxPage = Math.ceil(numEntries / $ENTRIES_PER_PAGE) - 1;

	async function firstPage() {
		if (currentPage !== minPage) await changePage($page.url.pathname, minPage);
	}

	async function previousPage() {
		if (currentPage > minPage) await changePage($page.url.pathname, currentPage - 1);
	}

	async function nextPage() {
		if (currentPage < maxPage) await changePage($page.url.pathname, currentPage + 1);
	}

	async function lastPage() {
		if (currentPage !== maxPage) await changePage($page.url.pathname, maxPage);
	}
</script>

{#if numEntries > 0}
	<div class="page-buttons">
		<div class="prev-buttons">
			<button title={$t('first_page')} disabled={currentPage === minPage} on:click={firstPage}
				><i class="symbol">first_page</i></button
			>
			<button title={$t('previous_page')} disabled={currentPage <= minPage} on:click={previousPage}
				><i class="symbol">chevron_left</i></button
			>
		</div>
		<form
			on:submit|preventDefault={() => changePage($page.url.pathname, parseInt(pageInput.value) - 1)}
		>
			<label title={$t('current_page')} class="page-number">
				<input
					id="page-input"
					name="page-input"
					type="number"
					min={minPage + 1}
					max={maxPage + 1}
					autocomplete="off"
					value={currentPage + 1}
					bind:this={pageInput}
				/>
				<div id="slash">/</div>
				<div id="page-limit">{maxPage + 1}</div>
			</label>
		</form>
		<div class="next-buttons">
			<button title={$t('next_page')} disabled={currentPage >= maxPage} on:click={nextPage}
				><i class="symbol">chevron_right</i></button
			>
			<button title={$t('last_page')} disabled={currentPage === maxPage} on:click={lastPage}
				><i class="symbol">last_page</i></button
			>
		</div>
	</div>
{/if}

<style>
	.page-buttons {
		display: flex;
		justify-content: center;
		align-items: stretch;
		box-shadow: var(--shadow);
		border-radius: 5px;
		border: 1px solid var(--border-color-1);
		overflow: hidden;
	}

	.prev-buttons,
	.next-buttons {
		display: flex;
	}

	.prev-buttons button,
	.next-buttons button {
		box-shadow: none;
		border: none;
		border-radius: 0px;
		padding-left: 0em;
		padding-right: 0em;
	}

	.prev-buttons button {
		border-right: 1px solid var(--border-color-1);
	}

	.next-buttons button {
		border-left: 1px solid var(--border-color-1);
	}

	.page-number {
		display: flex;
		padding: 0.25em;
		background-color: var(--secondary-color-2);
		color: var(--text-color-1);
		text-align: center;
		text-shadow: var(--shadow);
		font-weight: 700;
		cursor: text;
	}

	#page-input {
		padding: 0em;
		margin: 0em;
		border: none;
		width: 1.5em;
		background-color: var(--secondary-color-2);
		color: var(--text-color-1);
		font-size: 1em;
		text-align: center;
		text-shadow: var(--shadow);
		font-weight: 700;
	}

	#page-input::-webkit-outer-spin-button,
	#page-input::-webkit-inner-spin-button {
		appearance: none;
		-webkit-appearance: none;
	}

	#page-input[type='number'] {
		appearance: textfield;
		-moz-appearance: textfield;
	}

	#slash {
		width: 1em;
	}

	#page-limit {
		width: 1.5em;
	}

	@media screen and (max-width: 768px) {
		#page-input {
			width: 1.25em;
		}

		#slash {
			width: 0.75em;
		}

		#page-limit {
			width: 1.25em;
		}
	}
</style>
