<script lang="ts">
	import { Hamburger } from 'svelte-hamburgers';
	import { slide } from 'svelte/transition';
	import { page } from '$app/stores';

	let open: boolean;
	let innerWidth: number;
	let innerHeight: number;

	// TODO: move welcome page to root path
	const navLinks = {
		Home: '/welcome',
		Create: '/create',
		Pending: '/pending',
		Summary: '/summary',
		Account: '/account'
	};

	function hideNav() {
		open = false;
	}
</script>

<svelte:window bind:innerWidth bind:innerHeight />

{#if innerWidth < 767}
	<div class="nav-burger">
		<i class="material-symbols-rounded">shield_person</i>
		<Hamburger bind:open --color="white" />
	</div>
{/if}

{#if open || innerWidth >= 767}
	<nav transition:slide>
		{#each Object.entries(navLinks) as [title, href]}
			<a
				{href}
				{title}
				class:active={$page.url.pathname === href}
				class:last={title === 'Account'}
				on:click={hideNav}>{title}</a
			>
		{/each}
	</nav>
{/if}

<style>
	nav {
		display: flex;
		flex-flow: row;
		width: 100%;
		justify-content: space-around;
		background-color: #1a1a1a;
	}

	.nav-burger {
		display: flex;
		flex-flow: row;
		justify-content: space-between;
		align-items: center;
		padding: 1em;
		color: white;
	}

	.nav-burger i {
		font-size: 3em;
	}

	a {
		padding: 0.5em 0 0.5em 0;
		text-align: center;
		color: #eaeaea;
		font-family: 'Jura';
		font-weight: bold;
		font-size: 1.5em;
		border: 1px solid #999999;
		border-left: none;
		width: 100%;
		text-decoration: none;
		transition: background-color 0.2s;
	}

	a:hover {
		background-color: #4a4a4a;
		transition: background-color 0.2s;
	}

	.active {
		background-color: #0075ff;
	}

	.active:hover {
		background-color: #0075ff;
	}

	.last {
		border-right: none;
	}

	@media screen and (max-width: 767px) {
		nav {
			flex-flow: column;
		}

		a {
			border-top: none;
			border-right: none;
		}
	}
</style>
