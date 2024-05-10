import { writable, type Writable } from 'svelte/store';
import { type ComponentType } from 'svelte';
import { QuestionError } from '$lib/entities/QuestionError';

export const title: Writable<string> = writable('');

export const questions: Writable<
	{
		component: ComponentType;
		required: boolean;
		question: string;
		choices: Array<string>;
		error: QuestionError;
	}[]
> = writable([]);
