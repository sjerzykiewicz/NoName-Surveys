<script lang="ts">
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';
	import Answers from '$lib/components/summary-page/answer/Answers.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import Back from '$lib/components/Back.svelte';
	import { goto } from '$app/navigation';
	import type { PageData } from './$types';

	export let data: PageData;
</script>

<Header>
	<div class="title">{data.answers[data.id].title}</div>
</Header>

<Content>
	<Answers answer={data.answers[data.id]} id={data.id} />
</Content>

<Footer>
	{#if data.answers[data.id].is_owned_by_user}
		<button
			title="Manage access to this summary"
			class="footer-button"
			on:click={() => goto('/' + data.code + '/summary/access')}
		>
			<i class="material-symbols-rounded">passkey</i>Access
		</button>
	{/if}
	<Back />
</Footer>
