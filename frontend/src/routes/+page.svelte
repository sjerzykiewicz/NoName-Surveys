<script lang="ts">
	import WelcomingBanner from '$lib/components/home-page/WelcomingBanner.svelte';
	import SurveyCodeForm from '$lib/components/home-page/SurveyCodeForm.svelte';
	import { title, questions, answers } from '$lib/stores/fill-page';

	export let form;

	$title = '';
	$questions = [];
	$answers = [];

	import init, { get_keypair } from 'wasm';
	import { onMount } from 'svelte';

	onMount(async () => {
		await init();
	});
</script>

<WelcomingBanner />
<SurveyCodeForm {form} />

<div>
	<button
		on:click={() => {
			let keypair = get_keypair();
			console.log(keypair.get_public_key());
			console.log(keypair.get_private_key());
		}}>Click Me</button
	>
</div>
