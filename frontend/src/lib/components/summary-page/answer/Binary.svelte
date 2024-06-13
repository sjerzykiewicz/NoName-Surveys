<script lang="ts">
	export let data: { answer: string; choices: string[] };
</script>

<div class="choice-area display binary">
	<label
		title={data.choices[0] === data.answer ? 'Selected answer' : 'Other choice'}
		class="choice binary"
		class:selected={data.choices[0] === data.answer}
	>
		<div class="icon">
			<input type="radio" disabled />
			<i class="material-symbols-rounded">thumb_up</i>
		</div>
		<div class="choice-input display binary">
			{data.choices[0]}
		</div>
	</label>
	<label
		title={data.choices[1] === data.answer ? 'Selected answer' : 'Other choice'}
		class="choice binary"
		class:selected={data.choices[1] === data.answer}
	>
		<div class="icon">
			<input type="radio" disabled />
			<i class="material-symbols-rounded">thumb_down</i>
		</div>
		<div class="choice-input display binary">
			{data.choices[1]}
		</div>
	</label>
</div>

<style>
	.choice-input,
	.choice-input:hover {
		background-color: var(--primary-dark-color);
		cursor: default;
	}

	.selected .choice-input,
	.selected .choice-input:hover {
		background-color: var(--secondary-dark-color);
	}

	input {
		cursor: default;
	}

	i {
		font-size: 1em;
	}

	.selected i {
		color: var(--accent-color);
		font-variation-settings:
			'FILL' 1,
			'GRAD' 200;
	}
</style>
