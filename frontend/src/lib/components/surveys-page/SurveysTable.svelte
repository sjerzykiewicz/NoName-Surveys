<script lang="ts">
	import { goto } from '$app/navigation';
	import QrCodeModal from '$lib/components/global/QrCodeModal.svelte';
	import { S, XL } from '$lib/stores/global';
	import { page } from '$app/stores';

	export let surveys: {
		title: string;
		survey_code: string;
		creation_date: string;
		uses_cryptographic_module: boolean;
		is_owned_by_user: boolean;
		group_size: number;
	}[];
	export let selectedSurveysToRemove: string[] = [];

	let innerWidth: number;
	let selectedCode: string;
	let isModalHidden: boolean = true;

	$: ownedSurveyCodes = surveys.filter((s) => s.is_owned_by_user).map((s) => s.survey_code);

	$: allSelected =
		selectedSurveysToRemove.length === ownedSurveyCodes.length &&
		selectedSurveysToRemove.length > 0;

	function toggleAll() {
		selectedSurveysToRemove = allSelected ? [] : [...ownedSurveyCodes];
	}

	function formatDate(isoString: string): string {
		return new Date(isoString).toLocaleString();
	}
</script>

<svelte:window bind:innerWidth />

<QrCodeModal title="Access Code" bind:isHidden={isModalHidden} surveyCode={selectedCode} />

{#if surveys.length === 0}
	<div class="info-row">
		<div title="Surveys" class="title empty">No surveys yet!</div>
		<div class="tooltip">
			<i class="symbol">info</i>
			<span class="tooltip-text {innerWidth <= $S ? 'bottom' : 'right'}">
				To create a survey, click on the "Create" tab at the top of the page or the button below.
				All your created surveys will be stored on this page.
			</span>
		</div>
	</div>
{:else}
	<table>
		<tr>
			<th title="Select all" class="checkbox-entry" class:disabled={ownedSurveyCodes.length === 0}
				><label
					><input
						type="checkbox"
						disabled={ownedSurveyCodes.length === 0}
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
		{#each surveys as survey}
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
							value={survey.survey_code}
						/>
					</label></td
				>
				<td class="info-entry tooltip">
					{#if survey.uses_cryptographic_module}
						<i class="symbol">encrypted</i>
						<span class="tooltip-text {innerWidth <= $XL ? 'right' : 'left'}"
							>This survey has an established group of possible respondents.</span
						>
					{:else}
						<i class="symbol">public</i>
						<span class="tooltip-text {innerWidth <= $XL ? 'right' : 'left'}"
							>Everyone can submit an answer to this survey.</span
						>
					{/if}
				</td>
				<td class="info-entry tooltip access">
					{#if survey.is_owned_by_user}
						<i class="symbol">verified</i>
						<span class="tooltip-text {innerWidth <= $XL ? 'right' : 'left'}"
							>You are the owner of this survey.</span
						>
					{:else}
						<i class="symbol">share</i>
						<span class="tooltip-text {innerWidth <= $XL ? 'right' : 'left'}"
							>Results of this survey have been shared with you.</span
						>
					{/if}
				</td>
				<td title="View the summary" class="title-entry"
					><button on:click={() => goto($page.url.pathname + '/' + survey.survey_code)}
						>{survey.title}</button
					></td
				>
				{#if survey.uses_cryptographic_module}
					<td title="View possible respondents" class="code-entry"
						><button
							on:click={() =>
								goto($page.url.pathname + '/' + survey.survey_code + '/respondents/0')}
							>{survey.group_size}</button
						>
					</td>
				{:else}
					<td title="Not available for public survey" class="info-entry">N/A</td>
				{/if}
				<td title="View QR code" class="code-entry"
					><button
						on:click={() => {
							selectedCode = survey.survey_code;
							isModalHidden = false;
						}}>{survey.survey_code}</button
					>
				</td>
				<td title="Creation date" class="date-entry">{formatDate(survey.creation_date)}</td>
			</tr>
		{/each}
	</table>
{/if}

<style>
	.tooltip.access {
		--tooltip-width: 13em;
	}

	#group-header {
		width: 8%;
	}

	#code-header {
		width: 11%;
	}

	#date-header {
		width: 11%;
	}

	@media screen and (max-width: 768px) {
		#group-header {
			width: 14%;
		}

		#code-header {
			width: 19%;
		}

		#date-header {
			width: 19%;
		}
	}
</style>
