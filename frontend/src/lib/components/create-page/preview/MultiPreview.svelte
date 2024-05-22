<script lang="ts">
	import { questions } from '$lib/stores/create-page';

	export let questionIndex: number;

	let selected: Array<boolean> = [];
	for (let i = 0; i < $questions[questionIndex].choices.length; i++) {
		selected[i] = false;
	}
</script>

<div class="choice-area display">
	{#each $questions[questionIndex].choices as choice, choiceIndex}
		<label title="Select your answer" class="choice">
			<div class="checkbox">
				<input
					type="checkbox"
					name={questionIndex.toString()}
					on:change={() => {
						selected[choiceIndex] = !selected[choiceIndex];
					}}
				/>
			</div>
			<div class="choice-input display" class:selected={selected[choiceIndex]}>
				{choice}
			</div>
		</label>
	{/each}
</div>

<style>
	.choice {
		cursor: pointer;
	}
</style>
