<script lang="ts">
  import { LogsIcon } from "@lucide/svelte";
</script>

<div id="log-viewer" class="flex flex-col fixed bottom-0 inset-x-0">
  <div id="shelf" class="flex justify-between p-2">
    <div></div>
    <button
      class="bg-violet-500 rounded-md px-3.5 py-1.5 flex items-center gap-x-2 text-white"
    >
      <LogsIcon />
      <span>Logs</span>
    </button>
  </div>
</div>
