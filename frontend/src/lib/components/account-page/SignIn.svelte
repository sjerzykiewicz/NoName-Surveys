<script lang="ts">
	import { signIn } from '@auth/sveltekit/client';
</script>

<h1>Sign in with:</h1>
<div class="sign-buttons">
	<button title="Google" class="sign-in" on:click={() => signIn('google')}
		><i class="fa-brands fa-google"></i></button
	>
	<button title="Microsoft" class="sign-in" disabled><i class="fa-brands fa-microsoft"></i></button>
	<button title="GitHub" class="sign-in" disabled><i class="fa-brands fa-github"></i></button>
</div>

<style>
	h1 {
		text-align: center;
		text-shadow: 0px 4px 4px var(--shadow-color);
		color: var(--text-color);
		font-size: 3em;
		font-weight: bold;
		cursor: default;
	}

	.sign-buttons {
		display: flex;
		flex-flow: row;
		align-items: center;
		justify-content: center;
	}

	.sign-in {
		margin-left: 0.5em;
		margin-right: 0.5em;
	}

	.sign-in {
		font-size: 1.75em;
	}

	@media screen and (max-width: 767px) {
		h1 {
			font-size: 2em;
		}

		.sign-in {
			font-size: 2em;
		}
	}
</style>
