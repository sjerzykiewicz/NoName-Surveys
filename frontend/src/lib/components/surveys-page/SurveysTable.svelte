<script lang="ts">
	import { goto, invalidateAll } from '$app/navigation';
	import { copyCode } from '$lib/utils/copyCode';
	import { delay } from '$lib/utils/delay';
	import { cubicInOut } from 'svelte/easing';
	import { fade } from 'svelte/transition';
	import QrCode from '$lib/components/QrCode.svelte';
	import { page } from '$app/stores';

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
				title="Copy the code"
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
						<QrCode code={entry.survey_code} size={100} />
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

<style>
	.tooltip {
		display: table-cell;
	}

	.code-entry.tooltip {
		cursor: pointer;
	}

	.code-entry.tooltip .tooltip-text.right {
		--tooltip-width: 100px;
		margin-left: 0em;
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
