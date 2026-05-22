<script>
  import { LogPanel, GlobalSidebar } from "$lib/components";
  import {
    setSidebarToggleState,
    sidebarMaxSize,
    sidebarMinSize,
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
</script>

<div class="px-3 bg-violet-600 text-white flex items-center h-10">
  <button
    class="p-1 cursor-pointer"
    onclick={() => (sidebarState = !sidebarState)}
  >
    <PanelLeftIcon size={21} />
  </button>
  <button class="p-1">
    <ArrowLeftIcon size={21} />
  </button>
  <button class="p-1">
    <ArrowRightIcon size={21} />
  </button>
  <div class="__draggable flex-1 size-full flex items-center">
    <span class="font-bold"> Home – Kyron [Development Build] </span>
  </div>
</div>

<div
  id="root"
  class="overflow-y-auto overflow-x-hidden flex relative transition-[margin] duration-200"
  style={`margin-left: calc(var(--spacing)*${!sidebarState ? sidebarMinSize : sidebarMaxSize})`}
>
  <GlobalSidebar />
  <main class="flex-1">
    {@render children?.()}
    <LogPanel />
  </main>
</div>

<style>
  #root {
    max-height: calc(100dvh - 2.5rem);
  }

  .__draggable {
    app-region: drag;
    -webkit-app-region: drag;
  }
</style>
