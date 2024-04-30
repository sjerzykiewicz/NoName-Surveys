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

	function processForm() {
		for (let i = 0; i < numQuestions; i++) {
			// TODO - implement actual processing
			console.log($answers[i].choices);
		}
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
	.footer-button {
		display: flex;
		text-decoration: none;
		background-color: #4a4a4a;
		padding: 0.25em;
		border: 1px solid #999999;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		font-size: 1.25em;
		font-family: 'Jura';
		color: #eaeaea;
		cursor: pointer;
		transition: background-color 0.2s;
		margin-left: 0.5em;
	}

	.footer-button:hover {
		background-color: #1a1a1a;
	}

	.submit {
		background-color: #0075ff;
	}

	.submit:hover {
		background-color: #001c53;
	}

	.footer-button:active,
	.submit:active {
		background-color: #999999;
	}

	i {
		font-size: 1.15em;
		margin-right: 0.15em;
	}

	@media screen and (max-width: 767px) {
		.footer-button {
			font-size: 1em;
		}
	}
</style>
