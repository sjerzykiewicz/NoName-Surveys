import { readable, type Readable } from 'svelte/store';

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
		required: false,
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
		required: false,
		question: 'Scale question',
		choices: ['1', '2', '3', '4', '5']
	},
	{
		type: 'multi',
		required: false,
		question: 'Multi question',
		choices: ['Choice 1', 'Choice 2', 'Choice 3', 'Choice 4']
	},
	{
		type: 'slider',
		required: false,
		question: 'Slider question',
		choices: ['1', '10']
	},
	{
		type: 'yesno',
		required: false,
		question: 'Yes/No question',
		choices: ['Yes', 'No']
	}
]);
