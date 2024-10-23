<script lang="ts">
	import Modal from '$lib/components/Modal.svelte';
	import { errorModalContent, isErrorModalHidden } from '$lib/stores/global';
</script>

<Modal
	icon="error"
	title="Error"
	textColor="var(--error-color)"
	borderColor="var(--error-color)"
	bind:isHidden={$isErrorModalHidden}
>
	<div slot="content" class="content">{$errorModalContent}</div>
	<button title="Ok" class="save" on:click={() => ($isErrorModalHidden = true)}
		><i class="material-symbols-rounded">done</i>OK</button
	>
</Modal>
