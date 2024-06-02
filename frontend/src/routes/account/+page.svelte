<script lang="ts">
	import type { PageServerData } from './$types';

	export let data: PageServerData;

	function getKeyFromFile(text: string): string {
		const words = text.split(' ');
		if (words.length > 1) {
			if (words[0] == 'ssh-rsa') {
				return words[1];
			}
		}
		return '';
	}

	function handleSubmit(event: Event) {
		event.preventDefault();
		const fileInput = document.querySelector<HTMLInputElement>('#file');
		const file = fileInput?.files?.[0];
		const reader = new FileReader();
		if (file) {
			reader.readAsText(file);
			reader.onload = function (e) {
				const fileData = e.target?.result;
				const text = fileData as string;
				const publicKey = getKeyFromFile(text);
				fetch('/api/users/update-public-key', {
					method: 'POST',
					headers: {
						'Content-Type': 'application/json'
					},
					body: JSON.stringify({ email: data.session.user?.email, public_key: publicKey })
				});
			};
		}
	}
</script>

<form on:submit={handleSubmit}>
	<label for="file">Choose public key file</label>
	<input type="file" name="file" id="file" />
	<button class="save" type="submit">Submit</button>
</form>

<style>
	form {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		text-align: center;
		color: var(--text-color);
		font-weight: bold;
		font-size: 2em;
		text-shadow: 0px 4px 4px var(--shadow-color);
	}

	label {
		margin-top: 1em;
	}

	input {
		margin-top: 0.5em;
		font-size: 1em;
		cursor: pointer;
		background-color: var(--secondary-dark-color);
		border: 1px solid var(--border-color);
		border-radius: 5px;
	}

	button {
		margin-top: 0.5em;
	}
</style>
