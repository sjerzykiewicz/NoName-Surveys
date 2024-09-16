<script lang="ts">
	import { MultiSelect } from 'svelte-multiselect';
	import { ringMembers } from '$lib/stores/create-page';

	export let users: string[];
</script>

<div title="Select users" class="user-list">
	<MultiSelect
		bind:selected={$ringMembers}
		options={users}
		--sms-max-width="100%"
		--sms-min-height="2.2em"
		--sms-border="1px solid var(--border-color)"
		--sms-border-radius="5px"
		--sms-bg="var(--secondary-dark-color)"
		--sms-selected-bg="var(--primary-color)"
		--sms-active-color="var(--text-color)"
		--sms-li-active-bg="var(--secondary-color)"
		--sms-text-color="var(--text-color)"
		--sms-open-z-index="0"
		--sms-options-max-height="16.5em"
		--sms-options-border="1px solid var(--border-color)"
		--sms-options-border-radius="5px"
		--sms-options-border-width="1px"
		--sms-options-bg="var(--primary-color)"
		--sms-options-shadow="0px 4px 4px var(--shadow-color)"
		--sms-remove-btn-hover-color="var(--error-color)"
		--sms-remove-btn-hover-bg="var(--secondary-color)"
	/>
</div>

<style>
	.user-list {
		flex: 1;
		box-shadow: 0px 4px 4px var(--shadow-color);
	}

	@media screen and (max-width: 767px) {
		.user-list {
			font-size: 0.8em;
		}
	}
</style>
