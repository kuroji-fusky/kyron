import { defineConfig } from "vite"
import tailwindcss from "@tailwindcss/vite"
import { sveltekit } from "@sveltejs/kit/vite"
import adapter from "@sveltejs/adapter-static"
import { vitePreprocess } from "@sveltejs/vite-plugin-svelte"

export default defineConfig({
  plugins: [
    tailwindcss(),
    sveltekit({
      preprocess: vitePreprocess(),
      adapter: adapter({
        pages: ".vite/renderer/main_window",
      }),
      compilerOptions: {
        // Force runes mode for the project, except for libraries. Can be removed in svelte 6.
        runes: ({ filename }) => filename.split(/[/\\]/).includes("node_modules") ? undefined : true
      },
    })
  ],
  optimizeDeps: {
    exclude: ["@lucide/svelte"],
  },
})
