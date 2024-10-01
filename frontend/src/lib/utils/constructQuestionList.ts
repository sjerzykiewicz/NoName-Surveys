import Question from '$lib/entities/questions/Question';
import { SingleQuestion } from '$lib/entities/questions/Single';
import { MultiQuestion } from '$lib/entities/questions/Multi';
import { ScaleQuestion } from '$lib/entities/questions/Scale';
import { SliderQuestion } from '$lib/entities/questions/Slider';
import { ListQuestion } from '$lib/entities/questions/List';
import { RankQuestion } from '$lib/entities/questions/Rank';
import { TextQuestion } from '$lib/entities/questions/Text';
import { BinaryQuestion } from '$lib/entities/questions/Binary';
import Single from '$lib/components/create-page/Single.svelte';
import Multi from '$lib/components/create-page/Multi.svelte';
import Scale from '$lib/components/create-page/Scale.svelte';
import Slider from '$lib/components/create-page/Slider.svelte';
import List from '$lib/components/create-page/List.svelte';
import Rank from '$lib/components/create-page/Rank.svelte';
import Binary from '$lib/components/create-page/Binary.svelte';
import Text from '$lib/components/create-page/Text.svelte';
import QuestionsStore from '$lib/entities/questions/QuestionsStore';

export function constructQuestionList(questions: Array<QuestionsStore>): Array<Question> {
	let questionList: Array<Question> = [];
	questions.forEach((q) => {
		switch (q.component) {
			case Single:
				questionList = [...questionList, new SingleQuestion(q.required, q.question, q.choices)];
				break;
			case Multi:
				questionList = [...questionList, new MultiQuestion(q.required, q.question, q.choices)];
				break;
			case Scale:
				questionList = [...questionList, new ScaleQuestion(q.required, q.question)];
				break;
			case Slider:
				questionList = [
					...questionList,
					new SliderQuestion(
						q.required,
						q.question,
						parseFloat(q.choices[0]),
						parseFloat(q.choices[1])
					)
				];
				break;
			case List:
				questionList = [...questionList, new ListQuestion(q.required, q.question, q.choices)];
				break;
			case Rank:
				questionList = [...questionList, new RankQuestion(q.required, q.question, q.choices)];
				break;
			case Text:
				questionList = [...questionList, new TextQuestion(q.required, q.question, q.choices[0])];
				break;
			case Binary:
				questionList = [...questionList, new BinaryQuestion(q.required, q.question, q.choices)];
				break;
		}
	});

	return questionList;
}
