<script lang="ts">
	import Header from '$lib/components/global/Header.svelte';
	import Content from '$lib/components/global/Content.svelte';
	import DraftsTable from '$lib/components/drafts-page/DraftsTable.svelte';
	import DraftsButtons from '$lib/components/drafts-page/DraftsButtons.svelte';
	import LimitWarning from '$lib/components/global/LimitWarning.svelte';
	import { LIMIT_OF_DRAFTS, M } from '$lib/stores/global';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';
	import WarningModal from '$lib/components/global/WarningModal.svelte';
	import RespondentModal from '$lib/components/create-page/RespondentModal.svelte';
	import QrCodeModal from '$lib/components/global/QrCodeModal.svelte';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let data;
	export let selectedDraftsToRemove: number[] = [];
	export let isRespondentModalHidden: boolean = true;
	export let invalidEmails: string[] = [];
	export let isExportButtonVisible: boolean = false;
	export let ringMembers: string[] = [];
	export let selectedGroups: string[] = [];
	export let useCrypto: boolean = false;

	let isSurveyModalHidden: boolean = true;
	let surveyCode: string;
	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

<RespondentModal
	bind:isHidden={isRespondentModalHidden}
	bind:users={data.user_list}
	bind:groups={data.group_list}
	bind:invalidEmails
	bind:isExportButtonVisible
	bind:ringMembers
	bind:selectedGroups
	bind:useCrypto
	bind:isSurveyModalHidden
	bind:surveyCode
	isFromDraft={true}
/>

<QrCodeModal bind:isHidden={isSurveyModalHidden} title={$t('survey_success')} {surveyCode} />

<WarningModal
	{isExportButtonVisible}
	emails={invalidEmails}
	--width-warning={innerWidth <= $M ? '20em' : '23em'}
/>

<Header>
	<div title={$t('your_drafts')} class="title static">
		<Tx text="your_drafts" />
		<span title={$t('number_of_drafts')} class:max={data.numDrafts >= $LIMIT_OF_DRAFTS}
			>[ {data.numDrafts} / {$LIMIT_OF_DRAFTS} ]</span
		>
	</div>
</Header>

<Content>
	<LimitWarning num={data.numDrafts} limit={$LIMIT_OF_DRAFTS} items={$t('drafts_genitive')} />
	<DraftsTable
		drafts={data.drafts}
		numSurveys={data.numSurveys}
		bind:selectedDraftsToRemove
		bind:isExportButtonVisible
		bind:isRespondentModalHidden
	/>
	<DraftsButtons drafts={data.drafts} numDrafts={data.numDrafts} bind:selectedDraftsToRemove />
</Content>

<style>
	.title span.max {
		color: var(--warning-color-1);
		transition:
			0.2s,
			outline 0s;
	}
</style>
