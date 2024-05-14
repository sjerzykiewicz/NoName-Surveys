<script lang="ts">
	import QuestionTitle from './QuestionTitle.svelte';
	import Single from './Single.svelte';
	import Text from './Text.svelte';
	import List from './List.svelte';
	import Scale from './Scale.svelte';
	import Multi from './Multi.svelte';
	import Slider from './Slider.svelte';
	import Binary from './Binary.svelte';
	import Rank from './Rank.svelte';
	import type { ComponentType } from 'svelte';

	export let answer;
	export let id: string;

	export const componentTypeMap: { [id: string]: ComponentType } = {
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
