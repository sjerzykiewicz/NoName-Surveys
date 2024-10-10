import { readable, type Readable } from 'svelte/store';

export const LIMIT_OF_ACTIVE_SURVEYS: Readable<number> = readable(200);
