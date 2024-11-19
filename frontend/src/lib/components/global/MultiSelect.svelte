<script lang="ts">
	import { MultiSelect, type Option } from 'svelte-multiselect';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let selected: string[];
	export let options: string[];
	export let placeholder: string = '';
	export let maxSelect: number | null = null;
	export let disabled: boolean = false;
	export let handleAdd: (e: CustomEvent<{ option: Option }>) => void = () => {};
	export let handleRemove: (e: CustomEvent<{ option: Option }>) => void = () => {};
	export let handleRemoveAll: () => void = () => {};
</script>

<MultiSelect
	bind:selected
	options={options.toSorted()}
	{placeholder}
	{maxSelect}
	{disabled}
	sortSelected={true}
	allowEmpty={true}
	duplicates={false}
	on:add={handleAdd}
	on:remove={handleRemove}
	on:removeAll={handleRemoveAll}
	createOptionMsg={$t('create_option')}
	defaultDisabledTitle={$t('default_disabled_title')}
	disabledInputTitle={$t('disabled_input_title')}
	noMatchingOptionsMsg={$t('no_matching_options')}
	duplicateOptionMsg={$t('duplicate_option')}
	removeAllTitle={$t('remove_all_title')}
	removeBtnTitle={$t('remove_btn_title')}
	--sms-max-width="100%"
	--sms-min-height="2.2em"
	--sms-border="1px solid var(--border-color-1)"
	--sms-border-radius="5px"
	--sms-bg="var(--secondary-color-2)"
	--sms-selected-bg="var(--primary-color-1)"
	--sms-active-color="var(--text-color-1)"
	--sms-li-active-bg="var(--secondary-color-1)"
	--sms-text-color="var(--text-color-1)"
	--sms-open-z-index="1"
	--sms-options-max-height="16.5em"
	--sms-options-border="1px solid var(--border-color-1)"
	--sms-options-border-radius="5px"
	--sms-options-border-width="1px"
	--sms-options-bg="var(--primary-color-1)"
	--sms-options-shadow="0px 4px 4px var(--shadow-color-1)"
	--sms-remove-btn-hover-color="var(--error-color-1)"
	--sms-remove-btn-hover-bg="var(--secondary-color-1)"
	--sms-disabled-bg="var(--secondary-color-1)"
>
	<i slot="expand-icon" class="symbol" class:open let:open>arrow_drop_down</i>
	<i slot="remove-icon" class="symbol close">close</i>
	<span slot="disabled-icon" />
</MultiSelect>

<style>
	i {
		font-variation-settings: 'wght' 700;
		transform: rotate(0deg);
		transition: transform 0.2s;
	}

	i.open {
		transform: rotate(180deg);
	}

	i.close {
		font-size: 1em;
	}
</style>
