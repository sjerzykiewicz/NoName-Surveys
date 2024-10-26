<script lang="ts">
	import { FileError } from '$lib/entities/FileError';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';

	export let error: FileError;
	export let element: HTMLInputElement | null;

	function errorMessage() {
		switch (error) {
			case FileError.FileRequired:
				return 'Please select a file.';
			case FileError.FileInvalid:
				return 'Please select a .txt file.';
		}
	}

	$: checkFileError = () => {
		switch (error) {
			case FileError.FileRequired:
				return element?.files?.length === 0;
			case FileError.FileInvalid:
				return element?.files?.[0].name.split('.').pop() !== 'txt';
		}
	};
</script>

{#if checkFileError()}
	<p title="Error" class="error" transition:slide={{ duration: 200, easing: cubicInOut }}>
		<i class="material-symbols-rounded">error</i>{errorMessage()}
	</p>
{/if}

<style>
	.error {
		margin: 0.5em 0em 0em 0em;
		font-size: 0.8em;
	}
</style>
