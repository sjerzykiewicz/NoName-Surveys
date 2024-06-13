<script lang="ts">
	export let data: { answers: string[]; choices: string[] };

	function calculatePercentage(answer: string, answers: string[]) {
		return ((answers.filter((a) => a === answer).length / answers.length) * 100).toFixed(2);
	}
</script>

<div class="choice-area display binary">
	<label title="Choice" class="choice binary">
		<div class="icon">
			<input type="radio" disabled />
			<i class="material-symbols-rounded">thumb_up</i>
		</div>
		<div class="choice-input display binary">
			{data.choices[0]}
		</div>
		<div class="choice-percentage" title="Average">
			{calculatePercentage(data.choices[0], data.answers)}%
		</div>
	</label>
	<label title="Choice" class="choice binary">
		<div class="icon">
			<input type="radio" disabled />
			<i class="material-symbols-rounded">thumb_down</i>
		</div>
		<div class="choice-input display binary">
			{data.choices[1]}
		</div>
		<div class="choice-percentage" title="Average">
			{calculatePercentage(data.choices[1], data.answers)}%
		</div>
	</label>
</div>

<style>
	.choice-input,
	.choice-input:hover {
		background-color: var(--primary-dark-color);
		cursor: default;
	}

	input {
		cursor: default;
	}

	i {
		font-size: 1em;
	}

	.choice-percentage {
		margin-left: none;
		margin-top: 0.5em;
	}
</style>
