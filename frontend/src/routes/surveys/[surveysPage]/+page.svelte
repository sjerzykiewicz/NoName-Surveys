<script lang="ts">
	import Header from '$lib/components/global/Header.svelte';
	import Content from '$lib/components/global/Content.svelte';
	import SurveysTable from '$lib/components/surveys-page/SurveysTable.svelte';
	import LimitWarning from '$lib/components/global/LimitWarning.svelte';
	import SurveysButtons from '$lib/components/surveys-page/SurveysButtons.svelte';
	import { LIMIT_OF_SURVEYS } from '$lib/stores/global';

	export let data;
	export let selectedSurveysToRemove: typeof data.survey_list = [];
</script>

<Header>
	<div class="title">
		Your surveys
		<span title="Number of surveys" class:max={data.numSurveys >= $LIMIT_OF_SURVEYS}
			>[ {data.numSurveys} / {$LIMIT_OF_SURVEYS} ]</span
		>
	</div>
</Header>

<Content>
	<LimitWarning num={data.numSurveys} limit={$LIMIT_OF_SURVEYS} items="Surveys" />
	<SurveysTable survey_list={data.survey_list.toReversed()} bind:selectedSurveysToRemove />
	<SurveysButtons
		survey_list={data.survey_list.toReversed()}
		numSurveys={data.numSurveys}
		bind:selectedSurveysToRemove
	/>
</Content>

<style>
	.title {
		display: flex;
		justify-content: space-between;
		white-space: normal !important;
	}

	.title span.max {
		color: var(--warning-color);
	}
</style>
