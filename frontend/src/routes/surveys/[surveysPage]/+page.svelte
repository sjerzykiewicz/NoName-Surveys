<script lang="ts">
	import Header from '$lib/components/global/Header.svelte';
	import Content from '$lib/components/global/Content.svelte';
	import SurveysTable from '$lib/components/surveys-page/SurveysTable.svelte';
	import LimitWarning from '$lib/components/global/LimitWarning.svelte';
	import SurveysButtons from '$lib/components/surveys-page/SurveysButtons.svelte';
	import { LIMIT_OF_SURVEYS, S } from '$lib/stores/global';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let data;
	export let selectedSurveysToRemove: typeof data.surveys = [];

	const surveyLink =
		'https://github.com/sjerzykiewicz/NoName-Surveys/tree/dev?tab=readme-ov-file#create-a-survey';

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

<Header>
	<div title={$t('your_surveys')} class="title static">
		<div class="header-tooltip">
			<Tx text="your_surveys" />
			<div class="tooltip hoverable">
				<i class="symbol">help</i>
				<span class="tooltip-text {innerWidth <= $S ? 'bottom' : 'right'}">
					<Tx text="surveys_info" /><a href={surveyLink} target="_blank"><Tx text="read_more" /></a>
				</span>
			</div>
		</div>
		<a
			href="/account/faq/#limit-items"
			title={$t('number_of_surveys')}
			class="items"
			class:max={data.numSurveys >= $LIMIT_OF_SURVEYS}
			>[ {data.numSurveys} / {$LIMIT_OF_SURVEYS} ]</a
		>
	</div>
</Header>

<Content>
	<LimitWarning num={data.numSurveys} limit={$LIMIT_OF_SURVEYS} items={$t('surveys_genitive')} />
	<SurveysTable surveys={data.surveys} bind:selectedSurveysToRemove />
	<SurveysButtons
		surveys={data.surveys}
		numSurveys={data.numSurveys}
		bind:selectedSurveysToRemove
	/>
</Content>

<style>
	.items {
		color: var(--text-color-1);
		opacity: 1;
		text-decoration: none;
		transition:
			0.2s,
			outline 0s;
	}

	.items:hover {
		opacity: 0.75;
	}

	.items.max {
		color: var(--warning-color-1);
	}
</style>
