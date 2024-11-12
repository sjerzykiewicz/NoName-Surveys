import type Survey from './Survey';

export default class DraftCreateInfo {
	title: string;
	survey_structure: Survey;
	constructor(title: string, survey_structure: Survey) {
		this.title = title;
		this.survey_structure = survey_structure;
	}
}
