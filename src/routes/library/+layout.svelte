<script lang="ts">
  import { Breadcrumbs } from "$lib/components";
  import type { WithCommonSnippet } from "$lib/components/shared";
  import { HardDriveIcon, PanelRightIcon } from "@lucide/svelte";

  const { children }: Required<WithCommonSnippet> = $props();
</script>

<div id="shelf" class="flex items-center justify-between">
  <Breadcrumbs />
  <span class="flex-1"></span>
  <div class="flex items-center gap-x-2 *:h-full">
    <button
      class="flex items-center gap-x-1 px-3 py-1.5 rounded-md bg-neutral-500/40"
    >
      <HardDriveIcon size={22} />
      <span class="ml-1 text-sm opacity-75">69 GB</span>
    </button>
    <button class="p-2 bg-violet-600 rounded-md">
      <PanelRightIcon />
    </button>
  </div>
</div>

{@render children()}
