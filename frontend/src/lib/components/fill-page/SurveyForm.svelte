<script lang="ts">
	import { answers, questions } from '$lib/stores/fill-page';
	import type { ComponentType } from 'svelte';
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';
	import SurveyTitle from '$lib/components/fill-page/SurveyTitle.svelte';
	import Single from '$lib/components/fill-page/Single.svelte';
	import Text from '$lib/components/fill-page/Text.svelte';
	import List from '$lib/components/fill-page/List.svelte';
	import Scale from '$lib/components/fill-page/Scale.svelte';
	import QuestionTitle from '$lib/components/fill-page/QuestionTitle.svelte';
	import Multi from '$lib/components/fill-page/Multi.svelte';
	import Slider from '$lib/components/fill-page/Slider.svelte';
	import YesNo from '$lib/components/fill-page/YesNo.svelte';
	import Rank from '$lib/components/fill-page/Rank.svelte';
	import Footer from '$lib/components/Footer.svelte';

	const componentTypeMap: { [id: string]: ComponentType } = {
		text: Text,
		single: Single,
		multi: Multi,
		scale: Scale,
		yesno: YesNo,
		slider: Slider,
		rank: Rank,
		list: List
	};

	const numQuestions = $questions.length;
	for (let i = 0; i < numQuestions; i++) {
		$answers = [...$answers, { choices: [] }];
	}

	let unansweredRequired: Array<number> = [];

	function processForm() {
		unansweredRequired = [];
		for (let i = 0; i < numQuestions; i++) {
			// TODO - remove console log
			console.log($answers[i].choices);
			if ($questions[i].required) {
				if ($answers[i].choices.length === 0) {
					unansweredRequired[i] = i;
				} else {
					for (let j in $answers[i].choices) {
						let choice = $answers[i].choices[j];
						if (choice === null || choice === undefined || choice.length === 0) {
							unansweredRequired[i] = i;
						}
					}
				}
			}
		}
		if (unansweredRequired.length > 0) {
			return;
		}
		// TODO - further processing
	}
</script>

<Header>
	<SurveyTitle />
</Header>
<Content>
	{#each $questions as question, questionIndex}
		<div class="question">
			<QuestionTitle {questionIndex} />
			<svelte:component this={componentTypeMap[question.type]} {questionIndex} />
		</div>
		{#if unansweredRequired.includes(questionIndex)}
			<p class="error">*An answer to question {questionIndex + 1} is required!</p>
		{/if}
	{/each}
</Content>
<Footer>
	<button title="Submit survey" class="footer-button submit" on:click={processForm}>
		<i class="material-symbols-rounded">done</i>Submit
	</button>
</Footer>

<style>
	.question {
		margin-bottom: 1.875em;
	}

	i {
		font-size: 1.15em;
		margin-right: 0.15em;
	}

	.error {
		padding-left: 5%;
	}

	@media screen and (max-width: 767px) {
		.footer-button {
			font-size: 1em;
		}
	}
</style>
