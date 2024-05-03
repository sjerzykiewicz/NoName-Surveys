<div class="login-box">Log in or register</div>
<div class="login-buttons">
	<button title="Log in"><i class="material-symbols-rounded">login</i>Log in</button>
	<button title="Register"><i class="material-symbols-rounded">person_edit</i>Register</button>
</div>

<style>
	.login-box {
		margin: 1em 0 0.5em 0;
		text-align: center;
		color: var(--text-color);
		font-family: 'Jura';
		font-weight: bold;
		font-size: 2em;
		text-shadow: 0px 4px 4px var(--shadow-color);
		cursor: default;
	}

	.login-buttons {
		display: flex;
		justify-content: space-between;
		width: 15em;
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 4em;
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
