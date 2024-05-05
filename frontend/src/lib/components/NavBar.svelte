<script lang="ts">
	import { Hamburger } from 'svelte-hamburgers';
	import { slide, fade } from 'svelte/transition';
	import { page } from '$app/stores';
	import { cubicInOut } from 'svelte/easing';
	import { onMount } from 'svelte';

	let open: boolean;
	let innerWidth: number;
	let innerHeight: number;

	// TODO: move welcome page to root path
	const navLinks = {
		Home: '/welcome',
		Create: '/create',
		Summary: '/summary',
		Account: '/account'
	};

	function hideNav() {
		open = false;
	}

	let hamburgerColor = '#dadada';
	let mode = 'dark_mode';

	onMount(() => {
		const colorScheme = localStorage.getItem('colorScheme') || 'dark';

		if (colorScheme === 'dark') {
			document.documentElement.dataset.colorScheme = 'dark';
		} else {
			document.documentElement.dataset.colorScheme = 'light';
			hamburgerColor = '#4a4a4a';
			mode = 'light_mode';
		}
	});

	function toggleDarkMode() {
		const currentColorScheme = document.documentElement.dataset.colorScheme;
		if (currentColorScheme === 'dark') {
			document.documentElement.dataset.colorScheme = 'light';
			hamburgerColor = '#4a4a4a';
			mode = 'light_mode';
			localStorage.setItem('colorScheme', 'light');
		} else {
			document.documentElement.dataset.colorScheme = 'dark';
			hamburgerColor = '#dadada';
			mode = 'dark_mode';
			localStorage.setItem('colorScheme', 'dark');
		}
	}
</script>

<svelte:window bind:innerWidth bind:innerHeight />

{#if innerWidth <= 767}
	<div class="nav-burger">
		<i class="material-symbols-rounded">shield_person</i>
		<Hamburger bind:open --color={hamburgerColor} />
	</div>
{/if}

{#if open || innerWidth > 767}
	<div class="bar">
		<nav transition:slide={{ duration: 200, easing: cubicInOut }}>
			{#each Object.entries(navLinks) as [title, href]}
				<a {href} {title} class:active={$page.url.pathname === href} on:click={hideNav}>{title}</a>
			{/each}
			<!-- {#key mode}
				<button in:fade on:click={toggleDarkMode} class="toggle-mode">
					<i class="material-symbols-rounded" class:active-mode={mode === 'light_mode'}
						>light_mode</i
					>
					<i class="material-symbols-rounded">horizontal_rule</i>
					<i class="material-symbols-rounded" class:active-mode={mode === 'dark_mode'}>dark_mode</i>
				</button>
			{/key} -->
		</nav>
	</div>
{/if}

<button in:fade on:click={toggleDarkMode} class="toggle-mode">
	<i class="material-symbols-rounded" class:active-mode={mode === 'light_mode'}>light_mode</i>
	<i class="material-symbols-rounded">horizontal_rule</i>
	<i class="material-symbols-rounded" class:active-mode={mode === 'dark_mode'}>dark_mode</i>
</button>

<style>
	nav {
		display: flex;
		flex-flow: row;
		margin: auto;
		min-width: 767px;
		width: 50%;
		justify-content: space-around;
		background-color: var(--shadow-color);
		border-left: 1px solid var(--border-color);
	}

	.bar {
		background-color: var(--shadow-color);
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
		background-color: var(--shadow-color);
	}

	.nav-burger i {
		font-size: 3em;
	}

	.toggle-mode {
		position: fixed;
		justify-content: center;
		top: 0.2em;
		right: 0.5em;
		background-color: var(--primary-dark-color);
		color: var(--text-color);
		border: none;
		border-radius: 5px;
		font-size: 1.5em;
		box-shadow: 0px 4px 4px var(--shadow-color);
		cursor: pointer;
		z-index: 5;
		transition: 0.2s;
	}

	.toggle-mode i {
		font-size: 0.8em;
		cursor: pointer;
	}
	a {
		padding: 0.5em 0 0.5em 0;
		text-align: center;
		color: var(--text-color);
		font-family: 'Jura';
		font-weight: bold;
		font-size: 1.5em;
		border-right: 1px solid var(--border-color);
		width: 100%;
		text-decoration: none;
		transition: background-color 0.2s;
	}
	a:hover {
		background-color: var(--primary-dark-color);
		transition: background-color 0.2s;
	}

	a:active {
		background-color: var(--border-color);
	}

	.active,
	.active:hover {
		background-color: var(--accent-color);
		color: var(--text-color-2);
	}

	i {
		cursor: default;
	}

	.active-mode {
		color: var(--theme-accent-color);
		font-size: 1.2em !important;
	}

	@media screen and (max-width: 978px) {
		.toggle-mode {
			top: 2.5em;
		}
	}

	@media screen and (max-width: 767px) {
		nav {
			flex-flow: column;
			border-left: none;
			width: 100%;
			min-width: 0px;
		}

		.bar {
			border-bottom: none;
		}
		a {
			border-top: 1px solid var(--border-color);
			border-right: none;
			border-bottom: none;
			padding: 0.5em 0 0.5em 0;
		}

		.toggle-mode {
			top: 0.6em;
			right: 2.5em;
			font-size: 1.75em;
		}
	}
</style>
