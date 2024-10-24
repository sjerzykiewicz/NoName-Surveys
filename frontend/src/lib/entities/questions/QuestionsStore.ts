import type { ComponentType } from 'svelte';
import { SurveyError } from '$lib/entities/SurveyError';

export default class QuestionsStore {
	component: ComponentType;
	preview: ComponentType;
	required: boolean;
	question: string;
	choices: Array<string>;
	error: SurveyError;
	constructor(
		component: ComponentType,
		preview: ComponentType,
		required: boolean,
		question: string,
		choices: Array<string>,
		error: SurveyError
	) {
		this.component = component;
		this.preview = preview;
		this.required = required;
		this.question = question;
		this.choices = choices;
		this.error = error;
	}
}
