import Single from '$lib/components/summary-page/Single.svelte';
import Text from '$lib/components/summary-page/Text.svelte';
import List from '$lib/components/summary-page/List.svelte';
import Scale from '$lib/components/summary-page/Scale.svelte';
import Multi from '$lib/components/summary-page/Multi.svelte';
import Slider from '$lib/components/summary-page/Slider.svelte';
import Binary from '$lib/components/summary-page/Binary.svelte';
import Rank from '$lib/components/summary-page/Rank.svelte';
import type { ComponentType } from 'svelte';

export const componentTypeMap: { [id: string]: ComponentType } = {
	text: Text,
	single: Single,
	multi: Multi,
	scale: Scale,
	binary: Binary,
	slider: Slider,
	rank: Rank,
	list: List
};
