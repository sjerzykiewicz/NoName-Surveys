<script lang="ts">
	import { errorModalContent, isErrorModalHidden, XL } from '$lib/stores/global';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';

	export let members: string[];
	export let selectedMembersToRemove: string[] = [];

	$: allSelected =
		selectedMembersToRemove.length === members.length && selectedMembersToRemove.length > 0;

	function toggleAll() {
		selectedMembersToRemove = allSelected ? [] : [...members];
	}

	async function hasPublicKey(member: string): Promise<boolean> {
		console.log(member);
		const response = await fetch('/api/users/has-public-key', {
			method: 'POST',
			body: JSON.stringify({
				user_email: member
			}),
			headers: {
				'Content-Type': 'application/json'
			}
		});

		if (!response.ok) {
			const body = await response.json();
			$errorModalContent = getErrorMessage(body.detail);
			$isErrorModalHidden = false;
			return false;
		}

		return await response.json();
	}

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

<table>
	<tr>
		<th title="Select all" class="checkbox-entry" class:disabled={members.length === 0}
			><label
				><input
					type="checkbox"
					disabled={members.length === 0}
					on:change={toggleAll}
					checked={allSelected}
				/></label
			></th
		>
		<th title="Keys information" id="info-header"
			><i class="material-symbols-rounded">encrypted</i></th
		>
		<th title="Group members" id="title-header">Group Members</th>
	</tr>
	{#each members.toSorted() as member}
		<tr>
			<td title="Select {member}" class="checkbox-entry"
				><label>
					<input type="checkbox" bind:group={selectedMembersToRemove} value={member} />
				</label></td
			>
			<td class="info-entry tooltip">
				{#await hasPublicKey(member)}
					<i class="material-symbols-rounded">sync</i>
					<span class="tooltip-text {innerWidth <= $XL ? 'right' : 'left'}"
						>Checking if user has generated his keys.</span
					>
				{:then hasKey}
					{#if hasKey}
						<i class="material-symbols-rounded">key</i>
						<span class="tooltip-text {innerWidth <= $XL ? 'right' : 'left'}"
							>This user has already generated his keys.</span
						>
					{:else}
						<i class="material-symbols-rounded">key_off</i>
						<span class="tooltip-text {innerWidth <= $XL ? 'right' : 'left'}"
							>This user has not generated his keys yet.</span
						>
					{/if}
				{:catch}
					<i class="material-symbols-rounded">error</i>
					<span class="tooltip-text {innerWidth <= $XL ? 'right' : 'left'}"
						>Could not check if user has generated his keys.</span
					>
				{/await}
			</td>
			<td title={member} class="basic-entry">{member}</td>
		</tr>
	{/each}
</table>
