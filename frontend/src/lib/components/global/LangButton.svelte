<script lang="ts">
	import { getContext, onMount } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	let { options } = getContext<SvelteTranslate>(CONTEXT_KEY);

	function changeLang(lang: string) {
		$options.currentLang = lang;
		localStorage.setItem('langPref', lang);
	}

	onMount(() => {
		$options.currentLang = localStorage.getItem('langPref') || 'en';
	});

	$: otherLang = $options.currentLang === 'en' ? 'pl' : 'en';

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

<button class="nav-button tooltip" on:click={() => changeLang(otherLang)}
	><i class="symbol">language</i>
	{otherLang === 'en' ? 'Angielski' : 'Polish'}
	<!-- {#if innerWidth > $M}<span class="tooltip-text left"><Tx text="toggle_lang" /></span>{/if} -->
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

	.lang-btn {
		--tooltip-width: 8em;
		top: 0.25em;
		right: 2.25em;
		font-weight: 700 !important;
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

		.lang-btn {
			right: 5em;
		}
	} */
</style>
