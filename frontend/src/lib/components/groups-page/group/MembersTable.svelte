<script lang="ts">
	export let members: string[];
	export let selectedMembersToRemove: string[] = [];

	$: allSelected =
		selectedMembersToRemove.length === members.length && selectedMembersToRemove.length > 0;

	function toggleAll() {
		selectedMembersToRemove = allSelected ? [] : [...members];
	}
</script>

<table>
	<tr>
		<th title="Select all" class="checkbox-entry"
			><label
				><input
					type="checkbox"
					disabled={members.length === 0}
					on:change={toggleAll}
					checked={allSelected}
				/></label
			></th
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
			<td title={member} class="basic-entry">{member}</td>
		</tr>
	{/each}
</table>
