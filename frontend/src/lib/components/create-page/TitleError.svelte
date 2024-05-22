<script lang="ts">
	import { title } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';

	export let titleError: boolean;

	function errorMessage() {
		return 'Please enter survey title.';
	}

	$: checkTitleError = () => {
		const t = $title;
		return titleError && (t === null || t === undefined || t.length === 0);
	};
</script>

{#if checkTitleError()}
	<p title="Error" class="error" transition:slide={{ duration: 200, easing: cubicInOut }}>
		<i class="material-symbols-rounded">error</i>{errorMessage()}
	</p>
{/if}
