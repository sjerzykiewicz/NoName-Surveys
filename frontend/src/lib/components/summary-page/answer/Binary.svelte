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
			<i class="symbol">thumb_up</i>
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
			<i class="symbol">thumb_down</i>
		</div>
		<div class="choice-input display binary">
			{data.choices[1]}
		</div>
	</label>
</div>

<style>
	.choice-input,
	.choice-input:hover {
		background-color: var(--primary-color-2);
		cursor: default;
		transition:
			0.2s,
			outline 0s;
	}

	.choice-input {
		margin-top: 0.5em;
	}

	.selected .choice-input,
	.selected .choice-input:hover {
		background-color: var(--secondary-color-2);
		transition:
			0.2s,
			outline 0s;
	}

	input {
		cursor: default !important;
	}

	i {
		font-size: 1.25em;
	}

	.selected i {
		color: var(--accent-color-1);
		font-variation-settings:
			'FILL' 1,
			'GRAD' 200;
		transition:
			0.2s,
			outline 0s;
	}
</style>
