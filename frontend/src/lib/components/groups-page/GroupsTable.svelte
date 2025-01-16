<script lang="ts">
	import { invalidateAll, goto } from '$app/navigation';
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
	let isSubmitButtonDisabled: boolean = false;

	$: groupNames = groups.map((g) => g.user_group_name);

	$: allSelected =
		selectedGroupsToRemove.length === groupNames.length && selectedGroupsToRemove.length > 0;

	function toggleAll() {
		selectedGroupsToRemove = allSelected ? [] : [...groupNames];
	}

	function checkCorrectness(name: string) {
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
			scrollToElement('.group-input');
			return false;
		}

		return true;
	}

	async function renameGroup() {
		const newGroupName = newName.trim();

		if (!checkCorrectness(newGroupName)) return;

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

	async function handleEnter(event: KeyboardEvent) {
		if (!isModalHidden && !isSubmitButtonDisabled && event.key === 'Enter') {
			event.preventDefault();
			event.stopImmediatePropagation();
			isSubmitButtonDisabled = true;
			await renameGroup();
			isSubmitButtonDisabled = false;
		}
	}

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />
<svelte:body on:keydown={handleEnter} />

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
			handleEnter={async (e) => {
				if (!isSubmitButtonDisabled && e.key === 'Enter') {
					e.preventDefault();
					e.stopImmediatePropagation();
					isSubmitButtonDisabled = true;
					await renameGroup();
					isSubmitButtonDisabled = false;
				}
			}}
			--margin-right="0em"
			--char-count-left="6.5em"
		/>
		<NameError name={newName.trim()} error={nameError} groups={groupNames} --font-size="0.8em" />
	</div>
	<button
		title={$t('save_new_group_name_title')}
		class="done"
		disabled={isSubmitButtonDisabled}
		on:click={async () => {
			isSubmitButtonDisabled = true;
			await renameGroup();
			isSubmitButtonDisabled = false;
		}}><i class="symbol">done</i><Tx text="submit" /></button
	>
</Modal>

{#if groups.length === 0}
	<div class="info-row">
		<div title={$t('groups')} class="title empty"><Tx text="no_groups_yet" /></div>
		<div class="tooltip hoverable">
			<i class="symbol">help</i>
			<span class="tooltip-text {innerWidth <= $S ? 'bottom' : 'right'}">
				<Tx text="groups_tooltip" /><a href="/account/faq#group"><Tx text="help" /></a>
			</span>
		</div>
	</div>
{:else}
	<div title={$t('groups_guide_title')} class="info">
		<div class="info-text">
			<Tx html="groups_guide" />
		</div>
	</div>
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
			<th title={$t('group_name')} id="title-header"><Tx text="group_name" /></th>
			<th title={$t('rename')} id="rename-header"><Tx text="rename" /></th>
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
							goto($page.url.pathname + '/' + encodeURIComponent(group.user_group_name) + '/0')}
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
	.info {
		padding-bottom: 0.5em;
	}

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
