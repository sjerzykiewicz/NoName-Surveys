<script lang="ts">
	import { beforeUpdate } from 'svelte';
	import { createEventDispatcher } from 'svelte';
	import { slide } from 'svelte/transition';
	import { cubicInOut } from 'svelte/easing';
	import { getRespondentTypeData } from '$lib/utils/getRespondentTypeData';
	import { Access } from '$lib/entities/Access';

	export let respondentType: Access;
	export let respondentTypeIndex: number;

	let respondentTypeData: { title: string; icon: string; text: string };

	const dispatch = createEventDispatcher();

	function handleClick() {
		dispatch('chooseRespondentType', { type: respondentType });
	}

	beforeUpdate(() => {
		respondentTypeData = getRespondentTypeData(respondentType);
	});
</script>

<button
	title={respondentTypeData.title}
	class:chosen={respondentTypeIndex === -1}
	class:last={respondentTypeIndex === 2}
	in:slide={{ axis: 'x', duration: 200, easing: cubicInOut }}
	on:click={handleClick}
	><i class="material-symbols-rounded">{respondentTypeData.icon}</i
	>{respondentTypeData.text}</button
>

<style>
	button {
		flex: 1;
		width: 5.5em;
		border: 0px;
		border-radius: 0px;
		border-left: 1px solid var(--border-color);
		border-right: 1px solid var(--border-color);
		box-shadow: none;
	}

	.last {
		border-radius: 0px 0px 5px 5px;
		border-bottom: 1px solid var(--border-color);
	}

	.chosen {
		border-radius: 0px 5px 5px 0px;
		border-left: 0px;
		border-top: 1px solid var(--border-color);
		border-bottom: 1px solid var(--border-color);
		width: auto;
	}

	i {
		font-size: 1em;
		margin-right: 0.25em;
		margin-left: 0.1em;
	}
</style>
