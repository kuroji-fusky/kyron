<script lang="ts">
  import { LogPanel, GlobalSidebar } from "$lib/components";
  import {
    setSidebarToggleState,
    sidebarMaxSize,
    sidebarMinSize,
    setModalStates,
    type ModalRecord,
  } from "$lib/contexts";
  import {
    PanelLeftIcon,
    ArrowRightIcon,
    ArrowLeftIcon,
    setLucideProps,
  } from "@lucide/svelte";

  const { children } = $props();

  setLucideProps({
    size: 20,
    strokeWidth: 1.5,
  });

  let sidebarState = $state(false);
  setSidebarToggleState(() => sidebarState);

  let modalStates = $state<ModalRecord>({
    settings: false,
    diskUsage: false,
  });
  setModalStates(() => modalStates);
</script>

<div class="px-3 text-white flex items-center h-11">
  <button
    class="p-1 cursor-pointer"
    onclick={() => (sidebarState = !sidebarState)}
  >
    <PanelLeftIcon size={21} />
  </button>
  <!-- <button class="p-1">
    <ArrowLeftIcon size={21} />
  </button>
  <button class="p-1">
    <ArrowRightIcon size={21} />
  </button> -->
  <div class="__draggable flex-1 size-full flex items-center px-2">
    <span class="font-bold text-sm">Library - Kyron</span>
  </div>
</div>

<div
  id="root"
  class=" flex relative transition-[margin] duration-200"
  style={`margin-left: calc(var(--spacing)*${!sidebarState ? sidebarMinSize : sidebarMaxSize})`}
>
  <GlobalSidebar />
  <div
    id="container"
    class="overflow-y-auto overflow-x-hidden flex-1 rounded-md border border-neutral-700 bg-neutral-900 h-full ml-0 mt-0 m-3 px-6 py-4"
  >
    {@render children?.()}
    <LogPanel />
  </div>
</div>

<style>
  #root {
    min-height: calc(100dvh - 2.5rem);
    height: 100dvh;
  }

  #container {
    max-height: calc(100dvh - 3.25rem);
  }

  .__draggable {
    app-region: drag;
    -webkit-app-region: drag;
  }
</style>
