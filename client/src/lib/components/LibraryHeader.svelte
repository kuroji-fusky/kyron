<script lang="ts">
  import { resolve } from "$app/paths";
  import {
    ArrowLeftIcon,
    HardDriveIcon,
    ListFilterIcon,
    PanelRightIcon,
    SearchIcon,
  } from "@lucide/svelte";
  import { page } from "$app/state";
  import type { Snippet } from "svelte";

  const isLibrary = page.url.pathname === "/library/";

  const { tabs }: { tabs?: Snippet } = $props();
</script>

<div data-library-header="" class="sticky -mt-4 -top-4 z-1">
  <section class="gap-y-2.5 py-4 bg-neutral-900">
    <div class="flex items-center justify-between">
      <div class="flex items-center">
        {#if !isLibrary}
          <a
            href={resolve("/library")}
            class="p-2 mr-2 hover:bg-neutral-700/80 rounded-md"
          >
            <ArrowLeftIcon size={22} />
          </a>
          <div class="size-9 bg-red-500 rounded-full mr-2.5"></div>
          <h1 class="text-2xl font-medium">__libraryHeading</h1>
        {:else}
          <h1 class="text-2xl font-medium">Libs</h1>
        {/if}
      </div>

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
    {@render tabs?.()}
  </section>
</div>
