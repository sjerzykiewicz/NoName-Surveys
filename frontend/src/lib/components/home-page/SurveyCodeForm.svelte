<script lang="ts">
	import { enhance } from '$app/forms';
	import type { ActionData } from '../../../routes/$types';
	import Content from '$lib/components/Content.svelte';

	export let form: ActionData;
</script>

<Content>
	<h1>NoName Anonymous Surveys</h1>
	<form method="POST" use:enhance>
		<label title="Enter a survey code to fill it out" for="code-input"
			>Enter a survey code to fill it out:
			<!-- svelte-ignore a11y-autofocus -->
			<input
				id="code-input"
				name="survey-code"
				type="text"
				required
				maxlength="6"
				autocomplete="off"
				autofocus
			/>
			<button title="Submit the code" class="save" type="submit">
				<i class="material-symbols-rounded">done</i>Submit
			</button>
		</label>
	</form>

	{#if form?.error}
		<p title="Error" class="error"><i class="material-symbols-rounded">error</i>{form.error}</p>
	{/if}
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
		font-size: 1.25em;
		width: 4.25em;
		margin-top: 0.5em;
		margin-left: auto;
		margin-right: auto;
	}

	.save {
		margin: 0.75em auto 0em auto;
	}

	.error {
		justify-content: center;
	}

	.save i {
		font-variation-settings: 'wght' 700;
	}

	@media screen and (max-width: 767px) {
		input,
		.error {
			font-size: 1em;
		}

		form {
			font-size: 1.5em;
		}
	}
</style>
