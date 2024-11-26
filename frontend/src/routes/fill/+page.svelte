<script lang="ts">
	import SurveyForm from '$lib/components/fill-page/SurveyForm.svelte';
	import init from 'wasm';
	import { onMount } from 'svelte';
	import { title, questions, answers } from '$lib/stores/fill-page';
	import { signOut } from '$lib/utils/signOut.js';
	import { page } from '$app/stores';
	import Modal from '$lib/components/global/Modal.svelte';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let data;

	let isModalHidden: boolean;

	$title = '';
	$questions = [];
	$answers = [];

	onMount(async () => {
		await init();
		if ($page.data.session) {
			isModalHidden = false;
		}
	});
</script>

<Modal
	icon="logout"
	title={$t('sign_out')}
	bind:isHidden={isModalHidden}
	hide={async () => {
		await signOut();
		isModalHidden = true;
	}}
>
	<span slot="content"><Tx text="sign_out_alert" /></span>
	<button
		title={$t('sign_out')}
		class="save"
		on:click={async () => {
			await signOut();
			isModalHidden = true;
		}}><i class="symbol">logout</i><Tx text="sign_out" /></button
	>
</Modal>

<SurveyForm
	survey_title={data.survey.title}
	survey={data.survey.survey_structure}
	code={data.survey.survey_code}
	uses_crypto={data.survey.uses_cryptographic_module}
	keys={data.survey.public_keys}
/>
