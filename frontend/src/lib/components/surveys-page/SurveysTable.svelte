<script lang="ts">
	import { goto, invalidateAll } from '$app/navigation';
	import QrCodeModal from '$lib/components/QrCodeModal.svelte';
	import { page } from '$app/stores';

	let innerWidth: number;
	let isModalHidden: boolean = true;
	let selectedCode: string;

	export let survey_list: {
		title: string;
		survey_code: string;
		creation_date: string;
		uses_cryptographic_module: boolean;
		is_owned_by_user: boolean;
		group_size: number;
	}[];

	function deleteSurvey(i: number) {
		fetch('/api/surveys/delete', {
			method: 'POST',
			body: JSON.stringify({
				user_email: $page.data.session?.user?.email,
				survey_code: survey_list[i].survey_code
			}),
			headers: {
				'Content-Type': 'application/json'
			}
		})
			.then(() => {
				survey_list.splice(i, 1);
				invalidateAll();
			})
			.catch(() => alert('Error deleting survey'));
	}

	const EMPTY_TOOLTIP_BREAKPOINT = 423;
	const TABLE_TOOLTIP_BREAKPOINT = 1239;
</script>

<svelte:window bind:innerWidth />

<QrCodeModal bind:isHidden={isModalHidden} title="Access Code" surveyCode={selectedCode} />

{#if survey_list.length === 0}
	<div class="info-row">
		<div title="Surveys" class="title empty">No surveys yet!</div>
		<div class="tooltip">
			<i class="material-symbols-rounded">info</i>
			<span class="tooltip-text {innerWidth <= EMPTY_TOOLTIP_BREAKPOINT ? 'bottom' : 'right'}">
				To create a survey, click on the "Create" tab at the top of the page or the button below.
				All your created surveys will be stored on this page.
			</span>
		</div>
	</div>
{:else}
	<table>
		<tr>
			<th title="Survey title" id="title-header" colspan="3">Survey Title</th>
			<th title="Group size" id="group-header">Size</th>
			<th title="Access code" id="code-header">Code</th>
			<th title="Creation date" id="date-header" colspan="2">Date</th>
		</tr>
		{#each survey_list.toReversed() as entry, entryIndex}
			<tr>
				<td class="info-entry tooltip">
					{#if entry.uses_cryptographic_module}
						<i class="material-symbols-rounded">encrypted</i>
						<span class="tooltip-text {innerWidth <= TABLE_TOOLTIP_BREAKPOINT ? 'right' : 'left'}"
							>This survey has an established group of possible respondents.</span
						>
					{:else}
						<i class="material-symbols-rounded">public</i>
						<span class="tooltip-text {innerWidth <= TABLE_TOOLTIP_BREAKPOINT ? 'right' : 'left'}"
							>Everyone can submit an answer to this survey.</span
						>
					{/if}
				</td>
				<td class="info-entry tooltip access">
					{#if entry.is_owned_by_user}
						<i class="material-symbols-rounded">verified</i>
						<span class="tooltip-text {innerWidth <= TABLE_TOOLTIP_BREAKPOINT ? 'right' : 'left'}"
							>You are the owner of this survey.</span
						>
					{:else}
						<i class="material-symbols-rounded">share</i>
						<span class="tooltip-text {innerWidth <= TABLE_TOOLTIP_BREAKPOINT ? 'right' : 'left'}"
							>Results of this survey have been shared with you.</span
						>
					{/if}
				</td>
				<td
					title="View the summary"
					class="title-entry"
					on:click={() => goto('/' + entry.survey_code + '/summary')}>{entry.title}</td
				>
				{#if entry.uses_cryptographic_module}
					<td
						title="View the respondents"
						class="code-entry"
						on:click={() => goto('/' + entry.survey_code + '/summary#survey-respondents')}
					>
						{entry.group_size}
					</td>
				{:else}
					<td title="Not Available" class="info-entry">N/A</td>
				{/if}
				<td
					title="View QR code"
					class="code-entry"
					on:click={() => {
						selectedCode = entry.survey_code;
						isModalHidden = false;
					}}
				>
					{entry.survey_code}
				</td>
				<td title="Creation date" class="date-entry">{entry.creation_date}</td>
				<td
					title="Delete the survey"
					class="button-entry"
					class:disabled={!entry.is_owned_by_user}
					on:click={() => {
						if (entry.is_owned_by_user) deleteSurvey(survey_list.length - entryIndex - 1);
					}}
				>
					<i class="material-symbols-rounded">delete</i></td
				>
			</tr>
		{/each}
	</table>
{/if}
<button title="Create a survey" on:click={() => goto('/create')}>
	<i class="material-symbols-rounded">add</i>Survey
</button>

<style>
	.tooltip.access {
		--tooltip-width: 13em;
	}

	button {
		font-size: 1.25em;
		margin-top: 0.5em;
	}

	button i {
		margin-right: 0.15em;
		font-variation-settings: 'wght' 700;
	}

	#group-header {
		width: 8%;
	}

	#code-header {
		width: 11%;
	}

	#date-header {
		width: 14%;
	}

	@media screen and (max-width: 767px) {
		button {
			font-size: 1em;
		}

		#group-header {
			width: 13%;
		}

		#code-header {
			width: 18%;
		}

		#date-header {
			width: 25%;
		}
	}
</style>
