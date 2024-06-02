import { writable, type Writable } from 'svelte/store';

export const redirectedOnce: Writable<boolean> = writable(false);
