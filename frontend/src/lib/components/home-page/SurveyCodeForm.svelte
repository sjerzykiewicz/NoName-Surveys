<script lang="ts">
	import { enhance } from '$app/forms';
	import type { ActionData } from '../../../routes/$types';
	import Header from '$lib/components/global/Header.svelte';
	import Content from '$lib/components/global/Content.svelte';
	import Footer from '$lib/components/global/Footer.svelte';
	import OpenSourceInfo from '$lib/components/global/OpenSourceInfo.svelte';
	import { M } from '$lib/stores/global';
	import { slide } from 'svelte/transition';
	import { cubicInOut } from 'svelte/easing';
	import { page } from '$app/stores';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let form: ActionData;

	const explanationsLink =
		'https://github.com/sjerzykiewicz/NoName-Surveys?tab=readme-ov-file#-explanations';

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

<Header>
	<h1>NoName Anonymous Surveys</h1>
	<div class="subtitle"><Tx text="slogan" /></div>
</Header>

<Content>
	<div class="code-text">
		<span><Tx text="code_info" /></span>
		<div class="tooltip hoverable">
			<i class="symbol">help</i>
			<span class="tooltip-text {innerWidth <= $M ? 'top' : 'bottom'}">
				<Tx text="code_tooltip" />
				<a href={explanationsLink} target="_blank"><Tx text="read_more" /></a>
			</span>
		</div>
	</div>
	<form method="POST" use:enhance>
		<label title={$t('code_info')} for="code-input">
			<!-- svelte-ignore a11y-autofocus -->
			<input
				id="code-input"
				name="survey-code"
				type="text"
				inputmode="numeric"
				placeholder="______"
				required
				maxlength="6"
				autocomplete="off"
				autofocus={innerWidth > $M}
			/>
			{#if form?.error}
				<p
					title={$t('error')}
					class="error"
					transition:slide={{ duration: 200, easing: cubicInOut }}
				>
					<i class="symbol">error</i>{form.error}
				</p>
			{/if}
			<button title={$t('submit_code')} class="done" type="submit">
				<i class="symbol">done</i><Tx text="submit" />
			</button>
		</label>
	</form>
	<p class="home-info">
		<Tx html="home_keys_info" /><a href="/account" title={$t('account')}><Tx text="account" /></a>
	</p>
	<p class="home-info">
		<Tx text="home_redirect" />
		{#if $page.data.session}
			<Tx text="home_redirect_create" /><a href="/create" title={$t('create')}
				><Tx text="create" /></a
			>
		{:else}
			<Tx text="home_redirect_account" /><a href="/account" title={$t('account')}
				><Tx text="account" /></a
			>
		{/if}
	</p>
</Content>

<Footer>
	<OpenSourceInfo />
</Footer>

<style>
	h1 {
		color: var(--text-color-1);
		text-align: center;
		text-shadow: var(--shadow);
		font-size: 3em;
		font-weight: 700;
		margin: 0em;
		padding-bottom: 0.25em;
		cursor: default;
		transition: 0.2s;
	}

	.subtitle {
		color: var(--text-color-1);
		text-align: center;
		text-shadow: var(--shadow);
		font-size: 1.25em;
		font-weight: 700;
		padding-top: 0.5em;
		border-top: 1px solid var(--border-color-1);
		cursor: default;
		transition: 0.2s;
	}

	.code-text {
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: center;
		text-align: center;
		color: var(--text-color-1);
		font-weight: 700;
		font-size: 2em;
		text-shadow: var(--shadow);
		padding-top: 0.25em;
		cursor: default;
		transition:
			0.2s,
			outline 0s;
	}

	.code-text .tooltip i {
		font-size: 1.25em;
	}

	label {
		display: flex;
		flex-flow: column;
		font-size: 2em;
	}

	input {
		text-align: center;
		padding: 0.25em;
		background-color: var(--secondary-color-2);
		border: 1px solid var(--border-color-1);
		border-radius: 5px;
		box-shadow: var(--shadow);
		color: var(--text-color-1);
		font-weight: 700;
		font-size: 1.5em;
		width: 4.25em;
		margin-top: 0.5em;
		margin-left: auto;
		margin-right: auto;
		transition:
			0.2s,
			outline 0s;
	}

	.error {
		justify-content: center;
		font-size: 0.5em;
		margin-bottom: -1.2em;
	}

	.done {
		font-size: 1.25em;
		margin: 0.75em auto 0em auto;
	}

	.tooltip {
		margin-left: 0.5em;
		font-size: 0.8em;
	}

	.tooltip .tooltip-text {
		text-align: left;
		font-size: 0.7em;
		font-weight: 400;
	}

	.home-info {
		text-align: center;
		text-shadow: var(--shadow);
		font-size: 1.2em;
		color: var(--text-color-1);
		cursor: default;
		transition:
			0.2s,
			outline 0s;
	}

	@media screen and (max-width: 768px) {
		h1 {
			font-size: 2.5em;
		}

		.subtitle {
			font-size: 1em;
		}

		.code-text {
			font-size: 1.75em;
			padding-top: 0em;
		}

		.error {
			font-size: 0.5em;
		}

		.tooltip {
			margin-left: 0em;
			margin-top: 0.5em;
		}

		.code-text {
			flex-flow: column;
		}

		.home-info {
			font-size: 1em;
		}
	}
</style>
