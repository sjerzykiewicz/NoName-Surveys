<script lang="ts">
	import Single from '$lib/components/Single.svelte';
	import Multi from '$lib/components/Multi.svelte';
	import Scale from '$lib/components/Scale.svelte';
	import Slider from '$lib/components/Slider.svelte';
	import List from '$lib/components/List.svelte';
	import Rank from '$lib/components/Rank.svelte';
	import { beforeUpdate, type ComponentType } from 'svelte';
	import { slide } from 'svelte/transition';
	import { cubicInOut } from 'svelte/easing';
	import { createEventDispatcher } from 'svelte';

	export let previousQuestion: ComponentType;

	let previousQuestionData: { title: string; icon: string; text: string } = {
		title: '',
		icon: '',
		text: ''
	};

	const dispatch = createEventDispatcher();

	function handleClick() {
		dispatch('addPreviousQuestion', { component: previousQuestion });
	}

	beforeUpdate(() => {
		if (previousQuestion === Single) {
			previousQuestionData = {
				title: 'Single choice',
				icon: 'radio_button_checked',
				text: 'Single'
			};
		} else if (previousQuestion === Multi) {
			previousQuestionData = { title: 'Multiple choice', icon: 'check_box', text: 'Multi' };
		} else if (previousQuestion === Scale) {
			previousQuestionData = { title: '1-5 scale', icon: 'star', text: 'Scale' };
		} else if (previousQuestion === Slider) {
			previousQuestionData = { title: 'Slider', icon: 'sliders', text: 'Slider' };
		} else if (previousQuestion === List) {
			previousQuestionData = { title: 'Dropdown menu', icon: 'expand_circle_down', text: 'List' };
		} else if (previousQuestion === Rank) {
			previousQuestionData = { title: 'Ranking choice', icon: 'numbers', text: 'Rank' };
		} else {
			previousQuestionData = { title: 'Open question', icon: 'text_fields', text: 'Text' };
		}
	});
</script>

<button
	title={previousQuestionData.title}
	in:slide={{ axis: 'x', duration: 300, easing: cubicInOut }}
	on:click={handleClick}
	><i class="material-symbols-rounded">{previousQuestionData.icon}</i
	>{previousQuestionData.text}</button
>

<style>
	button {
		display: flex;
		align-items: center;
		background-color: #4a4a4a;
		padding: 0.25em;
		width: auto;
		border: 1px solid #999999;
		border-left: 0px;
		border-radius: 0px 5px 5px 0px;
		font-size: 1.25em;
		font-family: 'Jura';
		color: #eaeaea;
		cursor: pointer;
		transition: background-color 0.3s;
	}

	button:hover {
		background-color: #1a1a1a;
	}

	button:active {
		background-color: #999999;
	}

	i {
		font-size: 1em;
		margin-right: 0.24375em;
		margin-left: 0.08125em;
	}
</style>
