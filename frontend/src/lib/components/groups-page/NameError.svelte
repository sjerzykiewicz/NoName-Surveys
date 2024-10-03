<script lang="ts">
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { GroupError } from '$lib/entities/GroupError';

	export let name: string;
	export let error: GroupError;
	export let groups: string[];

	function errorMessage(error: GroupError) {
		switch (error) {
			case GroupError.NameRequired:
				return 'Please enter group name.';
			case GroupError.NameNonUnique:
				return 'This group name already exists.';
		}
	}

	$: checkNameError = () => {
		const n = name;
		switch (error) {
			case GroupError.NameRequired:
				return n === null || n === undefined || n.length === 0;
			case GroupError.NameNonUnique:
				return groups.some((g) => g === n);
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

<style>
	.error {
		margin-left: 6.6em;
	}
</style>
