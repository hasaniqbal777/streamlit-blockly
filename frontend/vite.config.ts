import path from "path";
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

// https://vite.dev/config/
export default defineConfig({
  base: "./", // Set this to './' for relative paths
  plugins: [vue()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  build: {
    outDir: "../src/streamlit_blockly/streamlit/static",
    emptyOutDir: true,
  },
  server: {
    strictPort: true,
    port: 3001,
    cors: true,
  },
});
