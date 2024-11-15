<script lang="ts">
	import MultiSelect from '$lib/components/global/MultiSelect.svelte';
	import { selectedGroup } from '$lib/stores/create-page';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let groups: string[];
	export let disabled: boolean = false;
</script>

<div title={$t('select_group')} class="select-list">
	<MultiSelect
		bind:selected={$selectedGroup}
		options={groups}
		placeholder={$t('select_group')}
		maxSelect={1}
		{disabled}
	/>
</div>

<style>
	.select-list {
		margin-right: 0em;
	}
</style>
