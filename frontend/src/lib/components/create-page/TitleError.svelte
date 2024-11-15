<script lang="ts">
	import { SurveyError } from '$lib/entities/SurveyError';
	import { title } from '$lib/stores/create-page';
	import { LIMIT_OF_CHARS } from '$lib/stores/global';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	function errorMessage() {
		const error = $title.error;
		switch (error) {
			case SurveyError.TitleRequired:
				return $t('survey_title_error_required');
			case SurveyError.TitleTooLong:
				return $t('survey_title_error_limit', { limit: $LIMIT_OF_CHARS });
		}
	}

	$: checkTitleError = () => {
		const t = $title.title;
		const error = $title.error;
		switch (error) {
			case SurveyError.TitleRequired:
				return t === null || t === undefined || t.trim().length === 0;
			case SurveyError.TitleTooLong:
				return t.length > $LIMIT_OF_CHARS;
		}
	};
</script>

<div transition:slide={{ duration: 200, easing: cubicInOut }}>
	{#if checkTitleError()}
		<p title={$t('error')} class="error" transition:slide={{ duration: 200, easing: cubicInOut }}>
			<i class="symbol">error</i>
			{#key $t}
				{errorMessage()}
			{/key}
		</p>
	{/if}
</div>
