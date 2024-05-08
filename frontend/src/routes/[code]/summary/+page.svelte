<script lang="ts">
	import { page } from '$app/stores';
	import type { PageServerData } from './$types';

	export let data: PageServerData;
	console.log(data);
</script>

{#each data.answers as answer, i}
	<div class="entry">
		<div class="entry-title">
			<a href="{$page.url.pathname}/{i}">{i + 1}. answer to survey: '{answer.title}'</a>
		</div>
		<div class="entry-code">
			accessed with code: {data.code}
		</div>
	</div>
{/each}

<style>
	.entry {
		border: 1px solid var(--border-color);
		border-radius: 10px;
		font-family: 'Jura';
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
		font-family: 'Jura';
		font-weight: bold;
		font-size: 1.5em;
		width: 100%;
		text-decoration: none;
		transition: background-color 0.2s;
	}
</style>
