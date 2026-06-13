<script lang="ts">
  import type { ComponentProps } from "svelte";
  import Item from "./Item.svelte";
    import { EllipsisVerticalIcon } from "@lucide/svelte";

  interface Props extends ComponentProps<typeof Item> {
    handle?: string;
    name: string;
    id: string;
    meta: {
      lastUpdate: string;
      size: string;
      itemNums: number;
    };
  }

  const { viewType = "grid" }: Props = $props();
</script>

<Item {viewType}>
  {#snippet details()}
    <div class="grid gap-y-1 mt-1">
      <div class="flex justify-between mt-2.5">
        <a href={"itemLink"} aria-label={"ariaTitle"} class="reset-style">
          <h2 class="text-xl">Channel name</h2>
        </a>
        <button class="p-1">
          <EllipsisVerticalIcon />
        </button>
      </div>
      <div class="opacity-70">Collection</div>
      <ul class="flex gap-x-3 opacity-70">
        <li>2 days ago</li>
        <li>1.2 GB</li>
        <li>42 items</li>
      </ul>
    </div>
  {/snippet}
</Item>
