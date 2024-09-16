<script lang="ts">
	import SelectUsers from './SelectUsers.svelte';
	import SelectGroup from './SelectGroup.svelte';
	import { isAccessLimited } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { scrollToElement } from '$lib/utils/scrollToElement';
	import { Access } from '$lib/entities/Access';
	import { onMount } from 'svelte';
	import RespondentTypeButton from './RespondentTypeButton.svelte';

	export let users: string[];
	export let groups: string[];

	let isPanelVisible: boolean = false;
	let access: Access = Access.Public;
	let respondentTypes: Array<Access> = [Access.Public, Access.Users, Access.Group];
	let innerWidth: number;

	function togglePanel() {
		isPanelVisible = !isPanelVisible;
	}

	onMount(() => {
		function handleClick(event: MouseEvent) {
			if (isPanelVisible && !(event.target as HTMLElement).closest('.access-button')) {
				isPanelVisible = false;
			}
		}

		document.body.addEventListener('click', handleClick);

		return () => {
			document.body.removeEventListener('click', handleClick);
		};
	});
</script>

<svelte:window bind:innerWidth />

<div class="button-group">
	<div class="crypto-buttons">
		<button
			title={$isAccessLimited ? 'Respondent group defined' : 'Define respondent group'}
			class="access-button"
			class:clicked={isPanelVisible}
			on:click={togglePanel}
		>
			<i class="material-symbols-rounded">passkey</i>Access
		</button>
		<RespondentTypeButton respondentType={access} respondentTypeIndex={-1} />
	</div>
	{#if isPanelVisible}
		<div
			class="button-panel"
			transition:slide={{ duration: 200, easing: cubicInOut }}
			on:introstart={() => scrollToElement('.access-button')}
		>
			{#each respondentTypes as respondentType, respondentTypeIndex}
				<RespondentTypeButton
					{respondentType}
					{respondentTypeIndex}
					on:chooseRespondentType={(event) => (access = event.detail.type)}
				/>
			{/each}
		</div>
	{/if}
</div>
<div class="crypto-row">
	{#if access === Access.Users}
		<SelectUsers {users} />
	{:else if access === Access.Group}
		<SelectGroup {groups} />
	{:else}
		<div class="tooltip">
			<i class="material-symbols-rounded">info</i>
			<span class="tooltip-text {innerWidth <= 509 ? 'bottom' : 'right'}"
				>Use cryptography to allow only selected users to fill out the survey.</span
			>
		</div>
	{/if}
</div>

<style>
	.tooltip {
		--tooltip-width: 18em;
		font-size: 0.8em;
	}

	.tooltip i {
		font-size: 1.5em;
		color: var(--border-color);
	}

	button {
		width: 5.5em;
		box-shadow: none;
	}

	.button-group {
		width: fit-content;
		font-size: 1.25em;
		margin-right: 0.5em;
		margin-bottom: 0.5em;
	}

	.crypto-row {
		flex: 1;
		display: flex;
		flex-flow: row;
		align-items: center;
		justify-content: flex-start;
	}

	.crypto-buttons {
		display: flex;
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--shadow-color);
	}

	.button-panel {
		display: flex;
		flex-flow: column;
		border-radius: 0px 0px 5px 5px;
		box-shadow: 0px 4px 4px var(--shadow-color);
		width: fit-content;
		height: auto;
		position: absolute;
		z-index: 100;
	}

	.access-button {
		border-top-right-radius: 0px;
		border-bottom-right-radius: 0px;
		transition:
			background-color 0.2s,
			color 0.2s,
			border-radius 0.2s;
	}

	.access-button.clicked {
		background-color: var(--accent-color);
		border-bottom-right-radius: 0px;
		border-bottom-left-radius: 0px;
		color: var(--text-color-2);
	}

	.access-button.clicked:hover {
		background-color: var(--accent-dark-color);
	}

	.access-button.clicked:active {
		background-color: var(--border-color);
	}

	.access-button i {
		margin-right: 0.15em;
	}

	@media screen and (max-width: 767px) {
		.crypto-row {
			font-size: 1em;
		}
	}

	@media screen and (max-width: 509px) {
		.tooltip {
			--tooltip-width: 9em;
		}
	}
</style>
