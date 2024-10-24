<script lang="ts">
	import { enhance } from '$app/forms';
	import type { ActionData } from '../../../routes/$types';
	import Content from '$lib/components/Content.svelte';
	import { S, M } from '$lib/stores/global';
	import { slide } from 'svelte/transition';
	import { cubicInOut } from 'svelte/easing';

	export let form: ActionData;

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

<Content>
	<h1>NoName Anonymous Surveys</h1>
	<form method="POST" use:enhance>
		<label title="Enter a survey code to fill it out" for="code-input"
			><div class="code-text">
				<span>Enter a survey code to fill it out</span>
				<div title="" class="tooltip">
					<i class="material-symbols-rounded">info</i>
					<span
						class="tooltip-text {innerWidth <= $M ? (innerWidth <= $S ? 'top' : 'left') : 'bottom'}"
					>
						Enter the code provided to you by the survey creator. Your answers are completely
						anonymous.
					</span>
				</div>
			</div>
			<!-- svelte-ignore a11y-autofocus -->
			<input
				id="code-input"
				name="survey-code"
				type="text"
				placeholder="______"
				required
				maxlength="6"
				autocomplete="off"
				autofocus={innerWidth > $M}
			/>
			{#if form?.error}
				<p title="Error" class="error" transition:slide={{ duration: 200, easing: cubicInOut }}>
					<i class="material-symbols-rounded">error</i>{form.error}
				</p>
			{/if}
			<button title="Submit the code" class="save" type="submit">
				<i class="material-symbols-rounded">done</i>Submit
			</button>
		</label>
	</form>
</Content>

<style>
	h1 {
		color: var(--text-color);
		text-align: center;
		text-shadow: 0px 4px 4px var(--shadow-color);
		margin: 0em;
		padding: 0.25em 0em 0.5em;
		font-size: 3em;
		font-weight: bold;
		cursor: default;
		border-bottom: 1px solid var(--border-color);
	}

	label {
		display: flex;
		flex-flow: column;
	}

	form {
		text-align: center;
		color: var(--text-color);
		font-weight: bold;
		font-size: 2em;
		text-shadow: 0px 4px 4px var(--shadow-color);
		padding-top: 0.75em;
	}

	input {
		text-align: center;
		padding: 0.25em;
		background-color: var(--secondary-dark-color);
		border: 1px solid var(--border-color);
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--shadow-color);
		color: var(--text-color);
		font-weight: bold;
		font-size: 1.5em;
		width: 4.25em;
		margin-top: 0.5em;
		margin-left: auto;
		margin-right: auto;
	}

	.error {
		justify-content: center;
		font-size: 0.5em;
		margin-bottom: -1.2em;
	}

	.save {
		font-size: 1.25em;
		margin: 0.75em auto 0em auto;
	}

	.save i {
		font-variation-settings: 'wght' 700;
	}

	.code-text {
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: center;
	}

	.code-text .tooltip i {
		font-size: 1.25em;
	}

	.tooltip {
		margin-left: 0.25em;
		font-size: 0.8em;
	}

	.tooltip .tooltip-text {
		font-size: 0.7em;
		font-weight: normal;
	}

	@media screen and (max-width: 768px) {
		h1 {
			font-size: 2.5em;
		}

		.error {
			font-size: 0.5em;
		}
	}

	@media screen and (max-width: 425px) {
		.tooltip {
			margin-left: 0em;
			margin-top: 0.5em;
		}

		.code-text {
			flex-flow: column;
		}
	}
</style>
