<script lang="ts">
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { GroupError } from '$lib/entities/GroupError';
	import { LIMIT_OF_CHARS } from '$lib/stores/global';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let name: string;
	export let error: GroupError;
	export let groups: string[];

	function errorMessage(error: GroupError) {
		switch (error) {
			case GroupError.NameRequired:
				return $t('group_error_name_required');
			case GroupError.NameTooLong:
				return $t('group_error_name_too_long');
			case GroupError.NameNonUnique:
				return $t('group_error_already_exists');
			case GroupError.NameInvalid:
				return $t('group_error_name_invalid');
		}
	}

	$: checkNameError = () => {
		const n = name;
		switch (error) {
			case GroupError.NameRequired:
				return n === null || n === undefined || n.length === 0;
			case GroupError.NameTooLong:
				return n.length > $LIMIT_OF_CHARS;
			case GroupError.NameNonUnique:
				return groups.some((g) => g === n);
			case GroupError.NameInvalid:
				return n.match(/^[\p{L}\p{N} /-]+$/u) === null;
		}
	};
</script>

{#if checkNameError()}
	<p title={$t('error')} class="error" transition:slide={{ duration: 200, easing: cubicInOut }}>
		<i class="symbol">error</i>{errorMessage(error)}
	</p>
{/if}

<style>
	.error {
		font-size: var(--font-size, 1em);
	}
</style>
