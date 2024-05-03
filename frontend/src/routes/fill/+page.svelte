<script lang="ts">
	import SurveyForm from '$lib/components/fill-page/SurveyForm.svelte';
	import type Question from '$lib/entities/questions/Question';
	export let data: {
		title: string;
		questions: Array<Question>;
	};
</script>

<SurveyForm survey={data} />
