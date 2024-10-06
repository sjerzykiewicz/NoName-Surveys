<script lang="ts">
	import { onMount } from 'svelte';

	export let isHidden: boolean = true;
	export let icon: string;
	export let title: string;
	export let width: number = 20;

	onMount(() => {
		function handleEscape(event: KeyboardEvent) {
			if (!isHidden && event.key === 'Escape') {
				isHidden = true;
			}
		}

		document.body.addEventListener('keydown', handleEscape);

		return () => {
			document.body.removeEventListener('keydown', handleEscape);
		};
	});
</script>

<section class="overlay" class:hidden={isHidden}>
	<div class="modal" class:hidden={isHidden} style="width: {width}em">
		<div class="top">
			<div class="caption">
				<i class="material-symbols-rounded">{icon}</i>{title}
			</div>
			<button title="Cancel" class="cancel" on:click={() => (isHidden = true)}>
				<i class="material-symbols-rounded">close</i>
			</button>
		</div>
		<div class="content">
			<slot name="content" />
		</div>
		<div class="buttons">
			<slot />
		</div>
	</div>
</section>

<style>
	.overlay {
		display: flex;
		justify-content: center;
		position: fixed;
		top: 0;
		bottom: 0;
		left: 0;
		right: 0;
		width: 100%;
		height: 100%;
		background: rgba(0, 0, 0, 0.5);
		backdrop-filter: blur(2px);
		z-index: 9;
		opacity: 1;
		transition: 0.2s;
	}

	.overlay.hidden {
		visibility: hidden;
		opacity: 0;
	}

	.modal {
		display: flex;
		flex-direction: column;
		justify-content: center;
		top: 10%;
		position: absolute;
		background-color: var(--secondary-color);
		border: 1px solid var(--border-color);
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--shadow-color);
		font-size: 1.2em;
		color: var(--text-color);
		z-index: 10;
		opacity: 1;
		transform: scale(100%);
		transition: 0.2s;
	}

	.modal.hidden {
		visibility: hidden;
		opacity: 0;
		transform: scale(0%);
	}

	.modal div {
		display: flex;
	}

	.top {
		align-items: center;
		justify-content: space-between;
		background-color: var(--secondary-dark-color);
		border-bottom: 1px solid var(--border-color);
		border-top-left-radius: 5px;
		border-top-right-radius: 5px;
		padding: 0.5em;
	}

	.caption {
		align-items: center;
		font-weight: bold;
		font-size: 1.2em;
		text-shadow: 0px 4px 4px var(--shadow-color);
		cursor: default;
	}

	.caption i {
		margin-right: 0.15em;
	}

	.cancel i {
		font-variation-settings: 'wght' 700;
	}

	.content {
		flex-flow: column;
		justify-content: center;
		align-items: center;
		padding: 1em;
		text-align: center;
		text-shadow: 0px 4px 4px var(--shadow-color);
		cursor: default;
	}

	.buttons {
		flex-flow: row;
		justify-content: space-evenly;
		padding-bottom: 1em;
	}

	@media screen and (max-width: 767px) {
		.modal {
			font-size: 0.9em;
		}
	}
</style>
