<div class="login-box">Log in or register</div>
<div class="login-buttons">
	<button title="Log in"><i class="material-symbols-rounded">login</i>Log in</button>
	<button title="Register"><i class="material-symbols-rounded">person_edit</i>Register</button>
</div>

<style>
	.login-box {
		margin: 1.5em 0 0.5em 0;
		text-align: center;
		color: #eaeaea;
		font-family: 'Jura';
		font-weight: bold;
		font-size: 2em;
		text-shadow: 0px 4px 4px #1a1a1a;
		cursor: default;
	}

	.login-buttons {
		display: flex;
		justify-content: space-between;
		width: 15em;
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 5em;
	}

	button {
		display: flex;
		align-items: center;
		background-color: #4a4a4a;
		padding: 0.25em;
		border: 1px solid #999999;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		font-size: 1.25em;
		font-family: 'Jura';
		color: #eaeaea;
		cursor: pointer;
		transition: background-color 0.2s;
	}

	button:hover {
		background-color: #1a1a1a;
	}

	button:active {
		background-color: #999999;
	}

	i {
		font-size: 1.15em;
		margin-right: 0.15em;
	}

	@media screen and (max-width: 767px) {
		.login-box {
			font-size: 1.5em;
		}

		.login-buttons {
			width: 12em;
		}

		button,
		i {
			font-size: 1em;
		}
	}
</style>
