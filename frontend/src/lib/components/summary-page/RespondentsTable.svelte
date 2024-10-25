<script lang="ts">
	export let respondents;
</script>

<div title="Possible respondents" class="title respondent-list" id="survey-respondents">
	The following users can submit answers to this survey:
</div>
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

<style>
	.title.respondent-list {
		margin-top: 1em;
		margin-bottom: 0.1em;
	}
</style>
