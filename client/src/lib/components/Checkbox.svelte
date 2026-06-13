<script lang="ts">
  import type { WithCommonSnippet } from "./shared";

  interface Props {
    checked?: boolean;
    class?: string;
  }

  const props: WithCommonSnippet<Props> = $props();
  // svelte-ignore state_referenced_locally
  let isChecked = $state(props.checked || false);

  const checkedState = (e: Event) => {
    isChecked = (e.target as HTMLInputElement).checked;
  };

  const _rnd = crypto.randomUUID();
</script>

<label
  for={_rnd}
  class={["flex items-center gap-x-1.5", props.class]}
  data-checked={isChecked ? "" : undefined}
>
  <input
    type="checkbox"
    name=""
    id={_rnd}
    checked={isChecked}
    onchange={checkedState}
  />
  <div>
    {@render props.children?.()}
  </div>
</label>
