<script lang="ts">
	import { goto, invalidateAll } from '$app/navigation';
	import { copyCode } from '$lib/utils/copyCode';
	import { delay } from '$lib/utils/delay';
	import { cubicInOut } from 'svelte/easing';
	import { fade } from 'svelte/transition';
	import QrCode from '$lib/components/QrCode.svelte';
	import { page } from '$app/stores';
	import noname_hat from '$lib/assets/noname_hat.png';

	let copiedIndex: number;
	let innerWidth: number;
	let isCopyPopupVisible: boolean = false;

	export let survey_list: {
		title: string;
		uses_cryptographic_module: boolean;
		survey_code: string;
		creation_date: string;
	}[];

	function deleteSurvey(i: number) {
		fetch('/api/surveys/delete', {
			method: 'POST',
			body: JSON.stringify({
				user_email: $page.data.session?.user?.email,
				survey_code: survey_list[i].survey_code
			}),
			headers: {
				'Content-Type': 'application/json'
			}
		})
			.then(() => {
				survey_list.splice(i, 1);
				invalidateAll();
			})
			.catch(() => alert('Error deleting survey'));
	}
</script>

<svelte:window bind:innerWidth />

{#if survey_list.length === 0}
	<div class="info-row">
		<div title="Surveys" class="title empty">No surveys yet!</div>
		<div class="tooltip">
			<i class="material-symbols-rounded">info</i>
			<span class="tooltip-text {innerWidth <= 423 ? 'bottom' : 'right'}">
				To create a survey, click on the "Create" tab at the top of the page or the button below.
				All your created surveys will be stored on this page.
			</span>
		</div>
	</div>
{:else}
	<table>
		<tr>
			<th title="Survey title" id="title-header" colspan="2">Survey Title</th>
			<th title="Access code" id="code-header">Code</th>
			<th title="Creation date" id="date-header" colspan="2">Date</th>
		</tr>
		{#each survey_list.toReversed() as entry, entryIndex}
			<tr>
				<td class="crypto-entry tooltip">
					{#if entry.uses_cryptographic_module}
						<i class="material-symbols-rounded">encrypted</i>
						<span class="tooltip-text {innerWidth <= 1272 ? 'right' : 'left'}"
							>This survey has an established group of possible respondents.</span
						>
					{:else}
						<i class="material-symbols-rounded">public</i>
						<span class="tooltip-text {innerWidth <= 1272 ? 'right' : 'left'}"
							>Everyone can submit an answer to this survey.</span
						>
					{/if}
				</td>
				<td
					title="View the summary"
					class="title-entry"
					on:click={() => goto('/' + entry.survey_code + '/summary')}>{entry.title}</td
				>
				<td
					title="Copy"
					class="code-entry tooltip popup"
					on:click={async () => {
						if (copyCode(entry.survey_code)) {
							copiedIndex = entryIndex;
							isCopyPopupVisible = true;
							await delay(2000);
							isCopyPopupVisible = false;
						}
					}}
				>
					{entry.survey_code}
					{#if copiedIndex === entryIndex && isCopyPopupVisible}
						<span
							title=""
							class="popup-text left"
							transition:fade={{ duration: 200, easing: cubicInOut }}>Copied!</span
						>
					{/if}
					{#if innerWidth > 767}
						<a
							href="/fill?code={entry.survey_code}"
							title="Fill out the survey"
							class="tooltip-text right"
							transition:fade={{ duration: 200, easing: cubicInOut }}
						>
							<QrCode code={entry.survey_code} codeSize={150} image={noname_hat} />
						</a>
					{/if}
				</td>
				<td title="Creation date" class="date-entry">{entry.creation_date}</td>
				<td
					title="Delete the survey"
					class="button-entry"
					on:click={() => deleteSurvey(survey_list.length - entryIndex - 1)}
				>
					<i class="material-symbols-rounded">delete</i></td
				>
			</tr>
		{/each}
	</table>
{/if}
<button title="Create a survey" on:click={() => goto('/create')}>
	<i class="material-symbols-rounded">add</i>Survey
</button>

<style>
	button {
		font-size: 1.25em;
		margin-top: 0.5em;
	}

	button i {
		margin-right: 0.15em;
		font-variation-settings: 'wght' 700;
	}

	table .tooltip {
		display: table-cell;
	}

	.code-entry.tooltip {
		cursor: pointer;
	}

	.code-entry.tooltip .tooltip-text.right {
		--tooltip-width: 150px;
		margin-left: 0em;
		padding: 0.25em;
		pointer-events: auto;
	}

	.code-entry.popup .popup-text.left {
		--tooltip-width: 4em;
	}

	#code-header {
		width: 12%;
	}

	#date-header {
		width: 19%;
	}

	@media screen and (max-width: 767px) {
		#code-header {
			width: 20%;
		}

		#date-header {
			width: 32%;
		}
	}
</style>
