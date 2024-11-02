<script lang="ts">
	import SurveyForm from '$lib/components/fill-page/SurveyForm.svelte';
	import type { PageServerData } from './$types';
	import init from 'wasm';
	import { onMount } from 'svelte';
	import { title, questions, answers } from '$lib/stores/fill-page';

	export let data: PageServerData;

	$title = '';
	$questions = [];
	$answers = [];

	onMount(async () => {
		await init();
	});
</script>

<SurveyForm
	survey_title={data.survey.title}
	survey={data.survey.survey_structure}
	code={data.survey.survey_code}
	uses_crypto={data.survey.uses_cryptographic_module}
	keys={data.survey.public_keys}
/>
