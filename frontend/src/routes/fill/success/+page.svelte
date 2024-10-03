<script lang="ts">
	import { goto } from '$app/navigation';
	import Content from '$lib/components/Content.svelte';
	import { title, questions, answers } from '$lib/stores/fill-page';

	$title = '';
	$questions = [];
	$answers = [];
</script>

<Content>
	<h2>Answer submitted successfully.</h2>
	<button title="OK" class="save" on:click={() => goto('/')}>
		<i class="material-symbols-rounded">done</i>OK</button
	>
</Content>

<style>
	h2 {
		color: var(--text-color);
		text-align: center;
		text-shadow: 0px 4px 4px var(--shadow-color);
		margin: 0em;
		padding: 0.25em 0em 0.5em;
		font-size: 3em;
		font-weight: bold;
		cursor: default;
		border-bottom: 1px solid var(--border-color);
	}

	.save {
		font-size: 2em;
		margin: 0.75em auto;
	}

	.save i {
		font-variation-settings: 'wght' 700;
	}

	@media screen and (max-width: 767px) {
		h2 {
			font-size: 2em;
		}

		.save {
			font-size: 1.5em;
		}
	}
</style>
