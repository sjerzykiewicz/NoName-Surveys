<script lang="ts">
	import { goto } from '$app/navigation';

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
	{#each survey_list.toReversed() as entry}
		<tr>
			<td
				title="Click to view summary"
				class="title-entry"
				on:click={() => goto('/' + entry.code + '/summary')}>{entry.title}</td
			>
			<td title="Access code" class="code-entry">{entry.code}</td>
			<td title="Creation date" class="date-entry">{entry.creation_date}</td>
		</tr>
	{/each}
</table>

<style>
	table {
		width: 100%;
		border-collapse: collapse;
		box-shadow: 0px 4px 4px var(--shadow-color);
		font-size: 1.25em;
		color: var(--text-color);
	}

	th,
	td {
		border: 1px solid var(--border-color);
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

	tr:nth-child(even) {
		background-color: var(--primary-color);
	}

	tr:nth-child(odd) {
		background-color: var(--primary-dark-color);
	}

	#title-header {
		width: 70%;
	}

	.title-entry {
		cursor: pointer;
	}

	.title-entry:hover {
		background-color: var(--secondary-color);
	}

	#code-header {
		width: 12%;
	}

	.code-entry {
		cursor: text;
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
