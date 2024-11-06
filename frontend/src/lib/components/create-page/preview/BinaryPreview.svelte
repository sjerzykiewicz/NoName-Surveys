<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';

	export let questionIndex: number;

	let checked: number;
</script>

<div class="choice-area display binary" transition:slide={{ duration: 200, easing: cubicInOut }}>
	<label title="Select your answer" class="choice binary" class:selected={checked === 0}
		><div class="icon">
			<input
				type="radio"
				name={questionIndex.toString()}
				on:change={() => {
					checked = 0;
				}}
			/>
			<i class="material-symbols-rounded">thumb_up</i>
		</div>
		<div class="choice-input display binary">
			{$questions[questionIndex].choices[0]}
		</div>
	</label>
	<label title="Select your answer" class="choice binary" class:selected={checked === 1}
		><div class="icon">
			<input
				type="radio"
				name={questionIndex.toString()}
				on:change={() => {
					checked = 1;
				}}
			/>
			<i class="material-symbols-rounded">thumb_down</i>
		</div>
		<div class="choice-input display binary">
			{$questions[questionIndex].choices[1]}
		</div>
	</label>
</div>

<style>
	.choice {
		cursor: pointer;
	}

	i {
		font-size: 1em;
	}

	.selected i {
		color: var(--accent-color);
		font-variation-settings:
			'FILL' 1,
			'GRAD' 200;
	}
</style>
