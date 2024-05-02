<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';

	export let questionIndex: number;
</script>

<div class="choice-area">
	{#each $questions[questionIndex].choices as choice}
		<label title="Select your answer" class="choice">
			<div class="radio">
				<input
					type="radio"
					name={$questions[questionIndex].question}
					on:change={() => {
						$answers[questionIndex].choices[0] = choice;
					}}
				/>
			</div>
			<div class="choice-in" class:selected={$answers[questionIndex].choices[0] === choice}>
				{choice}
			</div>
		</label>
	{/each}
</div>

<style>
	.choice {
		width: fit-content;
		cursor: pointer;
	}

	@media screen and (max-width: 767px) {
		.choice-area,
		.choice-in {
			font-size: 1em;
		}
	}
</style>
