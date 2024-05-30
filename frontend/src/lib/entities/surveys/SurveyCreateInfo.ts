import type Survey from '$lib/entities/surveys/Survey';

export default class SurveyCreateInfo {
	user_email: string;
	survey_structure: Survey;
	uses_cryptographic_module: boolean;
	ring_members: Array<string>;
	constructor(
		user_email: string,
		survey_structure: Survey,
		uses_cryptographic_module: boolean,
		ring_members: Array<string>
	) {
		this.user_email = user_email;
		this.survey_structure = survey_structure;
		this.ring_members = ring_members;
		this.uses_cryptographic_module = uses_cryptographic_module;
	}
}
