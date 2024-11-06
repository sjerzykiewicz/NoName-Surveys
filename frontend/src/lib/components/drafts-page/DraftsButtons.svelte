<script lang="ts">
	import PageButtons from '$lib/components/global/PageButtons.svelte';
	import DeleteModal from '$lib/components/global/DeleteModal.svelte';
	import { errorModalContent, isErrorModalHidden } from '$lib/stores/global';
	import { questions, title } from '$lib/stores/create-page';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';
	import { goto, invalidateAll } from '$app/navigation';
	// import { page } from '$app/stores';
	// import { changePage } from '$lib/utils/changePage';

	export let drafts: {
		id: number;
		title: string;
		creation_date: string;
	}[];
	export let numDrafts: number;
	export let selectedDraftsToRemove: typeof drafts = [];

	let isModalHidden: boolean = true;

	// $: currentPage = parseInt(
	// 	$page.url.pathname.substring($page.url.pathname.lastIndexOf('/') + 1, $page.url.pathname.length)
	// );

	async function deleteDrafts() {
		selectedDraftsToRemove.forEach(async (draft, i) => {
			const response = await fetch('/api/surveys/drafts/delete', {
				method: 'POST',
				body: JSON.stringify({ id: draft.id }),
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

			drafts.splice(i, 1);
		});

		// TODO: go to previous page if there are no drafts left on the current page

		isModalHidden = true;
		$title.title = '';
		$questions = [];
		selectedDraftsToRemove = [];
		invalidateAll();
	}
</script>

<DeleteModal title="Deleting Drafts" bind:isHidden={isModalHidden} deleteEntries={deleteDrafts} />

<div class="button-row">
	<div class="button-sub-row">
		<button title="Create a draft" class="add-draft" on:click={() => goto('/create')}>
			<i class="material-symbols-rounded">add</i>Draft
		</button>
		{#if drafts.length > 0}
			<button
				title="Delete selected drafts"
				class="delete-draft"
				disabled={selectedDraftsToRemove.length === 0}
				on:click={() => (isModalHidden = false)}
			>
				<i class="material-symbols-rounded">delete</i>Delete
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
