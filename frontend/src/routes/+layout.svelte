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
		min-height: calc(100% - 4.875em);
		width: 50%;
		min-width: 767px;
		margin: auto;
		margin-top: 1.5em;
		border: 1px solid var(--border-color);
		border-bottom: none;
		box-shadow: 0px 4px 4px var(--shadow-color);
		background-color: var(--secondary-color);
	}

	:root::-webkit-scrollbar {
		width: 1em;
	}

	:root::-webkit-scrollbar-track {
		background-color: var(--secondary-dark-color);
	}

	:root::-webkit-scrollbar-thumb {
		background-color: var(--primary-color);
		background-clip: padding-box;
		border-radius: 5px;
		border: 2px solid var(--secondary-dark-color);
	}

	:root::-webkit-scrollbar-thumb:hover {
		background-color: var(--text-dark-color);
	}

	:root::-webkit-scrollbar-thumb:active {
		background-color: var(--border-color);
	}

	@media screen and (max-width: 767px) {
		.box {
			width: 100%;
			min-width: 0px;
			min-height: calc(100% - 5.175em);
			margin-top: 0px;
			border-left: none;
			border-right: none;
		}
	}
</style>
