<script lang="ts">
	import Modal from '$lib/components/Modal.svelte';
	import { M } from '$lib/stores/global';
	import { onMount } from 'svelte';

	export let isHidden: boolean = true;
	export let title: string;
	export let deleteEntries: () => void;

	let innerWidth: number;

	onMount(() => {
		function handleEnter(event: KeyboardEvent) {
			if (!isHidden && event.key === 'Enter') {
				event.preventDefault();
				deleteEntries();
			}
		}

		document.body.addEventListener('keydown', handleEnter);

		return () => {
			document.body.removeEventListener('keydown', handleEnter);
		};
	});
</script>

<svelte:window bind:innerWidth />

<Modal icon="delete" {title} bind:isHidden width={innerWidth <= $M ? 20 : 22}>
	<span slot="content"
		>Are you sure you want to delete selected entries? You cannot undo this action.</span
	>
	<button
		title="Delete"
		class="save"
		on:click={() => {
			isHidden = true;
			deleteEntries();
		}}
	>
		<i class="material-symbols-rounded">delete</i>Delete
	</button>
	<button title="Cancel" class="not" on:click={() => (isHidden = true)}>
		<i class="material-symbols-rounded">close</i>Cancel
	</button>
</Modal>

<style>
	.not i {
		font-variation-settings: 'wght' 700;
	}
</style>
