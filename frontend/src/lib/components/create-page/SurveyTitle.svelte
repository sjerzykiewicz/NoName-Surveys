<script lang="ts">
	import { title } from '$lib/stores/create-page';
</script>

<div title="Enter survey title" class="title-input" contenteditable bind:textContent={$title}>
	{$title}
</div>

<style>
	.title-input {
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

	.title-input[contenteditable]:empty::before {
		content: 'Enter survey title...';
		color: #eaeaea40;
	}

	@media screen and (max-width: 767px) {
		.title-input {
			font-size: 1.25em;
		}
	}
</style>
