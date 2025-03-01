<script lang="ts">
	import { page } from '$app/stores';
	import { M } from '$lib/stores/global';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';
	import { startOAuth } from '$lib/utils/startOAuth';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	let isSignInButtonDisabled: boolean = false;

	const navLinks = {
		Fill: {
			name: 'fill',
			href: '/',
			page: '',
			disabled: false
		},
		Create: {
			name: 'create',
			href: '/create',
			page: '',
			disabled: !$page.data.session
		},
		Drafts: {
			name: 'drafts',
			href: '/drafts',
			page: '/0',
			disabled: !$page.data.session
		},
		Surveys: {
			name: 'surveys',
			href: '/surveys',
			page: '/0',
			disabled: !$page.data.session
		},
		Groups: {
			name: 'groups',
			href: '/groups',
			page: '/0',
			disabled: !$page.data.session
		},
		Account: {
			name: 'account',
			href: '/account',
			page: '',
			disabled: false
		}
	};

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

{#each Object.entries(navLinks) as [id, data]}
	<div
		title={data.disabled ? '' : $t(data.name)}
		{id}
		class="nav-link hoverable"
		class:tooltip={innerWidth > $M && data.disabled}
		class:disabled={data.disabled}
		class:active={$page.url.pathname.startsWith('/' + data.name) ||
			$page.url.pathname === data.href}
	>
		<a href={data.disabled ? '' : data.href + data.page}>{$t(data.name)}</a>
		{#if innerWidth > $M && data.disabled}
			<span class="tooltip-text bottom">
				<a
					href="#top"
					on:click={async () => {
						if (isSignInButtonDisabled) return;
						isSignInButtonDisabled = true;
						await startOAuth(data.href + data.page);
						isSignInButtonDisabled = false;
					}}><Tx text="sign_in_lower" /></a
				>
				<Tx text="sign_in_info" />
				<Tx text={data.name} />
			</span>
		{/if}
	</div>
{/each}

<style>
	.tooltip {
		--tooltip-width: 13em;
	}

	.tooltip .tooltip-text {
		margin-top: 0em;
		font-size: 0.8em;
		font-weight: 400;
		text-shadow: var(--shadow);
		background-color: var(--primary-color-2);
		cursor: default;
	}

	.tooltip .tooltip-text.bottom::after {
		border-color: transparent transparent var(--primary-color-2) transparent;
	}

	.tooltip .tooltip-text a:link,
	.tooltip .tooltip-text a:visited {
		color: var(--accent-color-1);
		font-weight: 400;
		text-decoration: underline;
		cursor: pointer;
		transition:
			0.2s,
			outline 0s;
	}

	.tooltip .tooltip-text a:hover {
		color: var(--accent-color-2);
	}

	.tooltip .tooltip-text a:active {
		color: var(--border-color-1);
	}

	.nav-link {
		display: flex;
		justify-content: center;
		align-items: center;
		text-align: center;
		color: var(--text-color-1);
		font-size: 1.5em;
		border-right: 1px solid var(--border-color-1);
		width: 100%;
		cursor: pointer;
		transition: background-color 0.2s;
	}

	.nav-link a {
		padding: 0.5em 0em;
		width: 100%;
		font-weight: 700;
		color: inherit;
		text-decoration: none;
		cursor: inherit;
		transition: 0s;
	}

	.nav-link:hover {
		background-color: var(--primary-color-2);
	}

	.nav-link:active {
		background-color: var(--border-color-1);
	}

	.nav-link.active,
	.nav-link.active:hover {
		background-color: var(--accent-color-1);
		color: var(--text-color-2);
	}

	.nav-link.disabled,
	.nav-link.disabled:hover,
	.nav-link.disabled:active {
		cursor: not-allowed;
		color: var(--text-color-3);
		background-color: var(--secondary-color-1);
	}

	@media screen and (max-width: 768px) {
		.tooltip .tooltip-text {
			font-size: 0.6em;
		}

		.nav-link {
			border-top: 1px solid var(--border-color-1);
			border-right: none;
			border-bottom: none;
		}

		.nav-link a {
			padding: 0.33em 0em;
		}
	}
</style>
