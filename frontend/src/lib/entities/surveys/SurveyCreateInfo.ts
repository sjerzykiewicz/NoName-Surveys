import type Survey from '$lib/entities/surveys/Survey';

export default class SurveyCreateInfo {
	title: string;
	survey_structure: Survey;
	uses_cryptographic_module: boolean;
	ring_members: Array<string>;
	constructor(
		title: string,
		survey_structure: Survey,
		uses_cryptographic_module: boolean,
		ring_members: Array<string>
	) {
		this.title = title;
		this.survey_structure = survey_structure;
		this.uses_cryptographic_module = uses_cryptographic_module;
		this.ring_members = ring_members;
	}
}
