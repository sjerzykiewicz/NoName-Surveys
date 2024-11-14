<script lang="ts">
	import Modal from '$lib/components/global/Modal.svelte';
	import { M } from '$lib/stores/global';
	import { onMount } from 'svelte';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let isHidden: boolean = true;
	export let title: string;
	export let deleteEntries: () => void;

	let innerWidth: number;

	onMount(() => {
		function handleEnter(event: KeyboardEvent) {
			if (!isHidden && event.key === 'Enter') {
				event.preventDefault();
				deleteEntries();
				event.stopImmediatePropagation();
			}
		}

		document.body.addEventListener('keydown', handleEnter);

		return () => {
			document.body.removeEventListener('keydown', handleEnter);
		};
	});
</script>

<svelte:window bind:innerWidth />

<Modal icon="delete" {title} bind:isHidden --width={innerWidth <= $M ? '20em' : '22em'}>
	<span slot="content"><Tx text="info_about_deleting"></Tx></span>
	<button
		title={$t('delete')}
		class="save"
		on:click={() => {
			isHidden = true;
			deleteEntries();
		}}
	>
		<i class="symbol">delete</i><Tx text="delete"></Tx>
	</button>
	<button title={$t('cancel')} class="not" on:click={() => (isHidden = true)}>
		<i class="symbol">close</i><Tx text="cancel"></Tx>
	</button>
</Modal>
