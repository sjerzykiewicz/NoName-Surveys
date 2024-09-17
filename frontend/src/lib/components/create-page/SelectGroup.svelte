<script lang="ts">
	import { selectedGroup } from '$lib/stores/create-page';

	export let groups: string[];

	if (groups.length > 0) {
		$selectedGroup = groups[0];
	}
</script>

<div>
	<select title="Select group" bind:value={$selectedGroup}>
		{#each groups as group}
			<option value={group}>
				{group}
			</option>
		{/each}
	</select>
</div>

<style>
	div {
		display: flex;
		max-width: 18.4em;
	}

	select {
		flex: 1;
		cursor: pointer;
		overflow-wrap: break-word;
		text-overflow: ellipsis;
		box-shadow: 0px 4px 4px var(--shadow-color);
		font-size: 1.25em;
		height: 1.75em;
		max-width: 100%;
	}

	@media screen and (max-width: 767px) {
		div {
			max-width: 16em;
		}

		select {
			font-size: 1em;
		}
	}
</style>
