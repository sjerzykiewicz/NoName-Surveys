import type DraftCreateInfo from '$lib/entities/surveys/DraftCreateInfo';
import type { SurveyAnswer } from '$lib/entities/surveys/SurveyAnswer';
import type SurveyCreateInfo from '$lib/entities/surveys/SurveyCreateInfo';
import { env } from '$env/dynamic/private';

let host = 'http://localhost:8000';

if (env.BACKEND_HOST) {
	host = env.BACKEND_HOST;
}

export const createSurvey = (info: SurveyCreateInfo) => {
	return fetch(`${host}/surveys/create`, {
		method: 'POST',
		body: JSON.stringify(info),
		headers: {
			'Content-Type': 'application/json'
		}
	});
};

export const getSurveyByCode = (survey_code: string) => {
	return fetch(`${host}/surveys/fetch`, {
		method: 'POST',
		body: JSON.stringify({ survey_code }),
		headers: {
			'Content-Type': 'application/json'
		}
	});
};

export const deleteSurveyByCode = (user_email: string, survey_code: string) => {
	return fetch(`${host}/surveys/delete`, {
		method: 'POST',
		body: JSON.stringify({ user_email, survey_code }),
		headers: {
			'Content-Type': 'application/json'
		}
	});
};

export const saveAnswer = (answer: SurveyAnswer) => {
	return fetch(`${host}/answers/fill`, {
		method: 'POST',
		body: JSON.stringify(answer),
		headers: {
			'Content-Type': 'application/json'
		}
	});
};

export const getSurveysOfUser = (user_email: string) => {
	return fetch(`${host}/surveys/all`, {
		method: 'POST',
		body: JSON.stringify({ user_email }),
		headers: {
			'Content-Type': 'application/json'
		}
	});
};

export const getSurveyAnswers = (user_email: string, survey_code: string) => {
	return fetch(`${host}/answers/fetch`, {
		method: 'POST',
		body: JSON.stringify({ user_email, survey_code }),
		headers: {
			'Content-Type': 'application/json'
		}
	});
};

export const saveDraft = (info: DraftCreateInfo) => {
	return fetch(`${host}/survey-drafts/create`, {
		method: 'POST',
		body: JSON.stringify(info),
		headers: {
			'Content-Type': 'application/json'
		}
	});
};

export const getDraftsOfUser = (user_email: string) => {
	return fetch(`${host}/survey-drafts/all`, {
		method: 'POST',
		body: JSON.stringify({ user_email }),
		headers: {
			'Content-Type': 'application/json'
		}
	});
};

export const getDraftStructureById = (user_email: string, id: number) => {
	return fetch(`${host}/survey-drafts/fetch`, {
		method: 'POST',
		body: JSON.stringify({ user_email, id }),
		headers: {
			'Content-Type': 'application/json'
		}
	});
};

export const deleteDraftStructureById = (user_email: string, id: number) => {
	return fetch(`${host}/survey-drafts/delete`, {
		method: 'POST',
		body: JSON.stringify({ user_email, id }),
		headers: {
			'Content-Type': 'application/json'
		}
	});
};

export const registerUser = (user_email: string) => {
	return fetch(`${host}/users/register`, {
		method: 'POST',
		body: JSON.stringify({ user_email }),
		headers: {
			'Content-Type': 'application/json'
		}
	});
};

export const validateUser = (user_email: string) => {
	return fetch(`${host}/users/validate`, {
		method: 'POST',
		body: JSON.stringify({ user_email }),
		headers: {
			'Content-Type': 'application/json'
		}
	});
};

export const updatePublicKey = (user_email: string, public_key: string) => {
	return fetch(`${host}/users/update-public-key`, {
		method: 'POST',
		body: JSON.stringify({ user_email, public_key }),
		headers: {
			'Content-Type': 'application/json'
		}
	});
};

export const userHasPublicKey = (user_email: string) => {
	return fetch(`${host}/users/has-public-key`, {
		method: 'POST',
		body: JSON.stringify({ user_email }),
		headers: {
			'Content-Type': 'application/json'
		}
	});
};

export const getAllUsers = () => {
	return fetch(`${host}/users/all-with-public-keys`, { method: 'GET' });
};
