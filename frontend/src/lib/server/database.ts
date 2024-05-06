import type Survey from '$lib/entities/surveys/Survey';
import type { SurveyAnswer } from '$lib/entities/surveys/SurveyAnswer';
import type SurveyCreateInfo from '$lib/entities/surveys/SurveyCreateInfo';
import { error } from '@sveltejs/kit';

const host = 'http://localhost:8000';

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
