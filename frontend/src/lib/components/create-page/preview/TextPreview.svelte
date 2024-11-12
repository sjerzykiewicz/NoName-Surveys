<script lang="ts">
	import Input from '$lib/components/global/Input.svelte';
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';

	export let questionIndex: number;

	let text: string = '';
</script>

<div class="choice-area text display" transition:slide={{ duration: 200, easing: cubicInOut }}>
	<div title="Question details" class="details">
		{$questions[questionIndex].choices[0]}
	</div>
	<Input bind:text label="Answer" title="Enter your answer" --margin-right="0em" />
</div>
