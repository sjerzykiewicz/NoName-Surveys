<script lang="ts">
	import { onMount } from 'svelte';
	import noname_black from '$lib/assets/noname_black.png';

	export let href: string;
	export let id: string;
	export let codeSize: number;
	export let codeMargin: number = 0;
	export let imageSize: number = 1;
	export let imageMargin: number = 0;

	onMount(() => {
		let script = document.createElement('script');
		script.src = 'https://unpkg.com/qr-code-styling@1.5.0/lib/qr-code-styling.js';
		document.head.appendChild(script);

		script.onload = () => {
			// @ts-expect-error QRCodeStyling is defined in the script above
			// eslint-disable-next-line no-undef
			let qrCode = new QRCodeStyling({
				width: codeSize,
				height: codeSize,
				margin: codeMargin,
				data: href,
				image: noname_black,
				dotsOptions: {
					color: '#000000',
					type: 'rounded'
				},
				backgroundOptions: {
					color: '#ffffff'
				},
				imageOptions: {
					hideBackgroundDots: true,
					size: imageSize,
					margin: imageMargin
				},
				qrOptions: {
					typeNumber: '0',
					mode: 'Byte',
					errorCorrectionLevel: 'Q'
				}
			});

			const element = document.getElementById(id);
			if (element) {
				qrCode.append(element);
			}
		};
	});
</script>

<div {id}></div>

<style>
	div {
		display: flex;
	}
</style>
