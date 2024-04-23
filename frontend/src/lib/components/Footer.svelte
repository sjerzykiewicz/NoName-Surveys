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
		align-items: center;
		position: fixed;
		bottom: 0;
		width: calc(50% - 1.5em);
		background-color: #2a2a2a;
	}
</style>
