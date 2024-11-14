<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import PageButtons from '$lib/components/global/PageButtons.svelte';

	export let numbers: Array<number>;

	$: currentPage = parseInt($page.url.pathname.substring($page.url.pathname.lastIndexOf('/') + 1));

	$: numbersPaginated = numbers.slice(currentPage * 10, currentPage * 10 + 10);
</script>

{#if numbersPaginated.length === 0}
	<div title="Number of answers" class="title empty">No answers yet!</div>
{:else}
	<table>
		<tr>
			<th title="Number of answer" id="info-header"><i class="symbol">numbers</i></th>
			<th title="Answers" id="title-header">Answers</th>
		</tr>
		{#each numbersPaginated as i}
			<tr>
				<td title="Answer no. {i + 1}" class="info-entry">{i + 1}.</td>
				<td title="View answer no. {i + 1}" class="title-entry"
					><button on:click={() => goto($page.url.pathname + '/' + i)}>Answer</button></td
				>
			</tr>
		{/each}
	</table>
	<div class="button-row">
		<PageButtons numEntries={numbers.length} />
	</div>
{/if}

<style>
	.info-entry {
		width: 2.3em;
		text-align: center;
		font-weight: 700 !important;
	}

	.button-row {
		justify-content: flex-end;
	}

	@media screen and (max-width: 768px) {
		.button-row {
			font-size: 0.9em;
		}
	}
</style>
