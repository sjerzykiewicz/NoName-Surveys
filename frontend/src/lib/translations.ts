export const data = {
	en: {
		submit: 'Submit',
		error: 'Error',
		warning: 'Warning',
		success: 'Success',
		message: 'Message',
		welcome: 'Welcome',
		generate: 'Generate',
		save: 'Save',
		cancel: 'Cancel',
		delete: 'Delete',
		sign_in: 'Sign In',
		sign_out: 'Sign Out',
		public: 'Public',
		secure: 'Secure',
		choice: 'Choice',
		minimum: 'Minimum',
		minimum_value: 'Minimum value',
		maximum: 'Maximum',
		maximum_value: 'Maximum value',
		precision: 'Precision',
		answer: 'Answer',
		average: 'Average',
		select_answer: 'Select your answer',
		selected_value: 'Selected value',
		creation_date: 'Creation Date',
		access_code: 'Access Code',
		survey_title: 'Survey Title',
		group_size: 'Group Size',
		survey_info: 'Survey Information',
		select_all: 'Select all',
		draft: 'Draft',
		group: 'Group',
		create: 'Create',

		single_text: 'Single',
		single_title: 'Single choice',
		multi_text: 'Multi',
		multi_title: 'Multiple choice',
		scale_text: 'Scale',
		scale_title: '1-5 choice',
		slider_text: 'Slider',
		slider_title: 'Range of values',
		list_text: 'List',
		list_title: 'Dropdown menu choice',
		rank_text: 'Rank',
		rank_title: 'Ranking choice',
		binary_text: 'Binary',
		binary_title: 'Yes/No choice',
		text_text: 'Text',
		text_title: 'Open question',
		number_text: 'Number',
		number_title: 'Numerical question',

		possible_respondents: 'Possible Respondents',
		possible_respondents_empty: 'No possible respondents to display!',

		info_about_leaving:
			'Are you sure you want to leave this page?\nLeaving will discard all unsaved changes.',
		info_about_deleting: 'Are you sure you want to delete selected entries?',

		error_message: 'Something went wrong, please contact the administrator.',

		nav_fill: 'Fill Out',
		nav_create: 'Create',
		nav_drafts: 'Drafts',
		nav_surveys: 'Surveys',
		nav_groups: 'Groups',
		nav_account: 'Account',
		nav_toggle_theme: 'Toggle theme',
		nav_toggle_lang: 'Toggle language',
		nav_scroll_to_top: 'Scroll to the top',
		nav_sign_in_info: 'Sign in to access ',

		home_code_info: 'Enter a survey code to fill it out',
		home_code_info_2:
			'Enter the code provided to you by the survey creator. Your answers are completely anonymous.',
		home_submit: 'Submit the code',
		home_redirect: 'If you want to create your own survey, go to',

		account_your: 'Your account',
		account_info_title: 'Account information',
		account_sign_in: 'Authorize yourself with AMU USOS:',
		account_authorization_info: `
Authorizing yourself will enable you to:
<ul class="account-ul">
	<li class="account-li">
		<div class="account-icon"><i class="symbol">article</i></div>
		<div>
			Create both
			<span class="account-accent">public</span>
			and <span class="account-accent">secure</span> surveys,
		</div>
	</li>
	<li class="account-li">
		<div class="account-icon"><i class="symbol">save</i></div>
		<div>
			Save surveys as
			<span class="account-accent">drafts</span> for later editing,
		</div>
	</li>
	<li class="account-li">
		<div class="account-icon"><i class="symbol">bar_chart</i></div>
		<div>
			View <span class="account-accent">responses</span>
			and <span class="account-accent">summaries</span> of your surveys,
		</div>
	</li>
	<li class="account-li">
		<div class="account-icon"><i class="symbol">share</i></div>
		<div><span class="account-accent">Share</span> surveys' results with others,</div>
	</li>
	<li class="account-li">
		<div class="account-icon"><i class="symbol">group</i></div>
		<div>
			Create and manage
			<span class="account-accent">user groups</span>,
		</div>
	</li>
	<li class="account-li">
		<div class="account-icon"><i class="symbol">encrypted</i></div>
		<div>
			Generate <span class="account-accent">digital signature keys</span> that allow you to participate
			in
			<span class="account-accent">secure surveys</span> without the need to sign in each time.
		</div>
	</li>
</ul>
		`,
		account_info: `We do not recommend signing in if you only wish to fill out a survey. For secure surveys, if you
		have already generated your digital signature keys, signing in is also not necessary.`,
		account_generating_keys: 'Generating Keys',
		account_new_key_alert:
			'Are you sure you want to generate new keys? Doing so will take away your ability to answer existing secure surveys.',
		account_new_key: 'Generate New Keys',
		account_keys_info: `These keys allow you to participate in secure surveys. Once they are generated, it is your
			responsibility to keep them safe. When submitting a secure survey, you will be asked to
			provide these keys to your browser for digital signature.`,

		create_groups_info: `Before creating a secure survey, consider setting up a user group. User groups make it
			easy to select the same set of respondents across multiple surveys. However, if you
			prefer, you can proceed without using them.`,

		create_survey_title_label: 'Survey Title',
		create_survey_title_title: 'Enter a survey title',
		create_survey_title_error_required: 'Please enter survey title.',
		create_survey_title_error_limit: 'Title must be {limit} or less characters long.',

		create_question: 'Question',
		create_question_index: 'Question no. {index}',
		create_question_up: 'Move question up',
		create_question_down: 'Move question down',
		create_question_label: 'Question',
		create_question_title: 'Enter a question',
		create_question_required: 'Required',
		create_question_not_required: 'Not required',
		create_question_remove: 'Remove question',
		create_question_choose_type: 'Choose question type',
		create_question_choose_type_stop: 'Stop choosing question type',

		create_question_error_required: 'Please enter question no. {index}.',
		create_question_error_limit: 'Question no. {index} must be {limit} or less characters long.',

		create_choice_title: 'Enter a choice',
		create_choice_remove: 'Remove choice',
		create_choice_add: 'Add choice',

		create_rank_choice: 'Choice no. {index}',

		create_text_details_label: 'Question Details',
		create_text_details_title: 'Enter question details',

		create_number_min_title: 'Enter a minimum value',
		create_number_min_placeholder: 'Enter a minimum value...',
		create_number_min_placeholder_short: 'Enter a min value...',
		create_number_max_title: 'Enter a maximum value',
		create_number_max_placeholder: 'Enter a maximum value...',
		create_number_max_placeholder_short: 'Enter a max value...',

		create_slider_precision_title: 'Enter the precision',
		create_slider_precision_placeholder: 'Enter precision...',
		create_slider_precision_placeholder_short: 'Enter prec...',

		create_binary_positive_label: 'Positive Choice',
		create_binary_positive_title: 'Enter a positive choice',
		create_binary_negative_label: 'Negative Choice',
		create_binary_negative_title: 'Enter a negative choice',

		create_choice_error_required: 'Please enter all choices for question no. {index}.',
		create_choice_error_binary_required: 'Please enter both choices for question no. {index}.',
		create_choice_error_number_required: 'Please enter both values for question no. {index}.',
		create_choice_error_slider_required: 'Please enter all values for question no. {index}.',
		create_choice_error_limit:
			'Choices must be {limit} or less characters long in question no. {index}.',
		create_choice_error_duplicate: 'Please remove duplicate choices from question no. {index}.',
		create_choice_error_slider_values:
			'Maximum value must be greater than minimum value in question no. {index}.',
		create_choice_error_slider_precision:
			'Precision must be lower than the range in question no. {index}.',

		create_saving_draft: 'Saving Draft',
		create_saving_draft_alert: 'Do you wish to overwrite the draft or save a new draft?',
		create_overwrite_draft: 'Overwrite Draft',
		create_save_new_draft: 'Save New Draft',
		create_define_respondent_group: 'Define Respondent Group',
		create_define_respondent_group_alert: 'Do you wish to make the survey public or secure?',
		create_define_respondent_group_error: 'Please define respondent group.',
		create_survey_success: 'Survey Created Successfully!',

		footer_edit: 'Edit',
		footer_edit_title: 'Edit survey',
		footer_preview: 'Preview',
		footer_save_draft: 'Save draft',
		footer_saved: 'Saved!',
		footer_create: 'Create',
		footer_create_title: 'Finish survey creation',

		select_users: 'Select users',
		select_group: 'Select group',
		select_members: 'Select members',

		import_csv_title: 'Import users from .csv file',
		import_csv_label: 'Or import users from .csv file',
		select_file: 'Select file',
		no_file_selected: 'No file selected',

		copy_link: 'Copy link',
		copy_code: 'Copy code',
		copied: 'Copied!',
		no_copy_insecure_connection: 'Could not copy due to an insecure connection.',

		survey_limit_reached:
			'You have reached the maximum number of surveys you can create. Please delete some surveys to create new ones.',
		draft_limit_reached:
			'You have reached the maximum number of drafts you can create. Please delete some drafts to create new ones.',
		survey_and_draft_limit_reached:
			'You have reached the maximum number of surveys and drafts you can create. Please delete some surveys and drafts to create new ones.',

		your_drafts: 'Your drafts',
		number_of_drafts: 'Number of drafts',
		no_drafts_yet: 'No drafts yet!',
		draft_tooltip: `When creating a survey, you can save it as a draft for later use. To create a survey, click
			on the "Create" tab at the top of the page or the button below. All your saved drafts will
			be stored on this page.`,
		draft_title: 'Draft Title',

		public_key_not_on_list: 'Your public key is not on the list.',
		answer_submit_success: 'Your answer has been submitted successfully.',
		load_keys: 'Load your digital signature keys',
		key_file_label: `Please load the file which you have previously generated on this application. The file
			contains your keys, necessary for cryptographic calculations which are needed for validating
			your right to fill out this survey.`,
		default_filename: 'Default filename',
		survey_not_secure: 'This survey is not secure.',
		only_respondent: ' You are the only person who can respond to this survey.',
		two_respondents:
			' There are only two people who can respond to this survey. The other person could be the creator of this survey.',
		answer_question_no: 'Please answer question no. ',
		error_no_file: 'Please select a file.',
		error_invalid_file: 'Please select a .pem file.',

		your_groups: 'Your groups',
		number_of_groups: 'Number of groups',
		renaming: 'Renaming',
		enter_new_group_name: 'Enter a new group name',
		no_groups_yet: 'No groups yet!',
		groups_tooltip: `When creating a secure survey, you can choose a group of possible respondents. To create a
			group, click on the button below. All your created groups will be stored on this page.`,
		group_name: 'Group Name',
		everyone_has_keys:
			'Everyone in this group have generated their keys. You can use this group in secure surveys.',
		not_everyone_has_keys:
			'Not everyone in this group have generated their keys. You cannot use this group in secure surveys.',
		max_groups_reached:
			'You have reached the maximum number of groups you can create. Please delete some groups to create new ones.',

		create_group: 'Create a group',
		create_group_stop: 'Stop creating group',
		delete_selected_groups: 'Delete selected groups',
		enter_group_name: 'Enter a group name',
		select_group_members: 'Select group members',
		save_group: 'Save the group',
		import_members_title: 'Import group members from a .csv file',
		import_members_label: 'Or import group members from a .csv file.',
		members_error: 'Please select group members.',
		group_error_name_required: 'Please enter group name.',
		group_error_name_too_long: `Group name must be {$LIMIT_OF_CHARS} or less characters long.`,
		group_error_already_exists: 'This group name already exists.',
		group_error_name_invalid:
			'Group name can only contain letters, numbers, spaces, slashes and hyphens.',

		removing_group_members: 'Removing group members',
		add_group_members: 'Add group memebers',
		add_group_members_stop: 'Stop adding group members',
		members: 'Members',
		remove_selected_members: 'Remove selected group members',
		select_mebers: 'Select group members',
		add_members_finish: 'Finish adding group members',
		group_members: 'Group members',
		no_members_yet: 'No group members yet!',
		user_has_keys: 'This user has already generated their keys.',
		user_has_no_keys: 'This user has not generated their keys yet.'
	},

	pl: {
		submit: 'Zatwierdź',
		error: 'Błąd',
		warning: 'Ostrzeżenie',
		success: 'Sukces',
		message: 'Wiadomość',
		welcome: 'Witaj',
		generate: 'Generuj',
		save: 'Zapisz',
		cancel: 'Anuluj',
		delete: 'Usuń',
		sign_in: 'Zaloguj się',
		sign_out: 'Wyloguj się',
		public: 'Publiczna',
		secure: 'Bezpieczna',
		choice: 'Wybór',
		minimum: 'Minimum',
		minimum_value: 'Wartość minimalna',
		maximum: 'Maksimum',
		maximum_value: 'Wartość maksymalna',
		precision: 'Precyzja',
		answer: 'Odpowiedź',
		average: 'Średnia',
		select_answer: 'Wybierz swoją odpowiedź',
		selected_value: 'Wybrana wartość',
		creation_date: 'Data utworzenia',
		access_code: 'Kod dostępu',
		survey_title: 'Tytuł ankiety',
		group_size: 'Rozmiar grupy',
		survey_info: 'Informacje o ankiecie',
		select_all: 'Wybierz wszystko',
		draft: 'Szkic',
		group: 'Grupa',
		create: 'Utwórz',

		single_text: 'Jednokrotne',
		single_title: 'Jednokrotny wybór',
		multi_text: 'Wielokrotne',
		multi_title: 'Wielokrotny wybór',
		scale_text: 'Skala',
		scale_title: 'Wybór 1-5',
		slider_text: 'Suwak',
		slider_title: 'Zakres wartości',
		list_text: 'Lista',
		list_title: 'Wybór z listy rozwijanej',
		rank_text: 'Ranking',
		rank_title: 'Wybór rankingowy',
		binary_text: 'Binarne',
		binary_title: 'Wybór Tak/Nie',
		text_text: 'Tekstowe',
		text_title: 'Pytanie otwarte',
		number_text: 'Liczbowe',
		number_title: 'Pytanie numeryczne',

		possible_respondents: 'Możliwi respondenci',
		possible_respondents_empty: 'Brak możliwych respondentów do wyświetlenia!',

		info_about_leaving:
			'Czy na pewno chcesz opuścić tę stronę?\nOpuszczenie spowoduje utratę wszystkich niezapisanych zmian.',
		info_about_deleting: 'Czy na pewno chcesz usunąć wybrane wpisy?',

		error_message: 'Coś poszło nie tak, skontaktuj się z administratorem.',

		nav_fill: 'Wypełnij',
		nav_create: 'Utwórz',
		nav_drafts: 'Szkice',
		nav_surveys: 'Ankiety',
		nav_groups: 'Grupy',
		nav_account: 'Konto',
		nav_toggle_theme: 'Zmień motyw',
		nav_toggle_lang: 'Zmień język',
		nav_scroll_to_top: 'Przewiń na samą górę',
		nav_sign_in_info: 'Zaloguj się, aby uzyskać dostęp do ',

		home_code_info: 'Podaj kod ankiety, by ją wypełnić',
		home_code_info_2:
			'Wprowadź kod podany przez twórcę ankiety. Twoje odpowiedzi są w pełni anonimowe.',
		home_submit: 'Wyślij kod',
		home_redirect: 'Jeśli chcesz utworzyć własną ankietę, przejdź do',

		account_your: 'Twoje konto',
		account_info_title: 'Informacje o koncie',
		account_sign_in: 'Zautoryzuj się za pomocą USOS UAM:',
		account_authorization_info: `
Zautoryzowanie się pozwoli Ci na:
<ul class="account-ul">
	<li class="account-li">
		<div class="account-icon"><i class="symbol">article</i></div>
		<div>
			Tworzenie zarówno <span class="account-accent">publicznych</span>, jak i <span class="account-accent">bezpiecznych</span> ankiet,
		</div>
	</li>
	<li class="account-li">
		<div class="account-icon"><i class="symbol">save</i></div>
		<div>
			Zapisywanie ankiet jako <span class="account-accent">szkice</span> do późniejszej edycji,
		</div>
	</li>
	<li class="account-li">
		<div class="account-icon"><i class="symbol">bar_chart</i></div>
		<div>
			Podgląd <span class="account-accent">odpowiedzi</span> i <span class="account-accent">podsumowań</span> swoich ankiet,
		</div>
	</li>
	<li class="account-li">
		<div class="account-icon"><i class="symbol">share</i></div>
		<div><span class="account-accent">Udostępnianie</span> wyników ankiet innym osobom,</div>
	</li>
	<li class="account-li">
		<div class="account-icon"><i class="symbol">group</i></div>
		<div>
			Tworzenie i zarządzanie <span class="account-accent">grupami użytkowników</span>,
		</div>
	</li>
	<li class="account-li">
		<div class="account-icon"><i class="symbol">encrypted</i></div>
		<div>
			Generowanie <span class="account-accent">kluczy podpisu cyfrowego</span>, które pozwalają na uczestniczenie
			w <span class="account-accent">bezpiecznych ankietach</span> bez konieczności logowania się za każdym razem.
		</div>
	</li>
</ul>
		`,
		account_info: `Nie zalecamy logowania się, jeśli chcesz jedynie wypełnić ankietę. W przypadku bezpiecznych ankiet, jeśli
		już wygenerowałeś klucze podpisu cyfrowego, logowanie się również nie jest konieczne.`,
		account_sign_out: 'Wyloguj się',
		account_generating_keys: 'Generowanie kluczy',
		account_new_key_alert:
			'Czy na pewno chcesz wygenerować nowe klucze? Spowoduje to utratę możliwości odpowiedzi na istniejące bezpieczne ankiety.',
		account_new_key: 'Wygeneruj nowe klucze',
		account_keys_info: `Te klucze pozwalają na uczestniczenie w bezpiecznych ankietach. Po ich wygenerowaniu, należy
			je zabezpieczyć. Podczas wypełniania bezpiecznej ankiety, zostaniesz poproszony o podanie
			tych kluczy przeglądarce do podpisu cyfrowego.`,

		create_groups_info: `Przed utworzeniem bezpiecznej ankiety, rozważ utworzenie grupy użytkowników. Grupy użytkowników ułatwiają wybór
			takiego samego zestawu respondentów w wielu ankietach. Możesz jednak kontynuować bez ich użycia, jeśli chcesz.`,

		create_survey_title_label: 'Tytuł ankiety',
		create_survey_title_title: 'Wprowadź tytuł ankiety',
		create_survey_title_error_required: 'Proszę wprowadzić tytuł ankiety.',
		create_survey_title_error_limit: 'Tytuł musi mieć {limit} lub mniej znaków.',

		create_question: 'Pytanie',
		create_question_index: 'Pytanie nr {index}',
		create_question_up: 'Przesuń pytanie w górę',
		create_question_down: 'Przesuń pytanie w dół',
		create_question_label: 'Pytanie',
		create_question_title: 'Wprowadź pytanie',
		create_question_required: 'Wymagane',
		create_question_not_required: 'Nie wymagane',
		create_question_remove: 'Usuń pytanie',
		create_question_choose_type: 'Wybierz typ pytania',
		create_question_choose_type_stop: 'Przestań wybierać typ pytania',

		create_question_error_required: 'Proszę wprowadzić pytanie nr {index}.',
		create_question_error_limit: 'Pytanie nr {index} musi mieć {limit} lub mniej znaków.',

		create_choice_title: 'Wprowadź wybór',
		create_choice_remove: 'Usuń wybór',
		create_choice_add: 'Dodaj wybór',

		create_rank_choice: 'Wybór nr {index}',

		create_text_details_label: 'Szczegóły pytania',
		create_text_details_title: 'Wprowadź szczegóły pytania',

		create_number_min_title: 'Podaj minimalną wartość',
		create_number_min_placeholder: 'Podaj minimum...',
		create_number_min_placeholder_short: 'Podaj min...',
		create_number_max_title: 'Podaj maksymalną wartość',
		create_number_max_placeholder: 'Podaj maksimum...',
		create_number_max_placeholder_short: 'Podaj maks...',

		create_slider_precision_title: 'Podaj precyzję',
		create_slider_precision_placeholder: 'Podaj precyzję...',
		create_slider_precision_placeholder_short: 'Podaj prec...',

		create_binary_positive_label: 'Pozytywny wybór',
		create_binary_positive_title: 'Wprowadź pozytywny wybór',
		create_binary_negative_label: 'Negatywny wybór',
		create_binary_negative_title: 'Wprowadź negatywny wybór',

		create_choice_error_required: 'Proszę wprowadzić wszystkie wybory dla pytania nr {index}.',
		create_choice_error_binary_required: 'Proszę wprowadzić oba wybory dla pytania nr {index}.',
		create_choice_error_number_required: 'Proszę wprowadzić obie wartości dla pytania nr {index}.',
		create_choice_error_slider_required:
			'Proszę wprowadzić wszystkie wartości dla pytania nr {index}.',
		create_choice_error_limit: 'Wybory muszą mieć {limit} lub mniej znaków w pytaniu nr {index}.',
		create_choice_error_duplicate: 'Proszę usunąć zduplikowane wybory z pytania nr {index}.',
		create_choice_error_slider_values:
			'Maksymalna wartość musi być większa niż minimalna wartość w pytaniu nr {index}.',
		create_choice_error_slider_precision:
			'Precyzja musi być mniejsza niż zakres w pytaniu nr {index}.',

		create_saving_draft: 'Zapisywanie szkicu',
		create_saving_draft_alert: 'Chcesz nadpisać szkic czy zapisać nowy szkic?',
		create_overwrite_draft: 'Nadpisz szkic',
		create_save_new_draft: 'Zapisz nowy szkic',
		create_define_respondent_group: 'Zdefiniuj grupę respondentów',
		create_define_respondent_group_alert: 'Chcesz stworzyć ankietę publiczną czy bezpieczną?',
		create_define_respondent_group_error: 'Proszę zdefiniować grupę respondentów.',
		create_survey_success: 'Ankieta utworzona pomyślnie!',

		footer_edit: 'Edytuj',
		footer_edit_title: 'Edytuj ankietę',
		footer_preview: 'Podgląd',
		footer_save_draft: 'Zapisz szkic',
		footer_saved: 'Zapisano!',
		footer_create: 'Utwórz',
		footer_create_title: 'Zakończ tworzenie ankiety',

		select_users: 'Wybierz użytkowników',
		select_group: 'Wybierz grupę',
		select_members: 'Wybierz członków',

		import_csv_title: 'Importuj użytkowników z pliku .csv',
		import_csv_label: 'Lub importuj użytkowników z pliku .csv',
		select_file: 'Wybierz plik',
		no_file_selected: 'Nie wybrano pliku',

		copy_link: 'Kopiuj link',
		copy_code: 'Kopiuj kod',
		copied: 'Skopiowano!',
		no_copy_insecure_connection: 'Kopiowanie nie powiodło się z powodu niebezpiecznego połączenia.',

		survey_limit_reached:
			'Osiągnięto maksymalną liczbę ankiet możliwych do utworzenia. Usuń któreś z istniejących, aby utworzyć nowe.',
		draft_limit_reached:
			'Osiągnięto maksymalną liczbę szkiców możliwych do utworzenia. Usuń któreś z istniejących, aby utworzyć nowe.',
		survey_and_draft_limit_reached:
			'Osiągnięto maksymalną liczbę ankiet i szkiców możliwych do utworzenia. Usuń któreś z istniejących, aby utworzyć nowe.',

		your_drafts: 'Twoje szkice',
		number_of_drafts: 'Liczba szkicy',
		no_drafts_yet: 'Brak szkicy!',
		draft_tooltip: `Podczas tworzenia ankiety, możesz zapisać ją jako szkic do późniejszego wykorzystania. Aby stworzyć ankietę, wejdź
			w zakładkę "Utwórz" na górze strony lub kliknij przycisk poniżej. Wszystkie zapisane szkice będą dostępne na tej stronie.`,
		draft_title: 'Tytuł Szkicu',

		public_key_not_on_list: 'Twój klucz publiczny nie znajduje się na liście',
		answer_submit_success: 'Twoja odpowiedź została przesłana pomyślnie',
		load_keys: 'Załaduj klucze kryptograficzne',
		key_file_label: `Załaduj plik wygenerowany wcześniej za pośrednictwem aplikacji. Plik zawiera Twoje klucze,
			niezbędne do przeprowadzenia obliczeń kryptograficznych potrzebnych do zweryfikowania Twojego prawa do
			wypełnienia tej ankiety.`,
		default_filename: 'Domyślna nazwa pliku',
		survey_not_secure: 'Ta ankieta nie jest bezpieczna.',
		only_respondent: ' Jesteś jedyną osobą, która może wypełnić tę ankietę.',
		two_respondents:
			' Tylko dwie osoby mogą wypełnić tę ankietę. Istnieje możliwość, że drugą osobą jest twórca ankiety.',
		answer_question_no: 'Wprowadź odpowiedź na pytanie nr. ',
		error_no_file: 'Załaduj plik.',
		error_invalid_file: 'Załaduj plik .pem.',

		your_groups: 'Twoje grupy',
		number_of_groups: 'Liczba grup',
		renaming: 'Zmienianie nazwy',
		enter_new_group_name: 'Wprowadź nową nazwę grupy',
		no_groups_yet: 'Brak grup!',
		groups_tooltip: `Podczas tworzenia bezpiecznej ankiety możesz wybrać grupę uprawnionych respondentów. Aby stworzyć
			grupę, kliknij przycisk poniżej. Wszystkie utworzone grupy będą dostępne na tej stronie.`,
		group_name: 'Nazwa Grupy',
		everyone_has_keys:
			'Każdy członek tej grupy wygenerował klucze. Ta grupa może być wykorzystana w bezpiecznych ankietach.',
		not_everyone_has_keys:
			'Nie każdy członek tej grupy wygenerował klucze. Ta grupa nie może być wykorzystana w bezpiecznych ankietach.',
		max_groups_reached:
			'Osiągnięto maksymalną liczbę grup możliwych do utworzenia. Usuń któreś z istniejących, aby utworzyć nowe.',

		create_group: 'Stwórz grupę',
		create_group_stop: 'Przestań tworzyć grupę',
		delete_selected_groups: 'Usuń wybrane grupy',
		enter_group_name: 'Wprowadź nazwę grupy',
		select_group_members: 'Wybierz członków grupy',
		save_group: 'Zapisz grupę',
		import_members_title: 'Importuj członków grupy z pliku .csv',
		import_members_label: 'Lub importuj członków grupy z pliku .csv.',
		members_error: 'Wybierz członkow grupy.',

		group_error_name_required: 'Wprowadź nazwę grupy.',
		group_error_name_too_long: `Nazwa grupy musi mieć {$LIMIT_OF_CHARS} lub mniej znaków.`,
		group_error_already_exists: 'Grupa o tej nazwie już istnieje.',
		group_error_name_invalid:
			'Nazwa gupy może zawierać tylko litery, cyfry, spacje, ukośniki i łączniki.',

		removing_group_members: 'Usuwanie członków grupy',
		add_group_members: 'Dodaj członków grupy',
		add_group_members_stop: 'Przestań dodawać członków grupy',
		members: 'Członkowie',
		remove_selected_members: 'Usuń wybranych członków grupy',
		select_mebers: 'Wybierz członków grupy',
		add_members_finish: 'Zakończ dodawanie członków grupy',
		group_members: 'Członkowie grupy',
		no_members_yet: 'Brak członków grupy!',
		user_has_keys: 'Ten użytkownik posiada klucze.',
		user_has_no_keys: 'Ten użytkownik nie posiada kluczy.'
	}
};
