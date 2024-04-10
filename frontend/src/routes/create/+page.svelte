<script lang="ts">
	import Header from '../Header.svelte';
	import Content from '../Content.svelte';
	import Footer from '../Footer.svelte';
	import Title from './components/Title.svelte';
	import Questions from './components/Questions.svelte';
	import FooterButtons from './components/FooterButtons.svelte';
</script>

<Header>
	<Title />
</Header>
<Content>
	<Questions />
</Content>
<Footer>
	<FooterButtons />
</Footer>
