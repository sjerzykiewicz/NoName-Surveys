<script lang="ts">
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import SurveyTitle from '$lib/components/create-page/SurveyTitle.svelte';
	import SurveyTitlePreview from '$lib/components/create-page/preview/SurveyTitlePreview.svelte';
	import TitleError from '$lib/components/create-page/TitleError.svelte';
	import SurveyForm from '$lib/components/create-page/SurveyForm.svelte';
	import FooterButtons from '$lib/components/create-page/FooterButtons.svelte';
	import type { PageServerData } from './$types';

	export let titleError: boolean;
	export let cryptoError: boolean;
	export let isPreview: boolean;
	export let data: PageServerData;
</script>

<Header>
	{#if isPreview}
		<SurveyTitlePreview />
	{:else}
		<SurveyTitle />
		<TitleError {titleError} />
	{/if}
</Header>
<Content>
	<SurveyForm {cryptoError} {isPreview} groups={data.group_list} users={data.user_list} />
</Content>
<Footer>
	<FooterButtons bind:titleError bind:cryptoError bind:isPreview />
</Footer>
