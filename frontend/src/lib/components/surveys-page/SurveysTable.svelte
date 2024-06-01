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
	table {
		width: 100%;
		border: 1px solid var(--border-color);
		border-collapse: separate;
		border-spacing: 0;
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--shadow-color);
		font-size: 1.25em;
		color: var(--text-color);
	}

	th,
	td {
		padding: 0.25em;
		text-align: left;
		text-shadow: 0px 4px 4px var(--shadow-color);
	}

	th {
		background-color: var(--secondary-dark-color);
		font-weight: bold;
		cursor: default;
		overflow-wrap: break-word;
	}

	td {
		overflow-wrap: anywhere;
	}

	tr:nth-child(2n + 1) td {
		background-color: var(--primary-dark-color);
	}

	tr:nth-child(2n + 2) td {
		background-color: var(--primary-color);
	}

	tr:first-of-type {
		border-radius: 4px 4px 0px 0px;
	}

	tr:last-of-type {
		border-radius: 0px 0px 4px 4px;
	}

	th:first-of-type {
		border-top-left-radius: 4px;
	}

	th:last-of-type {
		border-top-right-radius: 4px;
	}

	tr:last-of-type td:first-of-type {
		border-bottom-left-radius: 4px;
	}

	tr:last-of-type td:last-of-type {
		border-bottom-right-radius: 4px;
	}

	#title-header {
		width: 70%;
	}

	.title-entry,
	.code-entry {
		cursor: pointer;
	}

	.title-entry:hover,
	.code-entry:hover {
		background-color: var(--secondary-color);
	}

	.title-entry:active,
	.code-entry:active {
		background-color: var(--border-color);
	}

	#code-header {
		width: 12%;
	}

	#date-header {
		width: 18%;
	}

	.date-entry {
		cursor: default;
	}

	@media screen and (max-width: 767px) {
		table {
			font-size: 0.8em;
		}

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
