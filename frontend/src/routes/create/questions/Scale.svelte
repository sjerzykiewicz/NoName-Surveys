<script lang="ts">
	import { questions } from '../stores';

	export let qIndex: number;

	$questions[qIndex].choices = ['1', '2', '3', '4', '5'];
</script>

<div class="choice-area">
	{#each $questions[qIndex].choices as choice}
		<div class="choice">
			<div class="radio">
				<input type="radio" disabled name={$questions[qIndex].question} />
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
		justify-content: space-evenly;
		font-size: 1em;
		font-weight: normal;
		font-family: 'Jura';
		color: #eaeaea;
		width: 80%;
	}

	.choice {
		display: flex;
		flex-flow: column;
		align-items: center;
		text-align: center;
	}

	.radio {
		text-align: center;
	}

	.number {
		font-size: 1.25em;
	}
</style>
