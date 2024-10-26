<script lang="ts">
	import { invalidateAll } from '$app/navigation';
	import { page } from '$app/stores';
	import MultiSelect from '$lib/components/MultiSelect.svelte';
	import { handleNewLine } from '$lib/utils/handleNewLine';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { tick } from 'svelte';
	import { scrollToElement } from '$lib/utils/scrollToElement';
	import { GroupError } from '$lib/entities/GroupError';
	import MembersError from '$lib/components/groups-page/MembersError.svelte';
	import NameError from '$lib/components/groups-page/NameError.svelte';
	import {
		errorModalContent,
		isErrorModalHidden,
		warningModalContent,
		isWarningModalHidden,
		LIMIT_OF_CHARS
	} from '$lib/stores/global';
	import { limitInput } from '$lib/utils/limitInput';
	import { M } from '$lib/stores/global';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';
	import DeleteModal from '$lib/components/DeleteModal.svelte';
	import { FileError } from '$lib/entities/FileError';
	import EmailsWarning from './EmailsWarning.svelte';
	import { readFile } from '$lib/utils/readFile';

	export let groups: string[];
	export let users: string[];
	export let selectedGroupsToRemove: string[] = [];

	let isPanelVisible: boolean = false;
	let groupName: string = '';
	let groupMembers: string[] = [];
	let nameError: GroupError = GroupError.NoError;
	let membersError: GroupError = GroupError.NoError;
	let isModalHidden: boolean = true;

	function togglePanel() {
		isPanelVisible = !isPanelVisible;
		nameError = GroupError.NoError;
		membersError = GroupError.NoError;
	}

	async function checkCorrectness(name: string, members: string[]) {
		nameError = GroupError.NoError;
		const n = name;
		if (n === null || n === undefined || n.length === 0) {
			nameError = GroupError.NameRequired;
		} else if (n.length > $LIMIT_OF_CHARS) {
			nameError = GroupError.NameTooLong;
		} else if (groups.some((g) => g === n)) {
			nameError = GroupError.NameNonUnique;
		} else if (n.match(/^[\p{L}\p{N} /-]+$/u) === null) {
			nameError = GroupError.NameInvalid;
		}

		membersError = GroupError.NoError;
		const m = members;
		if (m === null || m === undefined || m.length === 0) {
			membersError = GroupError.MembersRequired;
		}

		if (nameError !== GroupError.NoError) {
			await tick();
			scrollToElement('.group-input');
			return false;
		}

		if (membersError !== GroupError.NoError) {
			await tick();
			scrollToElement('.select-list');
			return false;
		}

		return true;
	}

	async function filterUnregisteredUsers(emails: string[]): Promise<string[]> {
		const response = await fetch('/api/users/filter-unregistered-users', {
			method: 'POST',
			body: JSON.stringify({ emails: emails }),
			headers: {
				'Content-Type': 'application/json'
			}
		});

		if (!response.ok) {
			const body = await response.json();
			$errorModalContent = getErrorMessage(body.detail);
			$isErrorModalHidden = false;
			return emails;
		}

		return await response.json();
	}

	async function createGroup(user_group_name: string, user_group_members: string[]) {
		if (!(await checkCorrectness(user_group_name, user_group_members))) return;

		const response = await fetch('/api/groups/create', {
			method: 'POST',
			body: JSON.stringify({
				user_email: $page.data.session?.user?.email,
				user_group_name: user_group_name,
				user_group_members: user_group_members
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

		groupName = '';
		groupMembers = [];
		isPanelVisible = false;
		invalidateAll();
	}

	async function deleteGroups() {
		selectedGroupsToRemove.forEach(async (group) => {
			const response = await fetch('/api/groups/delete', {
				method: 'POST',
				body: JSON.stringify({ user_email: $page.data.session?.user?.email, name: group }),
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

			groups = groups.filter((g) => g !== group);
		});

		isModalHidden = true;
		selectedGroupsToRemove = [];
		invalidateAll();
	}

	let fileElement: HTMLInputElement | null = null;
	let fileName: string = 'No file selected';
	let fileWarning: FileError = FileError.NoError;

	async function handleFileChange() {
		fileElement = document.querySelector<HTMLInputElement>('#emails-file');
		fileName = fileElement?.files?.[0]?.name ?? 'No file selected';

		const emails = await processEmails();
		const unregisteredEmails = await filterUnregisteredUsers(emails);

		if (unregisteredEmails.length > 0 && $isErrorModalHidden) {
			$warningModalContent = `Could not import ${unregisteredEmails.length} users, because they haven't registered yet.`;
			$isWarningModalHidden = false;
		}

		const registeredEmails = emails.filter((e) => !unregisteredEmails.includes(e));
		const newGroupMembers = [...groupMembers, ...registeredEmails];

		groupMembers = [...new Set(newGroupMembers)];
	}

	function checkFileCorrectness() {
		fileWarning = FileError.NoError;

		if (fileElement?.files?.length === 0) {
			fileWarning = FileError.FileRequired;
			return false;
		} else if (fileElement?.files?.[0]?.name.split('.').pop() !== 'csv') {
			fileWarning = FileError.FileInvalid;
			return false;
		}

		return true;
	}

	async function processEmails() {
		if (!checkFileCorrectness()) return [];

		return await readFile(fileElement).then(
			(resolve) => {
				return resolve
					.split(';')
					.map((e) => e.trim())
					.filter((e) => e.length > 0);
			},
			(reject) => {
				$errorModalContent = reject as string;
				$isErrorModalHidden = false;
				return [];
			}
		);
	}

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

<DeleteModal title="Deleting Groups" bind:isHidden={isModalHidden} deleteEntries={deleteGroups} />

<div class="button-row">
	<button
		title={isPanelVisible ? 'Stop creating a group' : 'Create a group'}
		class="add-group"
		class:clicked={isPanelVisible}
		on:click={togglePanel}
	>
		<i class="material-symbols-rounded">add</i>Group
	</button>
	{#if groups.length > 0}
		<button
			title="Delete selected groups"
			class="delete-group"
			disabled={selectedGroupsToRemove.length === 0}
			on:click={() => (isModalHidden = false)}
		>
			<i class="material-symbols-rounded">delete</i>Delete
		</button>
	{/if}
</div>
{#if isPanelVisible}
	<div class="buttons-container" transition:slide={{ duration: 200, easing: cubicInOut }}>
		<div class="button-row">
			<div
				class="input-container"
				class:max={groupName.length > $LIMIT_OF_CHARS}
				transition:slide={{ duration: 200, easing: cubicInOut }}
			>
				<!-- svelte-ignore a11y-autofocus -->
				<div
					title="Enter a group name"
					class="group-input"
					contenteditable
					bind:textContent={groupName}
					autofocus={innerWidth > $M}
					role="textbox"
					tabindex="0"
					on:keydown={(e) => {
						handleNewLine(e);
						limitInput(e, groupName, $LIMIT_OF_CHARS);
					}}
				>
					{groupName}
				</div>
				<span class="char-count">{groupName.length} / {$LIMIT_OF_CHARS}</span>
			</div>
		</div>
		<NameError name={groupName.trim()} error={nameError} {groups} />
		<div class="button-row">
			<div title="Select group members" class="select-list">
				<MultiSelect
					bind:selected={groupMembers}
					options={users}
					placeholder="Select group members"
				/>
			</div>
			<button
				title="Save the group"
				class="save"
				on:click={() => {
					createGroup(groupName.trim(), groupMembers);
				}}
			>
				<i class="material-symbols-rounded">done</i>Create
			</button>
		</div>
		<MembersError members={groupMembers} error={membersError} />
		<div class="button-row">
			<div title="Import group members from a .csv file" class="file-div">
				<span class="file-label">Or import group members from a .csv file.</span>
				<label for="emails-file">
					<div class="file-input">
						<span class="file-button"
							><i class="material-symbols-rounded">upload_file</i>Select File</span
						>
						<span class="file-name">{fileName}</span>
					</div>
					<input type="file" name="emails" id="emails-file" on:change={handleFileChange} />
				</label>
			</div>
		</div>
		<EmailsWarning warning={fileWarning} element={fileElement} />
	</div>
{/if}

<style>
	.select-list {
		margin-bottom: 0em;
	}

	.buttons-container {
		padding: 0.2em;
		margin: -0.2em;
	}

	.group-input {
		margin: 0em;
	}

	.group-input[contenteditable]:empty::before {
		content: 'Enter group name...';
		color: var(--text-dark-color);
	}

	.save i {
		font-variation-settings: 'wght' 700;
		transform: rotate(0deg);
		transition: transform 0.2s;
	}

	.input-container {
		margin-bottom: -1.4em;
	}

	.file-label {
		font-size: 0.8em;
	}

	.file-input {
		margin-top: 0.625em;
	}
</style>
