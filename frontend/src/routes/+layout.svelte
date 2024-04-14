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
		min-height: 100%;
		width: 50%;
		margin: auto;
		margin-top: 2em;
		border: 1px solid #999999;
		box-shadow: 0px 4px 4px #1a1a1a;
		background-color: #2a2a2a;
		font-size: 1em;
		font-weight: normal;
		font-family: 'Jura';
		color: #eaeaea;
	}

	nav {
		display: flex;
		flex-flow: row;
		justify-content: space-around;
		background-color: #1a1a1a;
	}
</style>
