<script lang="ts">
	import type { ActionData } from "../../routes/welcome/$types";

	export let form: ActionData;
</script>

<form method="POST">
	<label for="code-input">Enter survey code</label>
	<br/>
	<input
		id="code-input" 
		name="survey-code"
		type="text"
		required
		maxlength=6
	/>
</form>

{#if form?.error}
	<p class="error">{form.error}</p>
{/if}

<style>
	form, input {
		text-align: center;
		color: #EAEAEA;
		font-family: "Jura";
		font-weight: bold;
		font-size: 2em;
	}
	
	input {
		background-color: #222;
		width: 4em;
		margin: 10px;
	}

	.error {
		text-align: center;
		color: #EAEAEA;
		font-family: "Jura";
		font-weight: bold;
	}
</style>