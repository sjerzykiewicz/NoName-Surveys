import { Access } from '$lib/entities/Access';

export function getRespondentTypeData(respondentType: Access) {
	switch (respondentType) {
		case Access.Public:
			return { icon: 'public', text: 'Public' };
		case Access.Private:
			return { icon: 'encrypted', text: 'Private' };
		default:
			return { icon: '', text: '' };
	}
}
