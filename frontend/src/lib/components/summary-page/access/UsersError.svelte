<script lang="ts">
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { GroupError } from '$lib/entities/GroupError';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let users: string[];
	export let error: GroupError;

	function errorMessage() {
		return $t('error_select_users');
	}

	$: checkUsersError = () => {
		const u = users;
		return (
			error === GroupError.MembersRequired && (u === null || u === undefined || u.length === 0)
		);
	};
</script>

{#if checkUsersError()}
	<p title={$t('error')} class="error" transition:slide={{ duration: 200, easing: cubicInOut }}>
		<i class="symbol">error</i>{errorMessage()}
	</p>
{/if}
