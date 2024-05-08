<script lang="ts">
	export let answer: any;
</script>

<p>{answer.title}</p>
{#each answer.questions as question}
	<p>{question.question}</p>
	<p>{question.answer}</p>
	<p>{question.question_type}</p>
	<p>{question.choices}</p>
{/each}

<style>
	p {
		color: white;
	}
</style>
