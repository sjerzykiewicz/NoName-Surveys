<script lang="ts">
	import { invalidateAll } from '$app/navigation';
	import PageButtons from '$lib/components/global/PageButtons.svelte';
	import DeleteModal from '$lib/components/global/DeleteModal.svelte';
	import { ENTRIES_PER_PAGE, errorModalContent, isErrorModalHidden } from '$lib/stores/global';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';
	import { page } from '$app/stores';
	import { changePage } from '$lib/utils/changePage';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';
	import ImportSummaryModal from '$lib/components/global/ImportSummaryModal.svelte';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let surveys: {
		title: string;
		survey_code: string;
		creation_date: string;
		uses_cryptographic_module: boolean;
		is_owned_by_user: boolean;
		group_size: number;
	}[];
	export let numSurveys: number;
	export let selectedSurveysToRemove: typeof surveys = [];

	let isDeleteModalHidden: boolean = true;
	let isImportModalHidden: boolean = true;

	async function deleteSurveys() {
		const ownedSurveyCodes = selectedSurveysToRemove
			.filter((s) => s.is_owned_by_user)
			.map((s) => s.survey_code);
		const sharedSurveyCodes = selectedSurveysToRemove
			.filter((s) => !s.is_owned_by_user)
			.map((s) => s.survey_code);

		if (ownedSurveyCodes.length > 0) {
			const deleteResponse = await fetch('/api/surveys/delete', {
				method: 'POST',
				body: JSON.stringify({
					survey_codes: ownedSurveyCodes
				}),
				headers: {
					'Content-Type': 'application/json'
				}
			});

			if (!deleteResponse.ok) {
				const body = await deleteResponse.json();
				$errorModalContent = getErrorMessage(body.detail);
				$isErrorModalHidden = false;
				return;
			}
		}

		if (sharedSurveyCodes.length > 0) {
			const rejectResponse = await fetch('/api/surveys/reject-access', {
				method: 'POST',
				body: JSON.stringify({
					survey_codes: sharedSurveyCodes
				}),
				headers: {
					'Content-Type': 'application/json'
				}
			});

			if (!rejectResponse.ok) {
				const body = await rejectResponse.json();
				$errorModalContent = getErrorMessage(body.detail);
				$isErrorModalHidden = false;
				return;
			}
		}

		const currentPage = parseInt($page.params.surveysPage);
		const maxPage = Math.ceil(numSurveys / $ENTRIES_PER_PAGE) - 1;
		if (
			selectedSurveysToRemove.length >= surveys.length &&
			currentPage >= maxPage &&
			currentPage > 0
		) {
			await changePage($page.url.pathname, currentPage - 1);
		}

		isDeleteModalHidden = true;
		selectedSurveysToRemove = [];
		await invalidateAll();
	}
</script>

<ImportSummaryModal bind:isHidden={isImportModalHidden} />

<DeleteModal
	title={$t('deleting_surveys')}
	bind:isHidden={isDeleteModalHidden}
	deleteEntries={deleteSurveys}
/>

<div class="button-row">
	<div class="button-sub-row">
		<button
			title={$t('import_survey_summary')}
			class="import-export-button"
			on:click={() => (isImportModalHidden = false)}
		>
			<i class="symbol">upload_file</i><Tx text="import" />
		</button>
		{#if surveys.length > 0}
			<button
				title={$t('delete_selected_surveys')}
				class="delete-survey"
				disabled={selectedSurveysToRemove.length === 0}
				on:click={() => (isDeleteModalHidden = false)}
			>
				<i class="symbol">delete</i><Tx text="delete" />
			</button>
		{/if}
	</div>
	<PageButtons numEntries={numSurveys} />
</div>

<style>
	@media screen and (max-width: 768px) {
		.button-row {
			font-size: 0.9em;
		}
	}
</style>
