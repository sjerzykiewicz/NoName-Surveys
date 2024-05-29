<script lang="ts">
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import SurveyTitle from '$lib/components/create-page/SurveyTitle.svelte';
	import SurveyTitlePreview from '$lib/components/create-page/preview/SurveyTitlePreview.svelte';
	import TitleError from '$lib/components/create-page/TitleError.svelte';
	import QuestionTitle from '$lib/components/create-page/QuestionTitle.svelte';
	import QuestionTitlePreview from '$lib/components/create-page/preview/QuestionTitlePreview.svelte';
	import QuestionError from './QuestionError.svelte';
	import ChoiceError from './ChoiceError.svelte';
	import AddQuestionButtons from '$lib/components/create-page/AddQuestionButtons.svelte';
	import FooterButtons from '$lib/components/create-page/FooterButtons.svelte';
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { scrollToElement } from '$lib/utils/scrollToElement';

	let isPreview: boolean;
	let titleError: boolean;
</script>

<Header>
	{#if isPreview}
		<SurveyTitlePreview />
	{:else}
		<SurveyTitle />
		<TitleError {titleError} />
	{/if}
</Header>

<Content>
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
	{/if}
</Content>

<Footer>
	<FooterButtons bind:titleError bind:isPreview />
</Footer>
