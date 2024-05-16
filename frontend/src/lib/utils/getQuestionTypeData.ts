import type { ComponentType } from 'svelte';
import Single from '$lib/components/create-page/Single.svelte';
import Multi from '$lib/components/create-page/Multi.svelte';
import Scale from '$lib/components/create-page/Scale.svelte';
import Slider from '$lib/components/create-page/Slider.svelte';
import List from '$lib/components/create-page/List.svelte';
import Rank from '$lib/components/create-page/Rank.svelte';
import Binary from '$lib/components/create-page/Binary.svelte';
import Text from '$lib/components/create-page/Text.svelte';

export function getQuestionTypeData(questionType: ComponentType) {
	switch (questionType) {
		case Single:
			return { title: 'Single choice', icon: 'radio_button_checked', text: 'Single' };
		case Multi:
			return { title: 'Multiple choice', icon: 'check_box', text: 'Multi' };
		case Scale:
			return { title: '1-5 choice', icon: 'star', text: 'Scale' };
		case Slider:
			return { title: 'Range of values', icon: 'sliders', text: 'Slider' };
		case List:
			return {
				title: 'Dropdown menu choice',
				icon: 'expand_circle_down',
				text: 'List'
			};
		case Rank:
			return { title: 'Ranking choice', icon: 'numbers', text: 'Rank' };
		case Binary:
			return { title: 'Yes/No choice', icon: 'thumbs_up_down', text: 'Binary' };
		case Text:
			return { title: 'Open question', icon: 'text_fields', text: 'Text' };
		default:
			return { title: '', icon: '', text: '' };
	}
}
