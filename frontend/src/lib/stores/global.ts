import { readable, type Readable } from 'svelte/store';

export const MOBILE_DEVICE_BREAKPOINT: Readable<number> = readable(767);
