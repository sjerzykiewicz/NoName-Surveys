<script lang="ts">
	import { Hamburger } from 'svelte-hamburgers';
	import { slide } from 'svelte/transition';
	import { cubicInOut } from 'svelte/easing';
	import { M } from '$lib/stores/global';
	import NavLinks from './NavLinks.svelte';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext, onMount } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';
	import LangButton from './LangButton.svelte';
	import ThemeButton from './ThemeButton.svelte';
	import { page } from '$app/stores';
	import { signOut } from '$lib/utils/signOut';
	import { startOAuth } from '$lib/utils/startOAuth';
	import noname_dark from '$lib/assets/noname_dark.png';
	import noname_light from '$lib/assets/noname_light.png';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let logo: string;
	export let bulb: string;

	let open: boolean = false;
	let isPanelVisible: boolean = false;

	function hideNav() {
		open = false;
	}

	function togglePanel() {
		isPanelVisible = !isPanelVisible;
	}

	onMount(() => {
		const colorScheme = localStorage.getItem('colorScheme') || 'dark';

		if (colorScheme === 'dark') {
			document.documentElement.dataset.colorScheme = 'dark';
			logo = noname_light;
			bulb = 'lightbulb';
		} else {
			document.documentElement.dataset.colorScheme = 'light';
			logo = noname_dark;
			bulb = 'light_off';
		}
	});

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

{#if innerWidth <= $M}
	<div class="nav-burger">
		<a href="/" title="NoName" class="nav-burger-logo"
			><img src={logo} alt="NoName logo" width="48" height="48" /></a
		>
		<div title={open ? $t('close_menu') : $t('open_menu')}>
			<Hamburger bind:open --color="var(--text-color-1)" />
		</div>
	</div>
	{#if open}
		<div class="bar">
			<nav transition:slide={{ duration: 200, easing: cubicInOut }}>
				<NavLinks {hideNav} />
			</nav>
		</div>
	{/if}
{:else}
	<div class="bar">
		<a href="/" title="NoName" class="nav-logo"
			><img src={logo} alt="NoName logo" width="48" height="48" /></a
		>
		<nav>
			<NavLinks {hideNav} />
		</nav>
	</div>
{/if}

<div class="button-group">
	<button title="" class="account-button" class:clicked={isPanelVisible} on:click={togglePanel}>
		<i class="symbol">{$page.data.session ? 'account_circle' : 'account_circle_off'}</i>
		<i class="symbol arrow">arrow_drop_down</i>
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
			<LangButton />
			<ThemeButton bind:logo {bulb} />
		</div>
	{/if}
</div>

<style>
	.button-group {
		display: flex;
		position: absolute;
		top: 0.45em;
		right: 0.45em;
		font-size: 1.25em;
	}

	.account-button {
		display: flex;
		justify-content: center;
		width: fit-content;
		height: 1.75em;
		box-shadow: none;
		border: none;
		transition:
			0.2s,
			outline 0s;
	}

	.account-button.clicked {
		background-color: var(--primary-color-2);
	}

	.account-button.clicked:hover {
		background-color: var(--secondary-color-1);
	}

	.account-button.clicked:active {
		background-color: var(--border-color-1);
	}

	.nav-button-panel {
		display: flex;
		flex-flow: column;
		position: absolute;
		top: 1.75em;
		right: 0;
		border-radius: 0px 0px 5px 5px;
		box-shadow: 0px 4px 4px var(--shadow-color-1);
		height: auto;
		position: absolute;
		z-index: 1;
	}

	:global(.nav-button-panel button:first-child) {
		border-top-left-radius: 5px;
		border-top-right-radius: 5px;
	}

	:global(.nav-button-panel button:last-child) {
		border-bottom-left-radius: 5px;
		border-bottom-right-radius: 5px;
	}

	.account-button.clicked .arrow {
		transform: rotate(180deg);
	}

	.account-button i {
		transform: rotate(0deg);
		transition: transform 0.2s;
	}

	nav {
		display: flex;
		flex-flow: row;
		margin: auto;
		min-width: 768px;
		width: 50%;
		justify-content: space-around;
		background-color: var(--secondary-color-2);
		border-left: 1px solid var(--border-color-1);
		transition:
			0.2s,
			outline 0s;
	}

	.bar {
		background-color: var(--secondary-color-2);
		border-bottom: 1px solid var(--border-color-1);
		box-shadow: 0px 4px 4px var(--shadow-color-1);
		transition:
			0.2s,
			outline 0s;
	}

	.nav-burger {
		display: flex;
		flex-flow: row;
		justify-content: space-between;
		align-items: center;
		padding: 0.75em;
		color: var(--text-color-1);
		background-color: var(--secondary-color-2);
		transition:
			0.2s,
			outline 0s;
	}

	.nav-burger-logo {
		display: flex;
		text-decoration: none;
		opacity: 1;
		transition:
			0.2s,
			outline 0s;
		cursor: pointer;
	}

	.nav-logo {
		position: absolute;
		top: 0.25em;
		left: 0.25em;
		text-decoration: none;
		opacity: 1;
		transition:
			0.2s,
			outline 0s;
		cursor: pointer;
	}

	.nav-burger-logo:hover,
	.nav-burger-logo:active,
	.nav-logo:hover,
	.nav-logo:active {
		opacity: 0.7;
	}

	@media screen and (max-width: 900px) {
		.nav-logo {
			visibility: hidden;
			opacity: 0 !important;
		}
	}

	@media screen and (max-width: 768px) {
		nav {
			flex-flow: column;
			border-left: none;
			width: 100%;
			min-width: 0px;
		}

		.bar {
			border-bottom: none;
		}
	}
</style>
