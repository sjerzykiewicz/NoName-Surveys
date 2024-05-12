<script lang="ts">
	export let data: { answers: string[]; choices: string[] };

	function calculatePercentage(answer: string, answers: string[]) {
		return ((answers.filter((a) => a === answer).length / answers.length) * 100).toFixed(2);
	}
</script>

<div class="choice-area">
	<label class="choice">
		<input type="radio" disabled />
		<i class="material-symbols-rounded">thumb_up</i>
		<div class="choice-in">
			{data.choices[0]}
		</div>
		<div class="choice-percentage" title="Average">
			{calculatePercentage(data.choices[0], data.answers)}%
		</div>
	</label>
	<label class="choice">
		<input type="radio" disabled />
		<i class="material-symbols-rounded">thumb_down</i>
		<div class="choice-in">
			{data.choices[1]}
		</div>
		<div class="choice-percentage" title="Average">
			{calculatePercentage(data.choices[1], data.answers)}%
		</div>
	</label>
</div>

<style>
	.choice-area {
		display: flex;
		flex-flow: row;
		align-items: center;
		justify-content: space-evenly;
		width: calc(86% - 2.25em);
		margin-left: 2.25em;
	}

	.choice {
		flex-flow: column;
		text-align: center;
		margin-bottom: 0em;
		padding: 0em 0.5em;
		cursor: default;
	}

	.choice-in {
		margin: 0.5em 0em 0em 0em;
		width: fit-content;
		max-width: 11em;
		overflow-wrap: break-word;
		cursor: default;
	}

	.choice-in:hover {
		background-color: var(--primary-color);
	}

	input {
		appearance: none;
		position: relative;
		top: 1.5em;
		margin: 0em;
		height: 1.5em;
		width: 1.5em;
		cursor: default;
	}

	i {
		font-size: 1.25em;
	}

	.choice-percentage {
		margin-left: none;
		margin-top: 0.5em;
	}

	@media screen and (max-width: 767px) {
		.choice-in,
		i {
			font-size: 1em;
		}

		.choice-in {
			max-width: 5em;
		}
	}
</style>
