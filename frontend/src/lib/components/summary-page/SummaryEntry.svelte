<script lang="ts">
	export let title: string;
	export let code: string;
</script>

<div class="entry">
	<div class="entry-title">
		<a href="/{code}/summary">{title}</a>
	</div>
	<div class="entry-code">
		Access code: {code}
	</div>
</div>

<style>
	.entry {
		border: 1px solid var(--border-color);
		border-radius: 10px;
		color: var(--text-color);
		padding: 5px;
		padding-left: 10px;
		margin: 5px;
		margin-bottom: 15px;
	}

	a {
		padding: 0.5em 0 0.5em 0;
		text-align: center;
		color: var(--text-color);
		font-weight: bold;
		font-size: 1.5em;
		width: 100%;
		text-decoration: none;
	}
</style>
