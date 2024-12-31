import { test, expect } from '@playwright/test';

const SURVEY_CODE = process.env.SURVEY_CODE;

test('disallows nondigit code', async ({ page }) => {
	await page.goto('/');

	await page.getByTitle('Enter a survey code to fill it out').fill('abcdef');
	await page.getByTitle('Submit the code').click();

	await expect(page.getByTitle('Error')).toBeVisible();
});

test('disallows short code', async ({ page }) => {
	await page.goto('/');

	await page.getByTitle('Enter a survey code to fill it out').fill('1');
	await page.getByTitle('Submit the code').click();

	await expect(page.getByTitle('Error')).toBeVisible();
});

// To pass this test you must remove BACKEND_HOST from env and run backend server locally
test('warns about nonexistent survey', async ({ page }) => {
	await page.goto('/');
	await page.getByTitle('Enter a survey code to fill it out').fill('123456');
	await page.getByTitle('Submit the code').click();

	await expect(page.getByTitle('Error')).toBeVisible();
});

test('check existent survey', async ({ page }) => {
	await page.goto('/');
	await page.getByTitle('Enter a survey code to fill it out').fill(SURVEY_CODE as string);
	await page.getByTitle('Submit the code').click();

	await expect(page.getByTitle('Survey Title')).toBeVisible();
});
