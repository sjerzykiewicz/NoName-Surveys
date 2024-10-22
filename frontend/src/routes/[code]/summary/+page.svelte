<script lang="ts">
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';
	import AnswersSummary from '$lib/components/summary-page/AnswersSummary.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import Back from '$lib/components/Back.svelte';
	import type { LayoutServerData } from './$types';
	import AnswersTable from '$lib/components/summary-page/AnswersTable.svelte';
	import RespondentsTable from '$lib/components/summary-page/RespondentsTable.svelte';
	import { goto } from '$app/navigation';

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
		<div title="Answers" class="title empty">No answers yet!</div>
	{:else}
		<AnswersSummary surveyAnswers={data.answers} />
		<AnswersTable {numbers} />
	{/if}
	{#if data.survey.uses_cryptographic_module}
		<RespondentsTable respondents={data.respondents} />
	{/if}
</Content>

<Footer>
	{#if data.answers.length > 0 && data.answers[0].is_owned_by_user}
		<button
			title="Manage access to this summary"
			class="footer-button"
			on:click={() => goto('/' + data.code + '/summary/access')}
		>
			<i class="material-symbols-rounded">passkey</i>Access
		</button>
	{/if}
	<Back />
</Footer>
