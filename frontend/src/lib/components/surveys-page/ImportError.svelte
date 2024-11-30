<script lang="ts">
	import { FileError } from '$lib/entities/FileError';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let error: FileError;
	export let element: HTMLInputElement | null;

	function errorMessage() {
		switch (error) {
			case FileError.FileRequired:
				return $t('error_no_file');
			case FileError.FileInvalid:
				return $t('error_file_not_json');
		}
	}

	$: checkFileError = () => {
		switch (error) {
			case FileError.FileRequired:
				return element?.files?.length === 0;
			case FileError.FileInvalid:
				return element?.files?.[0]?.name.split('.').pop() !== 'json';
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
