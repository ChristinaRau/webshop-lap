import { fileURLToPath, URL } from 'node:url';

import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import VueDevTools from 'vite-plugin-vue-devtools';
import fs from "fs";

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [
        vue(),
        VueDevTools(),
    ],
    resolve: {
        alias: {
            '@': fileURLToPath(new URL('./src', import.meta.url))
        }
    },
    define: {
    // defines global variable which can be accessed anywhere
        __API_URL__: JSON.stringify("http://127.0.0.1:5000")
    },
    server: {
        port: 8080,
        host: "127.0.0.1",
        https: {
            cert: fs.readFileSync("../domain.crt"),
            key: fs.readFileSync("../domain.key")
        }
    }
});
