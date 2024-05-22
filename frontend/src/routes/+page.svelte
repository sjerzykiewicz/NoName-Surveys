<script lang="ts">
	import WelcomingBanner from '$lib/components/home-page/WelcomingBanner.svelte';
	import SurveyCodeForm from '$lib/components/home-page/SurveyCodeForm.svelte';
	import LoginForm from '$lib/components/home-page/LoginForm.svelte';
	import { page } from '$app/stores';

	export let form;
</script>

<WelcomingBanner />
<SurveyCodeForm {form} />
<LoginForm />

{#if $page.data.session}
	<h1>
		Welcome, {$page.data.session.user?.email}!
	</h1>
{:else}
	<h1>Welcome, stranger!</h1>
{/if}
