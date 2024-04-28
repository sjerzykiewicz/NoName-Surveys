<script lang="ts">
	import { questions } from '$lib/components/fill-page/stores';
	import type { ComponentType } from 'svelte';
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';
	import SurveyTitle from '$lib/components/fill-page/SurveyTitle.svelte';
	import Single from '$lib/components/fill-page/Single.svelte';
	import Text from '$lib/components/fill-page/Text.svelte';
	import List from '$lib/components/fill-page/List.svelte';
	import Scale from '$lib/components/fill-page/Scale.svelte';
	import QuestionTitle from '$lib/components/fill-page/QuestionTitle.svelte';
	import Multi from '$lib/components/fill-page/Multi.svelte';
	import Slider from '$lib/components/fill-page/Slider.svelte';
	import YesNo from '$lib/components/fill-page/YesNo.svelte';
	import Footer from '$lib/components/Footer.svelte';

	const componentTypeMap: { [id: string]: ComponentType } = {
		text: Text,
		single: Single,
		multi: Multi,
		scale: Scale,
		yesno: YesNo,
		slider: Slider,
		list: List
	};
</script>

<form method="POST">
	<Header>
		<SurveyTitle />
	</Header>
	<Content>
		{#each $questions as question, questionIndex}
			<div class="question">
				<QuestionTitle {questionIndex} />
				<svelte:component this={componentTypeMap[question.type]} {questionIndex} />
			</div>
		{/each}
	</Content>
	<Footer>
		<button class="footer-button back" disabled>
			<!-- TODO insert icon -->
			<i class="material-symbols-rounded"></i>Back
		</button>
		<button class="footer-button submit" type="submit">
			<!-- TODO insert icon -->
			<i class="material-symbols-rounded"></i>Submit
		</button>
	</Footer>
</form>

<style>
	.question {
		margin-bottom: 1.875em;
	}
	.footer-button {
		display: flex;
		text-decoration: none;
		background-color: #4a4a4a;
		padding: 0.25em;
		border: 1px solid #999999;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		font-size: 1.25em;
		font-family: 'Jura';
		color: #eaeaea;
		cursor: pointer;
		transition: background-color 0.2s;
		margin-left: 0.5em;
	}

	.footer-button:hover {
		background-color: #1a1a1a;
	}

	.footer-button:active,
	.submit:active {
		background-color: #999999;
	}

	.submit {
		background-color: #0075ff;
	}

	.submit:hover {
		background-color: #001c53;
	}

	i {
		font-size: 1.15em;
		margin-right: 0.15em;
	}

	@media screen and (max-width: 767px) {
		.footer-button {
			font-size: 1em;
		}
	}
</style>
