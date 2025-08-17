<script lang="ts">
  import { onMount } from "svelte";
  import { getCurrentWindow } from "@tauri-apps/api/window";

  let minimizeButton: HTMLButtonElement;
  let maximizeRestoreButton: HTMLButtonElement;
  let killMeButton: HTMLButtonElement;

  const _window = getCurrentWindow();

  onMount(async () => {
    // await _window.onFocusChanged((e) => {
    // console.log(e);
    // });

    minimizeButton.addEventListener("click", () => {
      _window.minimize();
    });

    maximizeRestoreButton.addEventListener("click", async () => {
      maximizeRestoreButton.textContent = String(await _window.isMaximized());
      _window.toggleMaximize();
    });

    killMeButton.addEventListener("click", () => {
      _window.close();
    });
  });
</script>

<menu class="flex justify-between select-none fixed top-0 inset-x-0 h-10">
  <div data-tauri-drag-region="" class="flex-1 flex items-center px-2.5">
    <span id="titlebar">BentoBox (Development Build)</span>
  </div>
  <div id="controls" class="flex items-center">
    <div class="px-2" data-tauri-drag-region="">clouds</div>
    <button class="px-2 cursor-pointer">options</button>
    <button bind:this={minimizeButton} class="px-2 h-full cursor-pointer"
      >min</button
    >
    <button bind:this={maximizeRestoreButton} class="px-2 h-full cursor-pointer"
      >max</button
    >
    <button bind:this={killMeButton} class="px-2 h-full cursor-pointer"
      >close</button
    >
  </div>
</menu>

<style>
  *[data-tauri-drag-region] {
    app-region: drag;
  }
</style>
