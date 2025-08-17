<script>
  const { children } = $props();
  import "../app.css";
  import Titlebar from "../lib/components/Titlebar.svelte";
</script>

<Titlebar />
<div class="mt-10">
  {@render children()}
</div>
