<script lang="ts">
	import SurveyForm from '$lib/components/fill-page/SurveyForm.svelte';
	import type { PageServerData } from './$types';
	import init from 'wasm';
	import { onMount } from 'svelte';

	export let data: PageServerData;

	onMount(async () => {
		await init();
	});
</script>

<SurveyForm
	survey={data.survey_structure}
	uses_crypto={data.uses_cryptographic_module}
	keys={data.public_keys}
	code={data.survey_code}
/>
