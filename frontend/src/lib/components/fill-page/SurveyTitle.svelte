<script lang="ts">
	export let title: string = '';
</script>

<div title="Survey title" class="title">
	{title}
</div>

<style>
	.title {
		flex: 1;
		background-color: #1a1a1a;
		padding: 0.25em;
		border: 1px solid #999999;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		font-size: 1.5em;
		font-weight: bold;
		font-family: 'Jura';
		color: #eaeaea;
		cursor: text;
		overflow: hidden;
	}
</style>
