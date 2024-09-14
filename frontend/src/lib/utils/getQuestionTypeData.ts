import type { ComponentType } from 'svelte';
import SingleCreate from '$lib/components/create-page/Single.svelte';
import SingleFill from '$lib/components/fill-page/Single.svelte';
import SingleAnswer from '$lib/components/summary-page/answer/Single.svelte';
import SingleSummary from '$lib/components/summary-page/SingleSummary.svelte';
import MultiCreate from '$lib/components/create-page/Multi.svelte';
import MultiFill from '$lib/components/fill-page/Multi.svelte';
import MultiAnswer from '$lib/components/summary-page/answer/Multi.svelte';
import MultiSummary from '$lib/components/summary-page/MultiSummary.svelte';
import ScaleCreate from '$lib/components/create-page/Scale.svelte';
import ScaleFill from '$lib/components/fill-page/Scale.svelte';
import ScaleAnswer from '$lib/components/summary-page/answer/Scale.svelte';
import ScaleSummary from '$lib/components/summary-page/ScaleSummary.svelte';
import SliderCreate from '$lib/components/create-page/Slider.svelte';
import SliderFill from '$lib/components/fill-page/Slider.svelte';
import SliderAnswer from '$lib/components/summary-page/answer/Slider.svelte';
import SliderSummary from '$lib/components/summary-page/SliderSummary.svelte';
import ListCreate from '$lib/components/create-page/List.svelte';
import ListFill from '$lib/components/fill-page/List.svelte';
import ListAnswer from '$lib/components/summary-page/answer/List.svelte';
import ListSummary from '$lib/components/summary-page/ListSummary.svelte';
import RankCreate from '$lib/components/create-page/Rank.svelte';
import RankFill from '$lib/components/fill-page/Rank.svelte';
import RankAnswer from '$lib/components/summary-page/answer/Rank.svelte';
import RankSummary from '$lib/components/summary-page/RankSummary.svelte';
import BinaryCreate from '$lib/components/create-page/Binary.svelte';
import BinaryFill from '$lib/components/fill-page/Binary.svelte';
import BinaryAnswer from '$lib/components/summary-page/answer/Binary.svelte';
import BinarySummary from '$lib/components/summary-page/BinarySummary.svelte';
import TextCreate from '$lib/components/create-page/Text.svelte';
import TextFill from '$lib/components/fill-page/Text.svelte';
import TextAnswer from '$lib/components/summary-page/answer/Text.svelte';
import TextSummary from '$lib/components/summary-page/TextSummary.svelte';

export function getQuestionTypeData(questionType: ComponentType) {
	switch (questionType) {
		case SingleCreate:
		case SingleFill:
		case SingleAnswer:
		case SingleSummary:
			return { title: 'Single choice', icon: 'radio_button_checked', text: 'Single' };
		case MultiCreate:
		case MultiFill:
		case MultiAnswer:
		case MultiSummary:
			return { title: 'Multiple choice', icon: 'check_box', text: 'Multi' };
		case ScaleCreate:
		case ScaleFill:
		case ScaleAnswer:
		case ScaleSummary:
			return { title: '1-5 choice', icon: 'star', text: 'Scale' };
		case SliderCreate:
		case SliderFill:
		case SliderAnswer:
		case SliderSummary:
			return { title: 'Range of values', icon: 'sliders', text: 'Slider' };
		case ListCreate:
		case ListFill:
		case ListAnswer:
		case ListSummary:
			return {
				title: 'Dropdown menu choice',
				icon: 'expand_circle_down',
				text: 'List'
			};
		case RankCreate:
		case RankFill:
		case RankAnswer:
		case RankSummary:
			return { title: 'Ranking choice', icon: 'numbers', text: 'Rank' };
		case BinaryCreate:
		case BinaryFill:
		case BinaryAnswer:
		case BinarySummary:
			return { title: 'Yes/No choice', icon: 'thumbs_up_down', text: 'Binary' };
		case TextCreate:
		case TextFill:
		case TextAnswer:
		case TextSummary:
			return { title: 'Open question', icon: 'text_fields', text: 'Text' };
		default:
			return { title: '', icon: '', text: '' };
	}
}
