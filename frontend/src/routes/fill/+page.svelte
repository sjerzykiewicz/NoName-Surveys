<script lang="ts">
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';
	import SurveyTitle from '$lib/components/fill-page/SurveyTitle.svelte';
	import SurveyForm from '$lib/components/fill-page/SurveyForm.svelte';
</script>

<Header>
	<SurveyTitle />
</Header>

<Content>
	<SurveyForm />
</Content>
