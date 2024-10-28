<script lang="ts">
	import '../app.css';
	import NavBar from '$lib/components/global/NavBar.svelte';
	import ScrollToTop from '$lib/components/global/ScrollToTop.svelte';
	import ErrorModal from '$lib/components/global/ErrorModal.svelte';
	import WarningModal from '$lib/components/global/WarningModal.svelte';
</script>

<WarningModal />
<ErrorModal />

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
		min-width: 768px;
		margin: auto;
		margin-top: 1.5em;
		border: 1px solid var(--border-color);
		border-bottom: none;
		box-shadow: 0px 4px 4px var(--shadow-color);
		background-color: var(--secondary-color);
	}

	@media screen and (max-width: 768px) {
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
