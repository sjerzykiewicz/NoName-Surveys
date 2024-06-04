<script lang="ts">
	import QuestionTitle from '$lib/components/create-page/QuestionTitle.svelte';
	import QuestionTitlePreview from '$lib/components/create-page/preview/QuestionTitlePreview.svelte';
	import QuestionError from './QuestionError.svelte';
	import ChoiceError from './ChoiceError.svelte';
	import AddQuestionButtons from '$lib/components/create-page/AddQuestionButtons.svelte';
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { scrollToElement } from '$lib/utils/scrollToElement';
	import { MultiSelect } from 'svelte-multiselect';
	import { ringMembers } from '$lib/stores/create-page';
	import { isAccessLimited } from '$lib/stores/create-page';

	export let user_list: string[];
	export let isPreview: boolean;

	function toggleAccess() {
		$isAccessLimited = !$isAccessLimited;
	}
</script>

{#each $questions as question, questionIndex (question)}
	<div
		class="question"
		in:slide={{ duration: 200, easing: cubicInOut }}
		on:introend={() => scrollToElement('.add-question')}
	>
		{#if isPreview}
			<QuestionTitlePreview {questionIndex} />
			<svelte:component this={question.preview} {questionIndex} />
		{:else}
			<QuestionTitle {questionIndex} questionType={question.component} />
			<QuestionError {questionIndex} />
			<svelte:component this={question.component} {questionIndex} />
			<ChoiceError {questionIndex} />
		{/if}
	</div>
{/each}
{#if !isPreview}
	<div
		class="button-row"
		in:slide={{ delay: 200, duration: 200, easing: cubicInOut }}
		out:slide={{ duration: 200, easing: cubicInOut }}
	>
		<AddQuestionButtons />
		<button
			title={$isAccessLimited ? 'Respondent group defined' : 'Define respondent group'}
			class="access-button"
			class:checked={$isAccessLimited}
			on:click={toggleAccess}
		>
			<i class="material-symbols-rounded">passkey</i>
		</button>
		{#if $isAccessLimited}
			<div
				title="Select users"
				class="user-list"
				transition:slide={{ duration: 200, easing: cubicInOut }}
			>
				<MultiSelect
					bind:selected={$ringMembers}
					options={user_list}
					--sms-max-width="100%"
					--sms-min-height="2.2em"
					--sms-border="1px solid var(--border-color)"
					--sms-border-radius="5px"
					--sms-bg="var(--secondary-dark-color)"
					--sms-selected-bg="var(--primary-color)"
					--sms-active-color="var(--text-color)"
					--sms-li-active-bg="var(--secondary-color)"
					--sms-text-color="var(--text-color)"
					--sms-open-z-index="0"
					--sms-options-max-height="16.5em"
					--sms-options-border="1px solid var(--border-color)"
					--sms-options-border-radius="5px"
					--sms-options-border-width="1px"
					--sms-options-bg="var(--primary-color)"
					--sms-options-shadow="0px 4px 4px var(--shadow-color)"
					--sms-remove-btn-hover-color="var(--error-color)"
					--sms-remove-btn-hover-bg="var(--secondary-color)"
				/>
			</div>
		{/if}
	</div>
{/if}

<style>
	.button-row {
		display: flex;
		flex-flow: row wrap;
		align-items: flex-start;
		justify-content: flex-start;
		align-content: space-between;
		height: 4em;
	}

	.access-button {
		margin-right: 0.5em;
		font-size: 1.25em;
	}

	.access-button.checked {
		background-color: var(--accent-color);
		color: var(--text-color-2);
	}

	.access-button.checked:hover {
		background-color: var(--accent-dark-color);
	}

	.access-button.checked:active {
		background-color: var(--border-color);
	}

	.user-list {
		flex: 1;
		box-shadow: 0px 4px 4px var(--shadow-color);
	}

	@media screen and (max-width: 767px) {
		.access-button {
			font-size: 1em;
		}

		.user-list {
			font-size: 0.8em;
		}
	}
</style>
