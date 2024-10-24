<script lang="ts">
	import { useCrypto, ringMembers, selectedGroup } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';

	export let error: boolean;

	function errorMessage() {
		return 'Please define respondent group.';
	}

	$: checkCryptoError = () => {
		const g = $selectedGroup;
		const r = $ringMembers;
		return (
			error &&
			$useCrypto &&
			(g === null || g === undefined || g.length === 0) &&
			(r === null || r === undefined || r.length === 0)
		);
	};
</script>

{#if checkCryptoError()}
	<p title="Error" class="error" transition:slide={{ duration: 200, easing: cubicInOut }}>
		<i class="material-symbols-rounded">error</i>{errorMessage()}
	</p>
{/if}

<style>
	.error {
		font-size: 0.8em;
		margin: 0em;
	}
</style>
