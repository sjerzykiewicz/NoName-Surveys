export function urlify(str: string) {
	str = str.replace(/ /g, '%20');
	str = str.replace(/(\n|\r)/g, '%0A');
	str = str.replace(/\t/g, '%09');
	return str;
}
