<script lang="ts">
	import { page } from '$app/stores';
	import Header from '$lib/components/global/Header.svelte';
	import Content from '$lib/components/global/Content.svelte';
	import Footer from '$lib/components/global/Footer.svelte';
	import OpenSourceInfo from '$lib/components/global/OpenSourceInfo.svelte';
	import SignIn from '$lib/components/account-page/SignIn.svelte';
	import SignOut from '$lib/components/account-page/SignOut.svelte';
	import DownloadKey from '$lib/components/account-page/DownloadKey.svelte';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';
	import AccountButtons from '$lib/components/account-page/AccountButtons.svelte';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let data;
</script>

{#if $page.data.session}
	<Header>
		<div title={$t('your_account')} class="title static">
			<Tx text="welcome" />, {$page.data.session.user?.email.split('@')[0]}!
			<span title="" class="tooltip">
				{#if data.hasKey}
					<i class="symbol generated">key</i>
					<span class="tooltip-text left">
						<Tx text="keys_generated" />
					</span>
				{:else}
					<i class="symbol">key_off</i>
					<span class="tooltip-text left">
						<Tx text="keys_not_generated" />
					</span>
				{/if}
			</span>
		</div>
	</Header>

	<Content>
		<DownloadKey lastTime={data.keyCreationDate} bind:hasKey={data.hasKey} />
		<AccountButtons />
		<SignOut />
	</Content>
{:else}
	<Content>
		<SignIn />
		<AccountButtons />
	</Content>
{/if}
<Footer>
	<OpenSourceInfo />
</Footer>

<style>
	.tooltip .tooltip-text {
		font-size: 0.8em;
	}

	.generated {
		color: var(--accent-color-1);
	}
</style>
