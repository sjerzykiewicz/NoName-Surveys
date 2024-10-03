<script lang="ts">
	import MultiSelect from '$lib/components/MultiSelect.svelte';
	import { ringMembers } from '$lib/stores/create-page';

	export let users: string[];
</script>

<div title="Select users" class="select-list">
	<MultiSelect bind:selected={$ringMembers} options={users} placeholder="Select users" />
</div>
