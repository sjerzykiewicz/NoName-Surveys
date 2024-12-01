<script lang="ts">
	import { FileError } from '$lib/entities/FileError';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';
	import { magicNumber } from '$lib/entities/MagicNumber';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let error: FileError;
	export let element: HTMLInputElement | null;
	export let byteArray: Uint8Array;

	function errorMessage() {
		switch (error) {
			case FileError.FileRequired:
				return $t('error_no_file');
			case FileError.FileInvalid:
				return $t('invalid_key_file_format');
		}
	}

	$: checkFileError = () => {
		switch (error) {
			case FileError.FileRequired:
				return element?.files?.length === 0;
			case FileError.FileInvalid:
				return byteArray.slice(0, 8).toString() !== magicNumber.toString();
		}
	};
</script>

{#if checkFileError()}
	<p title={$t('error')} class="error" transition:slide={{ duration: 200, easing: cubicInOut }}>
		<i class="symbol">error</i>
		{#key [$t, error]}
			{errorMessage()}
		{/key}
	</p>
{/if}

<style>
	.error {
		font-size: 0.8em;
	}
</style>
