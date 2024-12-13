<script lang="ts">
	import Header from '$lib/components/global/Header.svelte';
	import Content from '$lib/components/global/Content.svelte';
	import Footer from '$lib/components/global/Footer.svelte';
	import OpenSourceInfo from '$lib/components/global/OpenSourceInfo.svelte';
	import Back from '$lib/components/global/Back.svelte';
	import Faq from '$lib/components/account-page/Faq.svelte';
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
		<Faq id="public" icon="public" q="faq_public_survey_q" a="faq_public_survey_a" />
		<Faq id="secure" icon="encrypted" q="faq_secure_survey_q" a="faq_secure_survey_a" />
		<Faq id="keys" icon="key" q="faq_keys_q" a="faq_keys_a" />
		<Faq id="ring" icon="graph_6" q="faq_ring_q" a="faq_ring_a" />
		<Faq id="authorize" icon="login" q="faq_authorize_q" a="faq_authorize_a" />
		<Faq id="personal" icon="badge" q="faq_personal_q" a="faq_personal_a" />
		<Faq id="code" icon="qr_code_2" q="faq_code_q" a="faq_code_a" />
		<Faq id="create" icon="edit" q="faq_create_q" a="faq_create_a" />
		<Faq id="draft" icon="save" q="faq_draft_q" a="faq_draft_a" />
		<Faq id="group" icon="group" q="faq_group_q" a="faq_group_a" />
		<Faq id="import-users" icon="csv" q="faq_import_users_q" a="faq_import_users_a" />
		<Faq id="secure-group" icon="group_off" q="faq_secure_group_q" a="faq_secure_group_a" />
		<Faq id="limit-answers" icon="mail_lock" q="faq_limit_answers_q" a="faq_limit_answers_a" />
		<Faq id="survey-time" icon="calendar_month" q="faq_survey_time_q" a="faq_survey_time_a" />
		<Faq id="summary" icon="bar_chart" q="faq_summary_q" a="faq_summary_a" />
		<Faq id="import_summary" icon="file_json" q="faq_import_summary_q" a="faq_import_summary_a" />
		<Faq id="limit-items" icon="block" q="faq_limit_items_q" a="faq_limit_items_a" />
		<Faq id="anonymous" icon="shield_person" q="faq_anonymous_q" a="faq_anonymous_a" />
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
