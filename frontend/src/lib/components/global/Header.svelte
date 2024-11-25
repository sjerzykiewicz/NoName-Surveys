<div class="header" id="header">
	<slot />
</div>

<style>
	.header {
		padding: 0.75em;
		border-bottom: 1px solid var(--border-color-1);
	}

	@media screen and (max-width: 768px) {
		.header {
			padding: 0.75em 0.25em;
		}
	}
</style>
