<script lang="ts">
	import SurveyForm from '$lib/components/fill-page/SurveyForm.svelte';
	import type Survey from '$lib/entities/surveys/Survey';
	export let data: Survey;
</script>

<SurveyForm survey={data} />
