<script lang="ts">
	import { goto } from '$app/navigation';
	import { copyCode } from '$lib/utils/copyCode';

	let copiedIndex: number;

	export let survey_list: {
		title: string;
		uses_crypto: boolean;
		code: string;
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
				title="Click to view summary"
				class="title-entry"
				on:click={() => goto('/' + entry.code + '/summary')}>{entry.title}</td
			>
			<td
				title={copiedIndex === entryIndex ? 'Copied!' : 'Click to copy code'}
				class="code-entry"
				on:click={() => {
					copyCode(entry.code);
					copiedIndex = entryIndex;
				}}>{entry.code}</td
			>
			<td title="Creation date" class="date-entry">{entry.creation_date}</td>
		</tr>
	{/each}
</table>

<style>
	#title-header {
		width: 70%;
	}

	#code-header {
		width: 12%;
	}

	#date-header {
		width: 18%;
	}

	@media screen and (max-width: 767px) {
		#title-header {
			width: 55%;
		}

		#code-header {
			width: 19%;
		}

		#date-header {
			width: 26%;
		}
	}
</style>
