<script lang="ts">
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';
	import { page } from '$app/stores';
	import type { PageServerData } from './$types';

	export let data: PageServerData;

	let numbers: Array<number> = [];

	for (let i = 0; i < data.answers.length; i++) {
		numbers.push(i);
	}
</script>

<Header>
	<div class="title">{data.survey.survey_structure.title}</div>
</Header>

<Content>
	{#each numbers as i}
		<div class="entry">
			<div>
				<a href="{$page.url.pathname}/{i}">{i + 1}. Answer</a>
			</div>
		</div>
	{/each}
</Content>

<style>
	.entry {
		border: 1px solid var(--border-color);
		border-radius: 10px;
		color: var(--text-color);
		padding: 5px;
		padding-left: 10px;
		margin: 5px;
		margin-bottom: 15px;
	}

	a {
		padding: 0.5em 0 0.5em 0;
		text-align: center;
		color: var(--text-color);
		font-weight: bold;
		font-size: 1.5em;
		width: 100%;
		text-decoration: none;
		transition: background-color 0.2s;
	}
</style>
