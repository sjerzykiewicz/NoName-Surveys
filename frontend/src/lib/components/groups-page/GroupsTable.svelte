<script lang="ts">
	import { invalidateAll, goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { handleNewLine } from '$lib/utils/handleNewLine';
	import { tick } from 'svelte';
	import { scrollToElement } from '$lib/utils/scrollToElement';
	import { GroupError } from '$lib/entities/GroupError';
	import NameTableError from '$lib/components/groups-page/NameTableError.svelte';
	import { LIMIT_OF_CHARS } from '$lib/stores/global';
	import { limitInput } from '$lib/utils/limitInput';
	import { M, S } from '$lib/stores/global';

	export let groups: string[];
	export let selectedGroupsToRemove: string[] = [];
	export let editedIndex: number = -1;

	let newName: string = '';
	let nameError: GroupError = GroupError.NoError;

	$: allSelected = selectedGroupsToRemove.length === groups.length;

	function toggleAll() {
		selectedGroupsToRemove = allSelected ? [] : [...groups];
	}

	async function checkCorrectness(name: string) {
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

		if (nameError !== GroupError.NoError) {
			await tick();
			scrollToElement('.table-input');
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
			alert(body.detail);
			return;
		}

		editedIndex = -1;
		newName = '';
		invalidateAll();
	}

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

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
			<th title="Select all" class="checkbox-entry"
				><label
					><input
						type="checkbox"
						disabled={groups.length === 0}
						on:change={toggleAll}
						checked={allSelected}
					/></label
				></th
			>
			<th title="Group title" id="title-header" colspan="3">Group Title</th>
		</tr>
		{#each groups.toSorted() as group, groupIndex}
			<tr>
				<td title="Select {group}" class="checkbox-entry"
					><label>
						<input type="checkbox" bind:group={selectedGroupsToRemove} value={group} />
					</label></td
				>
				{#if editedIndex === groupIndex}
					<td
						title="Stop renaming the group"
						class="button-entry"
						on:click={() => {
							editedIndex = -1;
							newName = '';
							nameError = GroupError.NoError;
						}}><i class="material-symbols-rounded">edit_off</i></td
					>
					<td>
						<div class="input-container" class:max={newName.length > $LIMIT_OF_CHARS}>
							<!-- svelte-ignore a11y-autofocus -->
							<div
								title="Enter a new group name"
								class="table-input"
								contenteditable
								bind:textContent={newName}
								autofocus={innerWidth > $M}
								role="textbox"
								tabindex="0"
								on:keydown={(e) => {
									handleNewLine(e);
									limitInput(e, newName, $LIMIT_OF_CHARS);
								}}
							>
								{newName}
							</div>
							<span class="char-count">{newName.length} / {$LIMIT_OF_CHARS}</span>
						</div>
						<NameTableError name={newName.trim()} error={nameError} {groups} />
					</td>
					<td
						title="Save the new group name"
						class="button-entry save-entry"
						on:click={() => renameGroup(group, newName.trim())}
					>
						<i class="material-symbols-rounded">save</i></td
					>
				{:else}
					<td
						title="Rename the group"
						class="button-entry"
						on:click={() => {
							editedIndex = groupIndex;
							newName = '';
							nameError = GroupError.NoError;
						}}><i class="material-symbols-rounded">edit</i></td
					>
					<td
						title="Open the group"
						class="title-entry"
						colspan="2"
						on:click={() => goto('/groups/' + encodeURI(group))}>{group}</td
					>
				{/if}
			</tr>
		{/each}
	</table>
{/if}

<style>
	.table-input {
		margin: 0em;
		overflow-wrap: anywhere;
	}

	.table-input[contenteditable]:empty::before {
		content: 'Enter group name...';
		color: var(--text-dark-color);
	}
	.save-entry {
		background-color: var(--accent-color);
	}

	.save-entry:hover {
		background-color: var(--accent-dark-color);
	}

	.save-entry:active {
		background-color: var(--border-color);
	}

	.input-container {
		margin-bottom: -1.35em;
	}
</style>
