import { writable, type Writable } from 'svelte/store';
import { type ComponentType } from 'svelte';

export const questions: Writable<{ type: ComponentType; value: string }[]> = writable([]);
