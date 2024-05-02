<script lang="ts">
	import { title } from '$lib/stores/fill-page';
</script>

<div title="Survey title" class="title">
	{$title}
</div>

<style>
	.title {
		flex: 1;
		background-color: var(--secondary-color);
		padding: 0.25em;
		border: 1px solid var(--border-color);
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--box-shadow-color);
		font-size: 1.5em;
		font-weight: bold;
		font-family: 'Jura';
		color: var(--text-color);
		cursor: text;
		overflow: hidden;
	}

	@media screen and (max-width: 767px) {
		.title {
			font-size: 1.25em;
		}
	}
</style>
