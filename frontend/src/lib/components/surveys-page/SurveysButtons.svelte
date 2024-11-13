<script lang="ts">
	import { goto, invalidateAll } from '$app/navigation';
	import PageButtons from '$lib/components/global/PageButtons.svelte';
	import DeleteModal from '$lib/components/global/DeleteModal.svelte';
	import { ENTRIES_PER_PAGE, errorModalContent, isErrorModalHidden } from '$lib/stores/global';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';
	import { page } from '$app/stores';
	import { changePage } from '$lib/utils/changePage';

	export let surveys: {
		title: string;
		survey_code: string;
		creation_date: string;
		uses_cryptographic_module: boolean;
		is_owned_by_user: boolean;
		group_size: number;
	}[];
	export let numSurveys: number;
	export let selectedSurveysToRemove: string[] = [];

	let isModalHidden: boolean = true;

	async function deleteSurveys() {
		const response = await fetch('/api/surveys/delete', {
			method: 'POST',
			body: JSON.stringify({
				survey_codes: selectedSurveysToRemove
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

		const currentPage = parseInt($page.params.surveysPage);
		const maxPage = Math.ceil(numSurveys / $ENTRIES_PER_PAGE) - 1;
		if (
			selectedSurveysToRemove.length >= surveys.length &&
			currentPage >= maxPage &&
			currentPage > 0
		) {
			await changePage($page.url.pathname, currentPage - 1);
		}

		isModalHidden = true;
		selectedSurveysToRemove = [];
		await invalidateAll();
	}
</script>

<DeleteModal title="Deleting Surveys" bind:isHidden={isModalHidden} deleteEntries={deleteSurveys} />

<div class="button-row">
	<div class="button-sub-row">
		<button title="Create a survey" class="add-survey" on:click={() => goto('/create')}>
			<i class="symbol">add</i>Survey
		</button>
		{#if surveys.length > 0}
			<button
				title="Delete selected surveys"
				class="delete-survey"
				disabled={selectedSurveysToRemove.length === 0}
				on:click={() => (isModalHidden = false)}
			>
				<i class="symbol">delete</i>Delete
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
