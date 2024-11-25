<div class="footer">
	<slot />
</div>

<style>
	.footer {
		display: flex;
		flex-flow: row wrap;
		justify-content: flex-end;
		gap: 0.625em;
		position: fixed;
		bottom: 0;
		min-width: calc(768px - 1.5em);
		width: calc(50% - 1.5em);
		padding: 0.75em;
		border-top: 1px solid var(--border-color-1);
		background-color: var(--secondary-color-1);
		z-index: 1;
		transition: 0.2s;
	}

	@media screen and (max-width: 768px) {
		.footer {
			padding: 0.75em 0.25em;
			width: calc(100% - 0.5em);
			min-width: 0px;
		}
	}
</style>
