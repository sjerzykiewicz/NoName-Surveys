<script lang="ts">
	import { Hamburger } from 'svelte-hamburgers';
	import { slide } from 'svelte/transition';
	import { page } from '$app/stores';
	import { cubicInOut } from 'svelte/easing';

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
</script>

<svelte:window bind:innerWidth bind:innerHeight />

{#if innerWidth <= 767}
	<div class="nav-burger">
		<i class="material-symbols-rounded">shield_person</i>
		<Hamburger bind:open --color="#eaeaea" />
	</div>
{/if}

{#if open || innerWidth > 767}
	<div class="bar">
		<nav transition:slide={{ duration: 200, easing: cubicInOut }}>
			{#each Object.entries(navLinks) as [title, href]}
				<a {href} {title} class:active={$page.url.pathname === href} on:click={hideNav}>{title}</a>
			{/each}
		</nav>
	</div>
{/if}

<style>
	nav {
		display: flex;
		flex-flow: row;
		margin: auto;
		min-width: 767px;
		width: 50%;
		justify-content: space-around;
		background-color: var(--secondary-color);
		border-left: 1px solid var(--border-color);
	}

	.bar {
		background-color: var(--secondary-color);
		border-bottom: 1px solid var(--border-color);
	}

	.nav-burger {
		display: flex;
		flex-flow: row;
		justify-content: space-between;
		align-items: center;
		padding: 0.75em;
		color: var(--text-color);
		background-color: var(--secondary-color);
	}

	.nav-burger i {
		font-size: 3em;
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
		background-color: var(--primary-color);
		transition: background-color 0.2s;
	}

	a:active {
		background-color: var(--border-color);
	}

	.active,
	.active:hover {
		background-color: var(--accent-color);
	}

	i {
		cursor: default;
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
		}
	}
</style>
