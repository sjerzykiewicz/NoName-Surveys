<script lang="ts">
	import Answer from '$lib/components/summary-page/Answer.svelte';
	import type { PageServerData } from './$types';

	export let data: PageServerData;
</script>

<Answer answer={data.answers[data.id]} />
