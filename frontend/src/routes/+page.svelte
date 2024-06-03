<script lang="ts">
	import WelcomingBanner from '$lib/components/home-page/WelcomingBanner.svelte';
	import SurveyCodeForm from '$lib/components/home-page/SurveyCodeForm.svelte';
	// import { page } from '$app/stores';
	// import { onMount } from 'svelte';
	// import { goto } from '$app/navigation';
	// import { redirectedOnce } from '$lib/stores/add-key-account-redirect';

	export let form;

	// onMount(() => {
	// 	if (!$redirectedOnce) {
	// 		if ($page.data.session) {
	// 			const email = $page.data.session.user?.email;
	// 			if (email) {
	// 				fetch('/api/users/validate', {
	// 					method: 'POST',
	// 					body: JSON.stringify({ email: email }),
	// 					headers: {
	// 						'Content-Type': 'application/json'
	// 					}
	// 				}).then((res) => {
	// 					res.json().then((hasKey) => {
	// 						if (!hasKey) {
	// 							$redirectedOnce = true;
	// 							goto('/account');
	// 						}
	// 					});
	// 				});
	// 			}
	// 		}
	// 	}
	// });
</script>

<WelcomingBanner />
<SurveyCodeForm {form} />
