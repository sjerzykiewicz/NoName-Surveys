import { writable, type Writable } from 'svelte/store';
import { type ComponentType } from 'svelte';
import { QuestionError } from '$lib/entities/QuestionError';
import { getDraft } from '$lib/utils/getDraft';

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

export const useCrypto: Writable<boolean> = writable(false);

export const ringMembers: Writable<Array<string>> = writable([]);

export const selectedGroup: Writable<Array<string>> = writable([]);

export const isDraftPopupVisible: Writable<boolean> = writable(false);

export const currentDraftId: Writable<number | null> = writable(null);

export const draft: Writable<string> = writable(getDraft('', []));
