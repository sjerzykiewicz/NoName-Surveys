<script lang="ts">
	import type { ActionData } from '../../../routes/welcome/$types';

	export let form: ActionData;
</script>

<form method="POST">
	<label for="code-input">Enter survey code</label>
	<input
		title="Enter survey code"
		id="code-input"
		name="survey-code"
		type="text"
		required
		maxlength="6"
		autocomplete="off"
	/>
</form>

{#if form?.error}
	<p class="error"><i class="material-symbols-rounded">error</i>{form.error}</p>
{/if}

<style>
	form {
		display: flex;
		flex-flow: column;
		text-align: center;
		color: var(--text-color);
		font-family: 'Jura';
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
		font-family: 'Jura';
		font-weight: bold;
		font-size: 1.25em;
		width: 4.25em;
		margin-top: 0.5em;
		margin-left: auto;
		margin-right: auto;
	}

	.error {
		justify-content: center;
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
