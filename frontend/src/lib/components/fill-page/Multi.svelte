<script lang="ts">
	export let question: string;
	export let required: boolean;
	export let choices: Array<string>;
</script>

<div class="choice-area">
	{#each choices as choice}
		<div class="choice">
			<div class="checkbox">
				<input type="checkbox" {required} name={question} />
			</div>
			<div title="Select choice" class="choice-input">
				{choice}
			</div>
		</div>
	{/each}
</div>

<style>
	.choice-area {
		font-size: 1em;
		font-weight: normal;
		font-family: 'Jura';
		color: #eaeaea;
		width: 86%;
	}

	.choice {
		display: flex;
		align-items: center;
		flex-flow: row;
		margin-bottom: 0.5em;
	}

	.choice-input {
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

	.checkbox {
		text-align: right;
		width: 1.75em;
		margin-right: 0.5em;
	}
</style>
