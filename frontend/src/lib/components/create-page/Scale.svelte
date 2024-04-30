<script lang="ts">
	import { questions } from '$lib/stores/create-page';

	export let questionIndex: number;
</script>

<div class="choice-area">
	{#each $questions[questionIndex].choices as choice}
		<div class="choice">
			<div class="radio">
				<input type="radio" disabled name={$questions[questionIndex].question} />
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
		width: calc(86% - 2.25em);
		margin-left: 2.25em;
	}

	.choice {
		flex-flow: column;
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

	@media screen and (max-width: 767px) {
		.choice-area,
		.number {
			font-size: 1em;
		}
	}
</style>
