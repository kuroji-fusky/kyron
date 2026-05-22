<script lang="ts">
  import type { WithCommonSnippet } from "./shared";

  const { children }: WithCommonSnippet = $props();
</script>

<button class="px-3 py-2 rounded-md border inline-flex items-center gap-x-1">
  {@render children?.()}
</button>
