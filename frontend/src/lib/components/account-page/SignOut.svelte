<script lang="ts">
	import { signOut } from '@auth/sveltekit/client';
</script>

<div class="sign-buttons">
	<button title="Sign Out" class="sign-out" on:click={() => signOut()}
		><i class="material-symbols-rounded">logout</i>Sign Out</button
	>
</div>

<style>
	.sign-buttons {
		display: flex;
		flex-flow: row;
		align-items: center;
		justify-content: center;
	}

	.sign-out {
		margin-left: 0.5em;
		margin-right: 0.5em;
	}

	.sign-out {
		margin-top: 2em;
		font-size: 1.5em;
	}

	@media screen and (max-width: 767px) {
		.sign-out {
			font-size: 2em;
		}
	}
</style>
