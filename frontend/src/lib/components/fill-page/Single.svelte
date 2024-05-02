<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';
	export let questionIndex: number;

	let selected: number;

	function handleClick(id: number, choice: string) {
		if (selected !== id) {
			selected = id;
			$answers[questionIndex].choices[0] = choice;
		}
	}
</script>

<div class="choice-area">
	{#each $questions[questionIndex].choices as choice, choiceIndex}
		<label class="choice">
			<div class="radio">
				<input
					type="radio"
					name={$questions[questionIndex].question}
					on:click={() => handleClick(choiceIndex, choice)}
				/>
			</div>
			<div title="Enter choice" class="choice-in" class:selected={selected === choiceIndex}>
				{choice}
			</div>
		</label>
	{/each}
</div>

<style>
	@media screen and (max-width: 767px) {
		.choice-area,
		.choice-in {
			font-size: 1em;
		}
	}
</style>
