<div class="box">
	<slot />
</div>

<style>
	.box {
		display: flex;
		flex-flow: column;
		height: auto;
		min-height: 100%;
		width: 50%;
		margin: auto;
		margin-top: 3em;
		border: 1px solid #eaeaea;
		box-shadow: 0px 4px 4px #1a1a1a;
		background-color: #2a2a2a;
	}
</style>
