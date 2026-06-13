import type { Snippet } from "svelte"
import type { HTMLAttributes } from "svelte/elements"

// biome-ignore lint/complexity/noBannedTypes: required for full type safety
export type WithCommonSnippet<T extends object = {}> = {
  children?: Snippet
  class?: Pick<HTMLAttributes<HTMLDivElement>, "class">
} & T
