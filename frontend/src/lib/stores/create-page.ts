import { writable, type Writable } from 'svelte/store';
import { type ComponentType } from 'svelte';
import { SurveyError } from '$lib/entities/SurveyError';
import { getDraft } from '$lib/utils/getDraft';

export const title: Writable<{
	title: string;
	error: SurveyError;
}> = writable({ title: '', error: SurveyError.NoError });

export const questions: Writable<
	{
		component: ComponentType;
		preview: ComponentType;
		required: boolean;
		question: string;
		choices: Array<string>;
		error: SurveyError;
	}[]
> = writable([]);

export const previousQuestion: Writable<ComponentType | null> = writable(null);

export const useCrypto: Writable<boolean> = writable(false);

export const ringMembers: Writable<Array<string>> = writable([]);

export const selectedGroup: Writable<Array<string>> = writable([]);

export const currentDraftId: Writable<number | null> = writable(null);

export const draftStructure: Writable<string> = writable(getDraft('', []));
