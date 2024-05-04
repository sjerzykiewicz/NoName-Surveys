import { writable, type Writable } from 'svelte/store';

export const title: Writable<string> = writable('');
export const questions: Writable<
	{
		type: string;
		required: boolean;
		question: string;
		choices: Array<string>;
	}[]
> = writable([]);

export const answers: Writable<
	{
		choices: Array<string>;
	}[]
> = writable([]);
