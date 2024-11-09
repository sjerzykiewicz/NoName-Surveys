<script lang="ts">
	import EmailsWarning from '$lib/components/global/EmailsWarning.svelte';
	import { FileError } from '$lib/entities/FileError';
	import { readFile } from '$lib/utils/readFile';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';
	import {
		isErrorModalHidden,
		errorModalContent,
		isWarningModalHidden,
		warningModalContent
	} from '$lib/stores/global';

	export let users: string[];
	export let title: string;
	export let label: string;
	export let id: string;
	export let checkKeys: boolean;
	export let disabled: boolean = false;
	export let invalidEmails: string[] = [];

	let fileElement: HTMLInputElement | null = null;
	let fileName: string = 'No file selected';
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
		fileElement = document.querySelector<HTMLInputElement>('#emails-file');
		fileName = fileElement?.files?.[0]?.name ?? 'No file selected';

		const emails: string[] = await processEmails();
		const endpoint: string = checkKeys
			? 'filter-users-with-no-public-key'
			: 'filter-unregistered-users';
		const invalidEmailsSet = new Set(await filterUsers(endpoint, emails));
		invalidEmails = Array.from(invalidEmailsSet);

		if (invalidEmailsSet.size > 0 && $isErrorModalHidden) {
			$warningModalContent = `Could not import ${invalidEmailsSet.size} users, because they haven't ${checkKeys ? 'generated keys' : 'registered'} yet. You can export the list of invalid users if you want.`;
			$isWarningModalHidden = false;
		}

		const validEmails: string[] = emails.filter((e) => !invalidEmailsSet.has(e));
		const newUsers: string[] = [...users, ...validEmails];

		users = [...new Set(newUsers)];
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
					.split(';')
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
</script>

<div class="button-row">
	<div {title} class="file-div" class:disabled>
		<span class="file-label">{label}</span>
		<label for={id}>
			<div class="file-input">
				<span class="file-button"><i class="symbol">upload_file</i>Select File</span>
				<span class="file-name">{fileName}</span>
			</div>
			<input type="file" name={id} {id} {disabled} on:change={handleFileChange} />
		</label>
	</div>
</div>
<EmailsWarning warning={fileWarning} element={fileElement} {disabled} --font-size-warning />

<style>
	.button-row {
		margin-top: 0em;
		font-size: var(--font-size-button, 1em);
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
</style>
