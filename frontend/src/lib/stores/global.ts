import { readable, type Readable } from 'svelte/store';

export const LIMIT_OF_CHARS: Readable<number> = readable(5000);
