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

  interface Props {
    focusGuard?: boolean;
  }

  const { children, focusGuard }: WithCommonSnippet<Props> = $props();
</script>

{#if browser}
  {#if children}
    <div data-portal="" use:moveDom={"body"}>
      {#if focusGuard}
        <button data-focus-guard="" aria-hidden="true"></button>
      {/if}
      {@render children?.()}
      {#if focusGuard}
        <button data-focus-guard="" aria-hidden="true"></button>
      {/if}
    </div>
  {/if}
{/if}

<style>
  [data-portal] {
    @apply contents empty:hidden;
  }

  [data-focus-guard] {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip-path: inset(50%);
    white-space: nowrap;
    border-width: 0;
  }
</style>
