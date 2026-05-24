<script>
  import { resolve } from "$app/paths";
  import { Checkbox, CheckboxDetails } from "$lib/components";
  import {
    XIcon,
    ArrowRightIcon,
    ListChevronsUpDownIcon as ListExpandIcon,
    ChevronDownIcon,
  } from "@lucide/svelte";
</script>

<div class="max-w-5xl mx-auto flex flex-col gap-y-9">
  <section class="mt-12">
    <div class="mb-5">
      <label for="downloader-field" class="relative block">
        <div class="absolute top-0 right-0 py-2 px-3 flex gap-x-1">
          <button class="p-1.5 rounded-md bg-violet-200">
            <XIcon />
          </button>
          <button class="p-1.5 rounded-md bg-violet-200">
            <ListExpandIcon />
          </button>
          <button class="p-1.5 rounded-md bg-violet-600 text-white">
            <ArrowRightIcon />
          </button>
        </div>
        <input
          type="text"
          spellcheck="false"
          autocapitalize="off"
          id="downloader-field"
          class="resize-none w-full px-3.5 py-2.5 rounded-lg dark:bg-neutral-800 dark:border-neutral-600"
          placeholder="Paste URL(s) or search for videos"
        />
      </label>
      <span class="opacity-65 text-sm leading-0"
        >Press <kbd>Shift+Enter</kbd> for a new line</span
      >
    </div>

    <div class="py-3.5 px-4 bg-violet-200/40 dark:bg-violet-500/10 rounded-md">
      <div class="space-y-4 grid grid-cols-1 md:grid-cols-2 gap-x-12">
        <fieldset>
          <label for="v-quality">
            <span>Prefered quality:</span>
            <select
              name="vidya-quality"
              id="v-quality"
              class="px-2 py-0.5 rounded-md"
            >
              <option value="2160" selected>2160p (4K)</option>
              <option value="1080" selected>1080p</option>
              <option value="720">720p</option>
              <option value="480">480p</option>
              <option value="360">360p</option>
              <option value="custom">Custom</option>
            </select>
          </label>

          <Checkbox>Only download audio</Checkbox>

          <hr class="my-2 border-violet-600" />

          <Checkbox checked
            >Automatically find snapshots on Wayback Machine if video is
            unavailable or private</Checkbox
          >
        </fieldset>
        <fieldset>
          <CheckboxDetails>
            {#snippet checkboxSlot()}
              Include thumbnails
            {/snippet}
            <Checkbox>Embed thumbnails</Checkbox>
          </CheckboxDetails>

          <Checkbox>Download subtitles</Checkbox>
          <!-- cookies -->
          <CheckboxDetails>
            {#snippet checkboxSlot()}
              Use cookies (advanced)
            {/snippet}
            <button class="px-2.5 py-1.5 bg-violet-500/20 rounded-md"
              >Add file</button
            >
            <p>
              Learn more about exporting a cookie session from browsers via
              yt-dlp's recommendation
            </p>
          </CheckboxDetails>
        </fieldset>
      </div>

      <div class="flex items-center gap-x-2 mt-3">
        <button class="px-2.5 py-1.5 bg-violet-600 rounded-md text-white">
          <span>More options</span>
        </button>
        <button class="px-2.5 py-1.5 bg-violet-200/60 rounded-md">
          <span>Clear selection</span>
        </button>
        <button
          class="px-2.5 py-1.5 bg-violet-600 rounded-md text-white flex items-center gap-x-1"
        >
          <span>Presets</span>
          <ChevronDownIcon />
        </button>
      </div>
    </div>
  </section>

  <section>
    <h2>Bulk tasks</h2>
    <button class="px-2.5 py-1.5 bg-violet-600 rounded-md text-white">
      Download a channel or playlist
    </button>

    <button class="px-2.5 py-1.5 bg-violet-600 rounded-md text-white">
      Find lost video(s)
    </button>
  </section>

  <section class="mb-10">
    <p id="notice" class="opacity-50">
      Kyron heavily relies on <a
        href="https://github.com/yt-dlp/yt-dlp"
        target="_blank"
        class="font-mono px-1 py-0.5 bg-neutral-700/50 rounded-md">yt-dlp</a
      >
      in the background to download videos under the hood. For advanced usage, such
      as downloading a channel or performing bulk archives, go to
      <a href={resolve("/library")}>Library</a>.
    </p>
  </section>
</div>
