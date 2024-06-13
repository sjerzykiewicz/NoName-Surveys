<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';

	export let questionIndex: number;
</script>

<div class="choice-area display scale">
	{#each $questions[questionIndex].choices as choice}
		<label title="Select your answer" class="choice scale">
			<input
				type="radio"
				name={questionIndex.toString()}
				on:change={() => {
					$answers[questionIndex].choices[0] = choice;
				}}
			/>
			<div
				class="choice-input display scale"
				class:selected={$answers[questionIndex].choices[0] === choice}
			>
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
