<script lang="ts">
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { GroupError } from '$lib/entities/GroupError';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let members: string[];
	export let error: GroupError;

	function errorMessage() {
		return $t('members_error');
	}

	$: checkMembersError = () => {
		const m = members;
		return (
			error === GroupError.MembersRequired && (m === null || m === undefined || m.length === 0)
		);
	};
</script>

{#if checkMembersError()}
	<p title={$t('error')} class="error" transition:slide={{ duration: 200, easing: cubicInOut }}>
		<i class="symbol">error</i>
		{#key [$t, error]}
			{errorMessage()}
		{/key}
	</p>
{/if}

<style>
	.error {
		margin: 0em;
	}
</style>
