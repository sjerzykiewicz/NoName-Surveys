<script lang="ts">
	import { page } from '$app/stores';

	export let title: string;
	export let href: string;
</script>

<a {href} class:active={$page.url.pathname === href}>{title}</a>

<style>
	a {
		padding: 0.5em 0 0.5em 0;
		text-align: center;
		color: #eaeaea;
		font-family: 'Jura';
		font-weight: bold;
		font-size: 1.5em;
		border: 1px solid #999999;
		border-left: none;
		width: 100%;
		text-decoration: none;
		transition: background-color 0.2s;
	}

	a:hover {
		background-color: #0075ff;
		transition: background-color 0.2s;
	}

	.active {
		background-color: #0075ff;
	}
</style>
