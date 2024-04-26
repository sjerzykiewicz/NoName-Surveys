export class Question {
	required: boolean;
	question: string;
	constructor(required: boolean = false, question: string = '') {
		this.required = required;
		this.question = question;
	}
}

class SingleQuestionBody {
	choices: Array<string>;
	constructor(choices: Array<string> = []) {
		this.choices = choices;
	}
}

export class SingleQuestion extends Question {
	single: SingleQuestionBody;
	constructor(required: boolean = false, question: string = '', choices: Array<string> = []) {
		super(required, question);
		this.single = new SingleQuestionBody(choices);
	}
}

class MultiQuestionBody {
	choices: Array<string>;
	constructor(choices: Array<string> = []) {
		this.choices = choices;
	}
}

export class MultiQuestion extends Question {
	multi: MultiQuestionBody;
	constructor(required: boolean = false, question: string = '', choices: Array<string> = []) {
		super(required, question);
		this.multi = new MultiQuestionBody(choices);
	}
}

class ScaleQuestionBody {}

export class ScaleQuestion extends Question {
	scale: ScaleQuestionBody = {};
	constructor(required: boolean = false, question: string = '') {
		super(required, question);
	}
}

class SliderQuestionBody {
	min_value: number;
	max_value: number;
	constructor(min_value: number = 0, max_value: number = 0) {
		this.min_value = min_value;
		this.max_value = max_value;
	}
}

export class SliderQuestion extends Question {
	slider: SliderQuestionBody;
	constructor(
		required: boolean = false,
		question: string = '',
		min_value: number = 0,
		max_value: number = 0
	) {
		super(required, question);
		this.slider = new SliderQuestionBody(min_value, max_value);
	}
}

class ListQuestionBody {
	choices: Array<string>;
	constructor(choices: Array<string> = []) {
		this.choices = choices;
	}
}

export class ListQuestion extends Question {
	list: ListQuestionBody;
	constructor(required: boolean = false, question: string = '', choices: Array<string> = []) {
		super(required, question);
		this.list = new ListQuestionBody(choices);
	}
}

class RankQuestionBody {
	choices: Array<string>;
	constructor(choices: Array<string> = []) {
		this.choices = choices;
	}
}

export class RankQuestion extends Question {
	rank: RankQuestionBody;
	constructor(required: boolean = false, question: string = '', choices: Array<string> = []) {
		super(required, question);
		this.rank = new RankQuestionBody(choices);
	}
}

class TextQuestionBody {
	details: string;
	constructor(details: string = '') {
		this.details = details;
	}
}

export class TextQuestion extends Question {
	text: TextQuestionBody;
	constructor(required: boolean = false, question: string = '', details: string = '') {
		super(required, question);
		this.text = new TextQuestionBody(details);
	}
}

export class Survey {
	title: string;
	questions: Array<Question>;
	constructor(title: string = '', questions: Array<Question> = []) {
		this.title = title;
		this.questions = questions;
	}
}
