<script lang="ts">
	import type { PageServerData } from './$types';
	import { page } from '$app/stores';
	import Header from '$lib/components/Header.svelte';
	// import KeyError from '$lib/components/account-page/KeyError.svelte';
	import SignIn from '$lib/components/account-page/SignIn.svelte';
	import SignOut from '$lib/components/account-page/SignOut.svelte';

	export let data: PageServerData;

	// let isKeyValid: boolean = false;
	// let isSubmitted: boolean = false;

	// function getKeyFromFile(text: string): string {
	// 	const words = text.split(' ');
	// 	if (words.length > 1) {
	// 		if (words[0] === 'ssh-rsa') {
	// 			isKeyValid = true;
	// 			return words[1];
	// 		}
	// 	}
	// 	isKeyValid = false;
	// 	return '';
	// }

	// function handleSubmit(event: Event) {
	// 	event.preventDefault();
	// 	const fileInput = document.querySelector<HTMLInputElement>('#file');
	// 	const file = fileInput?.files?.[0];
	// 	const reader = new FileReader();
	// 	if (file) {
	// 		reader.readAsText(file);
	// 		reader.onload = function (e) {
	// 			const fileData = e.target?.result;
	// 			const text = fileData as string;
	// 			const publicKey = getKeyFromFile(text);
	// 			fetch('/api/users/update-public-key', {
	// 				method: 'POST',
	// 				headers: {
	// 					'Content-Type': 'application/json'
	// 				},
	// 				body: JSON.stringify({ email: data.session?.user?.email, public_key: publicKey })
	// 			});
	// 		};
	// 	}
	// 	isSubmitted = true;
	// }

	import init, { get_keypair } from 'wasm';
	import { onMount } from 'svelte';

	onMount(async () => {
		await init();
	});

	function download(filename: string, text: string) {
		var element = document.createElement('a');
		element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
		element.setAttribute('download', filename);

		element.style.display = 'none';
		document.body.appendChild(element);

		element.click();

		document.body.removeChild(element);
	}

	function pluckKey(text: string): string {
		let lines = text.split('\n');
		lines.shift();
		lines.pop();
		return lines.join('');
	}
</script>

{#if $page.data.session}
	<Header>
		<div title="Your account" class="title">
			Signed in as {$page.data.session.user?.email}
		</div>
	</Header>

	<!-- <form on:submit={handleSubmit}>
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
	</form> -->
	<div class="download-key">
		<button
			class="save"
			on:click={async () => {
				const keyPair = get_keypair();
				fetch('/api/users/update-public-key', {
					method: 'POST',
					headers: {
						'Content-Type': 'application/json'
					},
					body: JSON.stringify({
						email: data.session?.user?.email,
						public_key: pluckKey(keyPair.get_public_key())
					})
				}).then((res) => {
					if (res.ok) {
						download('keys.txt', keyPair.get_public_key() + '\n' + keyPair.get_private_key());
					}
				});
			}}
		>
			Download keys file
		</button>
	</div>
	<SignOut />
{:else}
	<SignIn />
{/if}

<style>
	.download-key {
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
	.save {
		margin-top: 0.5em;
		font-size: 1em;
	}
</style>
