<script lang="ts">
	import { page } from '$app/stores';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let id: string;
	export let icon: string;
	export let q: string;
	export let a: string;

	let isAnswerVisible: boolean = $page.url.href.includes(id);

	function toggleAnswer() {
		isAnswerVisible = !isAnswerVisible;
	}
</script>

<div class="faq-item" {id} title={$t(q)}>
	<button class="faq-question" class:clicked={isAnswerVisible} on:click={toggleAnswer}>
		<i class="symbol">{icon}</i>
		<Tx text={q} />
		<i class="symbol arrow">arrow_drop_down</i>
	</button>
	{#if isAnswerVisible}
		<div class="faq-answer" transition:slide={{ duration: 200, easing: cubicInOut }}>
			<Tx html={a} />
		</div>
	{/if}
</div>

<style>
	.faq-item {
		display: flex;
		flex-direction: column;
		text-align: justify;
		padding: 0.75em 0em;
	}

	.faq-item:first-of-type {
		padding-top: 0em;
	}

	.faq-item:not(:last-of-type) {
		border-bottom: 1px solid var(--border-color-1);
	}

	.faq-question {
		display: flex;
		align-items: flex-start;
		justify-content: flex-start;
		gap: 0.5em;
		padding: 0.5em 0em;
		border: none;
		border-radius: 0px;
		box-shadow: none;
		font-weight: 700;
		font-size: 1.1em;
		text-align: left;
		text-shadow: 0px 4px 4px var(--shadow-color-1);
		background-color: var(--secondary-color-1);
		color: var(--accent-color-1);
		cursor: pointer;
	}

	.faq-question:hover {
		background-color: var(--primary-color-2);
		color: var(--accent-color-2);
	}

	.faq-question:active {
		background-color: var(--primary-color-1);
		color: var(--text-color-1);
	}

	.faq-question .arrow {
		transform: rotate(0deg);
		transition: transform 0.2s;
	}

	.faq-question.clicked .arrow {
		transform: rotate(180deg);
	}

	.faq-answer {
		display: flex;
		align-items: center;
		justify-content: flex-start;
		text-shadow: 0px 4px 4px var(--shadow-color-1);
		color: var(--text-color-1);
		padding: 0.5em 0em;
	}
</style>
