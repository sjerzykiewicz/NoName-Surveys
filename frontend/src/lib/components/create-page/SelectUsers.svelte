<script lang="ts">
	import MultiSelect from '$lib/components/MultiSelect.svelte';
	import { ringMembers } from '$lib/stores/create-page';

	export let users: string[];
	export let disabled: boolean = false;
</script>

<div title="Select users" class="select-list">
	<MultiSelect bind:selected={$ringMembers} options={users} placeholder="Select users" {disabled} />
</div>

<style>
	.select-list {
		margin-right: 0em;
	}
</style>
