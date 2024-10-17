<script lang="ts">
	import { title } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
</script>

<div
	title="Survey title"
	class="title"
	in:slide={{ duration: 200, easing: cubicInOut }}
	out:slide={{ delay: 200, duration: 200, easing: cubicInOut }}
>
	{$title.title}
</div>
