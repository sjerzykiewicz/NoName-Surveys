<script lang="ts">
	import { cubicInOut } from 'svelte/easing';
	import { fade, scale } from 'svelte/transition';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let isHidden: boolean = true;
	export let icon: string;
	export let title: string;
	export let element: HTMLDivElement | null = null;
	export let hide: () => void = () => (isHidden = true);

	let isClickable: boolean = false;

	function handleEscape(event: KeyboardEvent) {
		if (!isHidden && event.key === 'Escape') {
			event.stopImmediatePropagation();
			hide();
		}
	}

	function handleClick(event: MouseEvent) {
		if (isClickable && !isHidden && !(event.target as HTMLElement).closest('.modal')) {
			event.stopImmediatePropagation();
			hide();
		}
	}
</script>

<svelte:body on:keydown={handleEscape} on:mousedown={handleClick} />

{#if !isHidden}
	<section class="overlay" transition:fade={{ duration: 200, easing: cubicInOut }}>
		<div
			class="modal"
			transition:scale={{ duration: 200, easing: cubicInOut }}
			on:introend={() => {
				isClickable = true;
				if (element) {
					element.focus();
				}
			}}
			on:outroend={() => (isClickable = false)}
		>
			<div class="top">
				<div class="caption">
					<i class="symbol">{icon}</i>{title}
				</div>
				<button title={$t('cancel')} class="cancel" on:click={hide}>
					<i class="symbol">close</i>
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
		z-index: calc(var(--z-index, 10) - 1);
	}

	.modal {
		display: flex;
		flex-direction: column;
		justify-content: center;
		top: 10%;
		position: absolute;
		background-color: var(--secondary-color-1);
		border-width: 1px;
		border-style: solid;
		border-radius: 5px;
		box-shadow: var(--shadow);
		font-size: 1.2em;
		color: var(--text-color, var(--text-color-1));
		border-color: var(--border-color, var(--border-color-1));
		width: var(--width, 20em);
		z-index: var(--z-index, 10);
		transition:
			0.2s,
			outline 0s;
	}

	.modal div {
		display: flex;
	}

	.top {
		align-items: center;
		justify-content: space-between;
		background-color: var(--secondary-color-2);
		border-bottom-width: 1px;
		border-bottom-style: solid;
		border-bottom-color: var(--border-color, var(--border-color-1));
		border-top-left-radius: 5px;
		border-top-right-radius: 5px;
		padding: 0.5em;
	}

	.caption {
		align-items: center;
		font-weight: 700;
		font-size: 1.2em;
		text-shadow: var(--shadow);
		cursor: default;
	}

	.caption i {
		margin-right: 0.15em;
	}

	.content {
		flex-flow: column;
		justify-content: center;
		align-items: center;
		padding: 1em;
		color: var(--text-color-1);
		text-align: center;
		text-shadow: var(--shadow);
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
