<script lang="ts">
  import type { Snippet } from "svelte";
  import type { WithCommonSnippet } from "../shared";
  import type { HTMLAttributes } from "svelte/elements";

  interface Props extends HTMLAttributes<HTMLDivElement> {
    viewType: "grid" | "list";
    details?: Snippet;
  }

  const {
    children,
    details,
    viewType,
    class: className,
    ...others
  }: WithCommonSnippet<Props> = $props();
</script>

<div data-item-renderer="" class={className} {...others}>
  {#if viewType === "grid"}
    {@render children?.()}
    {@render details?.()}
  {:else}
    {@render children?.()}
  {/if}
</div>
