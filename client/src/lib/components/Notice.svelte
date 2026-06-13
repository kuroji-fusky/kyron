<script lang="ts">
  import {
    CircleXIcon,
    InfoIcon,
    TriangleAlertIcon,
    type LucideIcon,
  } from "@lucide/svelte";
  import type { WithCommonSnippet } from "./shared";

  interface Props {
    kind: "warning" | "info" | "error";
    customIcon?: LucideIcon;
  }

  const {
    children,
    customIcon: CustomIcon,
    kind = "info",
  }: WithCommonSnippet<Props> = $props();

  const noticeMap = {
    error: {
      icon: CircleXIcon,
      css: "bg-red-400",
    },
    warning: {
      icon: TriangleAlertIcon,
      css: "bg-yellow-400",
    },
    info: {
      icon: InfoIcon,
      css: "bg-blue-400",
    },
  } satisfies Record<Props["kind"], { icon: LucideIcon; css: string }>;

  // svelte-ignore state_referenced_locally
  const NoticeIcon = noticeMap[kind].icon;
</script>

<div class={["", noticeMap[kind].css]}>
  {#if !CustomIcon}
    <NoticeIcon />
  {:else}
    <CustomIcon />
  {/if}
  <div>
    {@render children?.()}
  </div>
</div>
