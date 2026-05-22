import type { Snippet } from "svelte";

export type WithCommonSnippet<T extends object = {}> = { children?: Snippet } & T