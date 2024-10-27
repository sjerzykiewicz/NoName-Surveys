<script lang="ts">
	import { Hamburger } from 'svelte-hamburgers';
	import { slide, scale } from 'svelte/transition';
	import { page } from '$app/stores';
	import { cubicInOut } from 'svelte/easing';
	import { onMount } from 'svelte';
	import noname_dark from '$lib/assets/noname_dark.png';
	import noname_light from '$lib/assets/noname_light.png';
	import { M } from '$lib/stores/global';

	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	let { options } = getContext<SvelteTranslate>(CONTEXT_KEY);

	let open: boolean;
	let innerWidth: number;

	const navLinks = {
		Fill: {
			name: 'nav_fill',
			href: '/',
			disabled: false
		},
		Create: {
			name: 'nav_create',
			href: '/create',
			disabled: !$page.data.session
		},
		Drafts: {
			name: 'nav_drafts',
			href: '/drafts',
			disabled: !$page.data.session
		},
		Surveys: {
			name: 'nav_surveys',
			href: '/surveys',
			disabled: !$page.data.session
		},
		Groups: {
			name: 'nav_groups',
			href: '/groups',
			disabled: !$page.data.session
		},
		Account: {
			name: 'nav_account',
			href: '/account',
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
		<a href="/" title="Fill Out" class="nav-burger-logo"
			><img src={logo} alt="NoName logo" width="48" height="48" /></a
		>
		<div title={open ? 'Close menu' : 'Open menu'}>
			<Hamburger bind:open --color="var(--text-color)" />
		</div>
	</div>
{/if}

{#if open || innerWidth > $M}
	<div class="bar">
		<nav transition:slide={{ duration: 200, easing: cubicInOut }}>
			{#each Object.entries(navLinks) as [id, data]}
				<div
					title={data.disabled ? $t('nav_sign_in_info') + $t(data.name) : $t(data.name)}
					{id}
					class="nav-link"
					class:tooltip={innerWidth > $M && data.disabled}
					class:active={$page.url.pathname === data.href}
					class:disabled={data.disabled}
				>
					<a href={data.disabled ? '' : data.href} on:click={hideNav}>{$t(data.name)}</a>
					{#if innerWidth > $M && data.disabled}
						<span class="tooltip-text bottom">
							<Tx text="nav_sign_in_info"></Tx>
							<Tx text={data.name}></Tx>
						</span>
					{/if}
				</div>
			{/each}
		</nav>
	</div>
{/if}

{#if showToggleButtons}
	<button
		transition:scale={{ duration: 200, easing: cubicInOut }}
		on:click={toggleThemeMode}
		class="toggle-mode theme-btn tooltip"
	>
		<i class="material-symbols-rounded">{bulb}</i>
		<span class="tooltip-text left"><Tx text="nav_toggle_theme"></Tx></span>
	</button>
{/if}
{#if showToggleButtons && $options.currentLang === 'en'}
	<button
		transition:scale={{ duration: 200, easing: cubicInOut }}
		on:click={() => changeLang('pl')}
		class="toggle-mode lang-btn zindex-0"
	>
		Polski
	</button>
{:else if showToggleButtons && $options.currentLang === 'pl'}
	<button
		transition:scale={{ duration: 200, easing: cubicInOut }}
		on:click={() => changeLang('en')}
		class="toggle-mode lang-btn zindex-0"
	>
		English
	</button>
{/if}

<style>
	.zindex-0 {
		z-index: 0;
	}

	.bar .tooltip {
		--tooltip-width: 12.5em;
	}

	.bar .tooltip .tooltip-text {
		font-size: 0.8em;
		font-weight: normal;
		background-color: var(--primary-dark-color);
	}

	.bar .tooltip .tooltip-text.bottom::after {
		border-color: transparent transparent var(--primary-dark-color) transparent;
	}

	.toggle-mode.tooltip {
		--tooltip-width: 7em;
		z-index: 1;
	}

	.toggle-mode.tooltip .tooltip-text {
		font-size: 0.8em;
		background-color: var(--primary-dark-color);
		z-index: 2;
	}

	.toggle-mode.tooltip .tooltip-text.left::after {
		border-color: transparent transparent transparent var(--primary-dark-color);
	}

	nav {
		display: flex;
		flex-flow: row;
		margin: auto;
		min-width: 768px;
		width: 50%;
		justify-content: space-around;
		background-color: var(--secondary-dark-color);
		border-left: 1px solid var(--border-color);
	}

	.bar {
		background-color: var(--secondary-dark-color);
		border-bottom: 1px solid var(--border-color);
		box-shadow: 0px 4px 4px var(--shadow-color);
	}

	.nav-burger {
		display: flex;
		flex-flow: row;
		justify-content: space-between;
		align-items: center;
		padding: 0.75em;
		color: var(--text-color);
		background-color: var(--secondary-dark-color);
	}

	.toggle-mode {
		position: fixed;
		justify-content: center;
		background-color: var(--primary-dark-color);
		border: none;
		font-size: 1.5em;
		z-index: 1;
		transition: 0.2s;
		cursor: pointer;
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
		background-color: var(--border-color);
	}

	.nav-burger-logo {
		display: flex;
		color: var(--text-color);
		text-decoration: none;
		transition: 0.2s;
		cursor: pointer;
	}

	.nav-burger-logo:hover,
	.nav-burger-logo:active {
		background-color: transparent;
		opacity: 0.7;
	}

	.nav-link {
		display: flex;
		justify-content: center;
		align-items: center;
		text-align: center;
		color: var(--text-color);
		font-weight: bold;
		font-size: 1.5em;
		border-right: 1px solid var(--border-color);
		width: 100%;
		cursor: pointer;
	}

	.nav-link a {
		padding: 0.5em 0em;
		width: 100%;
		color: inherit;
		text-decoration: none;
		cursor: inherit;
	}

	.nav-link:hover {
		background-color: var(--primary-dark-color);
	}

	.nav-link:active {
		background-color: var(--border-color);
	}

	.nav-link.active,
	.nav-link.active:hover {
		background-color: var(--accent-color);
		color: var(--text-color-2);
	}

	.nav-link.disabled,
	.nav-link.disabled:hover,
	.nav-link.disabled:active {
		cursor: not-allowed;
		color: var(--text-dark-color);
		background-color: var(--secondary-color);
	}

	@media screen and (max-width: 1078px) {
		.theme-btn,
		.lang-btn {
			top: 2.5em;
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

		.nav-link {
			border-top: 1px solid var(--border-color);
			border-right: none;
			border-bottom: none;
		}

		.theme-btn {
			top: 0.6em;
			right: 3em;
			font-size: 1.75em;
		}

		.lang-btn {
			top: 0.6em;
			right: 5em;
			font-size: 1.75em;
		}
	}
</style>
