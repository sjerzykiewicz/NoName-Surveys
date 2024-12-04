<script lang="ts">
	import Modal from '$lib/components/global/Modal.svelte';
	import { M } from '$lib/stores/global';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let isHidden: boolean = true;
	export let title: string;
	export let deleteEntries: () => Promise<void>;

	let innerWidth: number;
	let isButtonDisabled: boolean = false;

	async function handleEnter(event: KeyboardEvent) {
		if (!isHidden && !isButtonDisabled && event.key === 'Enter') {
			event.preventDefault();
			event.stopImmediatePropagation();
			isButtonDisabled = true;
			await deleteEntries();
			isButtonDisabled = false;
		}
	}
</script>

<svelte:window bind:innerWidth />
<svelte:body on:keydown={handleEnter} />

<Modal icon="delete" {title} bind:isHidden --width={innerWidth <= $M ? '20em' : '22em'}>
	<span slot="content"><Tx text="info_about_deleting" /></span>
	<button
		title={$t('delete')}
		class="save"
		disabled={isButtonDisabled}
		on:click={async () => {
			isHidden = true;
			isButtonDisabled = true;
			await deleteEntries();
			isButtonDisabled = false;
		}}
	>
		<i class="symbol">delete</i><Tx text="delete" />
	</button>
	<button title={$t('cancel')} class="not" on:click={() => (isHidden = true)}>
		<i class="symbol">close</i><Tx text="cancel" />
	</button>
</Modal>
