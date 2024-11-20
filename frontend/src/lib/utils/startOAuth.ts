export async function startOAuth() {
	try {
		const response = await fetch('/api/oauth/request-token', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			}
		});

		const data = await response.json();

		const expires = new Date(Date.now() + 3 * 60 * 1000).toUTCString();
		document.cookie = `oauth_token_secret=${data.oauth_token_secret}; path=/; secure; expires=${expires}`;

		if (data.oauth_token) {
			window.location.href = `/auth/redirect?oauth_token=${data.oauth_token}`;
		} else {
			console.error('Failed to get OAuth token');
		}
	} catch (error) {
		console.error('OAuth request failed:', error);
	}
}
