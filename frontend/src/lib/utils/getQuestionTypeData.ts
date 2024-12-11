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
import NumberCreate from '$lib/components/create-page/Number.svelte';
import NumberFill from '$lib/components/fill-page/Number.svelte';
import NumberAnswer from '$lib/components/summary-page/answer/Number.svelte';
import NumberSummary from '$lib/components/summary-page/NumberSummary.svelte';

export function getQuestionTypeData(questionType: ComponentType) {
	switch (questionType) {
		case SingleCreate:
		case SingleFill:
		case SingleAnswer:
		case SingleSummary:
			return { title: 'single_title', icon: 'radio_button_checked', text: 'single_text' };
		case MultiCreate:
		case MultiFill:
		case MultiAnswer:
		case MultiSummary:
			return { title: 'multi_title', icon: 'check_box', text: 'multi_text' };
		case ScaleCreate:
		case ScaleFill:
		case ScaleAnswer:
		case ScaleSummary:
			return { title: 'scale_title', icon: 'star', text: 'scale_text' };
		case SliderCreate:
		case SliderFill:
		case SliderAnswer:
		case SliderSummary:
			return { title: 'slider_title', icon: 'switches', text: 'slider_text' };
		case ListCreate:
		case ListFill:
		case ListAnswer:
		case ListSummary:
			return {
				title: 'list_title',
				icon: 'expand_circle_down',
				text: 'list_text'
			};
		case RankCreate:
		case RankFill:
		case RankAnswer:
		case RankSummary:
			return { title: 'rank_title', icon: 'leaderboard', text: 'rank_text' };
		case BinaryCreate:
		case BinaryFill:
		case BinaryAnswer:
		case BinarySummary:
			return { title: 'binary_title', icon: 'thumbs_up_down', text: 'binary_text' };
		case TextCreate:
		case TextFill:
		case TextAnswer:
		case TextSummary:
			return { title: 'text_title', icon: 'text_fields', text: 'text_text' };
		case NumberCreate:
		case NumberFill:
		case NumberAnswer:
		case NumberSummary:
			return { title: 'number_title', icon: 'numbers', text: 'number_text' };
		default:
			return { title: 'subtitle', icon: 'title', text: 'subtitle' };
	}
}
