<script lang="ts">
	import WelcomingBanner from '$lib/components/home-page/WelcomingBanner.svelte';
	import SurveyCodeForm from '$lib/components/home-page/SurveyCodeForm.svelte';

	export let form;
</script>

<WelcomingBanner />
<SurveyCodeForm {form} />
