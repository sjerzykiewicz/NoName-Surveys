<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';
	export let questionIndex: number;
	let selected: number;

	function handleClick(id: number) {
		if (id === 0) {
			$answers[questionIndex].choices[0] = 'yes';
			if (selected !== 0) selected = 0;
		} else {
			$answers[questionIndex].choices[0] = 'no';
			if (selected !== 1) selected = 1;
		}
	}
</script>

<div class="choice-area">
	<button class="choice" class:selected={selected === 0} on:click={() => handleClick(0)}>
		<i class="material-symbols-rounded">thumb_up</i>{$questions[questionIndex].choices[0]}
	</button>
	<button class="choice" class:selected={selected === 1} on:click={() => handleClick(1)}>
		<i class="material-symbols-rounded">thumb_down</i>{$questions[questionIndex].choices[1]}
	</button>
</div>

<style>
	.choice.selected,
	.choice.selected:hover {
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
