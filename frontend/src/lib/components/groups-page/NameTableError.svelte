<script lang="ts">
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

{#if checkNameError()}
	<p title="Error" class="error">
		<i class="material-symbols-rounded">error</i>{errorMessage(error)}
	</p>
{/if}

<style>
	.error {
		font-size: 0.8em;
	}
</style>
