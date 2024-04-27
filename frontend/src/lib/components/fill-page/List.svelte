<script lang="ts">
	export let question: string;
	export let required: boolean;
	export let choices: Array<string>;
</script>

<div class="choice-area">
	<select {required} name={question}>
		{#each choices as choice}
			<option value={choice}>
				{choice}
			</option>
		{/each}
	</select>
</div>

<style>
	.choice-area {
		font-size: 1em;
		font-weight: normal;
		font-family: 'Jura';
		color: #eaeaea;
		width: 86%;
		padding-left: 2.3em;
	}

	select {
		flex: 1;
		background-color: #1a1a1a;
		padding: 0.25em;
		border: 1px solid #999999;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		font-size: 1.25em;
		cursor: text;
		margin-right: 0.5em;
		font-size: 1em;
		font-weight: normal;
		font-family: 'Jura';
		color: #eaeaea;
	}
</style>
