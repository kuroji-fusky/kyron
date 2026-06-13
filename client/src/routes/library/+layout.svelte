<script lang="ts">
  import { LibraryHeader } from "$lib/components";
  import type { WithCommonSnippet } from "$lib/components/shared";

  const { children }: Required<WithCommonSnippet> = $props();
</script>

<LibraryHeader />
{@render children()}
