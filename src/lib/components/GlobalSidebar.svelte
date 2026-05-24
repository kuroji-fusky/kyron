<script lang="ts">
  import { resolve } from "$app/paths";
  import {
    getModalStates,
    getSidebarToggleState,
    sidebarMaxSize,
    sidebarMinSize,
  } from "$lib/contexts";
  import {
    DownloadIcon,
    HistoryIcon,
    LibraryBigIcon,
    SettingsIcon,
    ZapIcon,
    type LucideIcon,
  } from "@lucide/svelte";

  interface _MenuItem {
    name: string;
    href: string;
    icon: LucideIcon;
  }

  const menus: _MenuItem[] = [
    { name: "Download", href: "/download", icon: DownloadIcon },
    { name: "Library", href: "/library", icon: LibraryBigIcon },
    { name: "Tasks", href: "/tasks", icon: ZapIcon },
    { name: "History", href: "/history", icon: HistoryIcon },
  ];

  const sidebarToggleState = getSidebarToggleState();
  const modalState = getModalStates();

  const handleSettingsModal = () => {
    console.log(modalState());
  };
</script>

<nav
  class={[
    "overflow-hidden z-10 shrink-0 transition-[width,opacity] duration-200 fixed top-10 bottom-0 left-0 flex flex-col gap-y-1 px-3 py-3.5",
    !sidebarToggleState() ? "opacity-60 hover:opacity-100" : "",
  ]}
  style={`
    width: calc(var(--spacing)*${!sidebarToggleState() ? sidebarMinSize : sidebarMaxSize});
    --menu-item-opacity:${!sidebarToggleState() ? 0 : 1}
  `}
>
  {#each menus as { name, href, icon: Icon }}
    <a id="menu-item" href={resolve(href as any)} class="reset-style">
      <Icon size={21} class="shrink-0" />
      <span class="opacity-(--menu-item-opacity) transition-opacity"
        >{name}</span
      >
    </a>
  {/each}

  <span class="flex-1"></span>
  <button id="menu-item" class="reset-style" onclick={handleSettingsModal}>
    <SettingsIcon size={21} class="shrink-0" />
    <span class="opacity-(--menu-item-opacity) transition-opacity"
      >Settings</span
    >
  </button>
</nav>

<style>
  @reference "../../app.css";

  #menu-item {
    @apply p-2 rounded-md flex items-center gap-x-2 hover:bg-violet-400 dark:hover:bg-violet-600/50 transition-colors;
  }
</style>
