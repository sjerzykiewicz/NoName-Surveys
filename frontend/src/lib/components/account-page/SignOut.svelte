<script lang="ts">
	import { signOut } from '@auth/sveltekit/client';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
</script>

<div class="sign-buttons">
	<button title="Sign out" class="sign-out" on:click={() => signOut()}
		><i class="material-symbols-rounded">logout</i><Tx text="account_sign_out"></Tx></button
	>
</div>

<style>
	.sign-buttons {
		display: flex;
		flex-flow: row;
		align-items: center;
		justify-content: center;
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
