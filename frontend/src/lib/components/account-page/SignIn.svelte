<script lang="ts">
	import { signIn } from '@auth/sveltekit/client';
</script>

<h1>Sign in with:</h1>
<div class="sign-buttons">
	<button title="Google" class="sign-in" on:click={() => signIn('google')}
		><i class="fa-brands fa-google"></i></button
	>
	<button title="GitHub" class="sign-in" on:click={() => signIn('github')}
		><i class="fa-brands fa-github"></i></button
	>
	<button title="X" class="sign-in" disabled><i class="fa-brands fa-x-twitter"></i></button>
</div>
<div title="Account information" class="info">
	<div class="text">
		Authorizing yourself will enable you to:
		<ul>
			<li>
				<i class="material-symbols-rounded">chevron_right</i>Create both public and secure surveys,
			</li>
			<li>
				<i class="material-symbols-rounded">chevron_right</i>Save surveys as drafts for later
				editing,
			</li>
			<li>
				<i class="material-symbols-rounded">chevron_right</i>View responses and summaries of your
				surveys,
			</li>
			<li>
				<i class="material-symbols-rounded">chevron_right</i>Share surveys' results with others,
			</li>
			<li>
				<i class="material-symbols-rounded">chevron_right</i>Create and manage user groups,
			</li>
			<li>
				<i class="material-symbols-rounded">chevron_right</i>
				Generate digital signature keys that allow you to participate in secure surveys without needing
				to sign in each time.
			</li>
		</ul>
	</div>
</div>
<div title="Account information" class="info">
	<div class="text">
		We do not recommend signing in if you only wish to fill out a survey. For secure surveys, if you
		have already generated your digital signature keys, signing in is also not necessary.
	</div>
</div>

<style>
	ul {
		list-style-type: none;
		margin-top: 0.5em;
		padding-left: 1.5em;
	}

	li {
		display: flex;
		flex-flow: row nowrap;
		justify-content: flex-start;
		align-items: flex-start;
		padding-top: 0.5em;
	}

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
		margin-bottom: 2em;
	}

	.sign-in {
		margin-left: 0.5em;
		margin-right: 0.5em;
	}

	.sign-in {
		font-size: 2em;
	}

	@media screen and (max-width: 767px) {
		h1 {
			font-size: 2em;
		}

		ul {
			padding-left: 0.5em;
		}
	}
</style>
