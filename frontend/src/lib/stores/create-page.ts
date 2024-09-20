import { writable, type Writable } from 'svelte/store';
import { type ComponentType } from 'svelte';
import { QuestionError } from '$lib/entities/QuestionError';
import { Access } from '$lib/entities/Access';

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

export const previousQuestion: Writable<ComponentType | null> = writable(null);

export const access: Writable<Access> = writable(Access.Public);

export const ringMembers: Writable<Array<string>> = writable([]);

export const selectedGroup: Writable<Array<string>> = writable([]);
