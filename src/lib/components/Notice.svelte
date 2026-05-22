<script lang="ts">
  import type { WithCommonSnippet } from "./shared";

  interface Props {
    kind: "warning" | "info" | "error";
  }

  const props: WithCommonSnippet<Props> = $props();
</script>
