import { readable, type Readable, writable, type Writable } from 'svelte/store';

export const colorScheme: Writable<string> = writable('');

export const XS: Readable<number> = readable(320);
export const S: Readable<number> = readable(425);
export const M: Readable<number> = readable(768);
export const L: Readable<number> = readable(1024);
export const XL: Readable<number> = readable(1440);

export const LIMIT_OF_SURVEYS: Readable<number> = readable(50);
export const LIMIT_OF_DRAFTS: Readable<number> = readable(50);
export const LIMIT_OF_GROUPS: Readable<number> = readable(50);
export const LIMIT_OF_CHARS: Readable<number> = readable(1000);
export const ENTRIES_PER_PAGE: Readable<number> = readable(10);

export const isErrorModalHidden: Writable<boolean> = writable(true);
export const errorModalContent: Writable<string> = writable('');

export const isWarningModalHidden: Writable<boolean> = writable(true);
export const warningModalContent: Writable<string> = writable('');

export const isSuccessModalHidden: Writable<boolean> = writable(true);
export const successModalContent: Writable<string> = writable('');
