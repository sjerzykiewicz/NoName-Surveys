<script lang="ts">
	import { FileError } from '$lib/entities/FileError';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let warning: FileError;
	export let element: HTMLInputElement | null;

	function warningMessage() {
		switch (warning) {
			case FileError.FileRequired:
				return $t('warning_no_file');
			case FileError.FileInvalid:
				return $t('warning_file_not_csv');
		}
	}

	$: checkFileWarning = () => {
		switch (warning) {
			case FileError.FileRequired:
				return element?.files?.length === 0;
			case FileError.FileInvalid:
				return element?.files?.[0]?.name.split('.').pop() !== 'csv';
		}
	};
</script>

{#if checkFileWarning()}
	<p title={$t('warning')} class="warning" transition:slide={{ duration: 200, easing: cubicInOut }}>
		<i class="symbol">warning</i>
		{#key $t}
			{warningMessage()}
		{/key}
	</p>
{/if}
