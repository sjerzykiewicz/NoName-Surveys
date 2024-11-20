<script lang="ts">
	import noname_dark from '$lib/assets/noname_dark.png';
	import noname_light from '$lib/assets/noname_light.png';
	// import Tx from 'sveltekit-translate/translate/tx.svelte';

	export let logo: string;
	export let bulb: string;

	let theme: string = 'Light Theme';

	function toggleThemeMode() {
		const currentColorScheme = document.documentElement.dataset.colorScheme;

		if (currentColorScheme === 'dark') {
			document.documentElement.dataset.colorScheme = 'light';
			bulb = 'light_off';
			logo = noname_dark;
			theme = 'Dark Theme';
			localStorage.setItem('colorScheme', 'light');
		} else {
			document.documentElement.dataset.colorScheme = 'dark';
			bulb = 'lightbulb';
			logo = noname_light;
			theme = 'Light Theme';
			localStorage.setItem('colorScheme', 'dark');
		}
	}

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

<button class="nav-button tooltip" on:click={toggleThemeMode}>
	<i class="symbol">{bulb}</i>{theme}
	<!-- {#if innerWidth > $M}<span class="tooltip-text left"><Tx text="toggle_theme" /></span>{/if} -->
</button>

<style>
	/* .toggle-mode.tooltip .tooltip-text {
		font-size: 0.8em;
		background-color: var(--primary-color-2);
	}

	.toggle-mode.tooltip .tooltip-text.left::after {
		border-color: transparent transparent transparent var(--primary-color-2);
	}

	.toggle-mode {
		position: fixed;
		justify-content: center;
		top: 0.25em;
		right: 0.25em;
		background-color: var(--primary-color-1);
		border: none;
		box-shadow: none;
		width: 1.667em;
		height: 1.667em;
		font-size: 1.5em;
		z-index: 1;
		cursor: pointer;
		transition:
			0.2s,
			outline 0s;
	}

	.toggle-mode:hover {
		transform: scale(110%);
	}

	.toggle-mode:active {
		background-color: var(--border-color-1);
	}

	.theme-btn {
		--tooltip-width: 7em;
		top: 0.25em;
		right: 0.25em;
		z-index: 2;
	}

	@media screen and (max-width: 980px) {
		.toggle-mode {
			top: 2.5em;
		}
	}

	@media screen and (max-width: 768px) {
		.tooltip .tooltip-text {
			font-size: 0.6em;
		}

		.toggle-mode {
			top: 0.6em;
			right: 3em;
			width: 1.75em;
			height: 1.75em;
			font-size: 1.75em;
		}
	} */
</style>
