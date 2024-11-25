<div class="content">
	<slot />
</div>

<style>
	.content {
		padding: 0.75em 0.75em 23.5em;
		flex: 1;
	}

	@media screen and (max-width: 768px) {
		.content {
			padding: 0.75em 0.25em 23.5em;
		}
	}
</style>
