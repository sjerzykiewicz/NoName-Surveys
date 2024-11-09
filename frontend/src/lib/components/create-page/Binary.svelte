<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import Input from '$lib/components/global/Input.svelte';

	export let questionIndex: number;
</script>

<div class="choice-area binary" transition:slide={{ duration: 200, easing: cubicInOut }}>
	<label class="choice binary">
		<div class="icon">
			<input type="radio" disabled name={questionIndex.toString()} />
			<i class="symbol">thumb_up</i>
		</div>
		<Input
			bind:text={$questions[questionIndex].choices[0]}
			label="Positive Choice"
			title="Enter a positive choice"
			--label-top="18px"
			--label-top-mobile="14px"
		/>
	</label>
	<label class="choice binary">
		<div class="icon">
			<input type="radio" disabled name={questionIndex.toString()} />
			<i class="symbol">thumb_down</i>
		</div>
		<Input
			bind:text={$questions[questionIndex].choices[1]}
			label="Negative Choice"
			title="Enter a negative choice"
			--label-top="18px"
			--label-top-mobile="14px"
		/>
	</label>
</div>

<style>
	.choice-area {
		justify-content: space-between;
		width: calc(86% - 2.25em);
	}

	input {
		cursor: default !important;
	}

	i {
		font-size: 1em;
		color: var(--border-color-1);
		cursor: default;
		transition:
			0.2s,
			outline 0s;
	}

	@media screen and (max-width: 768px) {
		.choice-area {
			width: 86%;
		}

		.choice {
			width: 100%;
		}
	}
</style>
