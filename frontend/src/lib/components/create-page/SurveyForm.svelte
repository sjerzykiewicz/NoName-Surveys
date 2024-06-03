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

	export let user_list: string[];
	export let isPreview: boolean;

	user_list.push('zxczxczxdzsd@gmail.com');
	user_list.push('bfdsya@gmail.com');
	user_list.push('s567w54myt@gmail.com');
	user_list.push('bmncgfdsgvmfgkhj@gmail.com');

	let isLimited: boolean = false;

	function toggleAccess() {
		isLimited = !isLimited;
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
			title={isLimited ? 'Respondent group defined' : 'Define respondent group'}
			class="access-button"
			class:checked={isLimited}
			on:click={toggleAccess}
		>
			<i class="material-symbols-rounded">passkey</i>
		</button>
		{#if isLimited}
			<div
				title="Select users"
				class="user-list"
				transition:slide={{ duration: 200, easing: cubicInOut }}
			>
				<MultiSelect
					bind:selected={$ringMembers}
					options={user_list}
					--sms-border="1px solid var(--border-color)"
					--sms-border-radius="5px"
					--sms-min-height="2.2em"
					--sms-active-color="var(--text-color)"
					--sms-open-z-index="0"
					--sms-selected-bg="var(--primary-dark-color)"
					--sms-text-color="var(--text-color)"
					--sms-bg="var(--secondary-dark-color)"
					--sms-max-width="100%"
					--sms-options-bg="var(--primary-color)"
					--sms-li-active-bg="var(--secondary-color)"
					--sms-options-border="1px solid var(--border-color)"
				/>
			</div>
		{/if}
	</div>
{/if}

<style>
	.button-row {
		display: flex;
		flex-flow: row;
		align-items: flex-start;
		justify-content: flex-start;
	}

	.access-button {
		margin-left: 0.5em;
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
	}
</style>
