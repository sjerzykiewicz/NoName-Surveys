<script lang="ts">
	import { enhance } from '$app/forms';
	import type { ActionData } from '../../../routes/$types';
	import Content from '$lib/components/global/Content.svelte';
	import { M } from '$lib/stores/global';
	import { slide } from 'svelte/transition';
	import { cubicInOut } from 'svelte/easing';
	import { page } from '$app/stores';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';
	import Footer from '../global/Footer.svelte';
	import Header from '../global/Header.svelte';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let form: ActionData;

	const githubLink = 'https://github.com/sjerzykiewicz/NoName-Surveys';

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
		<!-- TODO: better link -->
		<a href={githubLink} target="_blank" class="tooltip clickable">
			<i class="symbol">help</i>
			<span class="tooltip-text {innerWidth <= $M ? 'top' : 'bottom'}">
				<Tx text="code_tooltip" />
			</span>
		</a>
	</div>
	<form method="POST" use:enhance>
		<label title={$t('code_info')} for="code-input">
			<!-- svelte-ignore a11y-autofocus -->
			<input
				id="code-input"
				name="survey-code"
				type="text"
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
		<Tx text="home_redirect" />
		{#if $page.data.session}<a href="/create" title={$t('create')}><Tx text="create" /></a>.
		{:else}<a href="/account" title={$t('account')}><Tx text="account" /></a>.
		{/if}
	</p>
</Content>

<Footer>
	<div class="open-source-info">
		<Tx text="open_source_info" />
		<a href={githubLink} target="_blank" title="GitHub">GitHub</a>.
	</div>
</Footer>

<style>
	h1 {
		color: var(--text-color-1);
		text-align: center;
		text-shadow: 0px 4px 4px var(--shadow-color-1);
		font-size: 3em;
		font-weight: 700 !important;
		margin: 0em;
		padding-bottom: 0.25em;
		cursor: default;
		transition: 0.2s;
	}

	.subtitle {
		color: var(--text-color-1);
		text-align: center;
		text-shadow: 0px 4px 4px var(--shadow-color-1);
		font-size: 1.25em;
		font-weight: 700 !important;
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
		font-weight: 700 !important;
		font-size: 2em;
		text-shadow: 0px 4px 4px var(--shadow-color-1);
		padding-top: 0.5em;
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
		box-shadow: 0px 4px 4px var(--shadow-color-1);
		color: var(--text-color-1);
		font-weight: 700 !important;
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
		font-weight: 400 !important;
	}

	.home-info {
		text-align: center;
		text-shadow: 0px 4px 4px var(--shadow-color-1);
		font-size: 1.2em;
		color: var(--text-color-1);
		cursor: default;
		transition:
			0.2s,
			outline 0s;
	}

	.home-info a,
	.open-source-info a {
		font-weight: 700 !important;
	}

	.open-source-info {
		width: 100%;
		text-align: center;
		font-size: 1.2em;
		color: var(--text-color-1);
		text-shadow: 0px 4px 4px var(--shadow-color-1);
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

		.home-info,
		.open-source-info {
			font-size: 1em;
		}
	}
</style>
