<script lang="ts">
	import { SurveyError } from '$lib/entities/SurveyError';
	import { title } from '$lib/stores/create-page';
	import { LIMIT_OF_CHARS } from '$lib/stores/global';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';

	function errorMessage() {
		const error = $title.error;
		switch (error) {
			case SurveyError.TitleRequired:
				return 'Please enter survey title.';
			case SurveyError.TitleTooLong:
				return 'Title must be ' + $LIMIT_OF_CHARS + ' or less characters long.';
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
		<p title="Error" class="error" transition:slide={{ duration: 200, easing: cubicInOut }}>
			<i class="material-symbols-rounded">error</i>{errorMessage()}
		</p>
	{/if}
</div>
