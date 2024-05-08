<script lang="ts">
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';
	import Answers from '$lib/components/summary-page/Answers.svelte';
	import type { PageServerData } from './$types';

	export let data: PageServerData;
</script>

<Header>
	<div class="title">{data.answers[data.id].title}</div>
</Header>

<Content>
	<Answers answer={data.answers[data.id]} id={data.id} />
</Content>
