import { readable, type Readable } from 'svelte/store';

export const XS: Readable<number> = readable(320);
export const S: Readable<number> = readable(425);
export const M: Readable<number> = readable(768);
export const L: Readable<number> = readable(1024);
export const XL: Readable<number> = readable(1440);

export const LIMIT_OF_ACTIVE_SURVEYS: Readable<number> = readable(200);
