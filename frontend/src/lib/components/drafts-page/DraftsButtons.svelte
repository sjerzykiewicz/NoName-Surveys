<script lang="ts">
	import PageButtons from '$lib/components/global/PageButtons.svelte';
	import DeleteModal from '$lib/components/global/DeleteModal.svelte';
	import { ENTRIES_PER_PAGE, errorModalContent, isErrorModalHidden } from '$lib/stores/global';
	import { questions, title } from '$lib/stores/create-page';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';
	import { goto, invalidateAll } from '$app/navigation';
	import { page } from '$app/stores';
	import { changePage } from '$lib/utils/changePage';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);
	export let drafts: {
		id: number;
		title: string;
		creation_date: string;
	}[];
	export let numDrafts: number;
	export let selectedDraftsToRemove: number[] = [];

	let isModalHidden: boolean = true;

	async function deleteDrafts() {
		const response = await fetch('/api/surveys/drafts/delete', {
			method: 'POST',
			body: JSON.stringify({ ids: selectedDraftsToRemove }),
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

		const currentPage = parseInt($page.params.draftsPage);
		const maxPage = Math.ceil(numDrafts / $ENTRIES_PER_PAGE) - 1;
		if (
			selectedDraftsToRemove.length >= drafts.length &&
			currentPage >= maxPage &&
			currentPage > 0
		) {
			await changePage($page.url.pathname, currentPage - 1);
		}

		isModalHidden = true;
		$title.title = '';
		$questions = [];
		selectedDraftsToRemove = [];
		await invalidateAll();
	}
</script>

<DeleteModal
	title={$t('deleting_drafts')}
	bind:isHidden={isModalHidden}
	deleteEntries={deleteDrafts}
/>

<div class="button-row">
	<div class="button-sub-row">
		<button title={$t('create_draft')} class="add-draft" on:click={() => goto('/create')}>
			<i class="symbol">add</i><Tx text="draft" />
		</button>
		{#if drafts.length > 0}
			<button
				title={$t('delete_selected_drafts')}
				class="delete-draft"
				disabled={selectedDraftsToRemove.length === 0}
				on:click={() => (isModalHidden = false)}
			>
				<i class="symbol">delete</i><Tx text="delete" />
			</button>
		{/if}
	</div>
	<PageButtons numEntries={numDrafts} />
</div>

<style>
	@media screen and (max-width: 768px) {
		.button-row {
			font-size: 0.9em;
		}
	}
</style>
