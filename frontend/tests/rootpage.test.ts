import { test, expect } from '@playwright/test';

const SURVEY_CODE_1 = process.env.SURVEY_CODE_1;
const SURVEY_CODE_2 = process.env.SURVEY_CODE_2;

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

test('check required questions', async ({ page }) => {
	await page.goto('/');
	await page.getByTitle('Enter a survey code to fill it out').fill(SURVEY_CODE_1 as string);
	await page.getByTitle('Submit the code').click();

	await page.getByTitle('Submit survey').click();

	await expect(page.getByTitle('Error').first()).toBeVisible();
});

test('check survey filling', async ({ page }) => {
	await page.goto('/');
	await page.getByTitle('Enter a survey code to fill it out').fill(SURVEY_CODE_1 as string);
	await page.getByTitle('Submit the code').click();

	await page.getByTitle('Enter your answer').fill('Answer');
	await page.getByTitle('Selected value').first().fill('1');
	await page.getByText('a', { exact: true }).first().check();
	await page.getByText('b', { exact: true }).last().check();
	await page.getByText('c', { exact: true }).last().check();
	await page.getByText('No', { exact: true }).check();
	await page.getByText('3', { exact: true }).check();
	await page.getByTitle('Selected value').last().fill('3');
	await page.getByTitle('Select your answer').last().selectOption({ value: 'list_2' });
	await page.getByText('Do not answer').check();
	await page.getByTitle('Submit survey').click();

	await expect(page.getByText('Your answer has been submitted successfully')).toBeVisible();
});

test('check not active survey', async ({ page }) => {
	await page.goto('/');
	await page.getByTitle('Enter a survey code to fill it out').fill(SURVEY_CODE_2 as string);
	await page.getByTitle('Submit the code').click();

	await page.getByTitle('Enter your answer').fill('Answer');
	await page.getByTitle('Submit survey').click();

	await expect(page.getByText('Survey deactivated by the creator or not found')).toBeVisible();
});
