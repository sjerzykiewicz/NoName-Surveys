import { test, expect } from '@playwright/test';

test('disallows nondigit code', async ({ page }) => {
	await page.goto('/');

	await page.getByTitle('Enter a survey code to fill it out').fill('abcdef');
	await page.getByTitle('Submit code').click();

	await expect(page.getByTitle('Error')).toBeVisible();
});

test('disallows short code', async ({ page }) => {
	await page.goto('/');

	await page.getByTitle('Enter a survey code to fill it out').fill('1');
	await page.getByTitle('Submit code').click();

	await expect(page.getByTitle('Error')).toBeVisible();
});
