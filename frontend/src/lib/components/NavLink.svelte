<script lang="ts">
	import { page } from '$app/stores';

	export let title: string;
	export let href: string;
</script>

<a {href} class:active={$page.url.pathname === href}>{title}</a>

<style>
	a {
		padding: 0.5em;
		text-align: center;
		color: #eaeaea;
		font-family: 'Jura';
		font-weight: bold;
		font-size: 2.25em;
		border: 1px solid #999999;
		width: 100%;
		text-decoration: none;
	}

	a:hover {
		background-color: #4a4a4a;
		transition: background-color 0.3s;
	}

	.active {
		background-color: #4a4a4a;
	}
</style>
