<script lang="ts">
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { GroupError } from '$lib/entities/GroupError';

	export let users: string[];
	export let error: GroupError;

	function errorMessage() {
		return 'Please select users.';
	}

	$: checkUsersError = () => {
		const u = users;
		return (
			error === GroupError.MembersRequired && (u === null || u === undefined || u.length === 0)
		);
	};
</script>

<div
	in:slide={{ delay: 200, duration: 200, easing: cubicInOut }}
	out:slide={{ duration: 200, easing: cubicInOut }}
>
	{#if checkUsersError()}
		<p title="Error" class="error" transition:slide={{ duration: 200, easing: cubicInOut }}>
			<i class="material-symbols-rounded">error</i>{errorMessage()}
		</p>
	{/if}
</div>
