<script lang="ts">
	import Header from '$lib/components/Header.svelte';
	import Content from '../Content.svelte';
	import SurveyTitle from '$lib/components/fill-page/SurveyTitle.svelte';
	import type { ComponentType } from 'svelte';
	import Single from './Single.svelte';
	import Text from './Text.svelte';
	import List from './List.svelte';
	import Scale from './Scale.svelte';
	import QuestionTitle from './QuestionTitle.svelte';
	import Multi from './Multi.svelte';
	import Slider from './Slider.svelte';

	// TODO this is for demonstration purposes only, survey will be constructed from JSON
	const title: string = 'Test survey';
	const questions: Array<{
		component: ComponentType;
		required: boolean;
		question: string;
		choices: Array<string>;
	}> = [
		{
			component: Single,
			required: false,
			question: 'Single question',
			choices: ['Choice 1', 'Choice 2', 'Choice 3']
		},
		{
			component: Text,
			required: true,
			question: 'Text question',
			choices: ['Question details']
		},
		{
			component: List,
			required: true,
			question: 'List question',
			choices: ['Choice 1', 'Choice 2', 'Choice 3', 'Choice 4']
		},
		{
			component: Scale,
			required: false,
			question: 'Scale question',
			choices: ['1', '2', '3', '4', '5']
		},
		{
			component: Multi,
			required: false,
			question: 'Multi question',
			choices: ['Choice 1', 'Choice 2', 'Choice 3', 'Choice 4']
		},
		{
			component: Slider,
			required: false,
			question: 'Slider Question',
			choices: ['1', '10']
		}
	];
</script>

<Header>
	<SurveyTitle {title} />
</Header>

<Content>
	<form method="POST">
		{#each questions as question, questionNumber}
			<div class="question">
				<QuestionTitle question={question.question} questionNumber={questionNumber + 1} />
				<svelte:component
					this={question.component}
					question={question.question}
					required={question.required}
					choices={question.choices}
				/>
			</div>
		{/each}
	</form>
</Content>

<style>
	.question {
		margin-bottom: 1.875em;
	}
</style>
