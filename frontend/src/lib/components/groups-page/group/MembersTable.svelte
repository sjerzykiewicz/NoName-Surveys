<script lang="ts">
	import { goto, invalidateAll } from '$app/navigation';
	import { page } from '$app/stores';

	export let users: string[];
	export let group: string;

	let selectedUsers: string[] = [];

	$: allSelected = selectedUsers.length === users.length;

	function toggleAll() {
		selectedUsers = allSelected ? [] : [...users];
	}

	async function removeMembers() {
		const deleteResponse = await fetch('/api/groups/delete', {
			method: 'POST',
			body: JSON.stringify({ user_email: $page.data.session?.user?.email, name: group }),
			headers: {
				'Content-Type': 'application/json'
			}
		});

		if (!deleteResponse.ok) {
			const body = await deleteResponse.json();
			alert(body.detail);
			return;
		}

		if (allSelected) {
			goto('/groups', { replaceState: true, invalidateAll: true });
			return;
		}

		const members = users.filter((user: string) => !selectedUsers.includes(user));

		const createResponse = await fetch('/api/groups/create', {
			method: 'POST',
			body: JSON.stringify({
				user_email: $page.data.session?.user?.email,
				user_group_name: group,
				user_group_members: members
			}),
			headers: {
				'Content-Type': 'application/json'
			}
		});

		if (!createResponse.ok) {
			const body = await createResponse.json();
			alert(body.detail);
			return;
		}

		selectedUsers = [];
		invalidateAll();
	}
</script>

<table>
	<tr>
		<th title="Select all" class="checkbox-entry"
			><label
				><input
					type="checkbox"
					disabled={users.length === 0}
					on:change={toggleAll}
					checked={allSelected}
				/></label
			></th
		>
		<th title="Group members" id="title-header">Group Members</th>
	</tr>
	{#each users.toSorted() as user}
		<tr>
			<td title="Select {user}" class="checkbox-entry"
				><label>
					<input type="checkbox" bind:group={selectedUsers} value={user} />
				</label></td
			>
			<td title={user} class="basic-entry">{user}</td>
		</tr>
	{/each}
</table>
<div class="button-row">
	<button
		title="Remove selected group members"
		disabled={selectedUsers.length === 0}
		on:click={removeMembers}
	>
		<i class="material-symbols-rounded">delete</i>Members
	</button>
</div>

<style>
	.button-row {
		display: flex;
		flex-flow: row wrap;
		align-items: flex-start;
		justify-content: flex-start;
		align-content: space-between;
		font-size: 1.25em;
		margin-top: 0.5em;
	}

	button i {
		margin-right: 0.15em;
		/* font-variation-settings: 'wght' 700; */
	}

	@media screen and (max-width: 768px) {
		.button-row {
			font-size: 1em;
		}
	}
</style>
