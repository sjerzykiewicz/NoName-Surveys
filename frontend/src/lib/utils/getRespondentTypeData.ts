export function getRespondentTypeData(useCrypto: boolean) {
	if (useCrypto) return { icon: 'encrypted', text: 'Private' };
	return { icon: 'public', text: 'Public' };
}
