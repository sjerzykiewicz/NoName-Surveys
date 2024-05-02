import { readable, type Readable, writable, type Writable } from 'svelte/store';

// TODO this is for demonstration purposes only, survey will be constructed from JSON
export const title: Readable<string> = readable('NoName Anonymous Surveys - Ankieta Testowa');
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
		question: 'Która strona podoba ci się najbardziej w NoName Anonymous Surveys?',
		choices: ['Home Page', 'Create Page', 'Fill Page']
	},
	{
		type: 'text',
		required: false,
		question: 'Uzasadnij swój wybór.',
		choices: ['Czemu wybrałeś akurat tę stronę? Podziel się swoją opinią.']
	},
	{
		type: 'list',
		required: true,
		question: 'Z jakiego wydziału jesteś?',
		choices: [
			'Wydział Matematyki i Informatyki',
			'Wydział Biologii',
			'Wydział Fizyki',
			'Wydział Chemii',
			'Wydział Historii',
			'Wydział Nauk Geograficznych i Geologicznych',
			'Inny'
		]
	},
	{
		type: 'scale',
		required: true,
		question: 'W skali od 1 do 5, jak bardzo podoba ci się NoName Anonymous Surveys?',
		choices: ['1', '2', '3', '4', '5']
	},
	{
		type: 'multi',
		required: false,
		question: 'Wybierz wszystkie stwierdzenia, z którymi się zgadzasz.',
		choices: [
			'Zespół NoName ma essę',
			'Członkowie zespołu NoName to same sigmy',
			'Nie mam ochoty wypełniać tej ankiety',
			'Ufam, że ankieta jest w pełni anonimowa'
		]
	},
	{
		type: 'slider',
		required: true,
		question: 'Ile masz lat?',
		choices: ['15', '80']
	},
	{
		type: 'yesno',
		required: true,
		question: 'Czy jesteś zainteresowany dalszą współpracą z naszym zespołem?',
		choices: ['Tak', 'Nie']
	},
	{
		type: 'rank',
		required: true,
		question: 'Ułóż poniższe przedmioty od najlepszego do najgorszego.',
		choices: ['Kompresja Danych', 'Szeregowanie Zadań', 'Programowanie Funkcyjne']
	}
]);

export const answers: Writable<
	{
		choices: Array<string>;
	}[]
> = writable([]);
