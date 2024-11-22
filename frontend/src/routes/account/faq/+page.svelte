<script lang="ts">
	import Header from '$lib/components/global/Header.svelte';
	import Content from '$lib/components/global/Content.svelte';
	import Footer from '$lib/components/global/Footer.svelte';
	import OpenSourceInfo from '$lib/components/global/OpenSourceInfo.svelte';
	import Back from '$lib/components/global/Back.svelte';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);
</script>

<Header>
	<div title={$t('faq_title')} class="title static">
		<Tx text="faq_title" />
	</div>
</Header>

<Content></Content>

<Footer>
	<div class="footer-box">
		<OpenSourceInfo />
		<Back />
	</div>
</Footer>

<style>
	.footer-box {
		display: flex;
		align-items: center;
		width: 100%;
		gap: 0.5em;
	}
</style>
