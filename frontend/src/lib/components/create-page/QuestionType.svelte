<script lang="ts">
	import Single from '$lib/components/create-page/Single.svelte';
	import Multi from '$lib/components/create-page/Multi.svelte';
	import Scale from '$lib/components/create-page/Scale.svelte';
	import Slider from '$lib/components/create-page/Slider.svelte';
	import List from '$lib/components/create-page/List.svelte';
	import Rank from '$lib/components/create-page/Rank.svelte';
	import Binary from '$lib/components/create-page/Binary.svelte';
	import Text from '$lib/components/create-page/Text.svelte';
	import { beforeUpdate, type ComponentType } from 'svelte';
	import { createEventDispatcher } from 'svelte';
	import { slide } from 'svelte/transition';
	import { cubicInOut } from 'svelte/easing';

	export let questionType: ComponentType;
	export let questionTypeIndex: number;
	export let isQuestionAdded: boolean;

	let questionTypeData: { title: string; icon: string; text: string } = {
		title: '',
		icon: '',
		text: ''
	};

	const dispatch = createEventDispatcher();

	function handleClick() {
		dispatch('addQuestionType', { component: questionType });
	}

	beforeUpdate(() => {
		switch (questionType) {
			case Single:
				questionTypeData = { title: 'Single choice', icon: 'radio_button_checked', text: 'Single' };
				break;
			case Multi:
				questionTypeData = { title: 'Multiple choice', icon: 'check_box', text: 'Multi' };
				break;
			case Scale:
				questionTypeData = { title: '1-5 choice', icon: 'star', text: 'Scale' };
				break;
			case Slider:
				questionTypeData = { title: 'Range of values', icon: 'sliders', text: 'Slider' };
				break;
			case List:
				questionTypeData = {
					title: 'Dropdown menu choice',
					icon: 'expand_circle_down',
					text: 'List'
				};
				break;
			case Rank:
				questionTypeData = { title: 'Ranking choice', icon: 'numbers', text: 'Rank' };
				break;
			case Binary:
				questionTypeData = { title: 'Yes/No choice', icon: 'thumbs_up_down', text: 'Binary' };
				break;
			case Text:
				questionTypeData = { title: 'Open question', icon: 'text_fields', text: 'Text' };
		}
	});
</script>

<button
	title={questionTypeData.title}
	class:previous={questionTypeIndex === -1}
	class:last={questionTypeIndex === 7 || (questionTypeIndex === 6 && isQuestionAdded)}
	in:slide={{ axis: 'x', duration: 200, easing: cubicInOut }}
	on:click={handleClick}
	><i class="material-symbols-rounded">{questionTypeData.icon}</i>{questionTypeData.text}</button
>

<style>
	button {
		flex: 1;
		display: flex;
		align-items: center;
		background-color: var(--primary-color);
		padding: 0.25em;
		width: 6.25em;
		border: 0px;
		border-left: 1px solid var(--border-color);
		border-right: 1px solid var(--border-color);
		font-size: 1.25em;
		font-family: 'Jura';
		color: var(--text-color);
		cursor: pointer;
		transition: background-color 0.2s;
	}

	button:hover {
		background-color: var(--secondary-color);
	}

	button:active {
		background-color: var(--border-color);
	}

	.last {
		border-radius: 0px 0px 5px 5px;
		border-bottom: 1px solid var(--border-color);
	}

	.previous {
		border-radius: 0px 5px 5px 0px;
		border-left: 0px;
		border-top: 1px solid var(--border-color);
		border-bottom: 1px solid var(--border-color);
		width: auto;
	}

	i {
		font-size: 1em;
		margin-right: 0.25em;
		margin-left: 0.1em;
	}

	@media screen and (max-width: 767px) {
		button {
			font-size: 1em;
		}
	}
</style>
