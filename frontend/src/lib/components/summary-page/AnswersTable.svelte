<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';

	export let numbers: Array<number>;
</script>

<table>
	<tr>
		<th title="Answers" id="title-header">Answers</th>
	</tr>
	{#each numbers as i}
		<tr>
			<td
				title="View answer no. {i + 1}"
				class="title-entry"
				on:click={() => goto($page.url.pathname + '/' + i)}>{i + 1}. Answer</td
			>
		</tr>
	{/each}
</table>
