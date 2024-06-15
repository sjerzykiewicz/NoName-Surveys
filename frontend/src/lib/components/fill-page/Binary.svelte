<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';

	export let questionIndex: number;
</script>

<div class="choice-area display binary">
	<label
		title="Select your answer"
		class="choice binary"
		class:selected={$answers[questionIndex].choices[0] === $questions[questionIndex].choices[0]}
		><div class="icon">
			<input
				type="radio"
				name={questionIndex.toString()}
				on:change={() => {
					$answers[questionIndex].choices[0] = $questions[questionIndex].choices[0];
				}}
			/>
			<i class="material-symbols-rounded">thumb_up</i>
		</div>
		<div class="choice-input display binary">
			{$questions[questionIndex].choices[0]}
		</div>
	</label>
	<label
		title="Select your answer"
		class="choice binary"
		class:selected={$answers[questionIndex].choices[0] === $questions[questionIndex].choices[1]}
		><div class="icon">
			<input
				type="radio"
				name={questionIndex.toString()}
				on:change={() => {
					$answers[questionIndex].choices[0] = $questions[questionIndex].choices[1];
				}}
			/>
			<i class="material-symbols-rounded">thumb_down</i>
		</div>
		<div class="choice-input display binary">
			{$questions[questionIndex].choices[1]}
		</div>
	</label>
</div>

<style>
	.choice {
		cursor: pointer;
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

	@media screen and (max-width: 767px) {
		i {
			font-size: 1.25em;
		}
	}
</style>
