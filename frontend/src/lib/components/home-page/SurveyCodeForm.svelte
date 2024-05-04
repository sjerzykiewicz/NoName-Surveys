<script lang="ts">
	import { goto } from '$app/navigation';

	let code: string;
	let error: string;

	function handleSubmit() {
		if (code === null || code === '') {
			error = 'Please enter code';
			return;
		}
		if (!/^[0-9]{6}$/.test(code)) {
			error = 'Code must be 6 characters long and contain only digits';
			return;
		}
		goto('http://localhost:5173/fill/' + code);
	}
</script>

<form on:submit|preventDefault={handleSubmit}>
	<label for="code-input">Enter survey code</label>
	<input
		title="Enter survey code"
		id="code-input"
		name="survey-code"
		type="text"
		required
		maxlength="6"
		autocomplete="off"
		bind:value={code}
	/>
</form>

{#if error}
	<p class="error">Code must be 6 characters long and contain only digits</p>
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
	}
</style>
