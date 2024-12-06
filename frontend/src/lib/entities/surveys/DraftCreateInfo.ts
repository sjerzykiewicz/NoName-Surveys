import type Survey from './Survey';

export default class DraftCreateInfo {
	title: string;
	survey_structure: Survey;
	user_email?: string;
	constructor(title: string, survey_structure: Survey, user_email?: string) {
		this.title = title;
		this.survey_structure = survey_structure;
		if (user_email) {
			this.user_email = user_email;
		}
	}
}
