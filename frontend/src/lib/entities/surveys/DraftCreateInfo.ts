import type Survey from './Survey';

export default class DraftCreateInfo {
	creator: number;
	survey_structure: Survey;
	constructor(creator: number, survey_structure: Survey) {
		this.creator = creator;
		this.survey_structure = survey_structure;
	}
}
