<script lang="ts">
	import SelectUsers from './SelectUsers.svelte';
	import SelectGroup from './SelectGroup.svelte';
	import { Access } from '$lib/entities/Access';
	import { getRespondentTypeData } from '$lib/utils/getRespondentTypeData';
	import { access } from '$lib/stores/create-page';

	export let users: string[];
	export let groups: string[];

	let innerWidth: number;

	function toggleAccess() {
		$access = $access === Access.Public ? Access.Private : Access.Public;
	}
</script>

<svelte:window bind:innerWidth />

<div class="crypto-row">
	<button title="Toggle access" class="access-button" on:click={toggleAccess}>
		<i class="material-symbols-rounded">{getRespondentTypeData($access).icon}</i
		>{getRespondentTypeData($access).text}
	</button>
	{#if $access === Access.Public}
		<div class="tooltip">
			<i class="material-symbols-rounded">info</i>
			<span class="tooltip-text {innerWidth <= 454 ? 'left' : 'right'}"
				>Use cryptography to allow only selected users to fill out the survey.</span
			>
		</div>
	{/if}
</div>
{#if $access === Access.Private}
	<div class="select-box">
		<SelectGroup {groups} />
		<SelectUsers {users} />
	</div>
{/if}

<style>
	.tooltip {
		--tooltip-width: 17em;
		margin-top: 0.33em;
		width: fit-content;
	}

	.tooltip i {
		font-size: 1.5em;
		color: var(--border-color);
	}

	.select-box {
		display: flex;
		flex-flow: column;
		flex: 1;
	}

	.crypto-row {
		display: flex;
		flex-flow: row wrap;
		align-items: flex-start;
		justify-content: flex-start;
	}

	.access-button {
		width: fit-content;
		justify-content: center;
		font-size: 1.25em;
		margin-right: 0.5em;
		margin-bottom: 0.5em;
		transition:
			background-color 0.2s,
			color 0.2s;
	}

	.access-button i {
		margin-right: 0.15em;
	}

	@media screen and (max-width: 767px) {
		.access-button {
			font-size: 1em;
		}

		.tooltip {
			margin-top: 0.17em;
		}
	}

	@media screen and (max-width: 544px) {
		.tooltip {
			--tooltip-width: 10em;
		}
	}
</style>
