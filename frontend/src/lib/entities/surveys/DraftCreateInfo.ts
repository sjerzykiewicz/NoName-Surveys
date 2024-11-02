import type Survey from './Survey';

export default class DraftCreateInfo {
	user_email: string;
	title: string;
	survey_structure: Survey;
	constructor(user_email: string, title: string, survey_structure: Survey) {
		this.user_email = user_email;
		this.title = title;
		this.survey_structure = survey_structure;
	}
}
