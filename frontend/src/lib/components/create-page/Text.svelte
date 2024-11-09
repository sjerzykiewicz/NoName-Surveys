<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import Input from '$lib/components/global/Input.svelte';

	export let questionIndex: number;
</script>

<div class="choice-area text" transition:slide={{ duration: 200, easing: cubicInOut }}>
	<div class="details">
		<Input
			bind:text={$questions[questionIndex].choices[0]}
			label="Question Details"
			title="Enter question details"
			--margin-right="0em"
		/>
	</div>
</div>

<style>
	.details {
		display: flex;
	}
</style>
