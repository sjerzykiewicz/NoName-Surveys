<script lang="ts">
	import { FileError } from '$lib/entities/FileError';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';

	export let warning: FileError;
	export let element: HTMLInputElement | null;
	export let disabled: boolean = false;

	function warningMessage() {
		switch (warning) {
			case FileError.FileRequired:
				return 'No file selected.';
			case FileError.FileInvalid:
				return 'File must be in .csv format.';
		}
	}

	$: checkFileWarning = () => {
		switch (warning) {
			case FileError.FileRequired:
				return !disabled && element?.files?.length === 0;
			case FileError.FileInvalid:
				return !disabled && element?.files?.[0]?.name.split('.').pop() !== 'csv';
		}
	};
</script>

{#if checkFileWarning()}
	<p title="Warning" class="warning" transition:slide={{ duration: 200, easing: cubicInOut }}>
		<i class="symbol">warning</i>{warningMessage()}
	</p>
{/if}

<style>
	.warning {
		font-size: var(--font-size-warning, 1em);
	}
</style>
