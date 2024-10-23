<script lang="ts">
	import { invalidateAll } from '$app/navigation';
	import { page } from '$app/stores';
	import MultiSelect from '$lib/components/MultiSelect.svelte';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { tick } from 'svelte';
	import { scrollToElement } from '$lib/utils/scrollToElement';
	import { GroupError } from '$lib/entities/GroupError';
	import UsersError from './UsersError.svelte';
	import { errorModalContent, isErrorModalHidden } from '$lib/stores/global';

	export let users: string[];
	export let code: string;
	export let selectedUsersToRemove: string[] = [];

	let isPanelVisible: boolean = false;
	let selectedUsersToAdd: string[] = [];
	let usersError: GroupError = GroupError.NoError;

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
				user_email: $page.data.session?.user?.email,
				survey_code: survey_code,
				user_emails_to_share_with: user_emails_to_share_with
			}),
			headers: {
				'Content-Type': 'application/json'
			}
		});

		if (!response.ok) {
			const body = await response.json();
			$errorModalContent = body.detail;
			$isErrorModalHidden = false;
			return;
		}

		selectedUsersToAdd = [];
		isPanelVisible = false;
		invalidateAll();
	}

	async function removeUsers() {
		selectedUsersToRemove.forEach(async (user, i) => {
			const response = await fetch('/api/surveys/take-away-access', {
				method: 'POST',
				body: JSON.stringify({
					user_email: $page.data.session?.user?.email,
					survey_code: code,
					user_email_to_take_access_from: user
				}),
				headers: {
					'Content-Type': 'application/json'
				}
			});

			if (!response.ok) {
				const body = await response.json();
				$errorModalContent = body.detail;
				$isErrorModalHidden = false;
				return;
			}

			users.splice(i, 1);
		});

		selectedUsersToRemove = [];
		invalidateAll();
	}
</script>

<div class="button-row">
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
		on:click={removeUsers}
	>
		<i class="material-symbols-rounded">delete</i>Delete
	</button>
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
	.save i {
		font-variation-settings: 'wght' 700;
	}
</style>
