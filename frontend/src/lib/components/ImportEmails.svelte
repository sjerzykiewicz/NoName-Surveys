<script lang="ts">
	import EmailsWarning from '$lib/components/EmailsWarning.svelte';
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
	export let size: number = 1;
	export let width: string = 'unset';

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

		const emails = await processEmails();
		let invalidEmails: string[] = [];

		if (checkKeys) {
			invalidEmails = await filterUsers('filter-users-with-no-public-key', emails);
		} else {
			invalidEmails = await filterUsers('filter-unregistered-users', emails);
		}

		if (invalidEmails.length > 0 && $isErrorModalHidden) {
			$warningModalContent = `Could not import ${invalidEmails.length} users, because they haven't ${checkKeys ? 'generated keys' : 'registered'} yet.`;
			$isWarningModalHidden = false;
		}

		const validEmails = emails.filter((e) => !invalidEmails.includes(e));
		const newUsers = [...users, ...validEmails];

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

<div class="button-row" style="font-size: {size}em;">
	<div {title} class="file-div" class:disabled style="width: {width};">
		<span class="file-label">{label}</span>
		<label for={id}>
			<div class="file-input">
				<span class="file-button"
					><i class="material-symbols-rounded">upload_file</i>Select File</span
				>
				<span class="file-name">{fileName}</span>
			</div>
			<input type="file" name={id} {id} {disabled} on:change={handleFileChange} />
		</label>
	</div>
</div>
<EmailsWarning warning={fileWarning} element={fileElement} size={0.8} {disabled} />

<style>
	.button-row {
		margin-top: 0em;
	}

	.file-label {
		font-size: 0.8em;
	}

	.file-input {
		margin-top: 0.625em;
	}
</style>
