<script lang="ts">
	import { type ComponentType } from 'svelte';
	import { createEventDispatcher } from 'svelte';
	import { slide } from 'svelte/transition';
	import { cubicInOut } from 'svelte/easing';

	export let questionType: ComponentType;
	export let questionTypeData: { title: string; icon: string; text: string };
	export let questionTypeIndex: number;

	const dispatch = createEventDispatcher();

	function handleClick() {
		dispatch('addQuestionType', { component: questionType });
	}
</script>

<button
	title={questionTypeData.title}
	class:previous={questionTypeIndex === -1}
	class:last={questionTypeIndex === 8}
	in:slide={{ axis: 'x', duration: 200, easing: cubicInOut }}
	on:click={handleClick}
	><i class="symbol">{questionTypeData.icon}</i>{questionTypeData.text}</button
>

<style>
	button {
		flex: 1;
		width: 6.25em;
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
		width: auto;
	}

	i {
		font-size: 1em;
		margin-right: 0.25em;
		margin-left: 0.1em;
	}
</style>
