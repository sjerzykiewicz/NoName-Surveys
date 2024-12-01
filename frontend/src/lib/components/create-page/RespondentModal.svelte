<script lang="ts">
	import Modal from '$lib/components/global/Modal.svelte';
	import SelectGroup from './SelectGroup.svelte';
	import SelectUsers from './SelectUsers.svelte';
	import CryptoError from './CryptoError.svelte';
	import ImportEmails from '$lib/components/global/ImportEmails.svelte';
	import { errorModalContent, isErrorModalHidden, M } from '$lib/stores/global';
	import { slide } from 'svelte/transition';
	import { cubicInOut } from 'svelte/easing';
	import Survey from '$lib/entities/surveys/Survey';
	import SurveyCreateInfo from '$lib/entities/surveys/SurveyCreateInfo';
	import { constructQuestionList } from '$lib/utils/constructQuestionList';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';
	import { invalidateAll } from '$app/navigation';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';
	import { currentDraftId, questions, title } from '$lib/stores/create-page';
	import { SurveyError } from '$lib/entities/SurveyError';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let isHidden: boolean = true;
	export let users: string[];
	export let groups: string[];
	export let invalidEmails: string[] = [];
	export let isExportButtonVisible: boolean = false;
	export let ringMembers: string[] = [];
	export let selectedGroups: string[] = [];
	export let useCrypto: boolean = false;
	export let surveyCode: string;
	export let isSurveyModalHidden: boolean = true;
	export let isFromDraft: boolean;

	let cryptoError: boolean = false;

	function checkCorrectness() {
		cryptoError = false;
		const g = selectedGroups;
		const r = ringMembers;
		if (
			useCrypto &&
			(g === null || g === undefined || g.length === 0) &&
			(r === null || r === undefined || r.length === 0)
		) {
			cryptoError = true;
			return false;
		}
		return true;
	}

	async function createSurvey() {
		if (!checkCorrectness()) return;

		isHidden = true;

		const parsedSurvey = new Survey(constructQuestionList($questions));
		const surveyInfo = new SurveyCreateInfo($title.title, parsedSurvey, useCrypto, ringMembers);

		const response = await fetch('/api/surveys/create', {
			method: 'POST',
			body: JSON.stringify(surveyInfo),
			headers: {
				'Content-Type': 'application/json'
			}
		});

		if (!response.ok) {
			const body = await response.json();
			$errorModalContent = getErrorMessage(body.detail);
			$isErrorModalHidden = false;
			return;
		}

		const body = await response.json();
		useCrypto = false;
		ringMembers = [];
		selectedGroups = [];
		surveyCode = body.survey_code;
		isSurveyModalHidden = false;
		if (isFromDraft) {
			clearDraft();
		}
		await invalidateAll();
	}

	function clearDraft() {
		$title = { title: '', error: SurveyError.NoError };
		$questions = [];
		$currentDraftId = null;
	}

	async function handleEnter(event: KeyboardEvent) {
		if (!isHidden && event.key === 'Enter') {
			event.preventDefault();
			await createSurvey();
			event.stopImmediatePropagation();
		}
	}

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />
<svelte:body on:keydown={handleEnter} />

<Modal
	icon="group"
	title={$t('define_respondent_group')}
	bind:isHidden
	--width={innerWidth <= $M ? '20em' : '26em'}
	hide={() => {
		isHidden = true;
		if (isFromDraft) {
			clearDraft();
		}
	}}
>
	<div slot="content">
		<span><Tx text="define_respondent_group_alert" /></span>
		<div class="crypto-buttons">
			<button
				title={$t('public')}
				class="access-button"
				class:save={!useCrypto}
				on:click={() => (useCrypto = false)}
			>
				<i class="symbol">public</i><Tx text="public" />
			</button>
			<button
				title={$t('secure')}
				class="access-button"
				class:save={useCrypto}
				on:click={() => (useCrypto = true)}
			>
				<i class="symbol">encrypted</i><Tx text="secure" />
			</button>
		</div>
		{#if useCrypto}
			<div class="select-box" transition:slide={{ duration: 200, easing: cubicInOut }}>
				<SelectGroup {groups} bind:ringMembers bind:selectedGroups />
				<div id="or"><Tx text="or" /></div>
				<SelectUsers {users} bind:ringMembers />
				<CryptoError error={cryptoError} bind:ringMembers bind:selectedGroups bind:useCrypto />
				<div class="import">
					<ImportEmails
						bind:users={ringMembers}
						title={$t('import_users_title')}
						label={$t('import_users_label')}
						checkKeys={true}
						--width="100%"
						bind:invalidEmails
						bind:isExportButtonVisible
					/>
				</div>
			</div>
		{/if}
	</div>
	<button title={$t('define_respondent_group')} class="done" on:click={createSurvey}
		><i class="symbol">done</i><Tx text="finish" /></button
	>
</Modal>

<style>
	.crypto-buttons {
		display: flex;
		flex-flow: row;
		justify-content: space-around;
		padding-top: 1em;
	}

	.access-button {
		width: fit-content;
		justify-content: center;
		margin-right: 0.5em;
		margin-bottom: 0.5em;
	}

	.access-button i {
		margin-right: 0.15em;
	}

	.select-box {
		text-align: left;
		padding-top: 1em;
	}

	#or {
		display: flex;
		flex-flow: row;
		align-items: flex-start;
		justify-content: flex-start;
		margin-bottom: 0.5em;
		font-size: 0.8em;
		color: var(--text-color-1);
		cursor: default;
		transition: 0.2s;
	}

	.import {
		font-size: 0.8em;
	}

	@media screen and (max-width: 768px) {
		.import {
			font-size: 1em;
		}
	}
</style>
