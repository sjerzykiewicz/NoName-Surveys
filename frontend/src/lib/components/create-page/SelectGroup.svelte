<script lang="ts">
	import MultiSelect from '../MultiSelect.svelte';
	import { selectedGroup } from '$lib/stores/create-page';

	export let groups: string[];
</script>

<div title="Select group" class="select-list">
	<MultiSelect
		bind:selected={$selectedGroup}
		options={groups}
		placeholder="Select group"
		maxSelect={1}
	/>
</div>
