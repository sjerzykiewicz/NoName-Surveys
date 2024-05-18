<script lang="ts">
	import { questions } from '$lib/stores/create-page';

	export let questionIndex: number;
</script>

<div class="choice-area">
	<div class="details">
		<div
			title="Enter question details"
			class="details-input"
			contenteditable
			bind:textContent={$questions[questionIndex].choices[0]}
		>
			{$questions[questionIndex].choices[0]}
		</div>
	</div>
</div>

<style>
	.details {
		display: flex;
	}

	.details-input {
		margin-right: 0em;
	}

	.details-input[contenteditable]:empty::before {
		content: 'Enter question details...';
	}

	@media screen and (max-width: 767px) {
		.choice-area {
			font-size: 1em;
		}
	}
</style>
