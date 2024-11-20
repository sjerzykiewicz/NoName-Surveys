<script lang="ts">
	import { slide } from 'svelte/transition';
	import { cubicInOut } from 'svelte/easing';
	import { M } from '$lib/stores/global';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext, onMount } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';
	import { page } from '$app/stores';
	import { signOut } from '$lib/utils/signOut';
	import { startOAuth } from '$lib/utils/startOAuth';
	import noname_dark from '$lib/assets/noname_dark.png';
	import noname_light from '$lib/assets/noname_light.png';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);
	let { options } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let logo: string;

	let bulb: string;
	let theme: string;
	let isPanelVisible: boolean = false;

	const ACCOUNT_BUTTON_BREAKPOINT = 1155;

	function togglePanel() {
		isPanelVisible = !isPanelVisible;
	}

	function changeLang(lang: string) {
		$options.currentLang = lang;
		localStorage.setItem('langPref', lang);
	}

	function toggleThemeMode() {
		const currentColorScheme = document.documentElement.dataset.colorScheme;

		if (currentColorScheme === 'dark') {
			document.documentElement.dataset.colorScheme = 'light';
			logo = noname_dark;
			bulb = 'light_off';
			theme = $t('dark_theme');
			localStorage.setItem('colorScheme', 'light');
		} else {
			document.documentElement.dataset.colorScheme = 'dark';
			logo = noname_light;
			bulb = 'lightbulb';
			theme = $t('light_theme');
			localStorage.setItem('colorScheme', 'dark');
		}
	}

	$: otherLang = $options.currentLang === 'en' ? 'pl' : 'en';

	onMount(() => {
		const colorScheme = localStorage.getItem('colorScheme') || 'dark';

		if (colorScheme === 'dark') {
			document.documentElement.dataset.colorScheme = 'dark';
			logo = noname_light;
			bulb = 'lightbulb';
			theme = $t('light_theme');
		} else {
			document.documentElement.dataset.colorScheme = 'light';
			logo = noname_dark;
			bulb = 'light_off';
			theme = $t('dark_theme');
		}

		$options.currentLang = localStorage.getItem('langPref') || 'en';
	});

	function handleClick(event: MouseEvent) {
		if (isPanelVisible && !(event.target as HTMLElement).closest('.button-group')) {
			isPanelVisible = false;
		}
	}

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />
<svelte:body on:click={handleClick} />

<div class="button-group">
	<button
		title={isPanelVisible ? $t('hide_account_options') : $t('show_account_options')}
		class="account-button tooltip"
		class:clicked={isPanelVisible}
		on:click={togglePanel}
	>
		<div class="button-text">
			<i class="symbol">{$page.data.session ? 'account_circle' : 'account_circle_off'}</i>
			{#if innerWidth > ACCOUNT_BUTTON_BREAKPOINT || innerWidth <= $M}
				{$page.data.session ? $page.data.session.user?.email.split('@')[0] : $t('signed_out')}
			{/if}
		</div>
		<i class="symbol arrow">arrow_drop_down</i>
		{#if $page.data.session && innerWidth > $M}
			<span class="tooltip-text left">{$page.data.session.user?.email}</span>
		{/if}
	</button>
	{#if isPanelVisible}
		<div class="nav-button-panel" transition:slide={{ duration: 200, easing: cubicInOut }}>
			{#if $page.data.session}
				<button title={$t('sign_out')} class="nav-button" on:click={signOut}
					><i class="symbol">logout</i><Tx text="sign_out" />
				</button>
			{:else}
				<button title={$t('sign_in')} class="nav-button" on:click={startOAuth}
					><i class="symbol">login</i><Tx text="sign_in" /></button
				>
			{/if}
			<button title={$t('toggle_lang')} class="nav-button" on:click={() => changeLang(otherLang)}
				><i class="symbol">language</i><Tx text="other_lang" />
			</button>
			<button title={$t('toggle_theme')} class="nav-button" on:click={toggleThemeMode}>
				<i class="symbol">{bulb}</i>{#key $t}{theme}{/key}
			</button>
		</div>
	{/if}
</div>

<style>
	.tooltip {
		--tooltip-width: fit-content;
	}

	.tooltip .tooltip-text {
		font-size: 0.8em;
	}

	.button-group {
		display: flex;
		justify-content: flex-end;
		align-items: center;
		position: absolute;
		top: 0;
		right: 0;
		width: fit-content;
		height: 2.6em;
		font-size: 1.25em;
	}

	.account-button {
		display: flex;
		justify-content: space-between;
		width: 9.2em;
		height: 100%;
		background-color: var(--secondary-color-2);
		box-shadow: none;
		border: none;
		border-radius: 0px;
		opacity: 1;
		transition:
			0.2s,
			outline 0s;
	}

	.account-button:hover .button-text,
	.account-button:hover .arrow {
		opacity: 0.7;
	}

	.account-button.clicked .arrow {
		transform: rotate(180deg);
	}

	.account-button i {
		transform: rotate(0deg);
		transition: transform 0.2s;
	}

	.button-text {
		display: flex;
		align-items: center;
	}

	.nav-button-panel {
		display: flex;
		flex-flow: column;
		position: absolute;
		top: 2.65em;
		right: 0;
		width: 9.2em;
		border-bottom-left-radius: 5px;
		border-left: 1px solid var(--border-color-1);
		border-bottom: 1px solid var(--border-color-1);
		box-shadow: 0px 4px 4px var(--shadow-color-1);
		z-index: 1;
	}

	.nav-button-panel button:last-child {
		border-bottom-left-radius: 5px;
	}

	.nav-button {
		width: 9.2em;
		border-radius: 0px;
		box-shadow: none;
		border: none;
	}

	.nav-button i,
	.button-text i {
		margin-right: 0.15em;
	}

	@media screen and (max-width: 1155px) {
		.account-button {
			width: 3em;
		}
	}

	@media screen and (max-width: 768px) {
		.button-group {
			position: static;
			height: 3em;
			font-size: 1em;
		}

		.account-button {
			width: fit-content;
		}

		.nav-button-panel {
			top: 4.55em;
			width: 100%;
			border-radius: 0px;
			border: none;
			border-bottom: 1px solid var(--border-color-1);
		}

		.nav-button-panel button:last-child {
			border-bottom-left-radius: 0px;
		}

		.nav-button {
			width: 100%;
			justify-content: center;
		}
	}
</style>
