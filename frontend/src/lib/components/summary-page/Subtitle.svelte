<script lang="ts">
	export let question: string;
</script>

<div class="question-area subtitle display" class:empty={question === ''}>
	<div class="question-title">
		{question}
	</div>
</div>
