<script lang="ts">
  import type { ComponentProps } from "svelte";
  import Item from "./Item.svelte";
  import { resolve } from "$app/paths";
  import { EllipsisVerticalIcon } from "@lucide/svelte";

  interface Props extends ComponentProps<typeof Item> {
    handle?: string;
    name: string;
    id: string;
    meta: {
      lastUpdate: string;
      size: string;
      videos: number;
    };
  }

  const {
    details,
    class: className,
    name,
    viewType = "grid",
  }: Partial<Props> = $props();

  const itemLink = resolve("/item/[slug]", { slug: "a" });
  // svelte-ignore state_referenced_locally
  const ariaTitle = `Item of channel ${name}`;
</script>

<Item
  {viewType}
  class={[
    "rounded-md border border-neutral-600 hover:border-neutral-400 p-3",
    className,
  ]}
>
  <a
    href={itemLink}
    aria-label={ariaTitle}
    class="grid place-items-center bg-purple-200 py-3.5 aspect-video rounded-md w-full"
  >
    <div class="aspect-square rounded-full">
      <div class="size-full bg-purple-600"></div>
    </div>
  </a>
  {#snippet details()}
    <div class="grid gap-y-1 mt-1">
      <div class="flex justify-between mt-2.5">
        <a href={itemLink} aria-label={ariaTitle} class="reset-style">
          <h2 class="text-xl">Channel name</h2>
        </a>
        <button class="p-1">
          <EllipsisVerticalIcon />
        </button>
      </div>
      <div class="opacity-70">@handle</div>
      <ul class="flex gap-x-3 opacity-70">
        <li>2 days ago</li>
        <li>1.2 GB</li>
        <li>42 videos</li>
      </ul>
    </div>
  {/snippet}
</Item>
