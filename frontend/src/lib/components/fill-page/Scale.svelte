<script lang="ts">
	import { questions } from './stores';
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
				/>
			</div>
			<div class="number">
				{choice}
			</div>
		</div>
	{/each}
</div>

<style>
	.choice-area {
		display: flex;
		flex-flow: row;
		align-items: center;
		justify-content: space-around;
		font-size: 1em;
		font-weight: normal;
		font-family: 'Jura';
		color: #eaeaea;
		width: calc(86% - 2.25em);
		margin-left: 2.25em;
	}

	.choice {
		display: flex;
		flex-flow: column;
		align-items: center;
		text-align: center;
	}

	.radio {
		display: flex;
		height: 1.5em;
		width: 1.5em;
	}

	.number {
		font-size: 1.25em;
		cursor: default;
	}
</style>
