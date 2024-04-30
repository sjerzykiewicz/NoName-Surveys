<script lang="ts">
	import '../app.css';

	import NavBar from '$lib/components/NavBar.svelte';
	import ScrollToTop from '$lib/components/ScrollToTop.svelte';
</script>

<NavBar />
<div class="box">
	<slot />
</div>
<ScrollToTop />

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

	@media screen and (max-width: 767px) {
		.box {
			width: 100%;
			min-width: 0px;
			margin-top: 0px;
			border: none;
			border-top: 1px solid #999999;
		}
	}
</style>
