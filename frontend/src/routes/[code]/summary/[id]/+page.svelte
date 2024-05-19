<script lang="ts">
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';
	import Answers from '$lib/components/summary-page/Answers.svelte';
	import Footer from '$lib/components/Footer.svelte';
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
	<button
		class="footer-button"
		on:click={() => {
			history.back();
		}}><i class="material-symbols-rounded">undo</i>Back</button
	>
</Footer>
