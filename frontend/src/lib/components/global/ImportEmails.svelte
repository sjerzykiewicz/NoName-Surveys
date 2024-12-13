<script lang="ts">
	import EmailsWarning from '$lib/components/global/EmailsWarning.svelte';
	import { FileError } from '$lib/entities/FileError';
	import { readFile } from '$lib/utils/readFile';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';
	import {
		isErrorModalHidden,
		errorModalContent,
		isWarningModalHidden,
		warningModalContent,
		M
	} from '$lib/stores/global';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let users: string[];
	export let title: string;
	export let label: string;
	export let checkKeys: boolean;
	export let invalidEmails: string[] = [];
	export let isExportButtonVisible: boolean = false;

	let fileElement: HTMLInputElement | null = null;
	let fileName: string = $t('no_file_selected');
	let fileWarning: FileError = FileError.NoError;

	async function filterUsers(filter: string, emails: string[]): Promise<string[]> {
		const response = await fetch(`/api/users/${filter}`, {
			method: 'POST',
			body: JSON.stringify({ emails: emails }),
			headers: {
				'Content-Type': 'application/json'
			}
		});

		if (!response.ok) {
			const body = await response.json();
			$errorModalContent = getErrorMessage(body.detail);
			$isErrorModalHidden = false;
			return emails;
		}

		return await response.json();
	}

	async function handleFileChange() {
		fileName = fileElement?.files?.[0]?.name ?? $t('no_file_selected');

		const emails: string[] = await processEmails();
		if (emails.length === 0) return;

		const endpoint: string = checkKeys
			? 'filter-users-with-no-public-key'
			: 'filter-unregistered-users';
		const invalidEmailsSet = new Set(await filterUsers(endpoint, emails));
		invalidEmails = Array.from(invalidEmailsSet);

		if (invalidEmailsSet.size > 0 && $isErrorModalHidden) {
			isExportButtonVisible = true;
			$warningModalContent = $t('could_not_import_emails', {
				number: invalidEmailsSet.size,
				reason: checkKeys ? $t('some_users_without_keys') : $t('some_users_not_registered')
			});
			$isWarningModalHidden = false;
		}

		const validEmails: string[] = emails.filter((e) => !invalidEmailsSet.has(e));
		const newUsers: string[] = [...users, ...validEmails];

		users = Array.from(new Set(newUsers));
	}

	function checkFileCorrectness() {
		fileWarning = FileError.NoError;

		if (fileElement?.files?.length === 0) {
			fileWarning = FileError.FileRequired;
			return false;
		} else if (fileElement?.files?.[0]?.name.split('.').pop() !== 'csv') {
			fileWarning = FileError.FileInvalid;
			return false;
		}

		return true;
	}

	async function processEmails() {
		if (!checkFileCorrectness()) return [];

		return await readFile(fileElement).then(
			(resolve) => {
				return resolve
					.split(/[;,]+/)
					.map((e) => e.trim())
					.filter((e) => e.length > 0);
			},
			(reject) => {
				$errorModalContent = reject as string;
				$isErrorModalHidden = false;
				return [];
			}
		);
	}

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

<div class="button-row">
	<div {title} class="file-div">
		<div class="label-container">
			<span class="file-label">{label}</span>
			<div title="" class="tooltip hoverable">
				<i class="symbol">help</i>
				<span class="tooltip-text {innerWidth <= $M ? 'bottom' : 'right'}">
					<Tx html="example_csv" /><a href="/account/faq#import-users"><Tx text="help" /></a>
				</span>
			</div>
		</div>
		<label>
			<div class="file-input">
				<span class="file-button"><i class="symbol">upload_file</i>{$t('select_file')}</span>
				<span class="file-name">{fileName}</span>
			</div>
			<input type="file" bind:this={fileElement} on:change={handleFileChange} />
		</label>
	</div>
</div>
<EmailsWarning warning={fileWarning} element={fileElement} />

<style>
	.tooltip {
		--tooltip-width: 19em;
	}

	.tooltip .tooltip-text {
		font-size: 0.8em;
		text-align: left;
	}

	.tooltip .tooltip-text.right {
		top: 350%;
	}

	.tooltip .tooltip-text.right::after {
		top: 12%;
	}

	.button-row {
		margin-top: 0em;
	}

	.file-div {
		width: var(--width, unset);
	}

	.file-label {
		font-size: 0.8em;
	}

	.file-input {
		margin-top: 0.625em;
	}

	.label-container {
		display: flex;
		align-items: center;
		gap: 0.5em;
	}

	@media screen and (max-width: 768px) {
		.tooltip .tooltip-text.bottom {
			left: -400%;
		}

		.tooltip .tooltip-text.bottom::after {
			left: 82.5%;
		}
	}
</style>
