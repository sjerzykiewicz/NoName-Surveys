<script lang="ts">
	import type { PageServerData } from './$types';
	import { page } from '$app/stores';
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';
	import SignIn from '$lib/components/account-page/SignIn.svelte';
	import SignOut from '$lib/components/account-page/SignOut.svelte';
	import DownloadKey from '$lib/components/account-page/DownloadKey.svelte';
	import Tx from 'sveltekit-translate/translate/tx.svelte';

	export let data: PageServerData;
</script>

{#if $page.data.session}
	<Header>
		<div title="Your account" class="title">
			<Tx text="welcome"></Tx>, {$page.data.session.user?.email}
		</div>
	</Header>

	<Content>
		<DownloadKey {data} />
		<SignOut />
	</Content>
{:else}
	<Content>
		<SignIn />
	</Content>
{/if}
