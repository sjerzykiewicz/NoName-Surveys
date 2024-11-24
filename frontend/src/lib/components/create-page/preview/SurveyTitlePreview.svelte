<script lang="ts">
	import { title } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';

	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);
</script>

<div
	title={$t('survey_title')}
	class="title"
	transition:slide={{ duration: 200, easing: cubicInOut }}
>
	{$title.title}
</div>
