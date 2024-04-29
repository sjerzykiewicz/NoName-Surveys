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
	.choice-area {
		font-size: 1em;
		font-weight: normal;
		font-family: 'Jura';
		color: #eaeaea;
		width: 86%;
	}

	.details {
		display: flex;
		align-items: center;
		flex-flow: row;
		margin-left: 2.25em;
	}

	.details-input {
		flex: 1;
		background-color: #1a1a1a;
		padding: 0.25em;
		border: 1px solid #999999;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		font-size: 1.25em;
		cursor: text;
		overflow: hidden;
	}

	.details-input[contenteditable]:empty::before {
		content: 'Enter question details...';
		color: #eaeaea40;
	}

	@media screen and (max-width: 767px) {
		.choice-area,
		.details-input {
			font-size: 1em;
		}
	}
</style>
