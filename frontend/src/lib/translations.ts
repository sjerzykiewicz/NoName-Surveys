export const data = {
	en: {
		submit: 'Submit',
		error: 'Error',
		message: 'Message',
		welcome: 'Welcome',
		generate: 'Generate',
		save: 'Save',
		cancel: 'Cancel',

		error_message: 'Something went wrong, please contact the administrator.',

		nav_fill: 'Fill out',
		nav_create: 'Create',
		nav_drafts: 'Drafts',
		nav_surveys: 'Surveys',
		nav_groups: 'Groups',
		nav_account: 'Account',
		nav_toggle_theme: 'Toggle theme',

		home_code_info: 'Enter a survey code to fill it out',
		home_code_info_2:
			'Enter the code provided to you by the survey creator. Your answers are completely anonymous.',

		account_sign_in: 'Authorize yourself with AMU USOS:',
		account_authorization_info: `
Authorizing yourself will enable you to:
		<ul>
			<li>
				<div class="icon"><i class="material-symbols-rounded">article</i></div>
				<div>
					Create both
					<span class="accent">public</span>
					and <span class="accent">secure</span> surveys,
				</div>
			</li>
			<li>
				<div class="icon"><i class="material-symbols-rounded">save</i></div>
				<div>
					Save surveys as
					<span class="accent">drafts</span> for later editing,
				</div>
			</li>
			<li>
				<div class="icon"><i class="material-symbols-rounded">bar_chart</i></div>
				<div>
					View <span class="accent">responses</span>
					and <span class="accent">summaries</span> of your surveys,
				</div>
			</li>
			<li>
				<div class="icon"><i class="material-symbols-rounded">share</i></div>
				<div><span class="accent">Share</span> surveys' results with others,</div>
			</li>
			<li>
				<div class="icon"><i class="material-symbols-rounded">group</i></div>
				<div>
					Create and manage
					<span class="accent">user groups</span>,
				</div>
			</li>
			<li>
				<div class="icon"><i class="material-symbols-rounded">encrypted</i></div>
				<div>
					Generate <span class="accent">digital signature keys</span> that allow you to participate
					in
					<span class="accent">secure surveys</span> without needing to sign in each time.
				</div>
			</li>
		</ul>
		`,
		account_info: `We do not recommend signing in if you only wish to fill out a survey. For secure surveys, if you
		have already generated your digital signature keys, signing in is also not necessary.`,
		account_sign_out: 'Sign out',
		account_generating_keys: 'Generating Keys',
		account_new_key_alert:
			'Are you sure you want to generate new keys? Doing so will take away your ability to answer existing secure surveys.',
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
		generate: 'Generuj',
		save: 'Zapisz',
		cancel: 'Anuluj',

		error_message: 'Coś poszło nie tak, skontaktuj się z administratorem.',

		nav_fill: 'Wypełnij',
		nav_create: 'Utwórz',
		nav_drafts: 'Szkice',
		nav_surveys: 'Ankiety',
		nav_groups: 'Grupy',
		nav_account: 'Konto',
		nav_toggle_theme: 'Zmień motyw',

		home_code_info: 'Wprowadź kod ankiety, aby ją wypełnić',

		account_sign_in: 'Zautoryzuj się za pomocą UAM USOS:',
		account_authorization_info: `
		Zautoryzowanie się pozwoli Ci na:
		<ul>
			<li>
				<div class="icon"><i class="material-symbols-rounded">article</i></div>
				<div>
					Tworzenie zarówno <span class="accent">publicznych</span>, jak i <span class="accent">bezpiecznych</span> ankiet,
				</div>
			</li>
			<li>
				<div class="icon"><i class="material-symbols-rounded">save</i></div>
				<div>
					Zapisywanie ankiet jako <span class="accent">szkice</span> do późniejszej edycji,
				</div>
			</li>
			<li>
				<div class="icon"><i class="material-symbols-rounded">bar_chart</i></div>
				<div>
					Podgląd <span class="accent">odpowiedzi</span> i <span class="accent">podsumowań</span> swoich ankiet,
				</div>
			</li>
			<li>
				<div class="icon"><i class="material-symbols-rounded">share</i></div>
				<div>Dzielenie się wynikami ankiet z innymi,</div>
			</li>
			<li>
				<div class="icon"><i class="material-symbols-rounded">group</i></div>
				<div>
					Tworzenie i zarządzanie <span class="accent">grupami użytkowników</span>,
				</div>
			</li>
			<li>
				<div class="icon"><i class="material-symbols-rounded">encrypted</i></div>
				<div>
					Generowanie <span class="accent">kluczy podpisu cyfrowego</span>, które pozwalają na uczestniczenie
					w <span class="accent">bezpiecznych ankietach</span> bez konieczności logowania się za każdym razem.
				</div>
			</li>
		`,
		account_info: `Nie zalecamy logowania się, jeśli chcesz jedynie wypełnić ankietę. W przypadku bezpiecznych ankiet, jeśli
		już wygenerowałeś klucze podpisu cyfrowego, logowanie się nie jest również konieczne.`,
		account_sign_out: 'Wyloguj się',
		account_generating_keys: 'Generowanie kluczy',
		account_new_key_alert:
			'Czy na pewno chcesz wygenerować nowe klucze? Spowoduje to utratę możliwości odpowiedzi na istniejące bezpieczne ankiety.',
		account_new_key: 'Wygeneruj nową parę kluczy',
		account_keys_info: `Te klucze pozwalają na uczestniczenie w bezpiecznych ankietach. Po ich wygenerowaniu, należy
			zabezpieczyć je. Podczas wypełniania bezpiecznej ankiety, zostaniesz poproszony o podanie
			tych kluczy przeglądarce do podpisu cyfrowego.`
	}
};
