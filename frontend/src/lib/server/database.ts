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
	const response = await fetch(`${host}/surveys/fetch`, {
		method: 'POST',
		body: JSON.stringify({ survey_code }),
		headers: {
			'Content-Type': 'application/json'
		}
	});

	if (!response.ok) {
		throw error(response.status, response.statusText);
	}

	const survey_info = await response.json();
	return survey_info;
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

export const getSurveysOfUser = async (user_email: string) => {
	const response = await fetch(`${host}/surveys/all`, {
		method: 'POST',
		body: JSON.stringify({ user_email }),
		headers: {
			'Content-Type': 'application/json'
		}
	});
	if (!response.ok) {
		throw error(response.status, response.statusText);
	}

	const surveys = await response.json();
	return surveys;
};

export const getSurveyAnswers = async (user_email: string, survey_code: string) => {
	const response = await fetch(`${host}/answers/fetch`, {
		method: 'POST',
		body: JSON.stringify({ user_email, survey_code }),
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

export const getDraftsOfUser = async (user_email: string) => {
	const response = await fetch(`${host}/survey-drafts/all`, {
		method: 'POST',
		body: JSON.stringify({ user_email }),
		headers: {
			'Content-Type': 'application/json'
		}
	});
	if (!response.ok) {
		throw error(response.status, response.statusText);
	}

	const drafts: Array<{ creator: number; survey_structure: Survey; creation_date: string }> =
		await response.json();
	return drafts;
};

export const registerUser = async (user_email: string) => {
	const response = await fetch(`${host}/users/register`, {
		method: 'POST',
		body: JSON.stringify({ user_email }),
		headers: {
			'Content-Type': 'application/json'
		}
	});
	return response;
};

export const validateUser = async (user_email: string) => {
	const response = await fetch(`${host}/users/validate`, {
		method: 'POST',
		body: JSON.stringify({ user_email }),
		headers: {
			'Content-Type': 'application/json'
		}
	});
	const value = await response.json();
	return value === true;
};

export const updatePublicKey = async (user_email: string, public_key: string) => {
	const response = await fetch(`${host}/users/update-public-key`, {
		method: 'POST',
		body: JSON.stringify({ user_email, public_key }),
		headers: {
			'Content-Type': 'application/json'
		}
	});
	return response;
};

export const userHasPublicKey = async (user_email: string) => {
	const response = await fetch(`${host}/users/has-public-key`, {
		method: 'POST',
		body: JSON.stringify({ user_email }),
		headers: {
			'Content-Type': 'application/json'
		}
	});
	const value = await response.json();
	return value === true;
};

export const getAllUsers = async () => {
	const response = await fetch(`${host}/users/all-with-public-keys`, { method: 'GET' });
	const user_list = await response.json();
	return user_list;
};
