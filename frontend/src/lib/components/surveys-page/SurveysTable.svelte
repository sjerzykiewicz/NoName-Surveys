<script lang="ts">
	import { goto, invalidateAll } from '$app/navigation';
	import QrCodeModal from '$lib/components/QrCodeModal.svelte';
	import { page } from '$app/stores';
	import { errorModalContent, isErrorModalHidden, S, XL } from '$lib/stores/global';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';

	export let survey_list: {
		title: string;
		survey_code: string;
		creation_date: string;
		uses_cryptographic_module: boolean;
		is_owned_by_user: boolean;
		group_size: number;
	}[];

	let innerWidth: number;
	let isModalHidden: boolean = true;
	let selectedCode: string;
	let selectedSurveysToRemove: typeof survey_list = [];

	$: ownedSurveys = survey_list.filter((s) => s.is_owned_by_user);

	$: allSelected =
		selectedSurveysToRemove.length === ownedSurveys.length && selectedSurveysToRemove.length > 0;

	function toggleAll() {
		selectedSurveysToRemove = allSelected ? [] : [...ownedSurveys];
	}

	function formatDate(isoString: string) {
		return new Date(isoString);
	}

	async function deleteSurveys() {
		selectedSurveysToRemove.forEach(async (survey, i) => {
			const response = await fetch('/api/surveys/delete', {
				method: 'POST',
				body: JSON.stringify({
					user_email: $page.data.session?.user?.email,
					survey_code: survey.survey_code
				}),
				headers: {
					'Content-Type': 'application/json'
				}
			});

			if (!response.ok) {
				const body = await response.json();
				$errorModalContent = getErrorMessage(body.detail);
				$isErrorModalHidden = false;
				return;
			}

			survey_list.splice(i, 1);
		});

		selectedSurveysToRemove = [];
		invalidateAll();
	}
</script>

<svelte:window bind:innerWidth />

<QrCodeModal bind:isHidden={isModalHidden} title="Access Code" surveyCode={selectedCode} />

{#if survey_list.length === 0}
	<div class="info-row">
		<div title="Surveys" class="title empty">No surveys yet!</div>
		<div class="tooltip">
			<i class="material-symbols-rounded">info</i>
			<span class="tooltip-text {innerWidth <= $S ? 'bottom' : 'right'}">
				To create a survey, click on the "Create" tab at the top of the page or the button below.
				All your created surveys will be stored on this page.
			</span>
		</div>
	</div>
{:else}
	<table>
		<tr>
			<th title="Select all" class="checkbox-entry" class:disabled={ownedSurveys.length === 0}
				><label
					><input
						type="checkbox"
						disabled={ownedSurveys.length === 0}
						on:change={toggleAll}
						checked={allSelected}
					/></label
				></th
			>
			<th title="Survey information" id="info-header" colspan="2">Info</th>
			<th title="Survey title" id="title-header">Survey Title</th>
			<th title="Group size" id="group-header">Group Size</th>
			<th title="Access code" id="code-header">Access Code</th>
			<th title="Creation date" id="date-header">Creation Date</th>
		</tr>
		{#each survey_list as survey}
			<tr>
				<td
					title="Select {survey.title}"
					class="checkbox-entry"
					class:disabled={!survey.is_owned_by_user}
					><label>
						<input
							type="checkbox"
							disabled={!survey.is_owned_by_user}
							bind:group={selectedSurveysToRemove}
							value={survey}
						/>
					</label></td
				>
				<td class="info-entry tooltip">
					{#if survey.uses_cryptographic_module}
						<i class="material-symbols-rounded">encrypted</i>
						<span class="tooltip-text {innerWidth <= $XL ? 'right' : 'left'}"
							>This survey has an established group of possible respondents.</span
						>
					{:else}
						<i class="material-symbols-rounded">public</i>
						<span class="tooltip-text {innerWidth <= $XL ? 'right' : 'left'}"
							>Everyone can submit an answer to this survey.</span
						>
					{/if}
				</td>
				<td class="info-entry tooltip access">
					{#if survey.is_owned_by_user}
						<i class="material-symbols-rounded">verified</i>
						<span class="tooltip-text {innerWidth <= $XL ? 'right' : 'left'}"
							>You are the owner of this survey.</span
						>
					{:else}
						<i class="material-symbols-rounded">share</i>
						<span class="tooltip-text {innerWidth <= $XL ? 'right' : 'left'}"
							>Results of this survey have been shared with you.</span
						>
					{/if}
				</td>
				<td
					title="View the summary"
					class="title-entry"
					on:click={() => goto('/' + survey.survey_code + '/summary')}>{survey.title}</td
				>
				{#if survey.uses_cryptographic_module}
					<td
						title="View the respondents"
						class="code-entry"
						on:click={() => goto('/' + survey.survey_code + '/summary#survey-respondents')}
					>
						{survey.group_size}
					</td>
				{:else}
					<td title="Not Available" class="info-entry">N/A</td>
				{/if}
				<td
					title="View QR code"
					class="code-entry"
					on:click={() => {
						selectedCode = survey.survey_code;
						isModalHidden = false;
					}}
				>
					{survey.survey_code}
				</td>
				<td title="Creation date" class="date-entry">{formatDate(survey.creation_date)}</td>
			</tr>
		{/each}
	</table>
{/if}
<div class="button-row">
	<button title="Create a survey" class="add-survey" on:click={() => goto('/create')}>
		<i class="material-symbols-rounded">add</i>Survey
	</button>
	{#if survey_list.length > 0}
		<button
			title="Delete selected surveys"
			class="delete-survey"
			disabled={selectedSurveysToRemove.length === 0}
			on:click={deleteSurveys}
		>
			<i class="material-symbols-rounded">delete</i>Delete
		</button>
	{/if}
</div>

<style>
	.tooltip.access {
		--tooltip-width: 13em;
	}

	#group-header {
		width: 8%;
	}

	#code-header {
		width: 10%;
	}

	#date-header {
		width: 12%;
	}

	@media screen and (max-width: 768px) {
		#group-header {
			width: 15%;
		}

		#code-header {
			width: 18%;
		}

		#date-header {
			width: 21%;
		}
	}
</style>
