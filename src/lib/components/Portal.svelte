<script lang="ts">
  import { browser } from "$app/environment";
  import type { WithCommonSnippet } from "./shared";

  const moveDom = (node: Element, inject: string) => {
    const target = document.querySelector(inject)!;
    target.appendChild(node);

    return {
      destroy() {
        node.remove();
      },
    };
  };

  const { children }: WithCommonSnippet = $props();
</script>

{#if browser}
  {#if children}
    <div data-portal="" use:moveDom={"body"}>
      {@render children?.()}
    </div>
  {/if}
{/if}

<style>
  [data-portal] {
    @apply contents empty:hidden;
  }
</style>
