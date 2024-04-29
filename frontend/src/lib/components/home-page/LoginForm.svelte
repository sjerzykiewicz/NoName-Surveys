<form method="POST">
	<label for="login_buttons">Log in or register</label>
	<br />
	<div id="login-buttons">
		<button disabled>Log in</button>
		<button disabled>Register</button>
	</div>
</form>

<style>
	form {
		margin: 2em 0 2em 0;
		text-align: center;
		color: #eaeaea;
		font-family: 'Jura';
		font-weight: bold;
		font-size: 2em;
	}

	button {
		background-color: #4a4a4a;
		border: 1px solid #eaeaea;
		color: #eaeaea;
		font-family: 'Jura';
		border-radius: 5px;
		padding: 5px;
		font-size: 0.6em;
		margin: 10px;
		transition: background-color 0.2s;
	}

	button:hover {
		background-color: #1a1a1a;
	}

	@media screen and (max-width: 767px) {
		form {
			font-size: 1.5em;
		}
	}
</style>
