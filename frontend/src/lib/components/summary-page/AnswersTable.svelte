<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';

	export let numbers: Array<number>;
</script>

<table>
	<tr>
		<th title="Number of answer" id="info-header"
			><i class="material-symbols-rounded">numbers</i></th
		>
		<th title="Answers" id="title-header">Answers</th>
	</tr>
	{#each numbers as i}
		<tr>
			<td title="Answer no. {i + 1}" class="info-entry">{i + 1}.</td>
			<td title="View answer no. {i + 1}" class="title-entry"
				><button on:click={() => goto($page.url.pathname + '/' + i)}>Answer</button></td
			>
		</tr>
	{/each}
</table>

<style>
	.info-entry {
		text-align: center;
		font-weight: 700;
	}
</style>
