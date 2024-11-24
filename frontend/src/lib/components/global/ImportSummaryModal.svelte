<script lang="ts">
	import { goto } from '$app/navigation';
	import { readFile } from '$lib/utils/readFile';
	import { FileError } from '$lib/entities/FileError';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';
	import { isErrorModalHidden, errorModalContent, M } from '$lib/stores/global';
	import Modal from '$lib/components/global/Modal.svelte';
	import ImportError from '$lib/components/surveys-page/ImportError.svelte';
	import { page } from '$app/stores';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let isHidden: boolean = true;

	let fileElement: HTMLInputElement | null = null;
	let fileName: string = $t('no_file_selected');
	let fileError: FileError = FileError.NoError;

	function handleFileChange() {
		fileName = fileElement?.files?.[0]?.name ?? $t('no_file_selected');
	}

	function checkFileCorrectness() {
		fileError = FileError.NoError;

		if (fileElement?.files?.length === 0) {
			fileError = FileError.FileRequired;
			return false;
		} else if (fileElement?.files?.[0]?.name.split('.').pop() !== 'json') {
			fileError = FileError.FileInvalid;
			return false;
		}

		return true;
	}

	async function processFile() {
		return await readFile(fileElement).then(
			(resolve) => {
				return resolve;
			},
			(reject) => {
				$errorModalContent = reject as string;
				$isErrorModalHidden = false;
				return '';
			}
		);
	}

	async function importSummary() {
		if (!checkFileCorrectness()) return;

		try {
			const fileContent = JSON.parse(await processFile());
			document.cookie = 'imported_summary=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
			document.cookie = `imported_summary=${encodeURIComponent(JSON.stringify(fileContent))}; expires=; path=/;`;
		} catch (e) {
			$errorModalContent = getErrorMessage(e as string);
			$isErrorModalHidden = false;
			return;
		}

		isHidden = true;
		if ($page.url.pathname === '/surveys/' + $page.params.surveysPage + '/imported') {
			window.location.reload();
		} else {
			await goto('/surveys/' + $page.params.surveysPage + '/imported', { invalidateAll: true });
		}
	}

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

<Modal
	icon="upload_file"
	title={$t('importing_summary')}
	bind:isHidden
	--width={innerWidth <= $M ? '20em' : '26em'}
>
	<div slot="content">
		<span><Tx text="importing_summary_alert" /></span>
		<div class="import">
			<div class="button-row">
				<div title={$t('import_summary_title')} class="file-div">
					<label>
						<div class="file-input">
							<span class="file-button"><i class="symbol">upload_file</i>{$t('select_file')}</span>
							<span class="file-name">{fileName}</span>
						</div>
						<input type="file" bind:this={fileElement} on:change={handleFileChange} />
					</label>
				</div>
			</div>
			<ImportError error={fileError} element={fileElement} />
		</div>
	</div>
	<button title={$t('submit_file')} class="done" on:click={importSummary}
		><i class="symbol">done</i><Tx text="submit" /></button
	>
</Modal>

<style>
	.import {
		font-size: 0.8em;
	}

	.file-div {
		width: 100%;
	}

	@media screen and (max-width: 768px) {
		.import {
			font-size: 1em;
		}
	}
</style>
