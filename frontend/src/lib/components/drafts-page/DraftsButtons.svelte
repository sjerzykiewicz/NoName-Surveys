<script lang="ts">
	import PageButtons from '$lib/components/global/PageButtons.svelte';
	import DeleteModal from '$lib/components/global/DeleteModal.svelte';
	import { errorModalContent, isErrorModalHidden } from '$lib/stores/global';
	import { questions, title } from '$lib/stores/create-page';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';
	import { goto, invalidateAll } from '$app/navigation';

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

		drafts = drafts.filter((d) => !new Set(selectedDraftsToRemove).has(d.id));
		// TODO: go to previous page if there are no drafts left on the current page

		isModalHidden = true;
		$title.title = '';
		$questions = [];
		selectedDraftsToRemove = [];
		await invalidateAll();
	}
</script>

<DeleteModal title="Deleting Drafts" bind:isHidden={isModalHidden} deleteEntries={deleteDrafts} />

<div class="button-row">
	<div class="button-sub-row">
		<button title="Create a draft" class="add-draft" on:click={() => goto('/create')}>
			<i class="symbol">add</i>Draft
		</button>
		{#if drafts.length > 0}
			<button
				title="Delete selected drafts"
				class="delete-draft"
				disabled={selectedDraftsToRemove.length === 0}
				on:click={() => (isModalHidden = false)}
			>
				<i class="symbol">delete</i>Delete
			</button>
		{/if}
	</div>
	<PageButtons numEntries={numDrafts} />
</div>

<style>
	@media screen and (max-width: 768px) {
		.button-row {
			font-size: 0.8em;
		}
	}
</style>
