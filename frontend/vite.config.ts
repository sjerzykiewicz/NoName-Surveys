import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
import wasmPack from 'vite-plugin-wasm-pack';

export default defineConfig({
	assetsInclude: ['./wasm/pkg/wasm.js'],
	plugins: [wasmPack('./wasm'), sveltekit()],
	optimizeDeps: {
		exclude: ['wasm']
	}
});
