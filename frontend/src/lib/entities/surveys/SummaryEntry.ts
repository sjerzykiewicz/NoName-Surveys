export class SummaryEntry {
	title: string;
	uses_cryptographic_module: boolean;
	survey_code: string;
	constructor(title: string, uses_cryptographic_module: boolean, survey_code: string) {
		this.title = title;
		this.uses_cryptographic_module = uses_cryptographic_module;
		this.survey_code = survey_code;
	}
}
