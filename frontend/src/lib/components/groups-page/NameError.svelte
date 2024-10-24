<script lang="ts">
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { GroupError } from '$lib/entities/GroupError';
	import { LIMIT_OF_CHARS } from '$lib/stores/global';

	export let name: string;
	export let error: GroupError;
	export let groups: string[];

	function errorMessage(error: GroupError) {
		switch (error) {
			case GroupError.NameRequired:
				return 'Please enter group name.';
			case GroupError.NameTooLong:
				return 'Group name must be ' + $LIMIT_OF_CHARS + ' or less characters long.';
			case GroupError.NameNonUnique:
				return 'This group name already exists.';
			case GroupError.NameInvalid:
				return 'Group name can only contain letters, numbers, spaces, slashes and hyphens.';
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

<div
	in:slide={{ delay: 200, duration: 200, easing: cubicInOut }}
	out:slide={{ duration: 200, easing: cubicInOut }}
>
	{#if checkNameError()}
		<p title="Error" class="error" transition:slide={{ duration: 200, easing: cubicInOut }}>
			<i class="material-symbols-rounded">error</i>{errorMessage(error)}
		</p>
	{/if}
</div>
