<script lang="ts">
	import WelcomingBanner from '$lib/components/home-page/WelcomingBanner.svelte';
	import SurveyCodeForm from '$lib/components/home-page/SurveyCodeForm.svelte';
	import LoginForm from '$lib/components/home-page/LoginForm.svelte';

	export let form;
</script>

<WelcomingBanner />
<SurveyCodeForm {form} />
<LoginForm />
