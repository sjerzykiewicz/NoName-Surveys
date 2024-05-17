<script lang="ts">
	import { beforeUpdate, type ComponentType } from 'svelte';
	import { createEventDispatcher } from 'svelte';
	import { slide } from 'svelte/transition';
	import { cubicInOut } from 'svelte/easing';
	import { getQuestionTypeData } from '$lib/utils/getQuestionTypeData';

	export let questionType: ComponentType;
	export let questionTypeIndex: number;

	let questionTypeData: { title: string; icon: string; text: string };

	const dispatch = createEventDispatcher();

	function handleClick() {
		dispatch('addQuestionType', { component: questionType });
	}

	beforeUpdate(() => {
		questionTypeData = getQuestionTypeData(questionType);
	});
</script>

<button
	title={questionTypeData.title}
	class:previous={questionTypeIndex === -1}
	class:last={questionTypeIndex === 7}
	in:slide={{ axis: 'x', duration: 200, easing: cubicInOut }}
	on:click={handleClick}
	><i class="material-symbols-rounded">{questionTypeData.icon}</i>{questionTypeData.text}</button
>

<style>
	button {
		flex: 1;
		width: 6.25em;
		border: 0px;
		border-radius: 0px;
		border-left: 1px solid var(--border-color);
		border-right: 1px solid var(--border-color);
		box-shadow: none;
	}

	.last {
		border-radius: 0px 0px 5px 5px;
		border-bottom: 1px solid var(--border-color);
	}

	.previous {
		border-radius: 0px 5px 5px 0px;
		border-left: 0px;
		border-top: 1px solid var(--border-color);
		border-bottom: 1px solid var(--border-color);
		width: auto;
	}

	i {
		font-size: 1em;
		margin-right: 0.25em;
		margin-left: 0.1em;
	}

	@media screen and (max-width: 767px) {
		button {
			font-size: 1em;
		}
	}
</style>
