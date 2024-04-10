<button class="footer-button" type="submit" form="form">
	<i class="material-icons">done</i>Save
</button>
<a href="/create" class="footer-button">
	<i class="material-icons">remove_red_eye</i>Preview
</a>
<a href="/" class="footer-button">
	<i class="material-icons">arrow_back</i>Back
</a>

<style>
	.footer-button {
		display: flex;
		flex-flow: row;
		justify-content: center;
		align-items: center;
		text-decoration: none;
		background-color: #4a4a4a;
		padding: 0.25em;
		border: 1px solid #eaeaea;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		width: fit-content;
		font-size: 1.25em;
		font-weight: normal;
		font-family: 'Jura';
		color: #eaeaea;
		cursor: pointer;
		transition: background-color 0.3s;
		margin-left: 0.75em;
		float: right;
	}

	.footer-button:hover {
		background-color: #1a1a1a;
	}

	.material-icons {
		font-size: 0.99em;
		font-weight: bold;
		padding-right: 0.25em;
	}
</style>
