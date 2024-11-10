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

	export let users: string[];
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

	async function addUsers(survey_code: string, user_emails: string[]) {
		if (!(await checkCorrectness(user_emails))) return;

		const response = await fetch('/api/surveys/give-access', {
			method: 'POST',
			body: JSON.stringify({
				survey_code: survey_code,
				user_emails: user_emails
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
		if (selectedUsersToRemove.length >= users.length && currentPage >= maxPage && currentPage > 0) {
			await changePage($page.url.pathname, currentPage - 1);
		}

		isModalHidden = true;
		selectedUsersToRemove = [];
		await invalidateAll();
	}
</script>

<DeleteModal title="Removing Access" bind:isHidden={isModalHidden} deleteEntries={removeUsers} />

<div class="button-row">
	<div class="button-sub-row">
		<button
			title={isPanelVisible ? 'Stop giving access' : 'Give access'}
			class="add-group"
			class:clicked={isPanelVisible}
			on:click={togglePanel}
		>
			<i class="symbol">add</i>Users
		</button>
		<button
			title="Take away access from selected users"
			class="delete-group"
			disabled={selectedUsersToRemove.length === 0}
			on:click={() => (isModalHidden = false)}
		>
			<i class="symbol">delete</i>Delete
		</button>
	</div>
	<PageButtons numEntries={numUsers} />
</div>
{#if isPanelVisible}
	<div class="button-row" transition:slide={{ duration: 200, easing: cubicInOut }}>
		<div title="Select users" class="select-list">
			<MultiSelect bind:selected={selectedUsersToAdd} options={users} placeholder="Select users" />
		</div>
		<button
			title="Finish giving access"
			class="done"
			on:click={() => addUsers(code, selectedUsersToAdd)}
		>
			<i class="symbol">done</i>Apply
		</button>
	</div>
	<UsersError users={selectedUsersToAdd} error={usersError} />
{/if}

<style>
	.select-list {
		margin-bottom: 0em;
	}
</style>
