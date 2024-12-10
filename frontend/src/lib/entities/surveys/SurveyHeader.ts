export default class SurveyHeader {
	title: string;
	survey_code: string;
	creation_date: string;
	uses_cryptographic_module: boolean;
	is_owned_by_user: boolean;
	group_size: number;
	is_enabled: boolean;
	constructor(
		title: string,
		survey_code: string,
		creation_date: string,
		uses_cryptographic_module: boolean,
		is_owned_by_user: boolean,
		group_size: number,
		is_enabled: boolean
	) {
		this.title = title;
		this.survey_code = survey_code;
		this.creation_date = creation_date;
		this.uses_cryptographic_module = uses_cryptographic_module;
		this.is_owned_by_user = is_owned_by_user;
		this.group_size = group_size;
		this.is_enabled = is_enabled;
	}
}
