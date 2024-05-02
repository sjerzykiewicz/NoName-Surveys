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
	<p class="error">{form.error}</p>
{/if}

<style>
	form {
		display: flex;
		flex-flow: column;
		text-align: center;
		color: #eaeaea;
		font-family: 'Jura';
		font-weight: bold;
		font-size: 2em;
		text-shadow: 0px 4px 4px #1a1a1a;
	}

	input {
		padding: 0.25em;
		background-color: #1a1a1a;
		border: 1px solid #999999;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		color: #eaeaea;
		font-family: 'Jura';
		font-weight: bold;
		font-size: 1.25em;
		width: 4.25em;
		margin-top: 0.5em;
		margin-left: auto;
		margin-right: auto;
	}

	.error {
		text-align: center;
		font-size: 1.25em;
		text-shadow: 0px 4px 4px #1a1a1a;
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
