<script lang="ts">
	import { invalidateAll, goto } from '$app/navigation';
	import { onMount, tick } from 'svelte';
	import { scrollToElement } from '$lib/utils/scrollToElement';
	import { GroupError } from '$lib/entities/GroupError';
	import { errorModalContent, isErrorModalHidden, LIMIT_OF_CHARS, XL } from '$lib/stores/global';
	import { M, S } from '$lib/stores/global';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';
	import Modal from '$lib/components/global/Modal.svelte';
	import NameError from './NameError.svelte';
	import { page } from '$app/stores';
	import Input from '$lib/components/global/Input.svelte';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let groups: {
		user_group_name: string;
		all_members_have_public_keys: true;
	}[];
	export let selectedGroupsToRemove: string[] = [];

	let selectedGroup: string = '';
	let newName: string = '';
	let nameError: GroupError = GroupError.NoError;
	let isModalHidden: boolean = true;
	let nameInput: HTMLDivElement;

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

	async function renameGroup() {
		const newGroupName = newName.trim();

		if (!(await checkCorrectness(newGroupName))) return;

		const response = await fetch('/api/groups/rename', {
			method: 'POST',
			body: JSON.stringify({
				name: selectedGroup,
				new_name: newGroupName
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
		await invalidateAll();
	}

	onMount(() => {
		function handleEnter(event: KeyboardEvent) {
			if (!isModalHidden && event.key === 'Enter') {
				event.preventDefault();
				renameGroup();
				event.stopImmediatePropagation();
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
	title={$t('rename_group')}
	bind:isHidden={isModalHidden}
	bind:element={nameInput}
	--width={innerWidth <= $M ? '20em' : '36em'}
>
	<div slot="content" class="modal-content">
		<div class="renaming"><Tx text="renaming" /> {selectedGroup}.</div>
		<Input
			bind:text={newName}
			label={$t('group_name')}
			title={$t('enter_new_group_name')}
			bind:element={nameInput}
			handleEnter={(e) => {
				if (e.key === 'Enter') {
					e.preventDefault();
					renameGroup();
					e.stopImmediatePropagation();
				}
			}}
			--margin-right="0em"
			--char-count-left="6.5em"
		/>
		<NameError name={newName.trim()} error={nameError} groups={groupNames} --font-size="0.8em" />
	</div>
	<button title={$t('save_new_group_name_title')} class="done" on:click={renameGroup}
		><i class="symbol">done</i><Tx text="submit" /></button
	>
</Modal>

{#if groups.length === 0}
	<div class="info-row">
		<div title={$t('groups')} class="title empty"><Tx text="no_groups_yet" /></div>
		<div class="tooltip">
			<i class="symbol">info</i>
			<span class="tooltip-text {innerWidth <= $S ? 'bottom' : 'right'}">
				<Tx text="groups_tooltip" />
			</span>
		</div>
	</div>
{:else}
	<table>
		<tr>
			<th title={$t('select_all')} class="checkbox-entry" class:disabled={groups.length === 0}
				><label
					><input
						type="checkbox"
						disabled={groups.length === 0}
						on:change={toggleAll}
						checked={allSelected}
					/></label
				></th
			>
			<th title={$t('keys_info_title')} id="info-header"><i class="symbol">encrypted</i></th>
			<th title={$t('group_title')} id="title-header" colspan="2"><Tx text="group_name" /></th>
		</tr>
		{#each groups as group}
			<tr>
				<td title="{$t('select')} {group.user_group_name}" class="checkbox-entry"
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
						<i class="symbol">key</i>
						<span class="tooltip-text {innerWidth <= $XL ? 'right' : 'left'}"
							><Tx text="everyone_has_keys" /></span
						>
					{:else}
						<i class="symbol">key_off</i>
						<span class="tooltip-text {innerWidth <= $XL ? 'right' : 'left'}"
							><Tx text="not_everyone_has_keys" /></span
						>
					{/if}
				</td>
				<td title="{$t('open')} {group.user_group_name}" class="title-entry"
					><button
						on:click={() =>
							goto($page.url.pathname + '/' + encodeURI(group.user_group_name) + '/0')}
						>{group.user_group_name}</button
					></td
				>
				<td title="{$t('rename')} {group.user_group_name}" class="button-entry">
					<button
						on:click={() => {
							selectedGroup = group.user_group_name;
							newName = '';
							nameError = GroupError.NoError;
							isModalHidden = false;
						}}><i class="symbol">edit</i></button
					></td
				>
			</tr>
		{/each}
	</table>
{/if}

<style>
	.info-entry.tooltip {
		--tooltip-width: 16em;
	}

	.modal-content {
		width: 100%;
	}

	.modal-content .renaming {
		overflow-wrap: break-word;
		margin-bottom: 0.5em;
	}
</style>
