<script lang="ts">
	import { page } from '$app/stores';

	$: errorMessage =
		typeof $page.error!.message === 'string'
			? $page.error!.message
			: // @ts-expect-error message is not necessarily a string
				typeof $page.error!.message.detail === 'string'
				? // @ts-expect-error message is not necessarily a string
					$page.error!.message.detail
				: 'Unknown error';
</script>

{#if $page.error}
	<div>
		<h1>Error: <span>{$page.status}</span></h1>
		<h2>Message: <span>{errorMessage}</span></h2>
		<p>Something went wrong, please contact the administrator.</p>
	</div>
{/if}

<style>
	div {
		text-align: center;
		color: var(--text-color);
		font-size: 1em;
		padding: 2em;
		margin: 2em;
		background-color: var(--secondary-dark-color);
		border: 1px solid var(--error-color);
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--shadow-color);
		text-shadow: 0px 4px 4px var(--shadow-color);
		cursor: default;
	}

	span {
		color: var(--error-color);
	}

	p {
		font-size: 1.5em;
	}

	@media screen and (max-width: 768px) {
		div {
			margin: 1em;
			padding: 1em;
			font-size: 0.8em;
		}
	}
</style>
