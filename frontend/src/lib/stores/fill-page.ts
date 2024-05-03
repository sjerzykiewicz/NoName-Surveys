import { writable, type Writable } from 'svelte/store';

// TODO this is for demonstration purposes only, survey will be constructed from JSON
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
