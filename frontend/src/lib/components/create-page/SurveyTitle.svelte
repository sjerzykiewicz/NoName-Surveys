<script lang="ts">
	import { title } from '$lib/stores/create-page';
	import { M } from '$lib/stores/global';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { onMount } from 'svelte';
	import Input from '$lib/components/global/Input.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	let titleInput: HTMLDivElement;
	let innerWidth: number;

	onMount(() => {
		if (innerWidth > $M && $title.title.length === 0) titleInput.focus();
	});
</script>

<svelte:window bind:innerWidth />

<div class="title-container" transition:slide={{ duration: 200, easing: cubicInOut }}>
	<Input
		bind:text={$title.title}
		label={$t('survey_title')}
		title={$t('survey_title_title')}
		id="title"
		bind:element={titleInput}
		--margin-right="0em"
		--char-count-left="7em"
	/>
</div>

<style>
	.title-container {
		font-size: 1.25em;
		padding: 0.8em 0.2em;
		margin: -0.8em -0.2em;
	}

	@media screen and (max-width: 768px) {
		.title-container {
			font-size: 1em;
		}
	}
</style>
