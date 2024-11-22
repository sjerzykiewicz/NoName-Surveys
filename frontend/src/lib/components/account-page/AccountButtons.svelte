<script lang="ts">
	import { toggleTheme } from '$lib/utils/toggleTheme';
	import { colorScheme } from '$lib/stores/global';
	import { goto } from '$app/navigation';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext, onMount } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);
	let { options } = getContext<SvelteTranslate>(CONTEXT_KEY);

	$: otherLang = $options.currentLang === 'en' ? 'pl' : 'en';
	$: bulb = $colorScheme === 'dark' ? 'lightbulb' : 'light_off';

	function changeLang(lang: string) {
		$options.currentLang = lang;
		localStorage.setItem('langPref', lang);
	}

	onMount(() => {
		$options.currentLang = localStorage.getItem('langPref') || 'en';
	});
</script>

<div class="account-buttons">
	<button title={$t('toggle_theme')} on:click={() => ($colorScheme = toggleTheme($colorScheme))}>
		<i class="symbol">{bulb}</i>
		{#key $t}
			{#if $colorScheme === 'dark'}
				<Tx text="light_theme" />
			{:else}
				<Tx text="dark_theme" />
			{/if}
		{/key}
	</button>
	<button title={$t('toggle_lang')} on:click={() => changeLang(otherLang)}
		><i class="symbol">language</i><Tx text="other_lang" />
	</button>
	<button title={$t('faq_title')} on:click={() => goto('/account/faq')}
		><i class="symbol">question_mark</i>FAQ
	</button>
</div>

<style>
	.account-buttons {
		display: flex;
		flex-direction: column;
		align-items: flex-start;
		gap: 0.5em;
		font-size: 1.5em;
		padding-top: 0.5em;
		padding-bottom: 0.5em;
		border-bottom: 1px solid var(--border-color-1);
	}

	i {
		margin-right: 0.15em;
	}

	@media screen and (max-width: 768px) {
		.account-buttons {
			font-size: 1.25em;
		}
	}
</style>
