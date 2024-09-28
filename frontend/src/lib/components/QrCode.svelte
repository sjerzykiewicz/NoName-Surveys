<script lang="ts">
	import { page } from '$app/stores';
	import { onMount } from 'svelte';

	export let code: string;
	export let codeSize: number;
	export let codeMargin: number = 0;
	export let image: string = '';
	export let imageSize: number = 1;
	export let imageMargin: number = 0;

	let data: string = $page.url.origin + '/fill?code=' + code;

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
				data: data,
				image: image,
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

			const element = document.getElementById(code);
			if (element) {
				qrCode.append(element);
			}
		};
	});
</script>

<div id={code}></div>

<style>
	div {
		display: flex;
	}
</style>
