export const data = {
	en: {
		// question types

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
		binary_yes: 'Yes',
		binary_no: 'No',
		text_text: 'Text',
		text_title: 'Open question',
		number_text: 'Number',
		number_title: 'Numerical question',

		// other

		submit: 'Submit',
		error: 'Error',
		unknown_error: 'Unknown error',
		something_went_wrong: 'Something went wrong',
		warning: 'Warning',
		success: 'Success',
		welcome: 'Welcome',
		generate: 'Generate',
		cancel: 'Cancel',
		delete: 'Delete',
		sign_in: 'Sign In',
		sign_in_lower: 'Sign in',
		sign_out: 'Sign Out',
		public: 'Public',
		secure: 'Secure',
		select_all: 'Select all',
		creation_date: 'Creation Date',
		access_code: 'Access Code',
		code: 'Code',
		copy_link: 'Copy link',
		copy_link_title: 'Copy the link',
		copy_code: 'Copy code',
		copy_code_title: 'Copy the code',
		copied: 'Copied!',
		no_copy_insecure_connection: 'Could not copy due to an insecure connection.',
		limit_reached:
			'You have reached the maximum number of {items}. Please delete some {items} to create new ones',
		limit_reached_title: '{items} limit reached',
		info_about_leaving:
			'Are you sure you want to leave this page?\nLeaving will discard all unsaved changes.',
		info_about_deleting: 'Are you sure you want to delete selected entries?',
		message: 'Message',
		error_message: 'Something went wrong, please contact the administrator.',
		show_account_options: 'Show account options',
		hide_account_options: 'Hide account options',
		dark_theme: 'Dark Theme',
		light_theme: 'Light Theme',
		toggle_theme: 'Toggle theme',
		toggle_lang: 'Toggle language',
		other_lang: 'Polish',
		scroll_to_top: 'Scroll to the top',
		signed_out: 'Signed Out',
		signed_out_info: 'You are signed out',
		sign_out_alert: 'Sign out to ensure security while filling out the survey.',
		sign_in_info: 'to access ',
		and: 'and',
		or: 'Or',
		select: 'Select',
		open: 'Open',
		rename: 'Rename',
		close_menu: 'Close menu',
		open_menu: 'Open menu',
		read_more: 'Read more...',
		slogan: 'Unlock true anonymity with the power of ring signatures!',
		open_source_info: 'Our project is open source. You can find the source code on ',
		hotkeys_info: `You can create surveys faster by using hotkeys.<br />
			Hold <span class="accent">[ LeftAlt ]</span> and press:<br />
			<span class="accent">[ 1 - 9 ]</span> - Add various question types<br />
			<span class="accent">[ 0 ]</span> - Add previous question type<br />
			<span class="accent">[ Enter ]</span> / <span class="accent">[ Ins ]</span> - Add choice to selected question<br />
			<span class="accent">[ Bksp ]</span> / <span class="accent">[ Del ]</span> - Remove selected question or choice<br />
			<span class="accent">[ PgUp ]</span> / <span class="accent">[ PgDn ]</span> - Move selected question up or down<br />
			<span class="accent">[ ~ ]</span> / <span class="accent">[ \\ ]</span> - Toggle requirement for selected question<br />
			<span class="accent">[<i class="symbol">arrow_left</i>]</span> / <span class="accent">[<i class="symbol">arrow_right</i>]</span> - Select previous or next input<br />
			<span class="accent">[<i class="symbol">arrow_drop_up</i>]</span> / <span class="accent">[<i class="symbol">arrow_drop_down</i>]</span> - Select previous or next question<br />
			<span class="accent">[ Home ]</span> - Select Survey Title<br />
			<span class="accent">[ End ]</span> - Select Create button<br />
			Besides that, you can still use <span class="accent">[ Tab ]</span> and <span class="accent">[ Shift ]</span> + <span class="accent">[ Tab ]</span>.`,

		// questions

		question: 'Question',
		question_index: 'Question no. {index}',
		question_up: 'Move question up',
		question_down: 'Move question down',
		question_label: 'Question',
		question_title: 'Enter a question',
		question_required: 'Required',
		question_not_required: 'Not required',
		question_remove: 'Remove question',
		question_choose_type: 'Choose question type',
		question_choose_type_stop: 'Stop choosing question type',
		question_error_required: 'Please enter question no. {index}.',
		question_error_limit: 'Question no. {index} must be {limit} or less characters long.',
		question_no: 'Question no. {index}',
		question_details: 'Question details',

		// choices

		choice: 'Choice',
		choice_title: 'Enter a choice',
		choice_remove: 'Remove choice',
		choice_add: 'Add choice',
		rank_choice: 'Choice no. {index}',
		text_details_label: 'Question Details',
		text_details_title: 'Enter question details',
		number_min_title: 'Enter a minimum value',
		number_min_placeholder: 'Enter a minimum value...',
		number_min_placeholder_short: 'Enter a min value...',
		number_max_title: 'Enter a maximum value',
		number_max_placeholder: 'Enter a maximum value...',
		number_max_placeholder_short: 'Enter a max value...',
		slider_precision_title: 'Enter the precision',
		slider_precision_placeholder: 'Enter precision...',
		slider_precision_placeholder_short: 'Enter prec...',
		binary_positive_label: 'Positive Choice',
		binary_positive_title: 'Enter a positive choice',
		binary_negative_label: 'Negative Choice',
		binary_negative_title: 'Enter a negative choice',
		choice_error_required: 'Please enter all choices for question no. {index}.',
		choice_error_binary_required: 'Please enter both choices for question no. {index}.',
		choice_error_number_required: 'Please enter both values for question no. {index}.',
		choice_error_slider_required: 'Please enter all values for question no. {index}.',
		choice_error_limit: 'Choices must be {limit} or less characters long in question no. {index}.',
		choice_error_duplicate: 'Please remove duplicate choices from question no. {index}.',
		choice_error_slider_values:
			'Maximum value must be greater than minimum value in question no. {index}.',
		choice_error_slider_precision:
			'Precision must be lower than the range in question no. {index}.',
		other_choice: 'Other choice',
		minimum: 'Minimum',
		minimum_value: 'Minimum value',
		maximum: 'Maximum',
		maximum_value: 'Maximum value',
		precision: 'Precision',
		average: 'Average',
		selected_value: 'Selected value',
		ordered_by_average_place: 'Ordered by average place',
		average_choice_ranking: 'Average ranking',

		// drafts

		draft: 'Draft',
		drafts: 'Drafts',
		drafts_genitive: 'drafts',
		saving_draft: 'Saving Draft',
		saving_draft_alert: 'Do you wish to overwrite the draft or save a new draft?',
		overwrite_draft: 'Overwrite',
		overwrite_draft_title: 'Overwrite Draft',
		save_new_draft: 'Save New',
		save_new_draft_title: 'Save New Draft',
		your_drafts: 'Your drafts',
		number_of_drafts: 'Number of drafts',
		no_drafts_yet: 'No drafts yet!',
		draft_tooltip: `When creating a survey, you can save it as a draft for later use. To create a survey, click
			on the "Create" tab at the top of the page or the button below. All your saved drafts will
			be stored on this page.`,
		draft_title: 'Draft Title',
		deleting_drafts: 'Deleting Drafts',
		create_draft: 'Create a draft',
		delete_selected_drafts: 'Delete selected drafts',
		save_draft: 'Save draft',
		saved: 'Saved!',

		// surveys

		fill: 'Fill Out',
		survey: 'Survey',
		surveys: 'Surveys',
		surveys_genitive: 'surveys',
		code_info: 'Enter a survey code to fill it out',
		code_tooltip:
			'Enter the code provided to you by the survey creator. Your answers are completely anonymous.',
		submit_code: 'Submit the code',
		home_keys_info: `To fill out a secure survey, you must have generated keys.<br />
			If you do not have keys, authorize yourself and generate them in `,
		home_redirect: 'If you want to create your own survey,',
		home_redirect_account: 'first authorize yourself in ',
		home_redirect_create: 'go to ',
		survey_info: 'Survey Information',
		survey_title: 'Survey Title',
		survey_title_title: 'Enter a survey title',
		survey_title_error_required: 'Please enter survey title.',
		survey_title_error_limit: 'Survey title must be {limit} or less characters long.',
		fill_survey: 'Fill out the survey',
		submit_survey: 'Submit survey',
		your_surveys: 'Your surveys',
		number_of_surveys: 'Number of surveys',
		no_surveys_yet: 'No surveys yet!',
		surveys_tooltip: `To create a survey, click on the "Create" tab at the top of the page or the button below.
			All your created surveys will be stored on this page.`,
		survey_is_secure: 'This survey has an established group of possible respondents.',
		survey_is_public: 'Everyone can submit an answer to this survey.',
		survey_owner: 'You are the owner of this survey.',
		survey_shared: 'Results of this survey have been shared with you.',
		share_results: 'Share survey results',
		share: 'Share',
		respondents: 'Respondents',
		summary: 'Summary',
		view_summary: 'View the summary',
		view_respondents: 'View possible respondents',
		not_available_for_public: 'Not available for public survey',
		view_qr: 'View QR code',
		deleting_surveys: 'Deleting Surveys',
		create_survey: 'Create a survey',
		delete_selected_surveys: 'Delete selected surveys',
		survey_public_title: 'Public survey',
		survey_public_info:
			'This survey is public. Anyone can respond to it multiple times. You will not have to provide your keys.',
		survey_secure_title: 'Secure survey',
		survey_secure_info:
			'This survey is secure. Selected users can respond to it only once. You will have to provide your keys when submitting this survey.',
		survey_not_secure_title: 'Survey not secure',
		survey_not_secure: 'This survey is not secure.',
		only_respondent: ' You are the only person who can respond to this survey.',
		two_respondents:
			' There are only two people who can respond to this survey. The other person could be the creator of this survey.',
		survey_success: 'Survey Created Successfully!',
		public_key_not_on_list: 'Your public key is not on the list.',
		possible_respondents: 'Possible Respondents',
		possible_respondents_empty: 'No possible respondents to display!',
		define_respondent_group: 'Define Respondent Group',
		define_respondent_group_alert: 'Do you wish to make the survey public or secure?',
		define_respondent_group_error: 'Please define respondent group.',
		edit: 'Edit',
		edit_title: 'Edit survey',
		preview: 'Preview',
		preview_title: 'Preview survey',
		create: 'Create',
		create_title: 'Finish survey creation',
		invalid_summary: 'Invalid survey summary',

		// groups

		group: 'Group',
		groups: 'Groups',
		groups_genitive: 'groups',
		group_size: 'Group Size',
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
		deleting_groups: 'DeletingGroups',
		create_group: 'Create a group',
		create_group_stop: 'Stop creating a group',
		delete_selected_groups: 'Delete selected groups',
		enter_group_name: 'Enter a group name',
		save_group: 'Save the group',
		select_group: 'Select group',
		group_error_name_required: 'Please enter a group name.',
		group_error_name_too_long: `Group name must be {limit} or less characters long.`,
		group_error_already_exists: 'This group name already exists.',
		group_error_name_invalid:
			'Group name can only contain letters, numbers, spaces, slashes and hyphens.',
		rename_group: 'Rename Group',
		save_new_group_name_title: 'Save the new group name',
		keys_info_title: 'Keys Information',
		groups_info: `Before creating a secure survey, consider setting up a user group. User groups make it
			easy to select the same set of respondents across multiple surveys. However, if you
			prefer, you can proceed without using them.`,

		// users / members

		users: 'Users',
		members: 'Members',
		user_type: 'User type',
		owner: 'Owner',
		user_with_access: 'User with access',
		users_with_access: 'Users With Access',
		no_users_with_access: 'No users with access to display!',
		removing_access: 'Removing access',
		give_access: 'Give access',
		stop_giving_access: 'Stop giving access',
		finish_giving_access: 'Finish giving access',
		take_away_access: 'Take away access from selected users',
		select_users: 'Select users',
		error_select_users: 'Please select users.',
		select_group_members: 'Select group members',
		members_error: 'Please select group members.',
		removing_group_members: 'Removing group members',
		remove_group_members: 'Remove group members',
		add_group_members: 'Add group memebers',
		add_group_members_stop: 'Stop adding group members',
		remove_selected_members: 'Remove selected group members',
		add_members_finish: 'Finish adding group members',
		group_members: 'Group Members',
		no_members_yet: 'No group members yet!',
		user_has_keys: 'This user has already generated their keys.',
		user_has_no_keys: 'This user has not generated their keys yet.',
		create_option: 'Create this option',
		default_disabled_title: 'This option is disabled',
		disabled_input_title: 'This input is disabled',
		no_matching_options: 'No matching options',
		duplicate_options: 'This option is already selected',
		remove_all_title: 'Remove all',
		remove_btn_title: 'Remove',

		// answers

		answer: 'Answer',
		answers: 'Answers',
		select_answer: 'Select your answer',
		select_no_answer: 'Not answered',
		enter_answer: 'Enter your answer',
		answer_question_no: 'Please answer question no. {index}.',
		move_answer_up: 'Move answer up',
		move_answer_down: 'Move answer down',
		answer_submit_success: 'Your answer has been submitted successfully.',
		no_answers_yet: 'No answers yet!',
		no_answer_yet: 'No {index}. answer yet!',
		no_answers_to_question: 'No answers to this question yet.',
		question_not_answered: 'The respondent has not answered this question.',
		number_of_answers: 'Number of answers: {number}',
		number_of_answers_title: 'Number of answers',
		answer_no: 'Answer no. {index}',
		view_answer_no: 'View answer no. {index}',
		selected_answer: 'Selected answer',
		click_to_get_answers: 'Click to display all answers',
		view_individual_answers: 'View individual answers',
		clear_answer_title: 'Clear the answer',
		clear_answer: 'Clear',
		dont_answer: 'Do not answer',

		// pages

		first_page: 'First page',
		previous_page: 'Previous page',
		current_page: 'Current page',
		next_page: 'Next page',
		last_page: 'Last page',
		back: 'Back',
		back_title: 'Go back',

		// files

		export: 'Export',
		export_invalid_emails: 'Export invalid emails',
		export_survey_summary: 'Export survey summary',
		import: 'Import',
		import_survey_summary: 'Import survey summary',
		import_users_title: 'Import users from a .csv file',
		import_users_label: 'Or import users from a .csv file',
		import_members_title: 'Import group members from a .csv file',
		import_members_label: 'Or import group members from a .csv file',
		import_summary_title: 'Import survey summary from a .json file',
		importing_summary: 'Importing Summary',
		importing_summary_alert: 'Select an earlier exported survey summary file in .json format.',
		some_users_not_registered: `they have not registered yet`,
		some_users_without_keys: `they have not generated keys yet`,
		could_not_import_emails: `Could not import {number} users, because {reason}.
			You can export the list of invalid users if you want.`,
		warning_no_file: 'No file selected.',
		warning_file_not_csv: 'File must be in .csv format.',
		error_no_file: 'Please select a file.',
		error_file_not_bin: 'Please select a .bin file.',
		error_file_not_json: 'Please select a .json file.',
		select_file: 'Select File',
		load_keys_title: 'Load your keys',
		load_keys: 'Load your digital signature keys',
		submit_keys: 'Submit keys',
		submit_file: 'Submit file',
		key_file_label: `Please load the file which you have previously generated on this application. The file
			contains your keys, necessary for cryptographic calculations which are needed for validating
			your right to fill out this survey.`,
		default_filename: 'Default filename',
		no_file_selected: 'No file selected',
		passphrase_title: 'Enter a passphrase',
		incorrect_passphrase: 'Incorrect passphrase.',
		error_empty_passphrase: 'Passphrase cannot be empty.',
		error_passphrase_confirm_no_match: 'Passphrases are not the same',
		provide_passphrase:
			'Please provide a passphrase to protect your keys on your device. Remember it, as it will be required to load your keys each time.',
		confirm_passphrase: 'Confirm passphrase',
		enter_passphrase: 'Enter passphrase to the file.',
		example_csv: `A valid .csv file should not contain a headline. Each email should be placed in a new line and separated by a comma or a semicolon.<br /><br />
			Example:<br />
			user1@st.amu.edu.pl,<br />
			user2@st.amu.edu.pl;<br />
			user3@amu.edu.pl`,

		// faq

		faq_title: 'Frequently Asked Questions',
		faq_public_survey_q: 'What is a public survey?',
		faq_public_survey_a: `A public survey is a survey that can be filled out multiple times by anyone with an access code.
			It is as safe as a secure survey. You do not need to authorize or generate keys to fill out a public survey.`,
		faq_secure_survey_q: 'What is a secure survey?',
		faq_secure_survey_a: `A secure survey is a survey that can be filled out only once by a selected group of respondents.
			You need to authorize at least once and generate keys which are needed to fill out a secure survey.
			After generating keys, you do not need to authorize again.`,
		faq_keys_q: 'What are digital signature keys?',
		faq_keys_a: `Digital signature keys are a pair of cryptographic, asymmetric keys that are used to sign and verify digital information via ring signatures.
			They are used in secure surveys to ensure the anonymity of the respondents and their right to answer a given survey.
			You can generate your keys in the "Account" tab after authorizing yourself. You will be asked to provide a passphrase to protect your keys.
			Remember it, as it will be required each time you load your keys. Make sure to generate new keys every year for increased security.`,
		faq_ring_q: 'What is a ring signature?',
		faq_ring_a: `Ring signature is a cryptographic scheme that allows a spontaneous creation of a group of users.
			Each of these users can then generate a signature that makes it possible to verify if they are members of this group, without revealing their identity.
			The linkable variant of ring signature additionally allows for determining whether two signed messages come from the same group member.`,
		faq_authorize_q: 'Why can I not sign in?',
		faq_authorize_a: `Only AMU employees and students are allowed to authorize in this instance of our application.
			If you are from AMU and are still having trouble signing in, it may be due to a problem with the AMU USOS authorization system.
			You can try clearing your cookies or contacting an administrator. You can also try again later.`,
		faq_personal_q: 'Can other users see my personal data?',
		faq_personal_a: `No, other users cannot see your personal data. If you choose to authorize yourself,
			then the only information that is visible to other authorized users is your email address.`,
		faq_code_q: 'What is an access code?',
		faq_code_a: `An access code is a unique 6-digit code that is generated when you create a survey.
			It is used to start filling out a survey. You can share this code with others to allow them to fill out your survey.`,
		faq_create_q: 'How do I create a survey?',
		faq_create_a: `To create a survey, click on the "Create" tab at the top of the page. You will be asked to provide a title for your survey
			and then you can start adding questions. You can choose from a variety of question types. You can toggle the requirement of answer to each question.
			You can also preview your survey and save it as a draft for later editing. When you are ready,
			you can finish creating your survey by clicking the "Create" button. Then you will have to choose between making your survey public or secure.
			In case of a secure survey, you will have to define a group of possible respondents.`,
		faq_draft_q: 'What is a draft?',
		faq_draft_a: `A draft is a survey that you have started creating but have not yet finished. You can save your progress as a draft
			and come back to it later. You can also use the draft to create multiple surveys of the same structure.
			All your saved drafts can be accessed in the "Drafts" tab.`,
		faq_group_q: 'What is a group?',
		faq_group_a: `A group is a set of users that you can use in secure surveys. You can define a group of possible respondents
			and use it in multiple secure surveys. You can create a group in the "Groups" tab. You can also import users from a .csv file.`,
		faq_import_users_q: 'Why can I not import users?',
		faq_import_users_a: `You can only import users who have already registered. If you are trying to import users who have not registered yet,
			you will not be able to do so. If you are sure that the users have registered, then the problem may be with the file format.
			Make sure that you are importing a valid .csv file. A valid .csv file should not contain a headline.
			Each email should be placed in a new line and separated by a comma or a semicolon.<br /><br />
			Example:<br />
			user1@st.amu.edu.pl,<br />
			user2@st.amu.edu.pl;<br />
			user3@amu.edu.pl`,
		faq_secure_group_q: 'Why can I not create a secure survey for a group I have created?',
		faq_secure_group_a: `You cannot create a secure survey for a group if not all users in this group have generated their keys.
			You can check the status of the users' keys in the "Groups" tab by clicking the group name.`,
		faq_limit_answers_q: 'Can I limit the number of answers a user can submit to a public survey?',
		faq_limit_answers_a: `No, you cannot limit the number of answers a user can submit to a public survey.
			This is only possible in secure surveys. In a public survey, anyone can submit an answer multiple times.`,
		faq_survey_time_q: 'Can I set a start and end time for a survey?',
		faq_survey_time_a: `No, you cannot set a start and end time for a survey. However, it is your choice when you share the access code with other users.
			If you want to limit the time when the survey is available, you can export the survey summary into a file and delete the survey.`,
		faq_summary_q: 'What is a survey summary?',
		faq_summary_a: `A survey summary is a collection of all the answers to a survey. You can view the averages of the answers to each question,
			as well as each individual answer. To access the survey summary, click on the "Surveys" tab at the top of the page and then click on the survey title.
			You can also share the results with others and export the summary to a .json file. In case of secure surveys you can view the possible respondents.`,
		faq_import_summary_q: 'How do I import a survey summary?',
		faq_import_summary_a: `To import a survey summary, click on the "Surveys" tab at the top of the page and then click on the "Import" button.
			You will be asked to select a file. The file must be in .json format. You can import a survey summary that you have previously exported.
			Make sure that the survey summary was exported from this application.`,
		faq_limit_items_q:
			'Is there a limit to the number of drafts, surveys, and groups I can create?',
		faq_limit_items_a: `Yes, there is a limit to the number of drafts, surveys, and groups you can create. You can check the number of items you have created on the "Drafts",
			"Surveys", and "Groups" pages in the top right corner. If you have reached the limit, you will have to delete some items to create new ones.`,
		faq_anonymous_q: 'Are the answers to surveys actually anonymous?',
		faq_anonymous_a: `Yes, the answers to surveys are fully anonymous. We do not store any data that could be used to identify the respondent. The answers are stored in a way
			that makes it impossible to link them to the respondent. This is possible thanks to the use of digital signature keys and ring signatures.
			If you still have doubts, you can check the source code of our application. Click on the GitHub link at the bottom of the page.`,

		// account

		account: 'Account',
		your_account: 'Your account',
		account_sign_in: 'Authorize yourself with AMU USOS:',
		account_info: `We do not recommend signing in if you only wish to fill out a public survey. For secure surveys, if you
			have already generated your digital signature keys, signing in is also not necessary.`,
		keys_generated: 'You have already generated your keys.',
		keys_not_generated: 'You have not generated your keys yet.',
		account_generating_keys: 'Generating Keys',
		account_new_key_alert: `Generating new keys will take away your ability to answer existing secure surveys.
			Make sure you have answered all the surveys you wanted before generating new keys.`,
		account_new_key: 'Generate New Keys',
		account_generate_info:
			'Generated file contains your public and private keys. Do not share this file with anyone. It is your responsibility to keep it safe.',
		account_last_key_update: 'Last key update',
		account_key_update_info:
			'In order to increase security, we recommend generating a new key pair every year.',
		account_expiration_warning: 'Key expiration warning',
		account_expiration_critical: 'Key expiration critical warning',
		account_keys_expire_soon:
			'Your keys have been generated {number} days ago.<br />We recommend generating a new pair soon.',
		account_keys_expired:
			'Your keys have been generated {number} days ago.<br />Please generate a new pair for increased security.',
		account_info_title: 'Account information',
		account_authorization_info: `Authorizing yourself will enable you to:
			<ul class="account-ul">
				<li class="account-li">
					<div class="account-icon"><i class="symbol">encrypted</i></div>
					<div>
						Generate <span class="account-accent">digital signature keys</span> that allow you to participate
						in
						<span class="account-accent">secure surveys</span> without the need to sign in each time,
					</div>
				</li>
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
						<span class="account-accent">user groups</span>.
					</div>
				</li>
			</ul>`,
		account_keys_info_title: 'Digital signature keys information',
		account_keys_info: `Important information about digital signature keys:
			<ul class="account-ul">
				<li class="account-li">
					<div class="account-icon"><i class="symbol">encrypted</i></div>
					<div>
						Generating them allows you to participate in <span class="account-accent">secure surveys</span> and remain fully anonymous,
					</div>
				</li>
				<li class="account-li">
					<div class="account-icon"><i class="symbol">graph_6</i></div>
					<div>
						They are being utilized in <span class="account-accent">ring signatures</span>,
					</div>
				</li>
				<li class="account-li">
					<div class="account-icon"><i class="symbol">contract_edit</i></div>
					<div>
						When answering a secure survey, you will have to provide these keys to your browser for a
						<span class="account-accent">digital signature</span>,
					</div>
				</li>
				<li class="account-li">
					<div class="account-icon"><i class="symbol">account_circle_off</i></div>
					<div>
						After generating them, you do not need to be signed in to participate in <span class="account-accent">secure surveys</span>,
					</div>
				</li>
				<li class="account-li">
					<div class="account-icon"><i class="symbol">priority_high</i></div>
					<div>
						If you are not going to take part in <span class="account-accent">secure surveys</span>, there is no need to generate them.
					</div>
				</li>
			</ul>`
	},

	pl: {
		// question types

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
		binary_yes: 'Tak',
		binary_no: 'Nie',
		text_text: 'Tekstowe',
		text_title: 'Pytanie otwarte',
		number_text: 'Liczbowe',
		number_title: 'Pytanie numeryczne',

		// other

		submit: 'Zatwierdź',
		error: 'Błąd',
		unknown_error: 'Nieznany błąd',
		something_went_wrong: 'Coś poszło nie tak',
		warning: 'Ostrzeżenie',
		success: 'Sukces',
		welcome: 'Witaj',
		generate: 'Generuj',
		cancel: 'Anuluj',
		delete: 'Usuń',
		sign_in: 'Zaloguj się',
		sign_in_lower: 'Zaloguj się',
		sign_out: 'Wyloguj się',
		public: 'Publiczna',
		secure: 'Bezpieczna',
		select_all: 'Wybierz wszystko',
		creation_date: 'Data utworzenia',
		access_code: 'Kod dostępu',
		code: 'Kod',
		copy_link: 'Kopiuj link',
		copy_link_title: 'Skopiuj link',
		copy_code: 'Kopiuj kod',
		copy_code_title: 'Skopiuj kod',
		copied: 'Skopiowano!',
		no_copy_insecure_connection: 'Kopiowanie nie powiodło się z powodu niebezpiecznego połączenia.',
		limit_reached:
			'Osiągnięto maksymalną liczbę {items}. Usuń niektóre z istniejących {items} aby utworzyć nowe.',
		limit_reached_title: 'Osiągnięto maksymalną liczbę {items}',
		info_about_leaving:
			'Czy na pewno chcesz opuścić tę stronę?\nOpuszczenie spowoduje utratę wszystkich niezapisanych zmian.',
		info_about_deleting: 'Czy na pewno chcesz usunąć wybrane wpisy?',
		message: 'Wiadomość',
		error_message: 'Coś poszło nie tak, skontaktuj się z administratorem.',
		show_account_options: 'Pokaż opcje konta',
		hide_account_options: 'Ukryj opcje konta',
		dark_theme: 'Ciemny motyw',
		light_theme: 'Jasny motyw',
		toggle_theme: 'Zmień motyw',
		toggle_lang: 'Zmień język',
		other_lang: 'Angielski',
		scroll_to_top: 'Przewiń na samą górę',
		signed_out: 'Wylogowany',
		signed_out_info: 'Jesteś wylogowany',
		sign_out_alert: 'Wyloguj się, aby zapewnić bezpieczeństwo podczas wypełniania ankiety.',
		sign_in_info: 'aby uzyskać dostęp do ',
		and: 'i',
		or: 'Lub',
		select: 'Wybierz',
		open: 'Otwórz',
		rename: 'Zmień nazwę',
		close_menu: 'Zamknij menu',
		open_menu: 'Otwórz menu',
		read_more: 'Czytaj więcej...',
		slogan: 'Zyskaj pełną anonimowość dzięki potędze podpisów pierścieniowych!',
		open_source_info: 'Nasz projekt jest open source. Kod źródłowy znajdziesz na ',
		hotkeys_info: `Możesz tworzyć ankiety szybciej używając skrótów klawiszowych.<br />
			Przytrzymaj <span class="accent">[ LeftAlt ]</span> i naciśnij:<br />
			<span class="accent">[ 1 - 9 ]</span> - Dodaj różne typy pytań<br />
			<span class="accent">[ 0 ]</span> - Dodaj poprzedni typ pytania<br />
			<span class="accent">[ Enter ]</span> / <span class="accent">[ Ins ]</span> - Dodaj wybór do zaznaczonego pytania<br />
			<span class="accent">[ Bksp ]</span> / <span class="accent">[ Del ]</span> - Usuń zaznaczone pytanie lub wybór<br />
			<span class="accent">[ PgUp ]</span> / <span class="accent">[ PgDn ]</span> - Przesuń zaznaczone pytanie w górę lub w dół<br />
			<span class="accent">[ ~ ]</span> / <span class="accent">[ \\ ]</span> - Przełącz wymaganie dla zaznaczonego pytania<br />
			<span class="accent">[<i class="symbol">arrow_left</i>]</span> / <span class="accent">[<i class="symbol">arrow_right</i>]</span> - Zaznacz poprzednie lub następne pole<br />
			<span class="accent">[<i class="symbol">arrow_drop_up</i>]</span> / <span class="accent">[<i class="symbol">arrow_drop_down</i>]</span> - Zaznacz poprzednie lub następne pytanie<br />
			<span class="accent">[ Home ]</span> - Zaznacz Tytuł ankiety<br />
			<span class="accent">[ End ]</span> - Zaznacz przycisk Utwórz<br />
			Poza tym, nadal możesz używać <span class="accent">[ Tab ]</span> i <span class="accent">[ Shift ]</span> + <span class="accent">[ Tab ]</span>.`,

		// questions

		question: 'Pytanie',
		question_index: 'Pytanie nr {index}',
		question_up: 'Przesuń pytanie w górę',
		question_down: 'Przesuń pytanie w dół',
		question_label: 'Pytanie',
		question_title: 'Wprowadź pytanie',
		question_required: 'Wymagane',
		question_not_required: 'Nie wymagane',
		question_remove: 'Usuń pytanie',
		question_choose_type: 'Wybierz typ pytania',
		question_choose_type_stop: 'Przestań wybierać typ pytania',
		question_error_required: 'Proszę wprowadzić pytanie nr {index}.',
		question_error_limit: 'Pytanie nr {index} musi mieć {limit} lub mniej znaków.',
		question_no: 'Pytanie nr. {index}',
		question_details: 'Szczegóły pytania',

		// choices

		choice: 'Wybór',
		choice_title: 'Wprowadź wybór',
		choice_remove: 'Usuń wybór',
		choice_add: 'Dodaj wybór',
		rank_choice: 'Wybór nr {index}',
		text_details_label: 'Szczegóły pytania',
		text_details_title: 'Wprowadź szczegóły pytania',
		number_min_title: 'Podaj minimalną wartość',
		number_min_placeholder: 'Podaj minimum...',
		number_min_placeholder_short: 'Podaj min...',
		number_max_title: 'Podaj maksymalną wartość',
		number_max_placeholder: 'Podaj maksimum...',
		number_max_placeholder_short: 'Podaj maks...',
		slider_precision_title: 'Podaj precyzję',
		slider_precision_placeholder: 'Podaj precyzję...',
		slider_precision_placeholder_short: 'Podaj prec...',
		binary_positive_label: 'Pozytywny wybór',
		binary_positive_title: 'Wprowadź pozytywny wybór',
		binary_negative_label: 'Negatywny wybór',
		binary_negative_title: 'Wprowadź negatywny wybór',
		choice_error_required: 'Proszę wprowadzić wszystkie wybory dla pytania nr {index}.',
		choice_error_binary_required: 'Proszę wprowadzić oba wybory dla pytania nr {index}.',
		choice_error_number_required: 'Proszę wprowadzić obie wartości dla pytania nr {index}.',
		choice_error_slider_required: 'Proszę wprowadzić wszystkie wartości dla pytania nr {index}.',
		choice_error_limit: 'Wybory muszą mieć {limit} lub mniej znaków w pytaniu nr {index}.',
		choice_error_duplicate: 'Proszę usunąć zduplikowane wybory z pytania nr {index}.',
		choice_error_slider_values:
			'Maksymalna wartość musi być większa niż minimalna wartość w pytaniu nr {index}.',
		choice_error_slider_precision: 'Precyzja musi być mniejsza niż zakres w pytaniu nr {index}.',
		other_choice: 'Inny wybór',
		minimum: 'Minimum',
		minimum_value: 'Wartość minimalna',
		maximum: 'Maksimum',
		maximum_value: 'Wartość maksymalna',
		precision: 'Precyzja',
		average: 'Średnia',
		selected_value: 'Wybrana wartość',
		ordered_by_average_place: 'Uporządkowane według średniej pozycji',
		average_choice_ranking: 'Średnia pozycja',

		// drafts

		draft: 'Szkic',
		drafts: 'Szkice',
		drafts_genitive: 'szkiców',
		saving_draft: 'Zapisywanie szkicu',
		saving_draft_alert: 'Chcesz nadpisać szkic czy zapisać nowy szkic?',
		overwrite_draft: 'Nadpisz',
		overwrite_draft_title: 'Nadpisz szkic',
		save_new_draft: 'Zapisz nowy',
		save_new_draft_title: 'Zapisz nowy szkic',
		your_drafts: 'Twoje szkice',
		number_of_drafts: 'Liczba szkiców',
		no_drafts_yet: 'Brak szkiców!',
		draft_tooltip: `Podczas tworzenia ankiety, możesz zapisać ją jako szkic do późniejszego wykorzystania. Aby stworzyć ankietę, wejdź
			w zakładkę "Utwórz" na górze strony lub kliknij przycisk poniżej. Wszystkie zapisane szkice będą dostępne na tej stronie.`,
		draft_title: 'Tytuł szkicu',
		deleting_drafts: 'Usuwanie szkiców',
		create_draft: 'Stwórz szkic',
		delete_selected_drafts: 'Usuń wybrane szkice',
		save_draft: 'Zapisz szkic',
		saved: 'Zapisano!',

		// surveys

		fill: 'Wypełnij',
		survey: 'Ankieta',
		surveys: 'Ankiety',
		surveys_genitive: 'ankiet',
		code_info: 'Podaj kod ankiety, by ją wypełnić',
		code_tooltip:
			'Wprowadź kod podany przez twórcę ankiety. Twoje odpowiedzi są w pełni anonimowe.',
		submit_code: 'Wyślij kod',
		home_keys_info: `By odpowiedzieć na bezpieczną ankietę, musisz mieć wygenerowane klucze.<br />
			Jeśli nie masz kluczy, zautoryzuj się i wygeneruj je w `,
		home_redirect: 'Jeśli chcesz utworzyć własną ankietę,',
		home_redirect_account: 'najpierw zautoryzuj się w ',
		home_redirect_create: 'przejdź do ',
		survey_info: 'Informacje o ankiecie',
		survey_title: 'Tytuł ankiety',
		survey_title_title: 'Wprowadź tytuł ankiety',
		survey_title_error_required: 'Proszę wprowadzić tytuł ankiety.',
		survey_title_error_limit: 'Tytuł ankiety musi mieć {limit} lub mniej znaków.',
		fill_survey: 'Wypełnij ankietę',
		submit_survey: 'Prześlij ankietę',
		your_surveys: 'Twoje ankiety',
		number_of_surveys: 'Liczba ankiet',
		no_surveys_yet: 'Brak ankiet!',
		surveys_tooltip: `Aby stworzyć ankietę, kliknij w zakładkę "Utwórz" na górze strony lub przycisk poniżej.
			Wszystkie stworzone ankiety będą dostępne na tej stronie.`,
		survey_is_secure: 'Ta ankieta ma określoną grupę możliwych respondentów.',
		survey_is_public: 'Każdy może przesłać odpowiedź do tej ankiety.',
		survey_owner: 'Jesteś właścicielem tej ankiety.',
		survey_shared: 'Wyniki tej ankiety zostały Tobie udostępnione.',
		share_results: 'Udostępnij wyniki ankiety',
		share: 'Udostępnij',
		respondents: 'Respondenci',
		summary: 'Podsumowanie',
		view_summary: 'Wyświetl podsumowanie',
		view_respondents: 'Wyświetl możliwych respondentów',
		not_available_for_public: 'Niedostępne dla ankiet publicznych',
		view_qr: 'Wyświetl kod QR',
		deleting_surveys: 'Usuwanie ankiet',
		create_survey: 'Stwórz ankietę',
		delete_selected_surveys: 'Usuń wybrane ankiety',
		survey_public_title: 'Ankieta publiczna',
		survey_public_info:
			'Ta ankieta jest publiczna. Każdy może odpowiedzieć na nią wielokrotnie. Nie będziesz musiał podawać swoich kluczy.',
		survey_secure_title: 'Ankieta bezpieczna',
		survey_secure_info:
			'Ta ankieta jest bezpieczna. Wybrani użytkownicy mogą odpowiedzieć na nią tylko raz. Będziesz musiał podać swoje klucze przy przesyłaniu tej ankiety.',
		survey_not_secure_title: 'Ankieta niebezpieczna',
		survey_not_secure: 'Ta ankieta nie jest bezpieczna.',
		only_respondent: ' Jesteś jedyną osobą, która może wypełnić tę ankietę.',
		two_respondents:
			' Tylko dwie osoby mogą wypełnić tę ankietę. Istnieje możliwość, że drugą osobą jest twórca ankiety.',
		survey_success: 'Ankieta utworzona pomyślnie!',
		public_key_not_on_list: 'Twój klucz publiczny nie znajduje się na liście',
		possible_respondents: 'Możliwi respondenci',
		possible_respondents_empty: 'Brak możliwych respondentów do wyświetlenia!',
		define_respondent_group: 'Zdefiniuj grupę respondentów',
		define_respondent_group_alert: 'Chcesz stworzyć ankietę publiczną czy bezpieczną?',
		define_respondent_group_error: 'Proszę zdefiniować grupę respondentów.',
		edit: 'Edytuj',
		edit_title: 'Edytuj ankietę',
		preview: 'Podgląd',
		preview_title: 'Podgląd ankiety',
		create: 'Utwórz',
		create_title: 'Zakończ tworzenie ankiety',
		invalid_summary: 'Niewłaściwe podsumowanie ankiety',

		// groups

		group: 'Grupa',
		groups: 'Grupy',
		groups_genitive: 'grup',
		group_size: 'Rozmiar grupy',
		your_groups: 'Twoje grupy',
		number_of_groups: 'Liczba grup',
		renaming: 'Zmienianie nazwy',
		enter_new_group_name: 'Wprowadź nową nazwę grupy',
		no_groups_yet: 'Brak grup!',
		groups_tooltip: `Podczas tworzenia bezpiecznej ankiety możesz wybrać grupę uprawnionych respondentów. Aby stworzyć
			grupę, kliknij przycisk poniżej. Wszystkie utworzone grupy będą dostępne na tej stronie.`,
		group_name: 'Nazwa grupy',
		everyone_has_keys:
			'Każdy członek tej grupy wygenerował klucze. Ta grupa może być wykorzystana w bezpiecznych ankietach.',
		not_everyone_has_keys:
			'Nie każdy członek tej grupy wygenerował klucze. Ta grupa nie może być wykorzystana w bezpiecznych ankietach.',
		max_groups_reached:
			'Osiągnięto maksymalną liczbę grup możliwych do utworzenia. Usuń któreś z istniejących, aby utworzyć nowe.',
		deleting_groups: 'Usuwanie grup',
		create_group: 'Stwórz grupę',
		create_group_stop: 'Przestań tworzyć grupę',
		delete_selected_groups: 'Usuń wybrane grupy',
		enter_group_name: 'Wprowadź nazwę grupy',
		save_group: 'Zapisz grupę',
		select_group: 'Wybierz grupę',
		group_error_name_required: 'Proszę wprowadzić nazwę grupy.',
		group_error_name_too_long: `Nazwa grupy musi mieć {limit} lub mniej znaków.`,
		group_error_already_exists: 'Ta nazwa grupy już istnieje.',
		group_error_name_invalid:
			'Nazwa grupy może zawierać tylko litery, cyfry, spacje, ukośniki i łączniki.',
		rename_group: 'Zmień nazwę grupy',
		save_new_group_name_title: 'Zapisz nową nazwę grupy',
		keys_info_title: 'Informacje o kluczach',
		groups_info: `Przed utworzeniem bezpiecznej ankiety, rozważ utworzenie grupy użytkowników. Grupy użytkowników ułatwiają wybór
			takiego samego zestawu respondentów w wielu ankietach. Możesz jednak kontynuować bez ich użycia, jeśli chcesz.`,

		// users / members

		users: 'Użytkownicy',
		members: 'Członkowie',
		user_type: 'Typ użytkownika',
		owner: 'Właściciel',
		user_with_access: 'Użytkownik z dostępem',
		users_with_access: 'Użytkownicy z dostępem',
		no_users_with_access: 'Brak użytkowników z dostępem do wyświetlenia!',
		removing_access: 'Usuwanie dostępu',
		give_access: 'Daj dostęp',
		stop_giving_access: 'Przestań dawać dostęp',
		finish_giving_access: 'Zakończ dawanie dostępu',
		take_away_access: 'Odbierz dostęp wybranym użytkownikom',
		select_users: 'Wybierz użytkowników',
		error_select_users: 'Proszę wybrać użytkowników.',
		select_group_members: 'Wybierz członków grupy',
		members_error: 'Proszę wybrać członków grupy.',
		removing_group_members: 'Usuwanie członków grupy',
		remove_group_members: 'Usuń członków grupy',
		add_group_members: 'Dodaj członków grupy',
		add_group_members_stop: 'Przestań dodawać członków grupy',
		remove_selected_members: 'Usuń wybranych członków grupy',
		add_members_finish: 'Zakończ dodawanie członków grupy',
		group_members: 'Członkowie grupy',
		no_members_yet: 'Brak członków grupy!',
		user_has_keys: 'Ten użytkownik wygenerował klucze.',
		user_has_no_keys: 'Ten użytkownik nie wygenerował kluczy.',
		create_option: 'Utwórz tę opcję',
		default_disabled_title: 'Ta opcja jest wyłączona',
		disabled_input_title: 'To pole jest wyłączone',
		no_matching_options: 'Brak pasujących opcji',
		duplicate_options: 'Ta opcja jest już wybrana',
		remove_all_title: 'Usuń wszystko',
		remove_btn_title: 'Usuń',

		// answers

		answer: 'Odpowiedź',
		answers: 'Odpowiedzi',
		select_answer: 'Wybierz swoją odpowiedź',
		select_no_answer: 'Nie odpowiedziano',
		enter_answer: 'Wprowadź swoją odpowiedź',
		answer_question_no: 'Proszę odpowiedzieć na pytanie nr. {index}.',
		move_answer_up: 'Przenieś odpowiedź w górę',
		move_answer_down: 'Przenieś odpowiedź w dół',
		answer_submit_success: 'Twoja odpowiedź została przesłana pomyślnie.',
		no_answers_yet: 'Brak odpowiedzi!',
		no_answer_yet: 'Brak odpowiedzi nr {index}!',
		no_answers_to_question: 'Brak odpowiedzi na to pytanie.',
		question_not_answered: 'Respondent nie udzielił odpowiedzi na to pytanie.',
		number_of_answers: 'Liczba odpowiedzi: {number}',
		number_of_answers_title: 'Liczba odpowiedzi',
		answer_no: 'Odpowiedź nr {index}',
		view_answer_no: 'Wyświetl odpowiedź nr {index}',
		selected_answer: 'Wybrana odpowiedź',
		click_to_get_answers: 'Kliknij, aby wyświetlić wszystkie odpowiedzi',
		view_individual_answers: 'Wyświetl indywidualne odpowiedzi',
		clear_answer_title: 'Wyczyść odpowiedź',
		clear_answer: 'Wyczyść',
		dont_answer: 'Nie udzielaj odpowiedzi',

		// pages

		first_page: 'Pierwsza strona',
		previous_page: 'Poprzednia strona',
		current_page: 'Aktualna strona',
		next_page: 'Następna strona',
		last_page: 'Ostatnia strona',
		back: 'Wróć',
		back_title: 'Wróć',

		// files

		export: 'Eksportuj',
		export_invalid_emails: 'Eksportuj niepoprawne emaile',
		export_survey_summary: 'Eksportuj podsumowanie ankiety',
		import: 'Importuj',
		import_survey_summary: 'Importuj podsumowanie ankiety',
		import_users_title: 'Importuj użytkowników z pliku .csv',
		import_users_label: 'Lub importuj użytkowników z pliku .csv',
		import_members_title: 'Importuj członków grupy z pliku .csv',
		import_members_label: 'Lub importuj członków grupy z pliku .csv',
		import_summary_title: 'Importuj podsumowanie ankiety z pliku .json',
		importing_summary: 'Importowanie podsumowania',
		importing_summary_alert:
			'Wybierz wcześniej wyeksportowany plik podsumowania ankiety w formacie .json.',
		some_users_not_registered: 'nie są zarejestrowani',
		some_users_without_keys: 'nie mają kluczy',
		could_not_import_emails: `Nie udało się zaimportować {number} użytkowników, ponieważ {reason}.
			Jeśli chcesz, możesz wyeksportować ich listę.`,
		warning_no_file: 'Nie wybrano pliku.',
		warning_file_not_csv: 'Plik musi być w formacie .csv.',
		error_no_file: 'Proszę wybrać plik.',
		error_file_not_bin: 'Proszę wybrać plik .bin.',
		error_file_not_json: 'Proszę wybrać plik .json.',
		select_file: 'Wybierz plik',
		load_keys_title: 'Załaduj swoje klucze',
		load_keys: 'Załaduj swoje klucze podpisu cyfrowego',
		submit_keys: 'Załaduj klucze',
		submit_file: 'Załaduj plik',
		key_file_label: `Załaduj plik, który wcześniej wygenerowałeś w tej aplikacji. Plik zawiera Twoje klucze, które są
			niezbędne do obliczeń kryptograficznych potrzebnych do weryfikacji Twojego prawa do wypełnienia tej ankiety.`,
		default_filename: 'Domyślna nazwa pliku: ',
		no_file_selected: 'Nie wybrano pliku',
		passphrase_title: 'Wprowadź hasło do pliku',
		incorrect_passphrase: 'Niepoprawne hasło.',
		error_empty_passphrase: 'Hasło nie może być puste.',
		error_passphrase_confirm_no_match: 'Hasła nie są takie same.',
		provide_passphrase:
			'Wprowadź hasło, które posłuży do ochrony kluczy na Twoim urządzeniu. Zapamiętaj je, gdyż będzie ono wymagane do każdego załadowania kluczy.',
		confirm_passphrase: 'Potwierdź hasło',
		enter_passphrase: 'Podaj hasło do pliku.',
		example_csv: `Poprawny plik .csv nie powinien zawierać nagłówka. Każdy email powinien być w osobnej linii oraz oddzielony przecinkiem lub średnikiem.<br /><br />
			Przykład:<br />
			user1@st.amu.edu.pl,<br />
			user2@st.amu.edu.pl;<br />
			user3@amu.edu.pl`,

		// faq

		faq_title: 'Często zadawane pytania',
		faq_public_survey_q: 'Czym jest publiczna ankieta?',
		faq_public_survey_a: `Publiczna ankieta jest ankietą, na którą może wielokrotnie odpowiedzieć każdy, kto zna jej kod dostępu.
			Jest tak samo anonimowa jak bezpieczna ankieta. Nie musisz się autoryzować lub generować kluczy, aby odpowiedzieć na publiczną ankietę.`,
		faq_secure_survey_q: 'Czym jest bezpieczna ankieta?',
		faq_secure_survey_a: `Bezpieczna ankieta jest ankietą, na którą może jednokrotnie odpowiedzieć wybrana grupa respondentów.
			Musisz się zautoryzować przynajmniej raz i wygenerować klucze, które są potrzebne do wypełnienia bezpiecznej ankiety.
			Po wygenerowaniu kluczy, nie musisz się autoryzować ponownie.`,
		faq_keys_q: 'Czym są klucze podpisu cyfrowego?',
		faq_keys_a: `Klucze podpisu cyfrowego są parą kryptograficznych, asymetrycznych kluczy, które są używane do podpisywania i weryfikacji cyfrowych informacji za pomocą podpisów pierścieniowych.
			Wykorzystywane są w bezpiecznych ankietach, aby zapewnić anonimowość respondentów i zweryfikować ich prawo do wypełnienia danej ankiety.
			Możesz wygenerować swoje klucze w zakładce "Konto" po zautoryzowaniu się. Będziesz poproszony o podanie hasła, które zabezpieczy Twoje klucze.
			Należy je zapamiętać, gdyż będzie ono wymagane do każdego załadowania kluczy. Generuj nowe klucze co roku, aby zwiększyć bezpieczeństwo.`,
		faq_ring_q: 'Czym jest podpis pierścieniowy?',
		faq_ring_a: `Podpis pierścieniowy to schemat kryptograficzny, który pozwala na spontaniczne utworzenie grupy użytkowników.
			Każdy z tych użytkowników może wtedy wygenerować podpis, który umożliwia weryfikację ich przynależności do tej grupy bez wyjawiania ich tożsamości.
			Wariant połączeniowy podpisu pierścieniowego dodatkowo pozwala na określenie czy dwie podpisane wiadomości pochodzą od tego samego członka grupy.`,
		faq_authorize_q: 'Czemu nie mogę się zautoryzować?',
		faq_authorize_a: `Tylko pracownicy i studenci UAM mogą zautoryzować się w tej instancji naszej aplikacji.
			Jeśli jesteś z UAM i nadal nie możesz się zautoryzować, może być to spowodowane problemami z systemem autoryzacyjnym USOS UAM.
			Możesz spróbować wyczyścić ciasteczka lub skontaktować się z administratorem. Możesz też spróbować ponownie później.`,
		faq_personal_q: 'Czy inni użytkownicy mogą zobaczyć moje dane osobowe?',
		faq_personal_a: `Nie, inni użytkownicy nie mogą zobaczyć twoich danych osobowych. Jeśli zdecydujesz się zautoryzować,
			wtedy jedyną informacją, która będzie widoczna dla innych zautoryzowanych użytkowników jest twój adres email.`,
		faq_code_q: 'Czym jest kod dostępu?',
		faq_code_a: `Kod dostępu to unikalny 6-cyfrowy kod, który jest generowany kiedy tworzysz ankietę.
			Jest on używany do wypełnienia ankiety. Możesz go udostępnić innym, aby mogli odpowiedzieć na twoją ankietę.`,
		faq_create_q: 'Jak mogę stworzyć ankietę?',
		faq_create_a: `Aby stworzyć ankietę, kliknij w zakładkę "Utwórz" na górze strony. Będziesz poproszony o podanie tytułu ankiety
			oraz pytań, które chcesz w niej zawrzeć. Możesz wybrać różnorodne typy pytań. Możesz przełączać wymaganie odpowiedzi dla każdego pytania.
			Możesz również zobaczyć podgląd swojej ankiety i zapisać ją jako szkic do późniejszej edycji. Kiedy będziesz gotowy,
			możesz zakończyć tworzenie ankiety klikając w przycisk "Utwórz". Wtedy będziesz musiał wybrać między ankietą publiczną i bezpieczną.
			W przypadku bezpiecznej ankiety, będziesz musiał wybrać grupę respondentów, którzy będą mogli na nią odpowiedzieć.`,
		faq_draft_q: 'Czym jest szkic?',
		faq_draft_a: `Szkic to ankieta, którą zacząłeś tworzyć, ale jej jeszcze nie ukończyłeś. Możesz zapisać swoje postępy jako szkic
			i wrócić do niegp później. Możesz także używać szkiców jako szablonów do tworzenia wielu ankiet o tej samej strukturze.
			Wszystkie zapisane szkice będą dostępne w zakładce "Szkice".`,
		faq_group_q: 'Czym jest grupa?',
		faq_group_a: `Grupa to zbiór użytkowników, którzy mogą być wykorzystani w bezpiecznych ankietach. Możesz zdefiniować grupę możliwych respondentów
			i używać ją w wielu ankietach. Możesz stworzyć grupę w zakładce "Grupy". Możesz również zaimportować użytkowników z pliku .csv.`,
		faq_import_users_q: 'Czemu nie mogę zaimportować użytkowników?',
		faq_import_users_a: `Możesz zaimportować jedynie użytkowników, którzy się już wcześniej zarejestrowali. Jeśli próbujesz zaimportować użytkowników, którzy się jeszcze nie zarejestrowali,
			nie będziesz mógł tego zrobić. Jeśli jesteś pewien, że użytkownicy są zarejestrowani, wtedy problemem może być format pliku.
			Upewnij się, że importujesz właściwy plik .csv. Właściwy plik .csv nie powinien zawierać nagłówka.
			Każdy email powinien być w osobnej linii oraz oddzielony przecinkiem lub średnikiem.<br /><br />
			Przykład:<br />
			user1@st.amu.edu.pl,<br />
			user2@st.amu.edu.pl;<br />
			user3@amu.edu.pl`,
		faq_secure_group_q:
			'Czemu nie mogę stworzyć bezpiecznej ankiety dla utworzonej wcześniej grupy?',
		faq_secure_group_a: `Nie możesz stworzyć bezpiecznej ankiety dla grupy, jeśli nie wszyscy członkowie tej grupy wygenerowali klucze.
			Możesz sprawdzić status kluczy członków grupy w zakładce "Grupy" poprzez kliknięcie w nazwę grupy.`,
		faq_limit_answers_q:
			'Czy mogę ograniczyć liczbę odpowiedzi jaką użytkownik może wysłać na publiczną ankietę?',
		faq_limit_answers_a: `Nie, nie możesz ograniczyć liczby odpowiedzi, jaką użytkownik może wysłać na publiczną ankietę.
			To jest możliwe jedynie w bezpiecznych ankietach. W publicznych ankietach każdy może odpowiedzieć wielokrotnie.`,
		faq_survey_time_q: 'Czy mogę ustawić czas, w którym ankieta będzie dostępna?',
		faq_survey_time_a: `Nie, nie możesz ustawić czasu, w którym ankieta będzie dostępna. Natomiast, do twojego wyboru należy kiedy udostępnisz jej kod dostępu innym użytkownikom.
			Jeśli chcesz ograniczyć czas, w którym ankieta jest dostępna, możesz wyeksportować podsumowanie ankiety do pliku i usunąć ankietę.`,
		faq_summary_q: 'Czym jest podsumowanie ankiety?',
		faq_summary_a: `Podsumowanie ankiety to kolekcja wszystkich odpowiedzi na daną ankietę. Możesz przeglądać średnie odpowiedzi do każdego pytania,
			jak i wszystkie indywidualne odpowiedzi. By sprawdzić podsumowanie ankiety, kliknij w zakładkę "Ankiety" na górze strony i kliknij w tytuł ankiety.
			Możesz też udostępnić wyniki ankiety innym użytkownikom i wyeksportować podsumowanie do pliku .json. W przypadku bezpiecznych ankiet, możesz też zobaczyć możliwych respondentów.`,
		faq_import_summary_q: 'Jak mogę zaimportować podsumowanie ankiety?',
		faq_import_summary_a: `By zaimportować podsumowanie ankiety, kliknij w zakładkę "Ankiety" na górze strony, a następnie kliknij przycisk "Importuj".
			Będziesz poproszony o wybranie pliku. Plik musi być w formacie .json. Możesz zaimportować podsumowanie ankiety, które wcześniej wyeksportowałeś.
			Upewnij się, że podsumowanie ankiety zostało wyeksportowane z tej aplikacji.`,
		faq_limit_items_q: 'Czy istnieje limit na liczbę szkiców, ankiet i grup, które mogę utworzyć?',
		faq_limit_items_a: `Tak, istnieje limit na liczbę szkiców, ankiet i grup, które możesz utworzyć. Możesz sprawdzić liczbę utworzonych pozycji w prawym górnym rogu strony
			w zakładkach "Szkice", "Ankiety" i "Grupy". Jeśli osiągniesz limit, nie będziesz mógł utworzyć nowych pozycji, dopóki nie usuniesz którejś z istniejących.`,
		faq_anonymous_q: 'Czy odpowiedzi na ankiety są naprawdę anonimowe?',
		faq_anonymous_a: `Tak, odpowiedzi na ankiety są w pełni anonimowe. Nie przechowujemy żadnych informacji, które mogłyby zostać użyte do zidentyfikowania respondenta. Odpowiedzi są przechowywane w taki sposób,
			że niemożliwe jest powiązanie ich z konkretnym użytkownikiem. Jest to możliwe dzięki użyciu kluczy podpisu cyfrowego i podpisów pierścieniowych.
			Jeśli wciąż masz wątpliwości, możesz sprawdzić kod źródłowy tej aplikacji. Kliknij w link do GitHuba na dole strony.`,

		// account

		account: 'Konto',
		your_account: 'Twoje konto',
		account_sign_in: 'Zautoryzuj się za pomocą USOS UAM:',
		account_info: `Nie zalecamy logowania się, jeśli chcesz jedynie wypełnić publiczną ankietę. W przypadku bezpiecznych ankiet, jeśli
			wygenerowałeś już klucze podpisu cyfrowego, logowanie się również nie jest konieczne.`,
		keys_generated: 'Klucze zostały już wygenerowane.',
		keys_not_generated: 'Nie wygenerowałeś jeszcze kluczy.',
		account_generating_keys: 'Generowanie kluczy',
		account_new_key_alert: `Wygenerowanie nowych kluczy spowoduje utratę możliwości odpowiedzi na istniejące bezpieczne ankiety.
			Upewnij się, że wypełniłeś wszystkie ankiety, które chciałeś, zanim wygenerujesz nowe klucze.`,
		account_new_key: 'Wygeneruj nowe klucze',
		account_generate_info:
			'Wygenerowany plik zawiera Twój publiczny i prywatny klucz. Nie udostępniaj nikomu tego pliku. Twoim obowiązkiem jest bezpieczne przechowanie go.',
		account_last_key_update: 'Ostatnia aktualizacja kluczy',
		account_key_update_info:
			'Aby zwiększyć bezpieczeństwo, zalecamy wygenerowanie nowej pary kluczy raz na rok.',
		account_expiration_warning: 'Ostrzeżenie o wygaśnięciu kluczy',
		account_expiration_critical: 'Krytyczne ostrzeżenie o wygaśnięciu kluczy',
		account_keys_expire_soon:
			'Twoje klucze zostały wygenerowane {number} dni temu.<br />Zalecamy wygenerowanie nowej pary.',
		account_keys_expired:
			'Twoje klucze zostały wygenerowane {number} dni temu.<br />Proszę wygenerować nową parę dla większego bezpieczeństwa.',
		account_info_title: 'Informacje o koncie',
		account_authorization_info: `Zautoryzowanie się pozwoli Ci na:
			<ul class="account-ul">
				<li class="account-li">
					<div class="account-icon"><i class="symbol">encrypted</i></div>
					<div>
						Generowanie <span class="account-accent">kluczy podpisu cyfrowego</span>, które pozwalają na uczestniczenie
						w <span class="account-accent">bezpiecznych ankietach</span> bez konieczności logowania się za każdym razem,
					</div>
				</li>
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
						Tworzenie i zarządzanie <span class="account-accent">grupami użytkowników</span>.
					</div>
				</li>
			</ul>`,
		account_keys_info_title: 'Informacje o kluczach podpisu cyfrowego',
		account_keys_info: `Ważne informacje o kluczach podpisu cyfrowego:
			<ul class="account-ul">
				<li class="account-li">
					<div class="account-icon"><i class="symbol">encrypted</i></div>
					<div>
						Wygenerowanie ich pozwala na uczestnictwo w <span class="account-accent">bezpiecznych ankietach</span> i pozostanie w pełni anonimowym,
					</div>
				</li>
				<li class="account-li">
					<div class="account-icon"><i class="symbol">graph_6</i></div>
					<div>
						Wykorzystywane są w <span class="account-accent">podpisach pierścieniowych</span>,
					</div>
				</li>
				<li class="account-li">
					<div class="account-icon"><i class="symbol">contract_edit</i></div>
					<div>
						Przy odpowiadaniu na bezpieczną ankietę, będziesz musiał podać te klucze swojej przeglądarce do
						<span class="account-accent">podpisu cyfrowego</span>,
					</div>
				</li>
				<li class="account-li">
					<div class="account-icon"><i class="symbol">account_circle_off</i></div>
					<div>
						Po ich wygenerowaniu, nie musisz być zalogowany, aby uczestniczyć w <span class="account-accent">bezpiecznych ankietach</span>,
					</div>
				</li>
				<li class="account-li">
					<div class="account-icon"><i class="symbol">priority_high</i></div>
					<div>
						Jeśli nie zamierzasz korzystać z <span class="account-accent">bezpiecznych ankiet</span>, nie ma potrzeby ich generować.
					</div>
				</li>
			</ul>`
	}
};
