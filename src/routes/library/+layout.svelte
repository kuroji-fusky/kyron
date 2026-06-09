<script lang="ts">
  import type { WithCommonSnippet } from "$lib/components/shared";
  import {
    HardDriveIcon,
    ListFilterIcon,
    PanelRightIcon,
    SearchIcon,
  } from "@lucide/svelte";

  const { children }: Required<WithCommonSnippet> = $props();
</script>

<div class="sticky -mt-4 -top-4">
  <section
    id="shelf"
    class="grid gap-y-2.5 z-10 py-4 bg-neutral-900 *:flex *:items-center *:justify-between"
  >
    <div>
      <h1 class="text-2xl font-medium">Library</h1>

      <span class="flex-1"></span>
      <div class="flex items-center gap-x-2">
        <button
          class="flex items-center gap-x-1 px-3 py-1.5 rounded-md hover:bg-neutral-500/60"
        >
          <HardDriveIcon size={22} />
          <span class="ml-1 opacity-75">69 GB</span>
        </button>
        <div class="w-64 relative">
          <span
            class="absolute inset-y-0 left-2.5 grid place-items-center pointer-events-none"
          >
            <SearchIcon size={22} />
          </span>
          <input
            type="text"
            role="searchbox"
            class="border w-full pl-9 pr-1.5 py-1.5 rounded-md bg-neutral-900"
            placeholder="Search"
          />
        </div>
        <button
          class="px-3 py-2 flex gap-x-2 items-center bg-neutral-700/60 rounded-md"
        >
          <ListFilterIcon />
          <span>Filters</span>
        </button>
        <button class="p-2.5 bg-neutral-700/60 rounded-md">
          <PanelRightIcon />
        </button>
      </div>
    </div>
  </section>
</div>

{@render children()}
