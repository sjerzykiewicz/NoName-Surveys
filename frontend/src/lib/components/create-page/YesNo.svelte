<script lang="ts">
	import { questions } from '$lib/components/create-page/stores';

	export let questionIndex: number;
</script>

<div class="choice-area">
	<button title={$questions[questionIndex].choices[0]} disabled>
		<i class="material-symbols-rounded">thumb_up</i>{$questions[questionIndex].choices[0]}
	</button>
	<button title={$questions[questionIndex].choices[1]} disabled>
		<i class="material-symbols-rounded">thumb_down</i>{$questions[questionIndex].choices[1]}
	</button>
</div>

<style>
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

	button {
		display: flex;
		background-color: #4a4a4a;
		padding: 0.25em;
		border: 1px solid #999999;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		font-size: 1.25em;
		font-family: 'Jura';
		color: #eaeaea;
		cursor: default;
	}

	i {
		font-size: 1.15em;
		margin-right: 0.15em;
	}

	@media screen and (max-width: 767px) {
		button,
		i {
			font-size: 1em;
		}
	}
</style>
