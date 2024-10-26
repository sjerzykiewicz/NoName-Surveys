<script lang="ts">
	import { onMount } from 'svelte';
	import { cubicInOut } from 'svelte/easing';
	import { fade, scale } from 'svelte/transition';

	export let isHidden: boolean = true;
	export let icon: string;
	export let title: string;
	export let width: number = 20;
	export let textColor: string = 'var(--text-color)';
	export let borderColor: string = 'var(--border-color)';
	export let zIndex: number = 10;
	export let hide: () => void = () => (isHidden = true);

	let isClickable: boolean = false;

	onMount(() => {
		function handleEscape(event: KeyboardEvent) {
			if (!isHidden && event.key === 'Escape') {
				hide();
			}
		}

		function handleClick(event: MouseEvent) {
			if (isClickable && !isHidden && !(event.target as HTMLElement).closest('.modal')) {
				hide();
			}
		}

		document.body.addEventListener('keydown', handleEscape);
		document.body.addEventListener('click', handleClick);

		return () => {
			document.body.removeEventListener('keydown', handleEscape);
			document.body.removeEventListener('click', handleClick);
		};
	});
</script>

{#if !isHidden}
	<section
		class="overlay"
		style="z-index: {zIndex - 1};"
		transition:fade={{ duration: 200, easing: cubicInOut }}
	>
		<div
			class="modal"
			style="width: {width}em;color: {textColor};border-color: {borderColor};z-index: {zIndex};"
			transition:scale={{ duration: 200, easing: cubicInOut }}
			on:introend={() => (isClickable = true)}
			on:outroend={() => (isClickable = false)}
		>
			<div class="top" style="border-bottom-color: {borderColor};">
				<div class="caption">
					<i class="material-symbols-rounded">{icon}</i>{title}
				</div>
				<button title="Cancel" class="cancel" on:click={hide}>
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
{/if}

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
	}

	.modal {
		display: flex;
		flex-direction: column;
		justify-content: center;
		top: 10%;
		position: absolute;
		background-color: var(--secondary-color);
		border-width: 1px;
		border-style: solid;
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--shadow-color);
		font-size: 1.2em;
	}

	.modal div {
		display: flex;
	}

	.top {
		align-items: center;
		justify-content: space-between;
		background-color: var(--secondary-dark-color);
		border-bottom-width: 1px;
		border-bottom-style: solid;
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
		color: var(--text-color);
		text-align: center;
		text-shadow: 0px 4px 4px var(--shadow-color);
		cursor: default;
	}

	.buttons {
		flex-flow: row;
		justify-content: space-evenly;
		padding-bottom: 1em;
	}

	@media screen and (max-width: 768px) {
		.modal {
			font-size: 0.9em;
		}
	}
</style>
