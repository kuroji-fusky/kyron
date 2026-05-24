<script lang="ts">
  import Portal from "../Portal.svelte";
  import type { WithCommonSnippet } from "../shared";

  interface Props {
    modalEvent?: () => void;
    open?: boolean;
  }

  const { children, open: isOpen }: WithCommonSnippet<Props> = $props();

  // svelte-ignore state_referenced_locally
  let isModalOpen = $state(isOpen ?? false);
</script>

<Portal>
  {#if isModalOpen}
    <div class="fixed inset-3.5 rounded-md bg-amber-900">
      {@render children?.()}
    </div>
  {/if}
</Portal>
