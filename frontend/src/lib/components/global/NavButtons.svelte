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
	import { goto } from '$app/navigation';
	import { toggleTheme } from '$lib/utils/toggleTheme';
	import { colorScheme } from '$lib/stores/global';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);
	let { options } = getContext<SvelteTranslate>(CONTEXT_KEY);

	let isPanelVisible: boolean = false;

	const ACCOUNT_BUTTON_BREAKPOINT = 1155;

	$: otherLang = $options.currentLang === 'en' ? 'pl' : 'en';
	$: bulb = $colorScheme === 'dark' ? 'lightbulb' : 'light_off';

	function togglePanel() {
		isPanelVisible = !isPanelVisible;
	}

	function changeLang(lang: string) {
		$options.currentLang = lang;
		localStorage.setItem('langPref', lang);
	}

	function handleEscape(event: KeyboardEvent) {
		if (isPanelVisible && event.key === 'Escape') {
			isPanelVisible = false;
		}
	}

	function handleClick(event: MouseEvent) {
		if (isPanelVisible && !(event.target as HTMLElement).closest('.button-group')) {
			isPanelVisible = false;
		}
	}

	onMount(() => {
		$options.currentLang = localStorage.getItem('langPref') || 'en';
	});

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />
<svelte:body on:keydown={handleEscape} on:click={handleClick} />

<div class="button-group">
	<button
		title={isPanelVisible ? $t('hide_account_options') : $t('show_account_options')}
		class="account-button tooltip"
		class:clicked={isPanelVisible}
		on:click={togglePanel}
	>
		<div class="button-text">
			<i class="symbol" class:signed-in={$page.data.session}
				>{$page.data.session ? 'account_circle' : 'account_circle_off'}</i
			>
			{#if innerWidth > ACCOUNT_BUTTON_BREAKPOINT || innerWidth <= $M}
				{$page.data.session ? $page.data.session.user?.email.split('@')[0] : $t('sign_in')}
			{/if}
		</div>
		<i class="symbol arrow">arrow_drop_down</i>
		{#if innerWidth > $M}
			<span class="tooltip-text left"
				>{$page.data.session ? $page.data.session.user?.email : $t('signed_out_info')}</span
			>
		{/if}
	</button>
	{#if isPanelVisible}
		<div class="nav-button-panel" transition:slide={{ duration: 200, easing: cubicInOut }}>
			<button
				title={$t('toggle_theme')}
				class="nav-button"
				on:click={() => ($colorScheme = toggleTheme($colorScheme))}
			>
				<i class="symbol">{bulb}</i>
				{#key $t}
					{#if $colorScheme === 'dark'}
						<Tx text="light_theme" />
					{:else}
						<Tx text="dark_theme" />
					{/if}
				{/key}
			</button>
			<button title={$t('toggle_lang')} class="nav-button" on:click={() => changeLang(otherLang)}
				><i class="symbol">language</i><Tx text="other_lang" />
			</button>
			<button title={$t('faq_title')} class="nav-button" on:click={() => goto('/account/faq')}
				><i class="symbol">question_mark</i>FAQ
			</button>
			{#if $page.data.session}
				<button title={$t('sign_out')} class="nav-button" on:click={signOut}
					><i class="symbol">logout</i><Tx text="sign_out" />
				</button>
			{:else}
				<button
					title={$t('sign_in')}
					class="nav-button"
					on:click={() => startOAuth($page.url.pathname === '/fill' ? '/' : $page.url.pathname)}
					><i class="symbol">login</i><Tx text="sign_in" /></button
				>
			{/if}
		</div>
	{/if}
</div>

<style>
	.tooltip {
		--tooltip-width: max-content;
	}

	.tooltip .tooltip-text {
		background-color: var(--primary-color-2);
		font-size: 0.8em;
	}

	.tooltip .tooltip-text.left::after {
		border-color: transparent transparent transparent var(--primary-color-2);
	}

	.signed-in {
		color: var(--accent-color-1);
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
		max-width: 9.2em;
		width: fit-content;
		height: 100%;
		background-color: var(--secondary-color-2);
		box-shadow: none;
		border: none;
		border-radius: 0px;
		opacity: 1;
	}

	.account-button:hover .button-text,
	.account-button:hover .arrow {
		opacity: 0.75;
	}

	.account-button .arrow {
		transform: rotate(0deg);
		transition:
			transform 0.2s,
			opacity 0.2s;
	}

	.account-button.clicked .arrow {
		transform: rotate(180deg);
	}

	.account-button .button-text {
		display: flex;
		align-items: center;
		transition: opacity 0.2s;
	}

	.nav-button-panel {
		display: flex;
		flex-flow: column;
		position: absolute;
		top: 2.65em;
		right: 0;
		border-bottom-left-radius: 5px;
		border-left: 1px solid var(--border-color-1);
		border-bottom: 1px solid var(--border-color-1);
		box-shadow: 0px 4px 4px var(--shadow-color-1);
		z-index: 2;
	}

	.nav-button-panel button:last-child {
		border-bottom-left-radius: 5px;
	}

	.nav-button-panel button:not(:last-child) {
		border-bottom: 1px solid var(--text-color-3);
	}

	.nav-button {
		width: 9em;
		border-radius: 0px;
		box-shadow: none;
		border: none;
		font-size: 1.1em;
	}

	.nav-button i,
	.button-text i {
		margin-right: 0.15em;
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
			flex-flow: row;
			top: 4.55em;
			width: 100%;
			border-radius: 0px;
			border: none;
			border-bottom: 1px solid var(--border-color-1);
		}

		.nav-button-panel button:last-child {
			border-bottom-left-radius: 0px;
		}

		.nav-button-panel button:not(:last-child) {
			border-bottom: none;
			border-right: 1px solid var(--text-color-3);
		}

		.nav-button {
			height: 3em;
			width: 100%;
			justify-content: center;
		}
	}

	@media screen and (max-width: 375px) {
		.nav-button-panel {
			flex-flow: column;
		}

		.nav-button-panel button:not(:last-child) {
			border-bottom: 1px solid var(--text-color-3);
			border-right: none;
		}

		.nav-button {
			height: 2em;
		}
	}
</style>
