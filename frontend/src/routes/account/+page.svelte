<script lang="ts">
	import type { PageServerData } from './$types';
	import { page } from '$app/stores';
	import Header from '$lib/components/Header.svelte';
	import KeyError from '$lib/components/account-page/KeyError.svelte';
	import SignIn from '$lib/components/account-page/SignIn.svelte';
	import SignOut from '$lib/components/account-page/SignOut.svelte';

	export let data: PageServerData;

	let isKeyValid: boolean = false;
	let isSubmitted: boolean = false;

	function getKeyFromFile(text: string): string {
		const words = text.split(' ');
		if (words.length > 1) {
			if (words[0] === 'ssh-rsa') {
				isKeyValid = true;
				return words[1];
			}
		}
		isKeyValid = false;
		return '';
	}

	function handleSubmit(event: Event) {
		event.preventDefault();
		const fileInput = document.querySelector<HTMLInputElement>('#file');
		const file = fileInput?.files?.[0];
		const reader = new FileReader();
		if (file) {
			reader.readAsText(file);
			reader.onload = function (e) {
				const fileData = e.target?.result;
				const text = fileData as string;
				const publicKey = getKeyFromFile(text);
				fetch('/api/users/update-public-key', {
					method: 'POST',
					headers: {
						'Content-Type': 'application/json'
					},
					body: JSON.stringify({ email: data.session?.user?.email, public_key: publicKey })
				});
			};
		}
		isSubmitted = true;
	}
</script>

{#if $page.data.session}
	<Header>
		<div title="Your account" class="title">
			Signed in as {$page.data.session.user?.email}
		</div>
	</Header>

	<form on:submit={handleSubmit}>
		<label title="Select and upload public key file" for="file"
			>Select and upload public key file
			<div>
				<input title="Select file" type="file" name="file" id="file" />
			</div>
		</label>
		{#if isSubmitted}
			<KeyError {isKeyValid} />
		{/if}
		<button title="Upload file" class="save" type="submit"
			><i class="material-symbols-rounded">upload_file</i>Upload</button
		>
	</form>
	<SignOut />
{:else}
	<SignIn />
{/if}

<style>
	form {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		text-align: center;
		color: var(--text-color);
		font-size: 1.5em;
		text-shadow: 0px 4px 4px var(--shadow-color);
		width: 100%;
		margin-top: 1em;
		margin-bottom: 1em;
	}

	label {
		font-weight: bold;
	}

	input[type='file'] {
		margin-top: 0.5em;
		background-color: var(--secondary-dark-color);
		border: 1px solid var(--border-color);
		border-radius: 5px;
		font-size: 0.8em;
		cursor: default;
	}

	input[type='file']::file-selector-button {
		padding: 0.25em;
		background-color: var(--primary-color);
		border: none;
		border-right: 1px solid var(--border-color);
		color: var(--text-color);
		font-family: 'Jura';
		cursor: pointer;
		transition: 0.2s;
	}

	input[type='file']::file-selector-button:hover {
		background-color: var(--secondary-color);
	}

	input[type='file']::file-selector-button:active {
		background-color: var(--border-color);
	}

	.save {
		margin-top: 0.5em;
		font-size: 1em;
	}

	@media screen and (max-width: 767px) {
		form {
			font-size: 1em;
		}
	}
</style>
