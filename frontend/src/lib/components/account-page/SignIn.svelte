<script lang="ts">
	import { signIn } from '@auth/sveltekit/client';
</script>

<h1>Sign in with:</h1>
<div class="sign-buttons">
	<button title="Google" class="sign-in" on:click={() => signIn('google')}
		><i class="fa-brands fa-google"></i></button
	>
	<button title="Microsoft" class="sign-in" on:click={() => signIn('usos')}
		><i class="fa-brands fa-microsoft"></i></button
	>
	<button title="GitHub" class="sign-in" on:click={() => signIn('github')}
		><i class="fa-brands fa-github"></i></button
	>
</div>
<div title="Account information" class="info">
	<div class="text">
		Authorizing yourself will enable you to:
		<ul>
			<li>Create your own surveys,</li>
			<li>Save survey drafts,</li>
			<li>View your survey's results,</li>
			<li>
				Generate digital signature keys that allow you to participate in secure surveys without
				needing to sign in each time.
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

	.info {
		font-size: 1.25em;
	}

	@media screen and (max-width: 767px) {
		h1 {
			font-size: 2em;
		}

		.info {
			font-size: 1em;
			margin-left: 0em;
			margin-right: 0em;
		}
	}
</style>
