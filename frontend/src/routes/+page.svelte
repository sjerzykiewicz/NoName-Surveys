<script lang="ts">
	import WelcomingBanner from '$lib/components/home-page/WelcomingBanner.svelte';
	import SurveyCodeForm from '$lib/components/home-page/SurveyCodeForm.svelte';
	import LoginForm from '$lib/components/home-page/LoginForm.svelte';
	export let form;

	import init, { greet } from 'wasm';
	import { onMount } from 'svelte';

	onMount(async () => {
		await init();
	});
</script>

<WelcomingBanner />
<SurveyCodeForm {form} />
<LoginForm />
<div>
	<button
		on:click={() => {
			greet('Eloi');
		}}>Click Me</button
	>
</div>
