<script lang="ts">
	import UsersTable from '../groups-page/group/UsersTable.svelte';
	export let respondents;
</script>

<div title="Respondents" class="title respondent-list" id="survey-respondents">
	The following users can submit answers to this survey:
</div>
<UsersTable users={respondents} title="Respondents" />

<style>
	.title.respondent-list {
		margin-top: 1em;
		margin-bottom: 0.1em;
	}
</style>
