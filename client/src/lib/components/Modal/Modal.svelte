<script lang="ts">
  import type { Snippet } from "svelte";
  import Portal from "../Portal.svelte";
  import type { HTMLAttributes } from "svelte/elements";

  type Props = {
    children?: Snippet;
    visible?: boolean;
  } & Pick<HTMLAttributes<HTMLDivElement>, "class">;

  const { children, visible, class: className }: Props = $props();
</script>

{#if visible}
  <Portal focusGuard={visible}>
    <div class={className} role="dialog" aria-modal="true">
      {@render children?.()}
    </div>
  </Portal>
{/if}
