<script lang="ts">
	import type { PageData } from '../../$types';

	export let data: PageData;
</script>

<div class="content">
	<h2>Survey created succesfully.</h2>
	<p>Access code:</p>
	<h1>{data.code}</h1>
</div>

<style>
	.content {
		text-align: center;
		text-shadow: 0px 4px 4px var(--shadow-color);
		color: var(--text-color);
		font-size: 3em;
		font-weight: bold;
		margin-bottom: 1em;
		cursor: default;
	}
</style>
