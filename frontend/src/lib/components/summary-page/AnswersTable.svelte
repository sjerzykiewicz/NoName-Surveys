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
				title="Click to view answer no. {i + 1}"
				class="title-entry"
				on:click={() => goto($page.url.pathname + '/' + i)}>{i + 1}. Answer</td
			>
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
		width: 100%;
	}

	.title-entry {
		cursor: pointer;
	}

	.title-entry:hover {
		background-color: var(--secondary-color);
	}

	.title-entry:active {
		background-color: var(--border-color);
	}

	@media screen and (max-width: 767px) {
		table {
			font-size: 0.8em;
		}
	}
</style>
