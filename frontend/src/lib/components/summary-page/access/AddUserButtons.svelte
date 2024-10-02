<script lang="ts">
	import { invalidateAll } from '$app/navigation';
	import { page } from '$app/stores';
	import MultiSelect from '$lib/components/MultiSelect.svelte';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';

	export let users: string[];
	export let code: string;

	let isPanelVisible: boolean = false;
	let selectedUsers: string[] = [];

	function togglePanel() {
		isPanelVisible = !isPanelVisible;
	}

	function giveAccess(survey_code: string, user_emails_to_share_with: string[]) {
		fetch('/api/surveys/give-access', {
			method: 'POST',
			body: JSON.stringify({
				user_email: $page.data.session?.user?.email,
				survey_code: survey_code,
				user_emails_to_share_with: user_emails_to_share_with
			}),
			headers: {
				'Content-Type': 'application/json'
			}
		})
			.then(() => {
				selectedUsers = [];
				isPanelVisible = false;
				invalidateAll();
			})
			.catch(() => alert('Error giving access'));
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
	{#if isPanelVisible}
		<div class="users-panel" transition:slide={{ duration: 200, easing: cubicInOut }}>
			<div title="Select users" class="select-list">
				<MultiSelect bind:selected={selectedUsers} options={users} placeholder="Select users" />
			</div>
			<button title="Apply access" class="save" on:click={() => giveAccess(code, selectedUsers)}>
				<i class="material-symbols-rounded">done</i>Apply
			</button>
		</div>
	{/if}
</div>

<style>
	.users-panel {
		display: flex;
		flex: 1;
		align-items: flex-start;
	}

	.button-row {
		display: flex;
		flex-flow: row wrap;
		align-items: flex-start;
		justify-content: flex-start;
		align-content: space-between;
		font-size: 1.25em;
		margin-top: 0.5em;
	}

	.select-list {
		font-size: 0.8em;
		margin-right: 0.625em;
		margin-bottom: 0em;
	}

	.save i {
		font-variation-settings: 'wght' 700;
		transform: rotate(0deg);
		transition: transform 0.2s;
	}

	@media screen and (max-width: 767px) {
		.button-row {
			font-size: 1em;
		}
	}
</style>
