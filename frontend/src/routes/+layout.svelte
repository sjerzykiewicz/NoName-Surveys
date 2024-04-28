<script>
	import NavLink from '$lib/components/NavLink.svelte';
</script>

<nav>
	<!-- TODO: move welcome page to root path -->
	<NavLink href="/welcome" title="Home" />
	<NavLink href="/create" title="Create" />
	<NavLink href="/pending" title="Pending" />
	<NavLink href="/summary" title="Summary" />
	<NavLink href="/account" title="Account" />
</nav>
<div class="box">
	<slot />
</div>

<style>
	.box {
		display: flex;
		flex-flow: column;
		height: auto;
		min-height: calc(100% - 5em);
		width: 50%;
		min-width: 767px;
		margin: auto;
		margin-top: 1.5em;
		border: 1px solid #999999;
		box-shadow: 0px 4px 4px #1a1a1a;
		background-color: #2a2a2a;
	}

	nav {
		display: flex;
		flex-flow: row;
		width: 100%;
		justify-content: space-around;
		background-color: #1a1a1a;
	}

	@media screen and (max-width: 767px) {
		.box {
			width: 100%;
			min-width: 0px;
			margin-top: 0px;
			border: none;
		}
	}

	@media screen and (max-width: 479px) {
		nav {
			flex-flow: column;
		}
	}
</style>
