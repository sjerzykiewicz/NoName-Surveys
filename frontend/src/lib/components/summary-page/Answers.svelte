<script lang="ts">
	import QuestionTitle from './QuestionTitle.svelte';
	import Single from '$lib/components/summary-page/Single.svelte';
	import Text from '$lib/components/summary-page/Text.svelte';
	import List from '$lib/components/summary-page/List.svelte';
	import Scale from '$lib/components/summary-page/Scale.svelte';
	import Multi from '$lib/components/summary-page/Multi.svelte';
	import Slider from '$lib/components/summary-page/Slider.svelte';
	import Binary from '$lib/components/summary-page/Binary.svelte';
	import Rank from '$lib/components/summary-page/Rank.svelte';
	import type { ComponentType } from 'svelte';

	export let answer;
	export let id: string;

	const componentTypeMap: { [id: string]: ComponentType } = {
		text: Text,
		single: Single,
		multi: Multi,
		scale: Scale,
		binary: Binary,
		slider: Slider,
		rank: Rank,
		list: List
	};
</script>

<div class="title">{parseFloat(id) + 1}. Answer</div>
{#each answer.questions as question, questionIndex}
	<div class="question">
		<QuestionTitle question={question.question} {questionIndex} required={question.required} />
		<svelte:component this={componentTypeMap[question.question_type]} data={question} />
	</div>
{/each}

<style>
	.title {
		font-size: 2em;
		margin-bottom: 1em;
	}
</style>
