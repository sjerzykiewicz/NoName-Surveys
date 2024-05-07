import { writable, type Writable } from 'svelte/store';
import { type ComponentType } from 'svelte';

export const title: Writable<string> = writable('');

export const questions: Writable<
	{
		component: ComponentType;
		required: boolean;
		question: string;
		choices: Array<string>;
	}[]
> = writable([]);

export const questionErrors: Writable<Array<string>> = writable([]);
