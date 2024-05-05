import type Survey from '$lib/entities/Survey';

export default class SurveyCreateInfo {
	creator: number;
	survey_structure: Survey;
	deadline: string;
	uses_cryptographic_module: boolean;
	constructor(
		creator: number,
		survey_structure: Survey,
		deadline: string,
		uses_cryptographic_module: boolean
	) {
		this.creator = creator;
		this.survey_structure = survey_structure;
		this.deadline = deadline;
		this.uses_cryptographic_module = uses_cryptographic_module;
	}
}
