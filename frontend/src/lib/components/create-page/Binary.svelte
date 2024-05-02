<script lang="ts">
	import { questions } from '$lib/stores/create-page';

	export let questionIndex: number;
</script>

<div class="choice-area">
	<div class="choice">
		<i class="material-symbols-rounded">thumb_up</i>
		<div
			title="Enter positive choice"
			class="choice-input yes"
			contenteditable
			bind:textContent={$questions[questionIndex].choices[0]}
		>
			{$questions[questionIndex].choices[0]}
		</div>
	</div>
	<div class="choice">
		<i class="material-symbols-rounded">thumb_down</i>
		<div
			title="Enter negative choice"
			class="choice-input no"
			contenteditable
			bind:textContent={$questions[questionIndex].choices[1]}
		>
			{$questions[questionIndex].choices[1]}
		</div>
	</div>
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
		margin: 0em 0.5em;
	}

	.choice-input {
		margin: 0.5em 0em 0em 0em;
		width: 11em;
	}

	.yes[contenteditable]:empty::before {
		content: 'Enter positive choice...';
	}

	.no[contenteditable]:empty::before {
		content: 'Enter negative choice...';
	}

	i {
		font-size: 1.25em;
		color: var(--border-color);
		cursor: default;
	}

	@media screen and (max-width: 767px) {
		.choice-area,
		.choice-input,
		i {
			font-size: 1em;
		}

		.choice-input {
			width: 5em;
		}
	}
</style>
