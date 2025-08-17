use tauri::Runtime;

#[tauri::command]
async fn maximize_state<R: Runtime>(window: tauri::Window<R>) -> Result<(), String> {
  Ok(())
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_opener::init())
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
