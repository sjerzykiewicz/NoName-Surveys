<script lang="ts">
	import type { PageServerData } from './$types';
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';
	import SurveysTable from '$lib/components/surveys-page/SurveysTable.svelte';
	import { LIMIT_OF_ACTIVE_SURVEYS } from '$lib/stores/global';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { afterUpdate } from 'svelte';

	export let data: PageServerData;

	let numSurveys: number = data.survey_list.length;

	afterUpdate(() => {
		numSurveys = data.survey_list.length;
	});
</script>

<Header>
	<div class="title">
		Your surveys
		<span title="Number of surveys" class:max={numSurveys >= $LIMIT_OF_ACTIVE_SURVEYS}
			>[ {numSurveys} / {$LIMIT_OF_ACTIVE_SURVEYS} ]</span
		>
	</div>
</Header>

<Content>
	{#if numSurveys >= $LIMIT_OF_ACTIVE_SURVEYS}
		<p
			title="Survey limit reached"
			class="error"
			transition:slide={{ duration: 200, easing: cubicInOut }}
		>
			<i class="material-symbols-rounded">error</i>You have reached the maximum number of surveys.
			Please delete some surveys to create new ones.
		</p>
	{/if}
	<SurveysTable survey_list={data.survey_list} />
</Content>

<style>
	.title {
		display: flex;
		justify-content: space-between;
		white-space: normal !important;
	}

	.title span.max {
		color: var(--error-color);
	}

	.error {
		margin: 0em 0em 0.75em;
	}
</style>
