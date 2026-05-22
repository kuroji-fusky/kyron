import type { Snippet } from "svelte"

// biome-ignore lint/complexity/noBannedTypes: required for full type safety
export type WithCommonSnippet<T extends object = {}> = {
  children?: Snippet
} & T
