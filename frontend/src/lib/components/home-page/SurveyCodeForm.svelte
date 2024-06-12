<script lang="ts">
	import { enhance } from '$app/forms';
	import type { ActionData } from '../../../routes/$types';

	export let form: ActionData;
</script>

<h1>NoName Anonymous Surveys</h1>
<form method="POST" use:enhance>
	<label for="code-input"
		>Enter a survey code to fill it out
		<input
			title="Enter a survey code to fill it out"
			id="code-input"
			name="survey-code"
			type="text"
			required
			maxlength="6"
			autocomplete="off"
		/>
		<button title="Submit code" class="save" type="submit">
			<i class="material-symbols-rounded">done</i>Submit
		</button>
	</label>
</form>

{#if form?.error}
	<p title="Error" class="error"><i class="material-symbols-rounded">error</i>{form.error}</p>
{/if}

<style>
	h1 {
		text-align: center;
		color: var(--text-color);
		font-size: 2.5em;
		text-shadow: 0px 4px 4px var(--shadow-color);
		margin-top: 1em;
		margin-left: 1em;
		margin-right: 1em;
		cursor: default;
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
		margin-top: 1em;
		margin-left: 1em;
		margin-right: 1em;
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
