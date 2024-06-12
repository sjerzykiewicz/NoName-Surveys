<script lang="ts">
	import { goto } from '$app/navigation';
	import { copyCode } from '$lib/utils/copyCode';

	let copiedIndex: number;

	export let survey_list: {
		title: string;
		uses_cryptographic_module: boolean;
		survey_code: string;
		creation_date: string;
	}[];
</script>

<table>
	<tr>
		<th title="Survey title" id="title-header">Survey Title</th>
		<th title="Access code" id="code-header">Code</th>
		<th title="Creation date" id="date-header">Date</th>
	</tr>
	{#each survey_list.toReversed() as entry, entryIndex}
		<tr>
			<td
				title="View the summary"
				class="title-entry"
				on:click={() => goto('/' + entry.survey_code + '/summary')}>{entry.title}</td
			>
			<td
				title={copiedIndex === entryIndex ? 'Copied!' : 'Copy the code'}
				class="code-entry"
				on:click={() => {
					copyCode(entry.survey_code);
					copiedIndex = entryIndex;
				}}>{entry.survey_code}</td
			>
			<td title="Creation date" class="date-entry">{entry.creation_date}</td>
		</tr>
	{/each}
</table>

<style>
	#code-header {
		width: 12%;
	}

	#date-header {
		width: 18%;
	}

	@media screen and (max-width: 767px) {
		#code-header {
			width: 20%;
		}

		#date-header {
			width: 27%;
		}
	}
</style>
