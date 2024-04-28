<script lang="ts">
	import type { ComponentType } from 'svelte';
	import Single from './Single.svelte';
	import Text from './Text.svelte';
	import List from './List.svelte';
	import Scale from './Scale.svelte';
	import QuestionTitle from './QuestionTitle.svelte';
	import Multi from './Multi.svelte';
	import Slider from './Slider.svelte';
	import YesNo from '../fill-page/YesNo.svelte';
	import { questions } from './stores';

	const componentTypeMap: { [id: string]: ComponentType } = {
		text: Text,
		single: Single,
		multi: Multi,
		scale: Scale,
		yesno: YesNo,
		slider: Slider,
		list: List
	};
</script>

<form method="POST">
	{#each $questions as question, questionIndex}
		<div class="question">
			<QuestionTitle {questionIndex} />
			<svelte:component this={componentTypeMap[question.type]} {questionIndex} />
		</div>
	{/each}
</form>

<style>
	.question {
		margin-bottom: 1.875em;
	}
</style>
