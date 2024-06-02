<script lang="ts">
	import QuestionTitle from '$lib/components/create-page/QuestionTitle.svelte';
	import QuestionTitlePreview from '$lib/components/create-page/preview/QuestionTitlePreview.svelte';
	import QuestionError from './QuestionError.svelte';
	import ChoiceError from './ChoiceError.svelte';
	import AddQuestionButtons from '$lib/components/create-page/AddQuestionButtons.svelte';
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { scrollToElement } from '$lib/utils/scrollToElement';
	import { MultiSelect } from 'svelte-multiselect';
	import { ringMembers } from '$lib/stores/create-page';

	export let user_list: string[];
	export let isPreview: boolean;
	let isLimited = false;
</script>

{#each $questions as question, questionIndex (question)}
	<div
		class="question"
		in:slide={{ duration: 200, easing: cubicInOut }}
		on:introend={() => scrollToElement('.add-question')}
	>
		{#if isPreview}
			<QuestionTitlePreview {questionIndex} />
			<svelte:component this={question.preview} {questionIndex} />
		{:else}
			<QuestionTitle {questionIndex} questionType={question.component} />
			<QuestionError {questionIndex} />
			<svelte:component this={question.component} {questionIndex} />
			<ChoiceError {questionIndex} />
		{/if}
	</div>
{/each}
{#if !isPreview}
	<AddQuestionButtons />
	<input type="checkbox" title="Define respondent group" bind:checked={isLimited} />Limit access
	{#if isLimited}
		<div class="user-list" title="Select users">
			<MultiSelect bind:selected={$ringMembers} options={user_list} />
		</div>
	{/if}
{/if}
