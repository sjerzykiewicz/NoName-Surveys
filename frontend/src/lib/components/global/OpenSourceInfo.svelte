<script lang="ts">
	import Tx from 'sveltekit-translate/translate/tx.svelte';

	const githubLink = 'https://github.com/sjerzykiewicz/NoName-Surveys';
</script>

<div class="open-source-info">
	<Tx text="open_source_info" />
	<a href={githubLink} target="_blank" title="GitHub">GitHub</a>.
</div>

<style>
	.open-source-info {
		width: 100%;
		text-align: center;
		font-size: 1.2em;
		color: var(--text-color-1);
		text-shadow: 0px 4px 4px var(--shadow-color-1);
		cursor: default;
		transition:
			0.2s,
			outline 0s;
	}

	@media screen and (max-width: 768px) {
		.open-source-info {
			font-size: 1em;
		}
	}
</style>
