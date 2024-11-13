<script lang="ts">
	import { Hamburger } from 'svelte-hamburgers';
	import { slide, scale } from 'svelte/transition';
	import { page } from '$app/stores';
	import { cubicInOut } from 'svelte/easing';
	import { onMount } from 'svelte';
	import noname_dark from '$lib/assets/noname_dark.png';
	import noname_light from '$lib/assets/noname_light.png';
	import { M } from '$lib/stores/global';
	import NavLinks from './NavLinks.svelte';

	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	let { options } = getContext<SvelteTranslate>(CONTEXT_KEY);

	let open: boolean;
	let innerWidth: number;

	const navLinks = {
		Fill: {
			name: 'nav_fill',
			href: '/',
			page: '',
			disabled: false
		},
		Create: {
			name: 'nav_create',
			href: '/create',
			page: '',
			disabled: !$page.data.session
		},
		Drafts: {
			name: 'nav_drafts',
			href: '/drafts',
			page: '/0',
			disabled: !$page.data.session
		},
		Surveys: {
			name: 'nav_surveys',
			href: '/surveys',
			page: '/0',
			disabled: !$page.data.session
		},
		Groups: {
			name: 'nav_groups',
			href: '/groups',
			page: '/0',
			disabled: !$page.data.session
		},
		Account: {
			name: 'nav_account',
			href: '/account',
			page: '',
			disabled: false
		}
	};

	function hideNav() {
		open = false;
	}

	let bulb = 'lightbulb';
	let logo = noname_dark;

	onMount(() => {
		const colorScheme = localStorage.getItem('colorScheme') || 'dark';

		if (colorScheme === 'dark') {
			document.documentElement.dataset.colorScheme = 'dark';
			logo = noname_light;
		} else {
			document.documentElement.dataset.colorScheme = 'light';
			logo = noname_dark;
			bulb = 'light_off';
		}

		$options.currentLang = localStorage.getItem('langPref') || 'en';
	});

	function toggleThemeMode() {
		const currentColorScheme = document.documentElement.dataset.colorScheme;

		if (currentColorScheme === 'dark') {
			document.documentElement.dataset.colorScheme = 'light';
			bulb = 'light_off';
			logo = noname_dark;
			localStorage.setItem('colorScheme', 'light');
		} else {
			document.documentElement.dataset.colorScheme = 'dark';
			bulb = 'lightbulb';
			logo = noname_light;
			localStorage.setItem('colorScheme', 'dark');
		}
	}

	function changeLang(lang: string) {
		$options.currentLang = lang;
		localStorage.setItem('langPref', lang);
	}

	let scrollHeight: number;
	$: showToggleButtons = scrollHeight == 0;
</script>

<svelte:window bind:innerWidth bind:scrollY={scrollHeight} />

{#if innerWidth <= $M}
	<div class="nav-burger">
		<a href="/" title="NoName" class="nav-burger-logo"
			><img src={logo} alt="NoName logo" width="48" height="48" /></a
		>
		<div title={open ? 'Close menu' : 'Open menu'}>
			<Hamburger bind:open --color="var(--text-color-1)" />
		</div>
	</div>
	{#if open}
		<div class="bar">
			<nav transition:slide={{ duration: 200, easing: cubicInOut }}>
				<NavLinks {navLinks} {hideNav} />
			</nav>
		</div>
	{/if}
{:else}
	<div class="bar">
		<a href="/" title="NoName" class="nav-logo"
			><img src={logo} alt="NoName logo" width="48" height="48" /></a
		>
		<nav>
			<NavLinks {navLinks} {hideNav} />
		</nav>
	</div>
{/if}

{#if showToggleButtons}
	<button
		transition:scale={{ duration: 200, easing: cubicInOut }}
		on:click={toggleThemeMode}
		class="toggle-mode theme-btn tooltip"
	>
		<i class="symbol">{bulb}</i>
		<span class="tooltip-text left"><Tx text="nav_toggle_theme"></Tx></span>
	</button>
{/if}
{#if showToggleButtons && $options.currentLang === 'en'}
	<button
		transition:scale={{ duration: 200, easing: cubicInOut }}
		on:click={() => changeLang('pl')}
		class="toggle-mode lang-btn tooltip"
	>
		PL
		<span class="tooltip-text left"><Tx text="nav_toggle_lang"></Tx></span>
	</button>
{:else if showToggleButtons && $options.currentLang === 'pl'}
	<button
		transition:scale={{ duration: 200, easing: cubicInOut }}
		on:click={() => changeLang('en')}
		class="toggle-mode lang-btn tooltip"
	>
		EN
		<span class="tooltip-text left"><Tx text="nav_toggle_lang"></Tx></span>
	</button>
{/if}

<style>
	.bar .tooltip .tooltip-text {
		font-size: 0.8em;
		font-weight: normal;
		background-color: var(--primary-dark-color);
	}

	.toggle-mode.tooltip {
		--tooltip-width: 7em;
	}

	.toggle-mode.tooltip .tooltip-text {
		font-size: 0.8em;
		background-color: var(--primary-color-2);
	}

	.toggle-mode.tooltip .tooltip-text.left::after {
		border-color: transparent transparent transparent var(--primary-color-2);
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

	.toggle-mode {
		position: fixed;
		justify-content: center;
		top: 0.25em;
		right: 0.25em;
		background-color: var(--primary-color-2);
		border: none;
		font-size: 1.5em;
		z-index: 1;
		cursor: pointer;
		transition:
			0.2s,
			outline 0s;
	}

	.theme-btn {
		top: 0.25em;
		right: 0.25em;
	}

	.lang-btn {
		top: 0.25em;
		right: 2.25em;
	}

	.toggle-mode:hover {
		transform: scale(110%);
	}

	.toggle-mode:active {
		background-color: var(--border-color-1);
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

	@media screen and (max-width: 980px) {
		.toggle-mode {
			top: 2.5em;
		}

		.nav-logo {
			visibility: hidden;
			opacity: 0 !important;
		}
	}

	@media screen and (max-width: 768px) {
		.tooltip .tooltip-text {
			font-size: 0.6em;
		}

		nav {
			flex-flow: column;
			border-left: none;
			width: 100%;
			min-width: 0px;
		}

		.bar {
			border-bottom: none;
		}

		.toggle-mode {
			top: 0.6em;
			right: 3em;
			font-size: 1.75em;
		}

		.lang-btn {
			right: 5em;
		}

		.toggle-mode.tooltip .tooltip-text {
			font-size: 0.5em;
		}
	}
</style>
