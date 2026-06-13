<script lang="ts">
  import type { WithCommonSnippet } from "./shared";

  interface Props {
    title: string;
    collapsible?: boolean;
    isOpen?: boolean;
  }

  const {
    title,
    children,
    collapsible = true,
    isOpen = true,
  }: WithCommonSnippet<Props> = $props();
</script>

<section id="group-section">
  <div>
    {title}
  </div>
  {@render children?.()}
</section>
