<script lang="ts">
	import { page } from '$app/stores';
	import Header from '$lib/components/global/Header.svelte';
	import Content from '$lib/components/global/Content.svelte';
	import Footer from '$lib/components/global/Footer.svelte';
	import OpenSourceInfo from '$lib/components/global/OpenSourceInfo.svelte';
	import SignIn from '$lib/components/account-page/SignIn.svelte';
	import SignOut from '$lib/components/account-page/SignOut.svelte';
	import DownloadKey from '$lib/components/account-page/DownloadKey.svelte';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import Modal from '$lib/components/global/Modal.svelte';
	import init, { get_keypair } from 'wasm';
	import { onMount } from 'svelte';
	import { errorModalContent, isErrorModalHidden, M } from '$lib/stores/global';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';
	import { downloadFile } from '$lib/utils/downloadFile';
	import { invalidateAll } from '$app/navigation';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';
	import AccountButtons from '$lib/components/account-page/AccountButtons.svelte';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let data;
	export let isModalHidden: boolean = true;

	onMount(async () => {
		await init();
	});

	async function generateKeyPair() {
		try {
			const keyPair = get_keypair();
			const publicKey = keyPair.get_public_key();
			const privateKey = keyPair.get_private_key();
			const fingerprint = keyPair.get_fingerprint();
			const response = await fetch('/api/users/update-public-key', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({
					public_key: publicKey,
					fingerprint: fingerprint
				})
			});

			if (!response.ok) {
				const body = await response.json();
				$errorModalContent = getErrorMessage(body.detail);
				$isErrorModalHidden = false;
				return;
			}

			downloadFile('noname-keys.pem', publicKey + '\n\n' + privateKey);
			await invalidateAll();
		} catch (e) {
			$errorModalContent = e as string;
			$isErrorModalHidden = false;
			return;
		}
	}

	onMount(() => {
		function handleEnter(event: KeyboardEvent) {
			if (!isModalHidden && event.key === 'Enter') {
				event.preventDefault();
				isModalHidden = true;
				generateKeyPair();
				event.stopImmediatePropagation();
			}
		}

		document.body.addEventListener('keydown', handleEnter);

		return () => {
			document.body.removeEventListener('keydown', handleEnter);
		};
	});

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

{#if $page.data.session}
	<Modal
		icon="encrypted"
		title={$t('account_generating_keys')}
		bind:isHidden={isModalHidden}
		--width={innerWidth <= $M ? '20em' : '22em'}
	>
		<span slot="content" class="content"><Tx text="account_new_key_alert" /></span>
		<button
			title={$t('generate')}
			class="done"
			on:click={() => {
				isModalHidden = true;
				generateKeyPair();
			}}
		>
			<i class="symbol">done</i><Tx text="generate" />
		</button>
		<button title={$t('cancel')} class="not" on:click={() => (isModalHidden = true)}>
			<i class="symbol">close</i><Tx text="cancel" />
		</button>
	</Modal>

	<Header>
		<div title={$t('your_account')} class="title static">
			<Tx text="welcome" />, {$page.data.session.user?.email.split('@')[0]}!
			{#if data.hasKey}
				<span title="" class="tooltip">
					<i class="symbol generated">key</i>
					<span class="tooltip-text left">
						<Tx text="keys_generated" />
					</span>
				</span>
			{:else}
				<span title="" class="tooltip">
					<i class="symbol">key_off</i>
					<span class="tooltip-text left">
						<Tx text="keys_not_generated" />
					</span>
				</span>
			{/if}
		</div>
	</Header>

	<Content>
		<DownloadKey bind:isModalHidden lastTime={data.keyCreationDate} />
		<AccountButtons />
		<SignOut />
	</Content>
{:else}
	<Content>
		<SignIn />
	</Content>
{/if}
<Footer>
	<OpenSourceInfo />
</Footer>

<style>
	.tooltip .tooltip-text {
		font-size: 0.8em;
	}

	.generated {
		color: var(--accent-color-1);
	}

	.content {
		text-align: justify;
	}
</style>
