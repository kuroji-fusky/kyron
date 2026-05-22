import { createContext } from "svelte"

export const [getSidebarToggleState, setSidebarToggleState] =
  createContext<() => boolean>()
export const sidebarMaxSize = 56
export const sidebarMinSize = 15.5
