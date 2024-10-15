export function extractTranslatedText(txElement: HTMLDivElement | null): string {
	if (txElement) {
		return txElement.textContent || '';
	}
	return '';
}

export const data = {
	en: {
		submit: 'Submit',
		error: 'Error',
		message: 'Message',
		welcome: 'Welcome',

		error_message: 'Something went wrong, please contact the administrator.',

		nav_fill: 'Fill out',
		nav_create: 'Create',
		nav_drafts: 'Drafts',
		nav_surveys: 'Surveys',
		nav_groups: 'Groups',
		nav_account: 'Account',
		nav_toggle_theme: 'Toggle theme',

		home_code_info: 'Enter a survey code to fill it out:',

		account_sign_in: 'Sign in with:',
		account_authorization_info: `
		Authorizing yourself will enable you to:
		<ul>
			<li>Create your own surveys,</li>
			<li>Save survey drafts,</li>
			<li>View your survey's results,</li>
			<li>
				Generate digital signature keys that allow you to participate in secure surveys without
				needing to sign in each time.
			</li>
		</ul>
		`,
		account_info: `We do not recommend signing in if you only wish to fill out a survey. For secure surveys, if you
		have already generated your digital signature keys, signing in is also not necessary.`,
		account_sign_out: 'Sign out',
		account_new_key_alert: 'Are you sure you want to generate new keys?',
		account_new_key: 'Generate new key pair',
		account_keys_info: `These keys allow you to participate in secure surveys. Once they are generated, it is your
			responsibility to keep them safe. When submitting a secure survey, you will be asked to
			provide these keys to your browser for digital signature.`
	},
	pl: {
		submit: 'Zatwierdź',
		error: 'Błąd',
		message: 'Wiadomość',
		welcome: 'Witaj',

		error_message: 'Coś poszło nie tak, skontaktuj się z administratorem.',

		nav_fill: 'Wypełnij',
		nav_create: 'Utwórz',
		nav_drafts: 'Szkice',
		nav_surveys: 'Ankiety',
		nav_groups: 'Grupy',
		nav_account: 'Konto',
		nav_toggle_theme: 'Zmień motyw',

		home_code_info: 'Wprowadź kod ankiety, aby ją wypełnić:',

		account_sign_in: 'Zaloguj się za pomocą:',
		account_authorization_info: `
		Udostępnienie autoryzacji pozwoli Ci na:
		<ul>
			<li>Tworzenie własnych ankiet,</li>
			<li>Zapisywanie szkiców ankiet,</li>
			<li>Przeglądanie wyników swoich ankiet,</li>
			<li>
				Generowanie kluczy podpisu cyfrowego, które pozwalają na uczestniczenie w bezpiecznych ankietach
				bez konieczności logowania się za każdym razem.
			</li>
		</ul>
		`,
		account_info: `Nie zalecamy logowania się, jeśli chcesz jedynie wypełnić ankietę. W przypadku bezpiecznych ankiet, jeśli
		już wygenerowałeś klucze podpisu cyfrowego, logowanie się nie jest również konieczne.`,
		account_sign_out: 'Wyloguj się',
		account_new_key_alert: 'Czy na pewno chcesz wygenerować nowe klucze?',
		account_new_key: 'Wygeneruj nową parę kluczy',
		account_keys_info: `Te klucze pozwalają na uczestniczenie w bezpiecznych ankietach. Po ich wygenerowaniu, należy
			zabezpieczyć je. Podczas wypełniania bezpiecznej ankiety, zostaniesz poproszony o podanie
			tych kluczy przeglądarce do podpisu cyfrowego.`
	}
};
