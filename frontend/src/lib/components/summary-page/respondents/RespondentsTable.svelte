<script lang="ts">
	export let respondents;
</script>

{#if respondents.length === 0}
	<div title="Possible respondents" class="title empty">No possible respondents to display!</div>
{:else}
	<table>
		<tr>
			<th title="Possible respondents" id="title-header">Possible Respondents</th>
		</tr>
		{#each respondents.toSorted() as respondent}
			<tr>
				<td title={respondent} class="basic-entry">{respondent}</td>
			</tr>
		{/each}
	</table>
{/if}
