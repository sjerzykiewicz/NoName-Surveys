<script lang="ts">
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let error: boolean;
	export let selectedGroups: string[];
	export let ringMembers: string[];
	export let useCrypto: boolean;

	function errorMessage() {
		return $t('define_respondent_group_error');
	}

	$: checkCryptoError = () => {
		const g = selectedGroups;
		const r = ringMembers;
		return (
			error &&
			useCrypto &&
			(g === null || g === undefined || g.length === 0) &&
			(r === null || r === undefined || r.length === 0)
		);
	};
</script>

{#if checkCryptoError()}
	<p title={$t('error')} class="error" transition:slide={{ duration: 200, easing: cubicInOut }}>
		<i class="symbol">error</i>
		{#key $t}
			{errorMessage()}
		{/key}
	</p>
{/if}

<style>
	.error {
		font-size: 0.8em;
		margin: 0em;
	}
</style>
