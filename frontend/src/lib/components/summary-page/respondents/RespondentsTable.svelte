<script lang="ts">
	import PageButtons from '$lib/components/global/PageButtons.svelte';

	export let respondents;
	export let numRespondents;
</script>

{#if respondents.length === 0}
	<div title="Possible respondents" class="title empty">No possible respondents to display!</div>
{:else}
	<table>
		<tr>
			<th title="Possible respondents" id="title-header">Possible Respondents</th>
		</tr>
		{#each respondents as respondent}
			<tr>
				<td title={respondent} class="basic-entry">{respondent}</td>
			</tr>
		{/each}
	</table>
	<div class="button-row">
		<PageButtons numEntries={numRespondents} />
	</div>
{/if}

<style>
	.button-row {
		justify-content: flex-end;
	}
</style>
