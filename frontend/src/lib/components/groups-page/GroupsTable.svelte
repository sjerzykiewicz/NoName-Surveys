<script lang="ts">
	import { invalidateAll, goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { onMount, tick } from 'svelte';
	import { scrollToElement } from '$lib/utils/scrollToElement';
	import { GroupError } from '$lib/entities/GroupError';
	import { errorModalContent, isErrorModalHidden, LIMIT_OF_CHARS, XL } from '$lib/stores/global';
	import { limitInput } from '$lib/utils/limitInput';
	import { M, S } from '$lib/stores/global';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';
	import Modal from '$lib/components/global/Modal.svelte';
	import NameError from './NameError.svelte';

	export let groups: {
		user_group_name: string;
		all_members_have_public_keys: true;
	}[];
	export let selectedGroupsToRemove: string[] = [];

	let selectedGroup: string = '';
	let newName: string = '';
	let nameError: GroupError = GroupError.NoError;
	let isModalHidden: boolean = true;

	$: groupNames = groups.map((g) => g.user_group_name);

	$: allSelected =
		selectedGroupsToRemove.length === groupNames.length && selectedGroupsToRemove.length > 0;

	function toggleAll() {
		selectedGroupsToRemove = allSelected ? [] : [...groupNames];
	}

	async function checkCorrectness(name: string) {
		nameError = GroupError.NoError;
		const n = name;
		if (n === null || n === undefined || n.length === 0) {
			nameError = GroupError.NameRequired;
		} else if (n.length > $LIMIT_OF_CHARS) {
			nameError = GroupError.NameTooLong;
		} else if (groupNames.some((g) => g === n)) {
			nameError = GroupError.NameNonUnique;
		} else if (n.match(/^[\p{L}\p{N} /-]+$/u) === null) {
			nameError = GroupError.NameInvalid;
		}

		if (nameError !== GroupError.NoError) {
			await tick();
			scrollToElement('.group-input');
			return false;
		}

		return true;
	}

	async function renameGroup(name: string, new_name: string) {
		if (!(await checkCorrectness(new_name))) return;

		const response = await fetch('/api/groups/rename', {
			method: 'POST',
			body: JSON.stringify({
				user_email: $page.data.session?.user?.email,
				name: name,
				new_name: new_name
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

		isModalHidden = true;
		selectedGroup = '';
		newName = '';
		invalidateAll();
	}

	onMount(() => {
		function handleEnter(event: KeyboardEvent) {
			if (!isModalHidden && event.key === 'Enter') {
				event.preventDefault();
				renameGroup(selectedGroup, newName.trim());
			}
		}

		document.body.addEventListener('keydown', handleEnter);

		return () => {
			document.body.removeEventListener('keydown', handleEnter);
		};
	});

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

<Modal
	icon="edit"
	title="Rename Group"
	bind:isHidden={isModalHidden}
	width={innerWidth <= $M ? 20 : 36}
>
	<div slot="content" class="modal-content">
		<span>Renaming {selectedGroup}.</span>
		<div class="input-container" class:max={newName.length > $LIMIT_OF_CHARS}>
			<!-- svelte-ignore a11y-autofocus -->
			<div
				title="Enter a new group name"
				class="group-input"
				contenteditable
				bind:textContent={newName}
				autofocus={innerWidth > $M}
				role="textbox"
				tabindex="0"
				on:keydown={(e) => {
					limitInput(e, newName, $LIMIT_OF_CHARS);
				}}
			>
				{newName}
			</div>
			<span class="char-count">{newName.length} / {$LIMIT_OF_CHARS}</span>
		</div>
		<NameError name={newName.trim()} error={nameError} groups={groupNames} fontSize={0.8} />
	</div>
	<button
		title="Save the new group name"
		class="save"
		on:click={() => renameGroup(selectedGroup, newName.trim())}
		><i class="material-symbols-rounded">done</i>Apply</button
	>
</Modal>

{#if groups.length === 0}
	<div class="info-row">
		<div title="Groups" class="title empty">No groups yet!</div>
		<div class="tooltip">
			<i class="material-symbols-rounded">info</i>
			<span class="tooltip-text {innerWidth <= $S ? 'bottom' : 'right'}">
				When creating a secure survey, you can choose a group of possible respondents. To create a
				group, click on the button below. All your created groups will be stored on this page.
			</span>
		</div>
	</div>
{:else}
	<table>
		<tr>
			<th title="Select all" class="checkbox-entry" class:disabled={groups.length === 0}
				><label
					><input
						type="checkbox"
						disabled={groups.length === 0}
						on:change={toggleAll}
						checked={allSelected}
					/></label
				></th
			>
			<th title="Keys information" id="info-header"
				><i class="material-symbols-rounded">encrypted</i></th
			>
			<th title="Group title" id="title-header" colspan="2">Group Title</th>
		</tr>
		{#each groups.toSorted((a, b) => a.user_group_name.localeCompare(b.user_group_name)) as group}
			<tr>
				<td title="Select {group}" class="checkbox-entry"
					><label>
						<input
							type="checkbox"
							bind:group={selectedGroupsToRemove}
							value={group.user_group_name}
						/>
					</label></td
				>
				<td class="info-entry tooltip">
					{#if group.all_members_have_public_keys}
						<i class="material-symbols-rounded">key</i>
						<span class="tooltip-text {innerWidth <= $XL ? 'right' : 'left'}"
							>Everyone in this group have generated their keys. You can use this group in secure
							surveys.</span
						>
					{:else}
						<i class="material-symbols-rounded">key_off</i>
						<span class="tooltip-text {innerWidth <= $XL ? 'right' : 'left'}"
							>Not everyone in this group have generated their keys. You cannot use this group in
							secure surveys.</span
						>
					{/if}
				</td>
				<td title="Open the group" class="title-entry"
					><button
						on:click={() =>
							goto($page.url.pathname + '/' + encodeURI(group.user_group_name)) + '/0'}
						>{group.user_group_name}</button
					></td
				>
				<td title="Rename the group" class="button-entry">
					<button
						on:click={() => {
							selectedGroup = group.user_group_name;
							newName = '';
							nameError = GroupError.NoError;
							isModalHidden = false;
						}}><i class="material-symbols-rounded">edit</i></button
					></td
				>
			</tr>
		{/each}
	</table>
{/if}

<style>
	.tooltip {
		--tooltip-width: 16em;
	}

	.group-input {
		margin: 0em;
		margin-top: 1em;
		overflow-wrap: anywhere;
		text-align: left;
	}

	.group-input[contenteditable]:empty::before {
		content: 'Enter group name...';
		color: var(--text-dark-color);
	}

	.input-container {
		margin-bottom: -1.35em;
	}

	.char-count {
		left: 35%;
	}

	.modal-content {
		width: 100%;
	}

	.modal-content span {
		overflow-wrap: break-word;
	}

	.save i {
		font-variation-settings: 'wght' 700;
	}
</style>
