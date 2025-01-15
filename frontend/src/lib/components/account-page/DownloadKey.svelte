<script lang="ts">
	import { L, LIMIT_OF_CHARS, M, errorModalContent, isErrorModalHidden } from '$lib/stores/global';
	import { formatDate } from '$lib/utils/formatDate';
	import Modal from '$lib/components/global/Modal.svelte';
	import init, { get_keypair } from 'wasm';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';
	import encryptKeys from '$lib/utils/encryptKeys';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext, onMount } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';
	import PassphraseError from './PassphraseError.svelte';
	import ConfirmError from './ConfirmError.svelte';
	import { downloadBinaryFile } from '$lib/utils/downloadFile';
	import { PassphraseErrorEnum } from '$lib/entities/PassphraseErrorEnum';
	import { magicNumber } from '$lib/entities/MagicNumber';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let lastTime: string;
	export let hasKey: boolean;

	let isModalHidden: boolean = true;
	let passphrase: string = '';
	let passphraseConfirm: string = '';
	let passphraseError: PassphraseErrorEnum = PassphraseErrorEnum.NoError;
	let passphraseConfirmError: PassphraseErrorEnum = PassphraseErrorEnum.NoError;
	let isGenerateButtonDisabled: boolean = false;

	const ERROR_THRESHOLD = 365;
	const WARNING_THRESHOLD = 335;

	const keysLink =
		'https://github.com/sjerzykiewicz/NoName-Surveys?tab=readme-ov-file#generate-keys';

	$: timeDiff = lastTime !== '' ? milisecondsToDays(Date.now() - Date.parse(lastTime)) : 0;

	function milisecondsToDays(miliseconds: number) {
		return parseInt((miliseconds / 1000 / 3600 / 24).toFixed(0));
	}

	function checkPassphraseCorrectness() {
		passphraseError = PassphraseErrorEnum.NoError;
		passphraseConfirmError = PassphraseErrorEnum.NoError;

		if (passphrase === '') {
			passphraseError = PassphraseErrorEnum.Empty;
			return false;
		} else if (passphrase !== passphraseConfirm) {
			passphraseConfirmError = PassphraseErrorEnum.ConfirmNotMatching;
			return false;
		}

		return true;
	}

	async function reloadCreationDate() {
		const response = await fetch('/api/users/get-key-creation-date');

		if (!response.ok) {
			const body = await response.json();
			$errorModalContent = getErrorMessage(body.detail);
			$isErrorModalHidden = false;
			return;
		}

		lastTime = await response.json();
	}

	async function reloadHasKey() {
		const response = await fetch('/api/users/has-public-key');

		if (!response.ok) {
			const body = await response.json();
			$errorModalContent = getErrorMessage(body.detail);
			$isErrorModalHidden = false;
			return;
		}

		hasKey = await response.json();
	}

	function hideModal() {
		isModalHidden = true;
		passphrase = '';
		passphraseConfirm = '';
		passphraseError = PassphraseErrorEnum.NoError;
		passphraseConfirmError = PassphraseErrorEnum.NoError;
	}

	async function generateKeyPair() {
		if (!checkPassphraseCorrectness()) return;

		try {
			const keyPair = get_keypair();
			const publicKey = keyPair.get_public_key();
			const privateKey = keyPair.get_private_key();
			const fingerprint = keyPair.get_fingerprint();

			const pemData = publicKey + '\n\n' + privateKey;
			const { salt, iv, ciphertext } = await encryptKeys(pemData, passphrase);
			const keysData = new Uint8Array(8 + salt.length + iv.length + ciphertext.length);
			keysData.set(magicNumber, 0);
			keysData.set(salt, 8);
			keysData.set(iv, 24);
			keysData.set(ciphertext, 36);

			downloadBinaryFile('noname-keys.bin', keysData);

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

			hideModal();
			reloadCreationDate();
			reloadHasKey();
		} catch (e) {
			$errorModalContent = e as string;
			$isErrorModalHidden = false;
			return;
		}
	}

	async function handleEnter(event: KeyboardEvent) {
		if (!isModalHidden && !isGenerateButtonDisabled && event.key === 'Enter') {
			event.preventDefault();
			event.stopImmediatePropagation();
			isGenerateButtonDisabled = true;
			await generateKeyPair();
			isGenerateButtonDisabled = false;
		}
	}

	onMount(async () => {
		await init();
	});

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />
<svelte:body on:keydown={handleEnter} />

<Modal
	icon="encrypted"
	title={$t('account_generating_keys')}
	bind:isHidden={isModalHidden}
	hide={hideModal}
	--width={innerWidth <= $M ? '20em' : '28em'}
