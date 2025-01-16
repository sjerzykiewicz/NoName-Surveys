<script lang="ts">
	import '../app.css';
	import NavBar from '$lib/components/global/NavBar.svelte';
	import ScrollToTop from '$lib/components/global/ScrollToTop.svelte';
	import ErrorModal from '$lib/components/global/ErrorModal.svelte';
	import Translate from 'sveltekit-translate/translate/Translate.svelte';
	import type { TranslateOptions } from 'sveltekit-translate/translate/translateStore';
	import { onMount } from 'svelte';
	import { data } from '$lib/translations';
	import { colorContrast, colorScheme, shadows } from '$lib/stores/global';
	import { setScheme } from '$lib/utils/setScheme';
	import { setContrast } from '$lib/utils/setContrast';
	import { setShadows } from '$lib/utils/setShadows';

	let opts: TranslateOptions = {
		defaultLang: 'en',
		currentLang: 'en'
	};

	onMount(() => {
		$colorScheme = setScheme();
		$colorContrast = setContrast();
		$shadows = setShadows();
	});
</script>

<Translate {opts} {data}>
	<ErrorModal />

	<NavBar />
	<div class="box">
		<slot />
	</div>
	<ScrollToTop />
</Translate>

<style>
	.box {
		display: flex;
		flex-flow: column;
		min-height: calc(100vh - 4.875em);
		width: 50%;
		min-width: 768px;
		margin: 1.5em auto auto;
		border: 1px solid var(--border-color-1);
		border-bottom: none;
		box-shadow: var(--shadow);
		background-color: var(--secondary-color-1);
		transition: background-color 0.2s;
	}

	@media screen and (max-width: 768px) {
		.box {
			width: 100%;
			min-width: 0px;
			min-height: calc(100vh - 4.5625em);
			margin-top: 0em;
			border-left: none;
			border-right: none;
		}
	}
</style>
