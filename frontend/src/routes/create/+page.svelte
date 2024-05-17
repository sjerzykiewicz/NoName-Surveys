<script lang="ts">
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import SurveyTitle from '$lib/components/create-page/SurveyTitle.svelte';
	import Survey from '$lib/components/create-page/Survey.svelte';
	import FooterButtons from '$lib/components/create-page/FooterButtons.svelte';

	export let titleError: boolean;
</script>

<Header>
	<SurveyTitle {titleError} />
</Header>
<Content>
	<Survey />
</Content>
<Footer>
	<FooterButtons bind:titleError />
</Footer>
