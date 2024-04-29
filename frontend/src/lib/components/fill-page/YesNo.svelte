<script lang="ts">
	import { questions } from '$lib/stores/fill-page';
	export let questionIndex: number;
</script>

<div class="choice-area">
	<label for="yes">
		<input
			type="radio"
			name={$questions[questionIndex].question}
			id="yes"
			title={$questions[questionIndex].choices[0]}
			required={$questions[questionIndex].required}
		/>
		<div class="choice">
			<i class="material-symbols-rounded">thumb_up</i>{$questions[questionIndex].choices[0]}
		</div>
	</label>
	<label for="no">
		<input
			type="radio"
			name={$questions[questionIndex].question}
			id="no"
			title={$questions[questionIndex].choices[1]}
			required={$questions[questionIndex].required}
		/>
		<div class="choice">
			<i class="material-symbols-rounded">thumb_down</i>{$questions[questionIndex].choices[1]}
		</div>
	</label>
</div>

<style>
	input[type='radio'] {
		visibility: hidden;
	}

	input[type='radio']:checked + .choice {
		background-color: #0075ff;
	}

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
		background-color: #1a1a1a;
		padding: 0.25em;
		border: 1px solid #999999;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		font-size: 1.25em;
		font-family: 'Jura';
		color: #eaeaea;
		cursor: default;
	}

	.choice:hover {
		background-color: #4a4a4a;
	}

	.choice:checked {
		background-color: #0075ff;
	}

	i {
		font-size: 1.15em;
		margin-right: 0.15em;
	}

	@media screen and (max-width: 767px) {
		.choice,
		i {
			font-size: 1em;
		}
	}
</style>
