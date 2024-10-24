<script lang="ts">
	import { page } from '$app/stores';
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';
	import SignIn from '$lib/components/account-page/SignIn.svelte';
	import SignOut from '$lib/components/account-page/SignOut.svelte';
	import DownloadKey from '$lib/components/account-page/DownloadKey.svelte';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import Modal from '$lib/components/Modal.svelte';
	import init, { get_keypair } from 'wasm';
	import { onMount } from 'svelte';
	import { errorModalContent, isErrorModalHidden, M } from '$lib/stores/global';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';

	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let isModalHidden: boolean = true;

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

	async function generateKeyPair() {
		const keyPair = get_keypair();
		const publicKey = keyPair.get_public_key();
		const privateKey = keyPair.get_private_key();
		const response = await fetch('/api/users/update-public-key', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				email: $page.data.session?.user?.email,
				public_key: publicKey
			})
		});

		if (!response.ok) {
			const body = await response.json();
			$errorModalContent = getErrorMessage(body.detail);
			$isErrorModalHidden = false;
			return;
		}

		download('noname-keys.txt', publicKey + '\n' + privateKey);
	}

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

{#if $page.data.session}
	<Modal
		icon="encrypted"
		title={$t('account_generating_keys')}
		bind:isHidden={isModalHidden}
		width={innerWidth <= $M ? 18 : 22}
	>
		<span slot="content"><Tx text="account_new_key_alert"></Tx></span>
		<button
			title={$t('generate')}
			class="save"
			on:click={() => {
				isModalHidden = true;
				generateKeyPair();
			}}
		>
			<i class="material-symbols-rounded">done</i><Tx text="generate"></Tx>
		</button>
		<button title={$t('cancel')} class="not" on:click={() => (isModalHidden = true)}>
			<i class="material-symbols-rounded">close</i><Tx text="cancel"></Tx>
		</button>
	</Modal>

	<Header>
		<div title="Your account" class="title">
			<Tx text="welcome"></Tx>, {$page.data.session.user?.email}
		</div>
	</Header>

	<Content>
		<DownloadKey bind:isModalHidden />
		<SignOut />
	</Content>
{:else}
	<Content>
		<SignIn />
	</Content>
{/if}

<style>
	button i {
		margin-right: 0.15em;
		font-variation-settings: 'wght' 700;
	}
</style>
