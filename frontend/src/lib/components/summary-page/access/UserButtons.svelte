<script lang="ts">
	import { invalidateAll } from '$app/navigation';
	import MultiSelect from '$lib/components/global/MultiSelect.svelte';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { tick } from 'svelte';
	import { scrollToElement } from '$lib/utils/scrollToElement';
	import { GroupError } from '$lib/entities/GroupError';
	import UsersError from './UsersError.svelte';
	import { ENTRIES_PER_PAGE, errorModalContent, isErrorModalHidden } from '$lib/stores/global';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';
	import DeleteModal from '$lib/components/global/DeleteModal.svelte';
	import PageButtons from '$lib/components/global/PageButtons.svelte';
	import { page } from '$app/stores';
	import { changePage } from '$lib/utils/changePage';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let usersWithoutAccess: string[];
	export let usersWithAccess: string[];
	export let code: string;
	export let numUsers: number;
	export let selectedUsersToRemove: string[] = [];

	let isPanelVisible: boolean = false;
	let selectedUsersToAdd: string[] = [];
	let usersError: GroupError = GroupError.NoError;
	let isModalHidden: boolean = true;

	function togglePanel() {
		isPanelVisible = !isPanelVisible;
		usersError = GroupError.NoError;
	}

	async function checkCorrectness(users: string[]) {
		usersError = GroupError.NoError;
		const u = users;
		if (u === null || u === undefined || u.length === 0) {
			usersError = GroupError.MembersRequired;
		}

		if (usersError !== GroupError.NoError) {
			await tick();
			scrollToElement('.select-list');
			return false;
		}

		return true;
	}

	async function addUsers() {
		if (!(await checkCorrectness(selectedUsersToAdd))) return;

		const response = await fetch('/api/surveys/give-access', {
			method: 'POST',
			body: JSON.stringify({
				survey_code: code,
				user_emails: selectedUsersToAdd
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

		selectedUsersToAdd = [];
		isPanelVisible = false;
		await invalidateAll();
	}

	async function removeUsers() {
		const response = await fetch('/api/surveys/take-away-access', {
			method: 'POST',
			body: JSON.stringify({
				survey_code: code,
				user_emails: selectedUsersToRemove
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

		const currentPage = parseInt($page.params.accessPage);
		const maxPage = Math.ceil(numUsers / $ENTRIES_PER_PAGE) - 1;
		if (
			selectedUsersToRemove.length >= usersWithAccess.length &&
			currentPage >= maxPage &&
			currentPage > 0
		) {
			await changePage($page.url.pathname, currentPage - 1);
		}

		isModalHidden = true;
		selectedUsersToRemove = [];
		await invalidateAll();
	}
</script>

<DeleteModal
	title={$t('removing_access')}
	bind:isHidden={isModalHidden}
	deleteEntries={removeUsers}
/>

<div class="button-row top-row">
	<div class="button-sub-row">
		<button
			title={isPanelVisible ? $t('stop_giving_access') : $t('give_access')}
			class="add-group"
			class:clicked={isPanelVisible}
			on:click={togglePanel}
		>
			<i class="symbol">add</i><Tx text="users"></Tx>
		</button>
		<button
			title={$t('take_away_access')}
			class="delete-group"
			disabled={selectedUsersToRemove.length === 0}
			on:click={() => (isModalHidden = false)}
		>
			<i class="symbol">delete</i><Tx text="delete"></Tx>
		</button>
	</div>
	<PageButtons numEntries={numUsers} />
</div>
{#if isPanelVisible}
	<div class="button-row" transition:slide={{ duration: 200, easing: cubicInOut }}>
		<div title={$t('select_users')} class="select-list">
			<MultiSelect
				bind:selected={selectedUsersToAdd}
				options={usersWithoutAccess}
				placeholder={$t('select_users')}
			/>
		</div>
		<button title={$t('finish_giving_access')} class="done" on:click={addUsers}>
			<i class="symbol">done</i><Tx text="submit"></Tx>
		</button>
	</div>
	<UsersError users={selectedUsersToAdd} error={usersError} />
{/if}

<style>
	.select-list {
		margin-bottom: 0em;
	}

	@media screen and (max-width: 768px) {
		.top-row {
			font-size: 0.9em;
		}
	}
</style>
