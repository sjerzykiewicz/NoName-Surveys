<script lang="ts">
	import Header from '$lib/components/global/Header.svelte';
	import Content from '$lib/components/global/Content.svelte';
	import AnswersSummary from '$lib/components/summary-page/AnswersSummary.svelte';
	import Footer from '$lib/components/global/Footer.svelte';
	import type { LayoutData } from './$types';
	import QrCodeModal from '$lib/components/global/QrCodeModal.svelte';
	import FooterButtons from '$lib/components/summary-page/buttons/FooterButtons.svelte';

	export let data: LayoutData;
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
	<AnswersSummary surveyAnswers={data.answers} />
</Content>

<Footer>
	<FooterButtons
		isOwnedByUser={data.survey_list[data.survey_index].is_owned_by_user}
		usesCryptographicModule={data.survey.uses_cryptographic_module}
		bind:isModalHidden
	/>
</Footer>
