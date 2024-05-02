<script lang="ts">
	import { questions } from '$lib/stores/create-page';

	export let questionIndex: number;
</script>

<div class="choice-area">
	<button class="create-page-button" title={$questions[questionIndex].choices[0]} disabled>
		<i class="material-symbols-rounded">thumb_up</i>{$questions[questionIndex].choices[0]}
	</button>
	<button class="create-page-button" title={$questions[questionIndex].choices[1]} disabled>
		<i class="material-symbols-rounded">thumb_down</i>{$questions[questionIndex].choices[1]}
	</button>
</div>

<style>
	.choice-area {
		display: flex;
		flex-flow: row;
		align-items: center;
		justify-content: space-around;
		width: calc(86% - 2.25em);
		margin-left: 2.25em;
	}

	button {
		cursor: default;
	}

	button:hover {
		background-color: var(--primary-color);
	}

	i {
		margin-right: 0.15em;
	}

	@media screen and (max-width: 767px) {
		.create-page-button,
		i {
			font-size: 1em;
		}
	}
</style>
