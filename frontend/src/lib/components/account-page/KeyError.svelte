<script lang="ts">
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';

	export let isKeyValid: boolean;

	function errorMessage() {
		if (isKeyValid) {
			return 'Key uploaded successfully.';
		}
		return 'Please select a valid public key.';
	}
</script>

<div
	in:slide={{ delay: 200, duration: 200, easing: cubicInOut }}
	out:slide={{ duration: 200, easing: cubicInOut }}
>
	{#if !isKeyValid}
		<p title="Error" class="error" transition:slide={{ duration: 200, easing: cubicInOut }}>
			<i class="material-symbols-rounded">error</i>{errorMessage()}
		</p>
	{:else}
		<p
			title="Success"
			class="error success"
			transition:slide={{ duration: 200, easing: cubicInOut }}
		>
			<i class="material-symbols-rounded">verified</i>{errorMessage()}
		</p>
	{/if}
</div>

<style>
	.error {
		justify-content: center;
		font-size: 0.8em;
	}

	.success {
		color: var(--accent-color);
	}
</style>
