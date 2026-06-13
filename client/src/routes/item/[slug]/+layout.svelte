<script lang="ts">
  import type { WithCommonSnippet } from "$lib/components/shared";
  import { LibraryHeader } from "$lib/components";
  import { resolve } from "$app/paths";
  import { page } from "$app/state";

  const { children }: WithCommonSnippet = $props();

  const [, slug] = page.url.pathname.split("/").filter(Boolean);

  const relativeResolvePaths = (path: string) => {
    return resolve(
      path === "/" ? "/item/[slug]" : (`/item/[slug]${path}` as any),
      { slug },
    );
  };

  const tabList = [
    { path: "/", text: "Overview" },
    { path: "/video", text: "Videos" },
    { path: "/video", text: "Contents" },
    { path: "/tasks", text: "Tasks" },
    { path: "/options", text: "Options" },
  ];
</script>

<LibraryHeader />
<div role="tablist" class="flex *:px-2">
  {#each tabList as { path, text }}
    <a role="tab" href={relativeResolvePaths(path)} class="reset-style">{text}</a>
  {/each}
</div>
{@render children?.()}
