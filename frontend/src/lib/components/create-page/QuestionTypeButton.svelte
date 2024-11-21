<script lang="ts">
	import { type ComponentType } from 'svelte';
	import { createEventDispatcher } from 'svelte';
	import { slide } from 'svelte/transition';
	import { cubicInOut } from 'svelte/easing';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let questionType: ComponentType;
	export let questionTypeData: { title: string; icon: string; text: string };
	export let questionTypeIndex: number;

	const dispatch = createEventDispatcher();

	function handleClick() {
		dispatch('addQuestionType', { component: questionType });
	}
</script>

<button
	title={$t(questionTypeData.title)}
	class:previous={questionTypeIndex === -1}
	class:last={questionTypeIndex === 8}
	in:slide={{ axis: 'x', duration: 200, easing: cubicInOut }}
	on:click={handleClick}
	><i class="symbol">{questionTypeData.icon}</i>
	{#key questionTypeData.text}
		<Tx text={questionTypeData.text} />
	{/key}
</button>

<style>
	button {
		flex: 1;
		width: var(--width, 7.5em);
		border: 0px;
		border-radius: 0px;
		border-left: 1px solid var(--border-color-1);
		border-right: 1px solid var(--border-color-1);
		box-shadow: none;
	}

	.last {
		border-radius: 0px 0px 5px 5px;
		border-bottom: 1px solid var(--border-color-1);
	}

	.previous {
		border-radius: 0px 5px 5px 0px;
		border-left: 0px;
		border-top: 1px solid var(--border-color-1);
		border-bottom: 1px solid var(--border-color-1);
		width: fit-content;
	}

	i {
		margin-right: 0.15em;
	}
</style>
