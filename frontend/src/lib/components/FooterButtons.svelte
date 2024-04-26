<a href="/create" title="Preview survey" class="footer-button">
	<i class="material-symbols-rounded">search</i>Preview
</a>
<button title="Save survey" class="footer-button save">
	<i class="material-symbols-rounded">save</i>Save
</button>

<style>
	.footer-button {
		display: flex;
		text-decoration: none;
		background-color: #4a4a4a;
		padding: 0.25em;
		border: 1px solid #999999;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		font-size: 1.25em;
		font-family: 'Jura';
		color: #eaeaea;
		cursor: pointer;
		transition: background-color 0.2s;
		margin-left: 0.5em;
	}

	.footer-button:hover {
		background-color: #1a1a1a;
	}

	.save {
		background-color: #0075ff;
	}

	.save:hover {
		background-color: #001c53;
	}

	i {
		font-size: 1.15em;
		margin-right: 0.15em;
	}

	@media screen and (max-width: 767px) {
		.footer-button {
			font-size: 1em;
		}
	}
</style>
