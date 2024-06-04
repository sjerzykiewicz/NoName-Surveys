import { writable, type Writable } from 'svelte/store';
import { type ComponentType } from 'svelte';
import { QuestionError } from '$lib/entities/QuestionError';

export const title: Writable<string> = writable('');

export const questions: Writable<
	{
		component: ComponentType;
		preview: ComponentType;
		required: boolean;
		question: string;
		choices: Array<string>;
		error: QuestionError;
	}[]
> = writable([]);

export const previousQuestion: Writable<ComponentType | null> = writable();

export const isAccessLimited: Writable<boolean> = writable(false);

export const ringMembers: Writable<Array<string>> = writable([]);
