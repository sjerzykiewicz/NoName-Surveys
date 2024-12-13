<script lang="ts">
	import { toggleScheme } from '$lib/utils/toggleScheme';
	import { toggleContrast } from '$lib/utils/toggleContrast';
	import { colorScheme, colorContrast } from '$lib/stores/global';
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
	<div class="button-sub-row">
		<button title={$t('toggle_theme')} on:click={() => ($colorScheme = toggleScheme($colorScheme))}>
			<i class="symbol">{bulb}</i>
			{#key $t}
				{#if $colorScheme === 'dark'}
					<Tx text="light_theme" />
				{:else}
					<Tx text="dark_theme" />
				{/if}
			{/key}
		</button>
		<button
			title={$t('toggle_contrast')}
			on:click={() => ($colorContrast = toggleContrast($colorContrast))}
		>
			<i class="symbol">contrast</i>
			{#key $t}
				{#if $colorContrast === 'medium'}
					<Tx text="high_contrast" />
				{:else}
					<Tx text="medium_contrast" />
				{/if}
			{/key}
		</button>
	</div>
	<div class="button-sub-row">
		<button title={$t('toggle_lang')} on:click={() => changeLang(otherLang)}
			><i class="symbol">language</i><Tx text="other_lang" />
		</button>
		<button title={$t('faq_title')} on:click={() => goto('/account/faq')}
			><i class="symbol">question_mark</i>FAQ
		</button>
	</div>
</div>

<style>
	.account-buttons {
		display: flex;
		flex-flow: row wrap;
		align-items: center;
		justify-content: flex-start;
		gap: 0.5em;
		font-size: 1.5em;
		padding-top: 1em;
		padding-bottom: 1em;
	}

	.button-sub-row {
		flex-wrap: wrap;
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
