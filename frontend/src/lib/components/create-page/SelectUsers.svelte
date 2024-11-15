<script lang="ts">
	import MultiSelect from '$lib/components/global/MultiSelect.svelte';
	import { ringMembers } from '$lib/stores/create-page';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let users: string[];
	export let disabled: boolean = false;
</script>

<div title={$t('select_users')} class="select-list">
	<MultiSelect
		bind:selected={$ringMembers}
		options={users}
		placeholder={$t('select_users')}
		{disabled}
	/>
</div>

<style>
	.select-list {
		margin-right: 0em;
	}
</style>
