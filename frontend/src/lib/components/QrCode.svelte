<script lang="ts">
	import { onMount } from 'svelte';

	export let data: string;
	export let size: number;

	onMount(() => {
		let script = document.createElement('script');
		script.src = 'https://unpkg.com/qr-code-styling@1.5.0/lib/qr-code-styling.js';
		document.head.appendChild(script);

		script.onload = () => {
			// @ts-expect-error QRCodeStyling is defined in the script above
			// eslint-disable-next-line no-undef
			let qrCode = new QRCodeStyling({
				width: size,
				height: size,
				data: data,
				image: '',
				dotsOptions: {
					color: '#000000',
					type: 'rounded'
				},
				backgroundOptions: {
					color: '#ffffff'
				},
				imageOptions: {
					crossOrigin: 'anonymous',
					margin: 20
				}
			});

			const element = document.getElementById('qr-code');
			if (element) {
				qrCode.append(element);
			}
		};
	});
</script>

<div id="qr-code"></div>
