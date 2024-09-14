import { test, expect } from '@playwright/test';

const authFile = 'playwright/.auth/user.json';

// authenticate with google
test('authenticate', async ({ page }) => {
	await page.goto('/account');
	await page.getByTitle('Google').click();

	await page.getByLabel('Email or phone').fill('');
	await page.getByText('Next').click();

	await page.getByLabel('Enter your password').fill('');
	await page.getByText('Next').click();

	await expect(page.getByTitle('Your account')).toBeVisible();

	await page.context().storageState({ path: authFile });
});
