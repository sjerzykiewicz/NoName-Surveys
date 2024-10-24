<script lang="ts">
	import MultiSelect from '$lib/components/MultiSelect.svelte';
	import { selectedGroup } from '$lib/stores/create-page';

	export let groups: string[];
	export let disabled: boolean = false;
</script>

<div title="Select group" class="select-list">
	<MultiSelect
		bind:selected={$selectedGroup}
		options={groups}
		placeholder="Select group"
		maxSelect={1}
		{disabled}
	/>
</div>

<style>
	.select-list {
		margin-right: 0em;
	}
</style>
