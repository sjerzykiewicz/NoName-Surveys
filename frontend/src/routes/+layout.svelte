<script lang="ts">
	import '../app.css';
	import NavBar from '$lib/components/global/NavBar.svelte';
	import ScrollToTop from '$lib/components/global/ScrollToTop.svelte';
	import ErrorModal from '$lib/components/global/ErrorModal.svelte';
	import Translate from 'sveltekit-translate/translate/Translate.svelte';
	import type { TranslateOptions } from 'sveltekit-translate/translate/translateStore';

	import { data } from '$lib/translations';

	let opts: TranslateOptions = {
		defaultLang: 'en',
		currentLang: 'en'
	};
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
		box-shadow: 0px 4px 4px var(--shadow-color-1);
		background-color: var(--secondary-color-1);
		transition: 0.2s;
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
