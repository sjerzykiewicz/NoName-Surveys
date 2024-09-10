<script lang="ts">
	import { signOut } from '@auth/sveltekit/client';
</script>

<div class="sign-buttons">
	<button title="Sign out" class="sign-out" on:click={() => signOut()}
		><i class="material-symbols-rounded">logout</i>Sign Out</button
	>
</div>

<style>
	.sign-buttons {
		display: flex;
		flex-flow: row;
		align-items: center;
		justify-content: flex-start;
		padding-top: 1.5em;
		padding-bottom: 1.5em;
		font-size: 1.5em;
	}

	@media screen and (max-width: 767px) {
		.sign-buttons {
			font-size: 1.25em;
		}
	}
</style>
