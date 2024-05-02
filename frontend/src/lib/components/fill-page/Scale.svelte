<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';
	export let questionIndex: number;
</script>

<div class="choice-area">
	{#each $questions[questionIndex].choices as choice}
		<label class="choice-div">
			<div class="choice">
				<div class="radio-scale">
					<input
						type="radio"
						name={$questions[questionIndex].question}
						on:click={() => ($answers[questionIndex].choices[0] = choice)}
					/>
				</div>
				<div class="number">
					{choice}
				</div>
			</div>
		</label>
	{/each}
</div>

<style>
	.choice-area {
		display: flex;
		flex-flow: row;
		align-items: center;
		justify-content: space-around;
		width: calc(86% - 2.25em);
		margin-left: 2.25em;
	}

	.choice {
		flex-flow: column;
		text-align: center;
		margin-bottom: none;
	}

	.radio-scale {
		display: flex;
		height: 1.5em;
		width: 1.5em;
	}

	.number {
		font-size: 1.25em;
		cursor: default;
	}

	@media screen and (max-width: 767px) {
		.choice-area,
		.number {
			font-size: 1em;
		}
	}
</style>
