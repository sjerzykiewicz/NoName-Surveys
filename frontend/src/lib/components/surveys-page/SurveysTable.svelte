<script lang="ts">
	import { goto, invalidateAll } from '$app/navigation';
	import QrCodeModal from '$lib/components/global/QrCodeModal.svelte';
	import { errorModalContent, isErrorModalHidden, S, XL } from '$lib/stores/global';
	import { page } from '$app/stores';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';
	import { formatDateTime } from '$lib/utils/formatDate';
	import type SurveyHeader from '$lib/entities/surveys/SurveyHeader';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let surveys: SurveyHeader[];
	export let selectedSurveysToRemove: typeof surveys = [];

	let innerWidth: number;
	let selectedCode: string;
	let isModalHidden: boolean = true;

	$: allSelected =
		selectedSurveysToRemove.length === surveys.length && selectedSurveysToRemove.length > 0;

	function toggleAll() {
		selectedSurveysToRemove = allSelected ? [] : [...surveys];
	}

	async function toggleSurveyActive(survey_code: string, is_enabled: boolean) {
		const response = await fetch('/api/surveys/toggle-enabled', {
			method: 'POST',
			body: JSON.stringify({ survey_code, is_enabled }),
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

		await invalidateAll();
	}
</script>

<svelte:window bind:innerWidth />

<QrCodeModal title={$t('access_code')} bind:isHidden={isModalHidden} surveyCode={selectedCode} />

{#if surveys.length === 0}
	<div class="info-row">
		<div title={$t('surveys')} class="title empty"><Tx text="no_surveys_yet" /></div>
		<div class="tooltip hoverable">
			<i class="symbol">help</i>
			<span class="tooltip-text {innerWidth <= $S ? 'bottom' : 'right'}">
				<Tx text="surveys_tooltip" /><a href="/account/faq#create"><Tx text="help" /></a>
			</span>
		</div>
	</div>
{:else}
	<div title={$t('surveys_guide_title')} class="info">
		<div class="info-text">
			<Tx html="surveys_guide" />
		</div>
	</div>
	<table>
		<tr>
			<th title={$t('select_all')} class="checkbox-entry" class:disabled={surveys.length === 0}
				><label
					><input
						type="checkbox"
						disabled={surveys.length === 0}
						on:change={toggleAll}
						checked={allSelected}
					/></label
				></th
			>
			<th title={$t('survey_info')} id="info-header" colspan="3">Info</th>
			<th title={$t('survey_title')} id="title-header"><Tx text="survey_title" /></th>
			<th title={$t('group_size')} id="group-header"><Tx text="group_size" /></th>
			<th title={$t('access_code')} id="code-header"><Tx text="access_code" /></th>
			<th title={$t('creation_date')} id="date-header"><Tx text="creation_date" /></th>
		</tr>
		{#each surveys as survey}
			<tr>
				<td title="{$t('select')} {survey.title}" class="checkbox-entry"
					><label>
						<input type="checkbox" bind:group={selectedSurveysToRemove} value={survey} />
					</label></td
				>
				<td class="info-entry tooltip">
					{#if survey.uses_cryptographic_module}
						<i class="symbol">encrypted</i>
						<span class="tooltip-text {innerWidth <= $XL ? 'right' : 'left'}"
							><Tx text="survey_is_secure" /></span
						>
					{:else}
						<i class="symbol">public</i>
						<span class="tooltip-text {innerWidth <= $XL ? 'right' : 'left'}"
							><Tx text="survey_is_public" /></span
						>
					{/if}
				</td>
				<td class="info-entry tooltip access">
					{#if survey.is_owned_by_user}
						<i class="symbol">verified</i>
						<span class="tooltip-text {innerWidth <= $XL ? 'right' : 'left'}"
							><Tx text="survey_owner" /></span
						>
					{:else}
						<i class="symbol">share</i>
						<span class="tooltip-text {innerWidth <= $XL ? 'right' : 'left'}"
							><Tx text="survey_shared" /></span
						>
					{/if}
				</td>
				<td class="button-entry tooltip active">
					<button
						disabled={!survey.is_owned_by_user}
						on:click={async () => await toggleSurveyActive(survey.survey_code, !survey.is_enabled)}
					>
						{#if survey.is_owned_by_user}
							{#if survey.is_enabled}
								<i class="symbol deactivate">mode_off_on</i>
								<span class="tooltip-text {innerWidth <= $XL ? 'right' : 'left'}"
									><Tx text="survey_deactivate" /></span
								>
							{:else}
								<i class="symbol activate">mode_off_on</i>
								<span class="tooltip-text {innerWidth <= $XL ? 'right' : 'left'}"
									><Tx text="survey_activate" /></span
								>
							{/if}
						{:else}
							<i class="symbol">mode_off_on</i>
						{/if}
					</button>
				</td>
				<td title={$t('view_summary')} class="title-entry"
					><button on:click={() => goto($page.url.pathname + '/' + survey.survey_code)}
						>{survey.title}</button
					></td
				>
				{#if survey.uses_cryptographic_module}
					<td title={$t('view_respondents')} class="code-entry"
						><button
							on:click={() =>
								goto($page.url.pathname + '/' + survey.survey_code + '/respondents/0')}
							>{survey.group_size}</button
						>
					</td>
				{:else}
					<td title={$t('not_available_for_public')} class="info-entry">N/A</td>
				{/if}
				<td title={$t('view_qr')} class="code-entry"
					><button
						on:click={() => {
							selectedCode = survey.survey_code;
							isModalHidden = false;
						}}>{survey.survey_code}</button
					>
				</td>
				<td title={$t('creation_date')} class="date-entry"
					>{formatDateTime(survey.creation_date)}</td
				>
			</tr>
		{/each}
	</table>
{/if}

<style>
	.info {
		padding-bottom: 0.5em;
	}

	.tooltip.access,
	.tooltip.active {
		--tooltip-width: 13em;
	}

	i.deactivate {
		color: var(--accent-color-1);
	}

	i.activate {
		color: var(--error-color-1);
	}

	#group-header {
		width: 8%;
		text-align: center;
	}

	#code-header {
		width: 11%;
		text-align: center;
	}

	#date-header {
		width: 11%;
		text-align: center;
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
