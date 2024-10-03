import type { ComponentType } from 'svelte';
import { QuestionError } from '$lib/entities/QuestionError';

export default class QuestionsStore {
	component: ComponentType;
	preview: ComponentType;
	required: boolean;
	question: string;
	choices: Array<string>;
	error: QuestionError;
	constructor(
		component: ComponentType,
		preview: ComponentType,
		required: boolean,
		question: string,
		choices: Array<string>,
		error: QuestionError
	) {
		this.component = component;
		this.preview = preview;
		this.required = required;
		this.question = question;
		this.choices = choices;
		this.error = error;
	}
}
