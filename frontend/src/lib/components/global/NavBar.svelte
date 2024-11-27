<script lang="ts">
	import { Hamburger } from 'svelte-hamburgers';
	import { slide } from 'svelte/transition';
	import { cubicInOut } from 'svelte/easing';
	import { colorScheme, colorContrast, M } from '$lib/stores/global';
	import NavLinks from './NavLinks.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';
	import NavButtons from './NavButtons.svelte';
	import noname_dark from '$lib/assets/noname_dark.png';
	import noname_black from '$lib/assets/noname_black.png';
	import noname_light from '$lib/assets/noname_light.png';
	import noname_white from '$lib/assets/noname_white.png';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	let open: boolean = false;

	$: logo =
		$colorScheme === 'dark'
			? $colorContrast === 'high'
				? noname_white
				: noname_light
			: $colorContrast === 'high'
				? noname_black
				: noname_dark;

	function handleClick(event: MouseEvent) {
		if (open && !(event.target as HTMLElement).closest('.hamburger')) {
			open = false;
		}
	}

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />
<svelte:body on:click={handleClick} />

{#if innerWidth <= $M}
	<div class="nav-burger">
		<a href="/" title="NoName" class="nav-burger-logo"
			><img src={logo} alt="NoName" width="48" height="48" /></a
		>
		<NavButtons />
		<div title={open ? $t('close_menu') : $t('open_menu')} class="hamburger">
			<Hamburger bind:open --color="var(--text-color-1)" --padding="10px" />
		</div>
	</div>
	{#if open}
		<div class="bar">
			<nav transition:slide={{ duration: 200, easing: cubicInOut }}>
				<NavLinks />
			</nav>
		</div>
	{/if}
{:else}
	<div class="bar">
		<a href="/" title="NoName" class="nav-logo"
			><img src={logo} alt="NoName" width="48" height="48" /></a
		>
		<nav>
			<NavLinks />
		</nav>
	</div>
	<NavButtons />
{/if}

<style>
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
		opacity: 0.75;
	}

	@media screen and (max-width: 900px) {
		nav {
			min-width: 638px;
		}
	}

	@media screen and (max-width: 768px) {
		nav {
			flex-flow: column;
			border-left: none;
			width: 100%;
			min-width: 0px;
			position: absolute;
			border-bottom: 1px solid var(--border-color-1);
			box-shadow: 0px 4px 4px var(--shadow-color-1);
			z-index: 8;
		}

		.bar {
			border-bottom: none;
		}
	}
</style>
