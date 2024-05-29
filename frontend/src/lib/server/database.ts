import type DraftCreateInfo from '$lib/entities/surveys/DraftCreateInfo';
import type Survey from '$lib/entities/surveys/Survey';
import type { SurveyAnswer } from '$lib/entities/surveys/SurveyAnswer';
import type SurveyCreateInfo from '$lib/entities/surveys/SurveyCreateInfo';
import { error } from '@sveltejs/kit';
import { env } from '$env/dynamic/private';

let host = 'http://localhost:8000';

if (env.BACKEND_HOST) {
	host = env.BACKEND_HOST;
}

export const createSurvey = async (info: SurveyCreateInfo) => {
	const response = await fetch(`${host}/surveys/create`, {
		method: 'POST',
		body: JSON.stringify(info),
		headers: {
			'Content-Type': 'application/json'
		}
	});

	if (!response.ok) {
		throw error(response.status, response.statusText);
	}

	const code = (await response.json()).survey_code;
	return { code };
};

export const getSurveyByCode = async (survey_code: string) => {
	const response = await fetch(`${host}/surveys`, {
		method: 'POST',
		body: JSON.stringify({ survey_code }),
		headers: {
			'Content-Type': 'application/json'
		}
	});

	if (!response.ok) {
		throw error(response.status, response.statusText);
	}

	const survey_structure: Survey = (await response.json()).survey_structure;
	return { survey_structure };
};

export const saveAnswer = async (answer: SurveyAnswer) => {
	const response = await fetch(`${host}/answers/fill`, {
		method: 'POST',
		body: JSON.stringify(answer),
		headers: {
			'Content-Type': 'application/json'
		}
	});

	if (!response.ok) {
		throw error(response.status, response.statusText);
	}

	return (await response.json()).message;
};

export const getSurveysOfUser = async (id: number) => {
	const response = await fetch(`${host}/surveys/all/${id}`, { method: 'GET' });
	if (!response.ok) {
		throw error(response.status, response.statusText);
	}

	const surveys = await response.json();
	const entry_list: Array<{ title: string; uses_crypto: boolean; code: string }> = [];
	for (let i = 0; i < surveys.length; i++) {
		const { survey_structure } = await getSurveyByCode(surveys[i].survey_code);
		const entry = {
			title: survey_structure.title,
			uses_crypto: surveys[i].uses_cryptographic_module,
			code: surveys[i].survey_code
		};
		entry_list[i] = entry;
	}

	return entry_list;
};

export const getSurveyAnswers = async (survey_code: string) => {
	const response = await fetch(`${host}/answers/fetch`, {
		method: 'POST',
		body: JSON.stringify({ survey_code }),
		headers: {
			'Content-Type': 'application/json'
		}
	});
	if (!response.ok) {
		throw error(response.status, response.statusText);
	}

	return await response.json();
};

export const saveDraft = async (info: DraftCreateInfo) => {
	const response = await fetch(`${host}/survey-drafts/create`, {
		method: 'POST',
		body: JSON.stringify(info),
		headers: {
			'Content-Type': 'application/json'
		}
	});
	if (!response.ok) {
		throw error(response.status, response.statusText);
	}
	return response.ok;
};

export const getDraftsOfUser = async (id: number) => {
	const response = await fetch(`${host}/survey-drafts/all/${id}`, { method: 'GET' });
	if (!response.ok) {
		throw error(response.status, response.statusText);
	}

	const drafts = await response.json();
	return { drafts };
};