>
	<span slot="content" class="content">
		{#if hasKey}
			<Tx text="account_new_key_alert" />
			<br />
			<br />
		{/if}
		<Tx text="provide_passphrase" />
		<br />
		<br />
		<label class="passphrase-label">
			<!-- svelte-ignore a11y-autofocus -->
			<input
				type="password"
				title={$t('passphrase_title')}
				class="passphrase-input"
				placeholder="{$t('passphrase_title')}..."
				required
				maxlength={$LIMIT_OF_CHARS}
				autocomplete="off"
				autofocus={innerWidth > $M}
				bind:value={passphrase}
			/></label
		>
		<PassphraseError error={passphraseError} {passphrase} />
		<br />
		<label class="passphrase-label">
			<input
				type="password"
				title={$t('confirm_passphrase')}
				class="passphrase-input"
				placeholder="{$t('confirm_passphrase')}..."
				required
				maxlength={$LIMIT_OF_CHARS}
				autocomplete="off"
				bind:value={passphraseConfirm}
			/>
		</label>
		<ConfirmError error={passphraseConfirmError} {passphrase} {passphraseConfirm} />
	</span>
	<button
		title={$t('generate')}
		class="done"
		disabled={isGenerateButtonDisabled}
		on:click={async () => {
			isGenerateButtonDisabled = true;
			await generateKeyPair();
			isGenerateButtonDisabled = false;
		}}
	>
		<i class="symbol">done</i><Tx text="generate" />
	</button>
	<button title={$t('cancel')} class="not" on:click={hideModal}>
		<i class="symbol">close</i><Tx text="cancel" />
	</button>
</Modal>

<div title={$t('account_keys_info_title')} class="info">
	<div class="info-text">
		<Tx html="account_keys_info" />
	</div>
</div>
<div class="key-container">
	<div class="key-box">
		<div class="download-key">
			<button title={$t('account_new_key')} class="save" on:click={() => (isModalHidden = false)}>
				<i class="symbol">encrypted</i><Tx text="account_new_key" />
			</button>
			<div class="tooltip hoverable">
				<i class="symbol">help</i>
				<span class="tooltip-text {innerWidth <= $L ? 'bottom' : 'right'}">
					<Tx text="account_generate_info" /><a href={keysLink} target="_blank"
						><Tx text="read_more" /></a
					>
				</span>
			</div>
		</div>
		{#if lastTime}
			<div class="last-update-container">
				<div title={$t('account_last_key_update')} class="last-update-info">
					<Tx text="account_last_key_update" />: {formatDate(lastTime)}
				</div>
				<div class="tooltip hoverable">
					<i class="symbol">help</i>
					<span class="tooltip-text {innerWidth <= $L ? 'bottom' : 'right'}">
						<Tx text="account_key_update_info" /><a href="/account/faq#keys"><Tx text="help" /></a>
					</span>
				</div>
			</div>
			<div class="warning-div">
				{#if timeDiff >= ERROR_THRESHOLD}
					<p title={$t('account_expiration_critical')} class="error">
						<i class="symbol">error</i><Tx
							html="account_keys_expired"
							params={{ number: timeDiff }}
						/>
					</p>
				{:else if timeDiff >= WARNING_THRESHOLD}
					<p title={$t('account_expiration_warning')} class="warning">
						<i class="symbol">warning</i><Tx
							html="account_keys_expire_soon"
							params={{ number: timeDiff }}
						/>
					</p>
				{/if}
			</div>
		{/if}
	</div>
</div>

<style>
	.content {
		text-align: justify;
	}

	.tooltip i {
		font-size: 1.25em;
	}

	.key-container {
		display: flex;
		justify-content: flex-start;
		color: var(--text-color-1);
		width: 100%;
		padding-bottom: 0.5em;
		font-size: 1.5em;
		border-bottom: 1px solid var(--border-color-1);
		transition:
			0.2s,
			outline 0s;
	}

	.key-box {
		display: flex;
		flex-direction: column;
	}

	.download-key .tooltip {
		--tooltip-width: 23em;
	}

	.download-key .tooltip .tooltip-text {
		text-align: left;
		font-size: 0.7em;
	}

	.download-key {
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: flex-start;
		width: 100%;
		padding-bottom: 0.5em;
	}

	.download-key button {
		margin-right: 0.5em;
	}

	.last-update-container {
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: flex-start;
		width: 100%;
		font-size: 0.8em;
		cursor: default;
	}

	.last-update-container .tooltip {
		--tooltip-width: 14em;
	}

	.last-update-container .tooltip .tooltip-text {
		text-align: left;
		font-size: 0.8em;
	}

	.last-update-info {
		margin-right: 0.5em;
		font-size: 0.8em;
		text-shadow: var(--shadow);
	}

	.warning-div {
		display: flex;
		justify-content: flex-start;
		width: 100%;
	}

	.warning,
	.error {
		font-size: 0.5em;
	}

	.warning i,
	.error i {
		margin-right: 0.5em;
	}

	@media screen and (max-width: 1440px) {
		.download-key .tooltip {
			--tooltip-width: 18em;
		}
	}

	@media screen and (max-width: 768px) {
		.key-container {
			font-size: 1.25em;
		}

		.download-key .tooltip .tooltip-text.bottom {
			left: -400%;
		}

		.download-key .tooltip .tooltip-text.bottom::after {
			left: 92.5%;
		}

		.last-update-container .tooltip .tooltip-text.bottom {
			left: -200%;
		}

		.last-update-container .tooltip .tooltip-text.bottom::after {
			left: 76%;
		}
	}
</style>
