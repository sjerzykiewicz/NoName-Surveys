<script lang="ts">
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import SurveyTitle from '$lib/components/create-page/SurveyTitle.svelte';
	import Questions from '$lib/components/create-page/Questions.svelte';
	import FooterButtons from '$lib/components/create-page/FooterButtons.svelte';
</script>

<Header>
	<SurveyTitle />
</Header>
<Content>
	<Questions />
</Content>
<Footer>
	<FooterButtons />
</Footer>
