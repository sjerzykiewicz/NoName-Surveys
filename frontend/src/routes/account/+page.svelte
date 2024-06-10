<script lang="ts">
	import type { PageServerData } from './$types';
	import { page } from '$app/stores';
	import Header from '$lib/components/Header.svelte';
	import SignIn from '$lib/components/account-page/SignIn.svelte';
	import SignOut from '$lib/components/account-page/SignOut.svelte';

	export let data: PageServerData;

	import init, { get_keypair } from 'wasm';
	import { onMount } from 'svelte';

	let updateKeyButtonClicked = false;

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
</script>

{#if $page.data.session}
	<Header>
		<div title="Your account" class="title">
			Signed in as {$page.data.session.user?.email}
		</div>
	</Header>

	<div class="download-key">
		<button
			class="save"
			on:click={async () => {
				if (!updateKeyButtonClicked) {
					const confirmChange = confirm('Are you sure you want to change your keys?');
					if (confirmChange) {
						updateKeyButtonClicked = true;
					} else {
						return;
					}
				}

				const keyPair = get_keypair();
				const publicKey = keyPair.get_public_key();
				const privateKey = keyPair.get_private_key();
				fetch('/api/users/update-public-key', {
					method: 'POST',
					headers: {
						'Content-Type': 'application/json'
					},
					body: JSON.stringify({
						email: data.session?.user?.email,
						public_key: publicKey
					})
				}).then((res) => {
					if (res.ok) {
						download(
							'noname-keys.txt',
							publicKey +
								'----------------------------------------------------------------\n' +
								privateKey
						);
					}
				});
			}}
		>
			Generate new key pair
		</button>
		<div title="Key information" class="info">
			<i class="material-symbols-rounded">info</i>
			<div class="text">
				These keys allow you to participate in secure surveys. Once they are generated, it is your
				responsibility to keep them safe. When submitting a secure survey, you will be asked to
				provide these keys to your browser for encryption.
			</div>
		</div>
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

	.info {
		display: flex;
		flex-flow: row;
		align-items: center;
		justify-content: center;
		margin-top: 0.5em;
		font-size: 0.67em;
		margin: 0.75em;
		text-shadow: 0px 4px 4px var(--shadow-color);
		cursor: default;
		overflow-wrap: break-word;
	}

	.info i {
		font-size: 1.5em;
		margin-right: 0.5em;
	}

	.text {
		text-align: justify;
	}

	@media screen and (max-width: 767px) {
		.info {
			flex-flow: column;
		}

		.info i {
			margin-right: 0em;
			margin-bottom: 0.5em;
		}
	}
</style>
