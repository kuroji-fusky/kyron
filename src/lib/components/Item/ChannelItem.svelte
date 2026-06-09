<script lang="ts">
  import type { ComponentProps } from "svelte";
  import Item from "./Item.svelte";

  interface Props extends ComponentProps<typeof Item> {}

  const {
    details,
    class: className,
    viewType = "grid",
  }: Partial<Props> = $props();
</script>

<Item
  {viewType}
  class={[
    "rounded-md border border-neutral-600 hover:border-neutral-400 p-3",
    className,
  ]}
>
  <div class="grid place-items-center bg-purple-200 py-3.5 aspect-video rounded-md w-full">
    <div class="aspect-square rounded-full">
      <div class="size-full bg-purple-600"></div>
    </div>
  </div>
  {#snippet details()}
    <h2 class="text-xl mt-2.5">Channel name</h2>
    <div>@handle</div>
    <div class="flex gap-x-2">
      <span>2 days ago</span>
      <span>1.2 GB</span>
      <span>42 videos</span>
    </div>
  {/snippet}
</Item>
