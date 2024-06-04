<script lang="ts">
	import WelcomingBanner from '$lib/components/home-page/WelcomingBanner.svelte';
	import SurveyCodeForm from '$lib/components/home-page/SurveyCodeForm.svelte';
	import { title, questions, answers } from '$lib/stores/fill-page';

	export let form;

	$title = '';
	$questions = [];
	$answers = [];
</script>

<WelcomingBanner />
<SurveyCodeForm {form} />
