export async function signOut() {
	try {
		await fetch('/api/oauth/sign-out', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			}
		});
		location.reload();
	} catch (error) {
		console.error('OAuth sign-out failed:', error);
	}
}
