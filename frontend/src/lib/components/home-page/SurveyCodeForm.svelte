<script lang="ts">
	import type { ActionData } from '../../../routes/$types';

	export let form: ActionData;
</script>

<form method="POST">
	<label for="code-input"
		>Enter survey code
		<input
			title="Enter survey code"
			id="code-input"
			name="survey-code"
			type="text"
			required
			maxlength="6"
			autocomplete="off"
		/>
		<button title="Submit code" class="submit" type="submit">
			<i class="material-symbols-rounded">done</i>Submit
		</button>
	</label>
</form>

{#if form?.error}
	<p class="error">{form.error}</p>
{/if}

<style>
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
	}

	input {
		text-align: center;
		padding: 0.25em;
		background-color: var(--shadow-color);
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

	.submit {
		font-size: 1em;
		margin: 0.75em auto 0em auto;
	}

	.error {
		text-align: center;
		font-size: 1.25em;
		text-shadow: 0px 4px 4px var(--shadow-color);
	}

	@media screen and (max-width: 767px) {
		input,
		.error {
			font-size: 1em;
		}

		form {
			font-size: 1.5em;
		}

		.submit {
			font-size: 0.75em;
		}
	}
</style>
