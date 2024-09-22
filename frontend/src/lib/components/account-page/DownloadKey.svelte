<script lang="ts">
	import type { PageServerData } from '../../../routes/account/$types';
	import init, { get_keypair } from 'wasm';
	import { onMount } from 'svelte';

	export let data: PageServerData;

	let innerWidth: number;

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
		if (!confirm('Are you sure you want to generate new keys?')) {
			return;
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
				download('noname-keys.txt', publicKey + '\n' + privateKey);
			}
		});
	}
</script>

<svelte:window bind:innerWidth />

<div class="download-key">
	<button title="Generate new key pair" class="save" on:click={generateKeyPair}>
		<i class="material-symbols-rounded">encrypted</i>Generate new key pair
	</button>
	<div class="tooltip">
		<i class="material-symbols-rounded">info</i>
		<span class="tooltip-text {innerWidth <= 633 ? 'bottom' : 'right'}">
			These keys allow you to participate in secure surveys. Once they are generated, it is your
			responsibility to keep them safe. When submitting a secure survey, you will be asked to
			provide these keys to your browser for digital signature.
		</span>
	</div>
</div>

<style>
	.tooltip {
		--tooltip-width: 29em;
	}

	.tooltip i {
		font-size: 1.25em;
	}

	.download-key {
		display: flex;
		flex-direction: row;
		align-items: center;
		color: var(--text-color);
		font-size: 1.5em;
		text-shadow: 0px 4px 4px var(--shadow-color);
		width: fit-content;
		margin-inline: auto;
		padding-top: 1em;
		padding-bottom: 1.5em;
		border-bottom: 1px solid var(--border-color);
	}

	.download-key button {
		margin-right: 0.5em;
	}

	@media screen and (max-width: 1512px) {
		.tooltip {
			--tooltip-width: 17em;
		}
	}

	@media screen and (max-width: 1048px) {
		.tooltip {
			--tooltip-width: 9.5em;
		}
	}

	@media screen and (max-width: 767px) {
		.download-key {
			font-size: 1.25em;
		}
	}

	@media screen and (max-width: 633px) {
		.tooltip {
			--tooltip-width: 19em;
		}

		.tooltip .tooltip-text.bottom {
			left: unset;
			right: -25%;
			margin-left: 0em;
			margin-right: -0.75em;
		}

		.tooltip .tooltip-text.bottom::after {
			left: 92%;
			margin-left: -0.75em;
		}
	}
</style>
