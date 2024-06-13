import type Survey from './Survey';

export default class DraftCreateInfo {
	user_email: string;
	survey_structure: Survey;
	constructor(user_email: string, survey_structure: Survey) {
		this.user_email = user_email;
		this.survey_structure = survey_structure;
	}
}
