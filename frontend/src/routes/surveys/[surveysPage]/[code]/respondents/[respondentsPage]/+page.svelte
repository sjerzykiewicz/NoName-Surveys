<script lang="ts">
	import Header from '$lib/components/global/Header.svelte';
	import Content from '$lib/components/global/Content.svelte';
	import Footer from '$lib/components/global/Footer.svelte';
	import QrCodeModal from '$lib/components/global/QrCodeModal.svelte';
	import RespondentsTable from '$lib/components/summary-page/respondents/RespondentsTable.svelte';
	import FooterButtons from '$lib/components/summary-page/buttons/FooterButtons.svelte';
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';

	export let data;
	export let isModalHidden: boolean = true;
</script>

<QrCodeModal
	bind:isHidden={isModalHidden}
	title="Access Code"
	surveyCode={data.survey.survey_code}
/>

<Header>
	<div title="Survey title" class="title">{data.survey.title}</div>
</Header>

<Content>
	<RespondentsTable respondents={data.respondents} numRespondents={data.numRespondents} />
</Content>

<Footer>
	<FooterButtons
		isOwnedByUser={data.surveys[data.survey_index].is_owned_by_user}
		usesCryptographicModule={data.survey.uses_cryptographic_module}
		goBack={() => goto('/surveys/' + $page.params.surveysPage)}
		bind:isModalHidden
	/>
</Footer>
