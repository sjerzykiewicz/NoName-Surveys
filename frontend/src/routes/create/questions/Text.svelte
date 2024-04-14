<script lang="ts">
	import { questions } from '../stores';

	export let qIndex: number;

	$questions[qIndex].choices = [''];

	function clearDetails() {
		$questions[qIndex].choices[0] = '';
	}
</script>

<div class="choice-area">
	<div class="details">
		<div class="details-input" contenteditable bind:textContent={$questions[qIndex].choices[0]}>
			{$questions[qIndex].choices[0]}
		</div>
		<button on:click={clearDetails}>
			<i class="material-icons">close</i>Details
		</button>
	</div>
</div>

<style>
	.choice-area {
		font-size: 1em;
		font-weight: normal;
		font-family: 'Jura';
		color: #eaeaea;
		width: 85%;
	}

	.details {
		display: flex;
		align-items: center;
		flex-flow: row;
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
		margin-right: 0.5em;
	}

	.details-input[contenteditable]:empty::before {
		content: 'Enter question details...';
		color: #eaeaea40;
	}

	button {
		display: flex;
		flex-flow: row;
		justify-content: center;
		align-items: flex-end;
		background-color: #4a4a4a;
		padding: 0.25em;
		border: 1px solid #999999;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		width: fit-content;
		font-size: 1.25em;
		font-weight: normal;
		font-family: 'Jura';
		color: #eaeaea;
		cursor: pointer;
		transition: background-color 0.3s;
	}

	button:hover {
		background-color: #1a1a1a;
	}

	.material-icons {
		font-size: 0.99em;
		font-weight: bold;
		padding-right: 0.25em;
	}
</style>
