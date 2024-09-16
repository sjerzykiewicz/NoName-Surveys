import { Access } from '$lib/entities/Access';

export function getRespondentTypeData(respondentType: Access) {
	switch (respondentType) {
		case Access.Public:
			return { title: 'Everyone can submit an answer', icon: 'public', text: 'Public' };
		case Access.Users:
			return { title: 'Only chosen users can submit an answer', icon: 'person', text: 'Users' };
		case Access.Group:
			return {
				title: 'Only chosen group of users can submit an answer',
				icon: 'group',
				text: 'Group'
			};
		default:
			return { title: '', icon: '', text: '' };
	}
}
