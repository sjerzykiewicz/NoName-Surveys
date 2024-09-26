<script lang="ts">
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { GroupError } from '$lib/entities/GroupError';

	export let members: string[];
	export let error: GroupError;

	function errorMessage() {
		return 'Please select group members.';
	}

	$: checkMembersError = () => {
		const m = members;
		return (
			error === GroupError.MembersRequired && (m === null || m === undefined || m.length === 0)
		);
	};
</script>

<div
	in:slide={{ delay: 200, duration: 200, easing: cubicInOut }}
	out:slide={{ duration: 200, easing: cubicInOut }}
>
	{#if checkMembersError()}
		<p title="Error" class="error" transition:slide={{ duration: 200, easing: cubicInOut }}>
			<i class="material-symbols-rounded">error</i>{errorMessage()}
		</p>
	{/if}
</div>
