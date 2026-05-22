<script lang="ts">
  import { resolve } from "$app/paths";
  import {
    getSidebarToggleState,
    sidebarMaxSize,
    sidebarMinSize,
  } from "$lib/contexts";
  import {
    Clock4Icon,
    DownloadIcon,
    LibraryBigIcon,
    SettingsIcon,
    type LucideIcon,
  } from "@lucide/svelte";

  interface _MenuItem {
    name: string;
    href: string;
    icon: LucideIcon;
  }

  const menus = [
    { name: "Download", href: "/", icon: DownloadIcon },
    { name: "Library", href: "/library", icon: LibraryBigIcon },
    { name: "Tasks", href: "/tasks", icon: Clock4Icon },
  ] as const satisfies _MenuItem[];

  const toggled = getSidebarToggleState();
</script>

<nav
  class="overflow-hidden z-10 shrink-0 bg-violet-100 transition-[width] duration-200 fixed top-10 bottom-0 left-0 flex flex-col gap-y-1 px-3 py-3.5"
  style={`width: calc(var(--spacing)*${!toggled() ? sidebarMinSize : sidebarMaxSize});--menu-item-opacity:${!toggled() ? 0 : 1}`}
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
  <a id="menu-item" href={resolve("/settings")} class="reset-style">
    <SettingsIcon size={21} class="shrink-0" />
    <span class="opacity-(--menu-item-opacity) transition-opacity"
      >Settings</span
    >
  </a>
</nav>

<style>
  @reference "../../app.css";

  #menu-item {
    @apply p-2 rounded-md flex items-center gap-x-2 bg-violet-400;
  }
</style>
