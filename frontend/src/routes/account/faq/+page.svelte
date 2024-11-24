<script lang="ts">
	import Header from '$lib/components/global/Header.svelte';
	import Content from '$lib/components/global/Content.svelte';
	import Footer from '$lib/components/global/Footer.svelte';
	import OpenSourceInfo from '$lib/components/global/OpenSourceInfo.svelte';
	import Back from '$lib/components/global/Back.svelte';
	import FaqItem from '$lib/components/account-page/FaqItem.svelte';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);
</script>

<Header>
	<div title={$t('faq_title')} class="title static">
		<Tx text="faq_title" />
	</div>
</Header>

<Content>
	<div class="faq">
		<FaqItem
			id="public"
			icon="public"
			question={$t('faq_public_survey_q')}
			answer={$t('faq_public_survey_a')}
		/>
		<FaqItem
			id="secure"
			icon="encrypted"
			question={$t('faq_secure_survey_q')}
			answer={$t('faq_secure_survey_a')}
		/>
		<FaqItem id="keys" icon="key" question={$t('faq_keys_q')} answer={$t('faq_keys_a')} />
		<FaqItem
			id="authorize"
			icon="login"
			question={$t('faq_authorize_q')}
			answer={$t('faq_authorize_a')}
		/>
		<FaqItem
			id="personal"
			icon="badge"
			question={$t('faq_personal_q')}
			answer={$t('faq_personal_a')}
		/>
		<FaqItem id="code" icon="qr_code_2" question={$t('faq_code_q')} answer={$t('faq_code_a')} />
		<FaqItem id="create" icon="edit" question={$t('faq_create_q')} answer={$t('faq_create_a')} />
		<FaqItem id="draft" icon="save" question={$t('faq_draft_q')} answer={$t('faq_draft_a')} />
		<FaqItem id="group" icon="group" question={$t('faq_group_q')} answer={$t('faq_group_a')} />
		<FaqItem
			id="import-users"
			icon="csv"
			question={$t('faq_import_users_q')}
			answer="faq_import_users_a"
			html={true}
		/>
		<FaqItem
			id="secure-group"
			icon="group_off"
			question={$t('faq_secure_group_q')}
			answer={$t('faq_secure_group_a')}
		/>
		<FaqItem
			id="limit-answers"
			icon="mail_lock"
			question={$t('faq_limit_answers_q')}
			answer={$t('faq_limit_answers_a')}
		/>
		<FaqItem
			id="survey-time"
			icon="calendar_month"
			question={$t('faq_survey_time_q')}
			answer={$t('faq_survey_time_a')}
		/>
		<FaqItem
			id="summary"
			icon="bar_chart"
			question={$t('faq_summary_q')}
			answer={$t('faq_summary_a')}
		/>
		<FaqItem
			id="import_summary"
			icon="file_json"
			question={$t('faq_import_summary_q')}
			answer={$t('faq_import_summary_a')}
		/>
		<FaqItem
			id="limit-items"
			icon="block"
			question={$t('faq_limit_items_q')}
			answer={$t('faq_limit_items_a')}
		/>
		<FaqItem
			id="anonymous"
			icon="shield_person"
			question={$t('faq_anonymous_q')}
			answer={$t('faq_anonymous_a')}
		/>
	</div>
</Content>

<Footer>
	<div class="footer-box">
		<OpenSourceInfo />
		<Back />
	</div>
</Footer>

<style>
	.faq {
		display: flex;
		flex-direction: column;
		font-size: 1.1em;
		cursor: default;
		transition: 0.2s;
	}

	.footer-box {
		display: flex;
		align-items: center;
		width: 100%;
		gap: 0.5em;
	}

	@media screen and (max-width: 768px) {
		.faq {
			font-size: 1em;
		}
	}
</style>
