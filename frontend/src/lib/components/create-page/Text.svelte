<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import Input from '$lib/components/global/Input.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let questionIndex: number;
</script>

<div class="choice-area text" transition:slide={{ duration: 200, easing: cubicInOut }}>
	<div class="details">
		<Input
			bind:text={$questions[questionIndex].choices[0]}
			label={$t('text_details_label')}
			title={$t('text_details_title')}
			--margin-right="0em"
		/>
	</div>
</div>

<style>
	.details {
		display: flex;
	}
</style>
