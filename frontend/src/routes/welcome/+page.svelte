<script lang="ts">
	import WelcomingBanner from '$lib/components/WelcomingBanner.svelte';
	import SurveyCodeForm from '$lib/components/SurveyCodeForm.svelte';
	import LoginForm from '$lib/components/LoginForm.svelte';

	export let form;
</script>

<WelcomingBanner />
<SurveyCodeForm {form} />
<LoginForm />
