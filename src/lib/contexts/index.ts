import { createContext } from "svelte"

export const [getSidebarToggleState, setSidebarToggleState] = createContext<() => boolean>()
export const sidebarMaxSize = 56
export const sidebarMinSize = 15.5

export type Modals = "settings" | "diskUsage"
export type ModalRecord = Partial<Record<Modals, boolean>>

export const [getModalStates, setModalStates] = createContext<() => ModalRecord>()
