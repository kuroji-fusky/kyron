<script>
  import ChannelItem from "$lib/components/Item/ChannelItem.svelte";
</script>

<div class="grid grid-cols-[repeat(auto-fill,minmax(--spacing(80),1fr))] gap-3">
  {#each [...Array(12)] as _}
    <ChannelItem />
  {/each}
</div>
