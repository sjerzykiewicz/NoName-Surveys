<script lang="ts">
	import type { PageServerData } from './$types';
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';
	import SurveysTable from '$lib/components/surveys-page/SurveysTable.svelte';

	export let data: PageServerData;
</script>

<Header>
	<div class="title">Your surveys</div>
</Header>

<Content>
	<SurveysTable survey_list={data.survey_list} />
</Content>
