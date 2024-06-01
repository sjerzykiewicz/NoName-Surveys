<script lang="ts">
	import type { PageServerData } from './$types';
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';
	import SurveyTable from '$lib/components/surveys-page/SurveyTable.svelte';

	export let data: PageServerData;
</script>

<Header>
	<div class="title">Your surveys</div>
</Header>

<Content>
	<SurveyTable survey_list={data.survey_list} />
</Content>
