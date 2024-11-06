<script lang="ts">
	import { invalidateAll } from '$app/navigation';
	import MultiSelect from '$lib/components/global/MultiSelect.svelte';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { tick } from 'svelte';
	import { scrollToElement } from '$lib/utils/scrollToElement';
	import { GroupError } from '$lib/entities/GroupError';
	import UsersError from './UsersError.svelte';
	import { errorModalContent, isErrorModalHidden } from '$lib/stores/global';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';
	import DeleteModal from '$lib/components/global/DeleteModal.svelte';

	export let users: string[];
	export let code: string;
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

	async function addUsers(survey_code: string, user_emails_to_share_with: string[]) {
		if (!(await checkCorrectness(user_emails_to_share_with))) return;

		const response = await fetch('/api/surveys/give-access', {
			method: 'POST',
			body: JSON.stringify({
				survey_code: survey_code,
				user_emails_to_share_with: user_emails_to_share_with
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
		// TODO: fix and improve this
		selectedUsersToRemove.forEach(async (user) => {
			const response = await fetch('/api/surveys/take-away-access', {
				method: 'POST',
				body: JSON.stringify({
					survey_code: code,
					user_email_to_take_access_from: user
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

			users = users.filter((u) => u !== user);
		});
		// TODO: go to previous page if there are no users left on the current page

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
			<i class="material-symbols-rounded">add</i>Users
		</button>
		<button
			title="Take away access from selected users"
			class="delete-group"
			disabled={selectedUsersToRemove.length === 0}
			on:click={() => (isModalHidden = false)}
		>
			<i class="material-symbols-rounded">delete</i>Delete
		</button>
	</div>
	<!-- TODO: <PageButtons /> -->
</div>
{#if isPanelVisible}
	<div class="button-row" transition:slide={{ duration: 200, easing: cubicInOut }}>
		<div class="users-panel">
			<div title="Select users" class="select-list">
				<MultiSelect
					bind:selected={selectedUsersToAdd}
					options={users}
					placeholder="Select users"
				/>
			</div>
			<button
				title="Finish giving access"
				class="save"
				on:click={() => addUsers(code, selectedUsersToAdd)}
			>
				<i class="material-symbols-rounded">done</i>Apply
			</button>
		</div>
	</div>
	<UsersError users={selectedUsersToAdd} error={usersError} />
{/if}

<style>
	.select-list {
		margin-bottom: 0em;
	}

	.save i {
		font-variation-settings: 'wght' 700;
	}
</style>
