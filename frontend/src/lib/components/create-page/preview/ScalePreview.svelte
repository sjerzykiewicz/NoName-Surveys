<script lang="ts">
	import { questions } from '$lib/stores/create-page';

	export let questionIndex: number;

	let checked: number;
</script>

<div class="choice-area display scale">
	{#each $questions[questionIndex].choices as choice, choiceIndex}
		<label title="Select your answer" class="choice scale">
			<input
				type="radio"
				name={questionIndex.toString()}
				on:change={() => {
					checked = choiceIndex;
				}}
			/>
			<div class="choice-input display scale" class:selected={checked === choiceIndex}>
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
