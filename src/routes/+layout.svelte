<script lang="ts">
  import "../global.css";

  import Button from "../components/Button.svelte";
  import {
    DownloadIcon,
    FolderSearchIcon,
    HouseIcon,
    LogsIcon,
    SearchIcon,
    Settings2Icon,
  } from "@lucide/svelte";

  const { children } = $props();

  const globalTabs = [
    { text: "Home", href: "/", icon: HouseIcon },
    { text: "Download", href: "/download", icon: DownloadIcon },
    { text: "Manage", href: "/manage", icon: FolderSearchIcon },
    { text: "Logs", href: "/logs", icon: LogsIcon },
  ];
</script>

<header class="flex items-center px-4 py-1 gap-x-1 fill-level-1">
  {#each globalTabs as { text, href, icon: Icon }}
    <a {href} class="inline-flex items-center gap-x-1 border-b py-2 px-2">
      <Icon size={21} />
      <span>{text}</span>
    </a>
  {/each}

  <span class="flex-1"></span>
  <Button>
    <SearchIcon size={21} />
  </Button>
  <div>Connectivity/Status</div>
  <Button>
    <Settings2Icon size={21} />
  </Button>
</header>

{@render children()}
