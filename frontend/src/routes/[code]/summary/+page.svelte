<script lang="ts">
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';
	import AnswersSummary from '$lib/components/summary-page/AnswersSummary.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import Back from '$lib/components/Back.svelte';
	import type { LayoutServerData } from './$types';
	import AnswersTable from '$lib/components/summary-page/AnswersTable.svelte';

	export let data: LayoutServerData;

	let numbers: Array<number> = [];

	for (let i = 0; i < data.answers.length; i++) {
		numbers.push(i);
	}
</script>

<Header>
	<div title="Survey title" class="title">{data.survey.survey_structure.title}</div>
</Header>

<Content>
	{#if data.answers.length === 0}
		<div title="Answers" class="title answers">No answers yet!</div>
	{:else}
		<AnswersSummary surveyAnswers={data.answers} />
		<AnswersTable {numbers} />
	{/if}
</Content>

<Footer>
	<Back />
</Footer>
