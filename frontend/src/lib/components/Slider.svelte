<script lang="ts">
	import { questions } from '$lib/stores';

	export let qIndex: number;

	$questions[qIndex].choices = ['', ''];
</script>

<div class="choice-area">
	<div class="slider">
		<input
			class="range"
			type="range"
			step="1"
			min={$questions[qIndex].choices[0]}
			max={$questions[qIndex].choices[1]}
			name={$questions[qIndex].question}
			disabled
		/>
	</div>
	<div class="limits">
		<input
			class="limit-input"
			type="number"
			name={$questions[qIndex].question}
			autocomplete="off"
			required
			placeholder="Enter min..."
			bind:value={$questions[qIndex].choices[0]}
		/>
		<input
			class="limit-input"
			type="number"
			name={$questions[qIndex].question}
			autocomplete="off"
			required
			placeholder="Enter max..."
			bind:value={$questions[qIndex].choices[1]}
		/>
	</div>
</div>

<style>
	.choice-area {
		display: flex;
		flex-flow: column;
		align-items: center;
		justify-content: center;
		font-size: 1em;
		font-weight: normal;
		font-family: 'Jura';
		color: #eaeaea;
		width: 85%;
	}

	.slider {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 100%;
		margin-top: 0.5em;
		margin-bottom: 1em;
	}

	.range {
		appearance: none;
		width: 85%;
		height: 0.5em;
		border-radius: 0.5em;
		background: #999999;
		outline: none;
		opacity: 1;
	}

	.range::-webkit-slider-thumb {
		appearance: none;
		width: 1.5em;
		height: 1.5em;
		border-radius: 1.5em;
		background: #eaeaea;
		cursor: default;
	}

	.range::-moz-range-thumb {
		appearance: none;
		width: 1.5em;
		height: 1.5em;
		border-radius: 1.5em;
		background: #eaeaea;
		cursor: default;
	}

	.limits {
		display: flex;
		align-items: center;
		justify-content: space-between;
		width: 85%;
	}

	.limit-input {
		background-color: #1a1a1a;
		padding: 0.25em;
		border: 1px solid #999999;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		font-size: 1.25em;
		font-weight: normal;
		font-family: 'Jura';
		color: #eaeaea;
		cursor: text;
		overflow: hidden;
		width: 6.5em;
	}

	.limit-input::placeholder {
		color: #eaeaea40;
	}
</style>
