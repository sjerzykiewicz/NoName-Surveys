import { writable, type Writable } from 'svelte/store';
import { type ComponentType } from 'svelte';

export const title: Writable<string> = writable('');
export const questions: Writable<
	{
		component: ComponentType;
		question: string;
		choices: Array<string>;
	}[]
> = writable([]);
