import { readable, type Readable, writable, type Writable } from 'svelte/store';

// TODO this is for demonstration purposes only, survey will be constructed from JSON
export const title: Readable<string> = readable('Test survey');
export const questions: Readable<
	{
		type: string;
		required: boolean;
		question: string;
		choices: Array<string>;
	}[]
> = readable([
	{
		type: 'single',
		required: true,
		question: 'Single question',
		choices: ['Choice 1', 'Choice 2', 'Choice 3']
	},
	{
		type: 'text',
		required: true,
		question: 'Text question',
		choices: ['Question details']
	},
	{
		type: 'list',
		required: true,
		question: 'List question',
		choices: ['Choice 1', 'Choice 2', 'Choice 3', 'Choice 4']
	},
	{
		type: 'scale',
		required: true,
		question: 'Scale question',
		choices: ['1', '2', '3', '4', '5']
	},
	{
		type: 'multi',
		required: true,
		question: 'Multi question',
		choices: ['Choice 1', 'Choice 2', 'Choice 3', 'Choice 4']
	},
	{
		type: 'slider',
		required: true,
		question: 'Slider question',
		choices: ['1', '10']
	},
	{
		type: 'yesno',
		required: true,
		question: 'Yes/No question',
		choices: ['Yes', 'No']
	},
	{
		type: 'rank',
		required: true,
		question: 'Rank question',
		choices: ['Choice 1', 'Choice 2', 'Choice 3']
	}
]);

export const answers: Writable<
	{
		choices: Array<string>;
	}[]
> = writable([]);
