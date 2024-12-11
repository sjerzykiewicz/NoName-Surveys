<script lang="ts">
	import { questions } from '$lib/stores/fill-page';

	export let questionIndex: number;
</script>

<div class="question-area subtitle display">
	<div class="question-title">
		{$questions[questionIndex].question}
	</div>
</div>
