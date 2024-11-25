<script lang="ts">
	import MultiSelect from '$lib/components/global/MultiSelect.svelte';
	import { errorModalContent, isErrorModalHidden } from '$lib/stores/global';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let groups: string[];
	export let disabled: boolean = false;
	export let ringMembers: string[] = [];
	export let selectedGroups: string[] = [];

	async function getGroupMembers(name: string): Promise<string[]> {
		const response = await fetch('/api/groups/fetch', {
			method: 'POST',
			body: JSON.stringify({ name: name }),
			headers: {
				'Content-Type': 'application/json'
			}
		});

		if (!response.ok) {
			const body = await response.json();
			$errorModalContent = getErrorMessage(body.detail);
			$isErrorModalHidden = false;
			return [];
		}

		const body: { email: string; has_public_key: boolean }[] = await response.json();
		return body.map((member) => member.email);
	}

	async function addRingMembers(groupName: string) {
		const groupMembers = await getGroupMembers(groupName);
		ringMembers = Array.from(new Set([...ringMembers, ...groupMembers]));
	}

	async function removeRingMembers(groupName: string) {
		const groupMembers = await getGroupMembers(groupName);
		ringMembers = ringMembers.filter((member) => !new Set(groupMembers).has(member));
	}
</script>

<div title={$t('select_group')} class="select-list">
	<MultiSelect
		bind:selected={selectedGroups}
		options={groups}
		placeholder={$t('select_group')}
		{disabled}
		handleAdd={(event) => addRingMembers(event.detail.option.toString())}
		handleRemove={(event) => removeRingMembers(event.detail.option.toString())}
		handleRemoveAll={() => (ringMembers = [])}
	/>
</div>

<style>
	.select-list {
		margin-right: 0em;
	}

	:global(.select-list *:where(div.multiselect > ul.selected)) {
		max-height: 9em;
	}
</style>
