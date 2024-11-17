import type DraftCreateInfo from '$lib/entities/surveys/DraftCreateInfo';
import type SurveyAnswer from '$lib/entities/surveys/SurveyAnswer';
import type SurveyCreateInfo from '$lib/entities/surveys/SurveyCreateInfo';
import { env } from '$env/dynamic/private';

let host = 'http://localhost:8000';

if (env.BACKEND_HOST) {
	host = env.BACKEND_HOST;
}

// answers

export const getSurveyAnswers = (user_email: string, survey_code: string) => {
	return fetch(`${host}/answers/fetch`, {
		method: 'POST',
		body: JSON.stringify({ user_email, survey_code }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const saveSurveyAnswer = (answer: SurveyAnswer) => {
	return fetch(`${host}/answers/fill`, {
		method: 'POST',
		body: JSON.stringify(answer),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

// survey drafts

export const getSurveyDrafts = (user_email: string, page: number) => {
	return fetch(`${host}/survey-drafts/all/${page}`, {
		method: 'POST',
		body: JSON.stringify({ user_email }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const getSurveyDraft = (user_email: string, id: number) => {
	return fetch(`${host}/survey-drafts/fetch`, {
		method: 'POST',
		body: JSON.stringify({ user_email, id }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const deleteSurveyDrafts = (user_email: string, ids: number[]) => {
	return fetch(`${host}/survey-drafts/delete`, {
		method: 'POST',
		body: JSON.stringify({ user_email, ids }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const createSurveyDraft = (info: DraftCreateInfo) => {
	return fetch(`${host}/survey-drafts/create`, {
		method: 'POST',
		body: JSON.stringify(info),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const countSurveyDrafts = (user_email: string) => {
	return fetch(`${host}/survey-drafts/count`, {
		method: 'POST',
		body: JSON.stringify({ user_email }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

// surveys

export const countSurveys = (user_email: string) => {
	return fetch(`${host}/surveys/count`, {
		method: 'POST',
		body: JSON.stringify({ user_email }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const getSurveys = (user_email: string, page: number) => {
	return fetch(`${host}/surveys/all/${page}`, {
		method: 'POST',
		body: JSON.stringify({ user_email }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const getSurvey = (survey_code: string) => {
	return fetch(`${host}/surveys/fetch`, {
		method: 'POST',
		body: JSON.stringify({ survey_code }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const countSurveyRespondents = (survey_code: string) => {
	return fetch(`${host}/surveys/respondents-count`, {
		method: 'POST',
		body: JSON.stringify({ survey_code }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const getSurveyRespondents = (survey_code: string, page: number) => {
	return fetch(`${host}/surveys/respondents/${page}`, {
		method: 'POST',
		body: JSON.stringify({ survey_code }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const deleteSurveys = (user_email: string, survey_codes: string[]) => {
	return fetch(`${host}/surveys/delete`, {
		method: 'POST',
		body: JSON.stringify({ user_email, survey_codes }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const createSurvey = (info: SurveyCreateInfo) => {
	return fetch(`${host}/surveys/create`, {
		method: 'POST',
		body: JSON.stringify(info),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const giveAccessToSurvey = (
	user_email: string,
	survey_code: string,
	user_emails: string[]
) => {
	return fetch(`${host}/surveys/give-access`, {
		method: 'POST',
		body: JSON.stringify({ user_email, survey_code, user_emails }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const takeAwayAccessToSurvey = (
	user_email: string,
	survey_code: string,
	user_emails: string[]
) => {
	return fetch(`${host}/surveys/take-away-access`, {
		method: 'POST',
		body: JSON.stringify({ user_email, survey_code, user_emails }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const rejectAccessToSurveys = (user_email: string, survey_codes: string[]) => {
	return fetch(`${host}/surveys/reject-access`, {
		method: 'POST',
		body: JSON.stringify({ user_email, survey_codes }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const countUsersWithAccess = (user_email: string, survey_code: string) => {
	return fetch(`${host}/surveys/all-with-access-count`, {
		method: 'POST',
		body: JSON.stringify({ user_email, survey_code }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const getAllUsersWithoutAccess = (user_email: string, survey_code: string) => {
	return fetch(`${host}/surveys/all-without-access`, {
		method: 'POST',
		body: JSON.stringify({ user_email, survey_code }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const checkAccessToSurvey = (user_email: string, survey_code: string, page: number) => {
	return fetch(`${host}/surveys/get-all-with-access/${page}`, {
		method: 'POST',
		body: JSON.stringify({ user_email, survey_code }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

// user groups

export const countUserGroups = (user_email: string) => {
	return fetch(`${host}/user-groups/count`, {
		method: 'POST',
		body: JSON.stringify({ user_email }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const getUserGroups = (user_email: string, page: number) => {
	return fetch(`${host}/user-groups/all/${page}`, {
		method: 'POST',
		body: JSON.stringify({ user_email }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const getUserGroupsWithKeys = (user_email: string) => {
	return fetch(`${host}/user-groups/all-with-public-keys`, {
		method: 'POST',
		body: JSON.stringify({ user_email }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const countUserGroupMembers = (user_email: string, name: string) => {
	return fetch(`${host}/user-groups/group-members-count`, {
		method: 'POST',
		body: JSON.stringify({ user_email, name }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const getAllUsersWhoAreNotMembers = (user_email: string, name: string) => {
	return fetch(`${host}/user-groups/all-who-are-not-members`, {
		method: 'POST',
		body: JSON.stringify({ user_email, name }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const getWholeUserGroup = (user_email: string, name: string) => {
	return fetch(`${host}/user-groups/fetch`, {
		method: 'POST',
		body: JSON.stringify({ user_email, name }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const getUserGroup = (user_email: string, name: string, page: number) => {
	return fetch(`${host}/user-groups/fetch/${page}`, {
		method: 'POST',
		body: JSON.stringify({ user_email, name }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const createUserGroup = (
	user_email: string,
	user_group_name: string,
	user_group_members: string[]
) => {
	return fetch(`${host}/user-groups/create`, {
		method: 'POST',
		body: JSON.stringify({ user_email, user_group_name, user_group_members }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const renameUserGroup = (user_email: string, name: string, new_name: string) => {
	return fetch(`${host}/user-groups/rename`, {
		method: 'POST',
		body: JSON.stringify({ user_email, name, new_name }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const deleteUserGroups = (user_email: string, names: string[]) => {
	return fetch(`${host}/user-groups/delete`, {
		method: 'POST',
		body: JSON.stringify({ user_email, names }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const addUsersToGroup = (user_email: string, name: string, users: string[]) => {
	return fetch(`${host}/user-groups/add-users`, {
		method: 'POST',
		body: JSON.stringify({ user_email, name, users }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const removeUsersFromGroup = (user_email: string, name: string, users: string[]) => {
	return fetch(`${host}/user-groups/remove-users`, {
		method: 'POST',
		body: JSON.stringify({ user_email, name, users }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

// users

export const getUsers = () => {
	return fetch(`${host}/users/all`, {
		method: 'GET',
		headers: {
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const getUsersWithKeys = () => {
	return fetch(`${host}/users/all-with-public-keys`, {
		method: 'GET',
		headers: {
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const validateUser = (user_email: string) => {
	return fetch(`${host}/users/validate`, {
		method: 'POST',
		body: JSON.stringify({ user_email }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const hasPublicKey = (user_email: string) => {
	return fetch(`${host}/users/has-public-key`, {
		method: 'POST',
		body: JSON.stringify({ user_email }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const createUser = (user_email: string) => {
	return fetch(`${host}/users/register`, {
		method: 'POST',
		body: JSON.stringify({ user_email }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const updatePublicKey = (user_email: string, public_key: string, fingerprint: string) => {
	return fetch(`${host}/users/update-public-key`, {
		method: 'POST',
		body: JSON.stringify({ user_email, public_key, fingerprint }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const filterUnregisteredUsers = (emails: string[]) => {
	return fetch(`${host}/users/filter-unregistered-users`, {
		method: 'POST',
		body: JSON.stringify({ emails }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};

export const filterUsersWithNoPublicKey = (emails: string[]) => {
	return fetch(`${host}/users/filter-users-with-no-public-key`, {
		method: 'POST',
		body: JSON.stringify({ emails }),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${env.BEARER_TOKEN}`
		}
	});
};
