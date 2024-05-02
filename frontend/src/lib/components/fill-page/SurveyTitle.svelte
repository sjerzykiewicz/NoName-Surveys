<script lang="ts">
	import { title } from '$lib/stores/fill-page';
</script>

<div title="Survey title" class="title">
	{$title}
</div>

<style>
	.title {
		flex: 1;
		text-shadow: 0px 4px 4px var(--box-shadow-color);
		font-size: 1.5em;
		font-weight: bold;
		font-family: 'Jura';
		color: var(--text-color);
		cursor: default;
		overflow: hidden;
	}

	@media screen and (max-width: 767px) {
		.title {
			font-size: 1.25em;
		}
	}
</style>
