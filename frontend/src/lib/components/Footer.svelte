<div class="footer">
	<slot />
</div>

<style>
	.footer {
		padding: 0.75em;
		border-top: 1px solid #999999;
		display: flex;
		flex-flow: row;
		justify-content: flex-end;
		position: fixed;
		bottom: 0;
		min-width: calc(767px - 1.5em);
		width: calc(50% - 1.5em);
		background-color: #2a2a2a;
	}

	@media screen and (max-width: 767px) {
		.footer {
			width: calc(100% - 1.5em);
			min-width: 0px;
		}
	}
</style>
