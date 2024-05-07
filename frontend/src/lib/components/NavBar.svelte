<script lang="ts">
	import { Hamburger } from 'svelte-hamburgers';
	import { slide, scale } from 'svelte/transition';
	import { page } from '$app/stores';
	import { cubicInOut } from 'svelte/easing';
	import { onMount } from 'svelte';

	let open: boolean;
	let innerWidth: number;
	let innerHeight: number;

	const navLinks = {
		Home: {
			href: '/',
			disabled: false
		},
		Create: {
			href: '/create',
			disabled: false
		},
		Summary: {
			href: '/summary',
			disabled: true
		},
		Account: {
			href: '/account',
			disabled: true
		}
	};

	function hideNav() {
		open = false;
	}

	let bulb = 'lightbulb';

	onMount(() => {
		const colorScheme = localStorage.getItem('colorScheme') || 'dark';

		if (colorScheme === 'dark') {
			document.documentElement.dataset.colorScheme = 'dark';
		} else {
			document.documentElement.dataset.colorScheme = 'light';
			bulb = 'light_off';
		}
	});

	function toggleThemeMode() {
		const currentColorScheme = document.documentElement.dataset.colorScheme;

		if (currentColorScheme === 'dark') {
			document.documentElement.dataset.colorScheme = 'light';
			bulb = 'light_off';
			localStorage.setItem('colorScheme', 'light');
		} else {
			document.documentElement.dataset.colorScheme = 'dark';
			bulb = 'lightbulb';
			localStorage.setItem('colorScheme', 'dark');
		}
	}

	let scrollHeight: number;
	$: showToggleThemeMode = scrollHeight == 0;
</script>

<svelte:window bind:innerWidth bind:innerHeight bind:scrollY={scrollHeight} />

{#if innerWidth <= 767}
	<div class="nav-burger">
		<i class="material-symbols-rounded">shield_person</i>
		<Hamburger bind:open --color="var(--text-color)" --box-shadow="none" />
	</div>
{/if}

{#if open || innerWidth > 767}
	<div class="bar">
		<nav transition:slide={{ duration: 200, easing: cubicInOut }}>
			{#each Object.entries(navLinks) as [title, data]}
				<a
					href={data.href}
					{title}
					class:active={$page.url.pathname === data.href}
					on:click={hideNav}
					class:disabled-link={data.disabled == true}>{title}</a
				>
			{/each}
		</nav>
	</div>
{/if}

{#if showToggleThemeMode}
	<button
		transition:scale={{ duration: 200, easing: cubicInOut }}
		on:click={toggleThemeMode}
		class="toggle-mode"
	>
		<i class="material-symbols-rounded">{bulb}</i>
	</button>
{/if}

<style>
	nav {
		display: flex;
		flex-flow: row;
		margin: auto;
		min-width: 767px;
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

	.nav-burger i {
		font-size: 3em;
		cursor: default;
	}

	.toggle-mode {
		position: fixed;
		justify-content: center;
		top: 0.25em;
		right: 0.5em;
		background-color: var(--primary-dark-color);
		border: none;
		font-size: 1.5em;
		z-index: 5;
		transition: 0.2s;
	}

	.toggle-mode:hover {
		transform: scale(110%);
	}

	.toggle-mode:active {
		background-color: var(--border-color);
	}

	a {
		padding: 0.5em 0 0.5em 0;
		text-align: center;
		color: var(--text-color);
		font-weight: bold;
		font-size: 1.5em;
		border-right: 1px solid var(--border-color);
		width: 100%;
		text-decoration: none;
	}

	a:hover {
		background-color: var(--primary-dark-color);
	}

	a:active {
		background-color: var(--border-color);
	}

	.active,
	.active:hover {
		background-color: var(--accent-color);
		color: var(--text-color-2);
	}

	.disabled-link {
		pointer-events: none;
		color: var(--text-dark-color);
		background-color: var(--secondary-color);
	}

	@media screen and (max-width: 892px) {
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
			right: 3em;
			font-size: 1.75em;
		}
	}
</style>
