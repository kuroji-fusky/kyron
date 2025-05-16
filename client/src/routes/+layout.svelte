<script>
  const { children } = $props();
  import "../app.css";
  import Navbar from "../lib/components/Navbar.svelte";
</script>

<Navbar />
{@render children()}
