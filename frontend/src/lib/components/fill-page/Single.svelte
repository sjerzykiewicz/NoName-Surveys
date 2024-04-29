<script lang="ts">
	import { questions } from '$lib/stores/fill-page';
	import { answers } from '$lib/stores/fill-page';
	export let questionIndex: number;
</script>

<div class="choice-area">
	{#each $questions[questionIndex].choices as choice}
		<div class="choice">
			<div class="radio">
				<input
					type="radio"
					required={$questions[questionIndex].required}
					name={$questions[questionIndex].question}
					on:click={() => ($answers[questionIndex].choices[0] = choice)}
				/>
			</div>
			<div title="Select choice" class="choice-input">
				{choice}
			</div>
		</div>
	{/each}
</div>

<style>
	.choice-area {
		font-size: 1em;
		font-weight: normal;
		font-family: 'Jura';
		color: #eaeaea;
		width: 86%;
	}

	.choice {
		display: flex;
		align-items: center;
		flex-flow: row;
		margin-bottom: 0.5em;
	}

	.choice-input {
		flex: 1;
		background-color: #1a1a1a;
		padding: 0.25em;
		border: 1px solid #999999;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		font-size: 1.25em;
		cursor: text;
		overflow: hidden;
		margin-right: 0.5em;
	}

	.radio {
		text-align: right;
		width: 1.75em;
		margin-right: 0.5em;
	}

	@media screen and (max-width: 767px) {
		.choice-area,
		.choice-input {
			font-size: 1em;
		}
	}
</style>
