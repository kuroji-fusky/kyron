<script lang="ts">
  import type { Snippet, ComponentProps } from "svelte";
  import Checkbox from "./Checkbox.svelte";
  import type { WithCommonSnippet } from "./shared";

  interface Props extends ComponentProps<typeof Checkbox> {
    checkboxSlot: Snippet;
  }

  const { checked, ...props }: WithCommonSnippet<Props> = $props();
</script>

<span class="contents">
  <Checkbox class="peer" {checked}>
    {@render props.checkboxSlot()}
  </Checkbox>
  <div class="hidden peer-data-checked:block ml-5">
    {@render props.children?.()}
  </div>
</span>
