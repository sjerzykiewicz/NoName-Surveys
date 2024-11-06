<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { delay } from '$lib/utils/delay';

	$: currentPage = parseInt(
		$page.url.pathname.substring($page.url.pathname.lastIndexOf('/') + 1, $page.url.pathname.length)
	);
	$: minPage = 0;
	$: maxPage = 4;

	async function changePage(numPage: number) {
		await goto($page.url.pathname.substring(0, $page.url.pathname.lastIndexOf('/') + 1) + numPage, {
			keepFocus: true,
			noScroll: true
		});
		await delay(200);
	}

	async function firstPage() {
		if (currentPage !== minPage) await changePage(minPage);
	}

	async function previousPage() {
		if (currentPage > minPage) await changePage(currentPage - 1);
	}

	async function nextPage() {
		if (currentPage < maxPage) await changePage(currentPage + 1);
	}

	async function lastPage() {
		if (currentPage !== maxPage) await changePage(maxPage);
	}
</script>

<div class="page-buttons">
	<div class="prev-buttons">
		<button title="First page" disabled={currentPage === minPage} on:click={firstPage}
			><i class="material-symbols-rounded">first_page</i></button
		>
		<button title="Previous page" disabled={currentPage <= minPage} on:click={previousPage}
			><i class="material-symbols-rounded">chevron_left</i></button
		>
	</div>
	<label title="Current page" class="page-number">
		<input
			id="page-input"
			name="page-input"
			type="number"
			min={minPage + 1}
			max={maxPage + 1}
			autocomplete="off"
		/>
		<div id="slash">/</div>
		<div id="page-limit">{maxPage + 1}</div>
	</label>
	<div class="next-buttons">
		<button title="Next page" disabled={currentPage >= maxPage} on:click={nextPage}
			><i class="material-symbols-rounded">chevron_right</i></button
		>
		<button title="Last page" disabled={currentPage === maxPage} on:click={lastPage}
			><i class="material-symbols-rounded">last_page</i></button
		>
	</div>
</div>

<style>
	.page-buttons {
		display: flex;
		justify-content: center;
		align-items: stretch;
		box-shadow: 0px 4px 4px var(--shadow-color);
		border-radius: 5px;
		border: 1px solid var(--border-color);
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
		border-right: 1px solid var(--border-color);
	}

	.next-buttons button {
		border-left: 1px solid var(--border-color);
	}

	.page-number {
		display: flex;
		padding: 0.25em;
		background-color: var(--secondary-dark-color);
		color: var(--text-color);
		text-align: center;
		text-shadow: 0px 4px 4px var(--shadow-color);
		font-weight: 700;
		cursor: text;
	}

	#page-input {
		padding: 0em;
		margin: 0em;
		border: none;
		width: 1.5em;
		background-color: var(--secondary-dark-color);
		color: var(--text-color);
		font-size: 1em;
		text-align: center;
		text-shadow: 0px 4px 4px var(--shadow-color);
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
		width: 0.5em;
	}

	#page-limit {
		width: 1.5em;
	}
</style>
