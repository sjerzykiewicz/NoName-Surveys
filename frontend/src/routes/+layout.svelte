<script lang="ts">
	import { Hamburger } from 'svelte-hamburgers';
	import { slide } from 'svelte/transition';

	import NavLink from '$lib/components/NavLink.svelte';

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
</script>

<svelte:window bind:innerWidth bind:innerHeight />

{#if innerWidth < 767}
	<Hamburger bind:open --color="white" />
{/if}

{#if open || innerWidth >= 767}
	<nav transition:slide>
		{#each Object.entries(navLinks) as [title, href]}
			<NavLink {href} {title} />
		{/each}
	</nav>
{/if}
<div class="box">
	<slot />
</div>

<style>
	.box {
		display: flex;
		flex-flow: column;
		height: auto;
		min-height: calc(100% - 5em);
		width: 50%;
		min-width: 767px;
		margin: auto;
		margin-top: 1.5em;
		border: 1px solid #999999;
		box-shadow: 0px 4px 4px #1a1a1a;
		background-color: #2a2a2a;
	}

	nav {
		display: flex;
		flex-flow: row;
		width: 100%;
		justify-content: space-around;
		background-color: #1a1a1a;
	}

	@media screen and (max-width: 767px) {
		.box {
			width: 100%;
			min-width: 0px;
			margin-top: 0px;
			border: none;
		}

		nav {
			flex-flow: column;
		}
	}
</style>
