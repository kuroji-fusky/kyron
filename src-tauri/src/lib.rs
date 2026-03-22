use tauri::{
    menu::{MenuBuilder, MenuItemBuilder},
    tray::{MouseButton, MouseButtonState, TrayIconBuilder, TrayIconEvent},
    Manager,
};

pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_os::init())
        // The persisted-scope plugin must be registered and initialized after the fs plugin
        .plugin(tauri_plugin_fs::init())
        .plugin(tauri_plugin_persisted_scope::init())
        .plugin(tauri_plugin_http::init())
        .plugin(tauri_plugin_clipboard_manager::init())
        .plugin(tauri_plugin_autostart::Builder::new().build())
        .plugin(tauri_plugin_sql::Builder::new().build())
        .plugin(tauri_plugin_notification::init())
        .plugin(tauri_plugin_updater::Builder::new().build())
        .plugin(tauri_plugin_positioner::init())
        .plugin(tauri_plugin_opener::init())
        .plugin(tauri_plugin_single_instance::init(|app, _args, _cwd| {
            let _ = app
                .get_webview_window("main")
                .expect("no main window")
                .set_focus();
        }))
        .setup(|app| {
            let menu = MenuBuilder::new(app)
                .item(
                    &MenuItemBuilder::new("No download queues - start one up cutie")
                        .enabled(false)
                        .id("manage_download_queues")
                        .build(app)?,
                )
                .item(
                    &MenuItemBuilder::new("Manage downloads")
                        .id("view_manage_tab")
                        .build(app)?,
                )
                .item(
                    &MenuItemBuilder::new("Update/Fetch cookies")
                        .id("cookie_jar")
                        .build(app)?,
                )
                .separator()
                .item(
                    &MenuItemBuilder::new("View Downloads")
                        .id("view_download_tab")
                        .build(app)?,
                )
                .item(
                    &MenuItemBuilder::new("View Logs")
                        .id("view_logs_tab")
                        .build(app)?,
                )
                .separator()
                .item(&MenuItemBuilder::new("Options").id("options").build(app)?)
                .separator()
                .item(
                    &MenuItemBuilder::new("Exit and touch grass")
                        .id("exit_app")
                        .build(app)?,
                )
                .build()?;

            let _tray = TrayIconBuilder::new()
                .icon(app.default_window_icon().unwrap().clone())
                .tooltip("Kyron Downloader version 69")
                .menu(&menu)
                .on_tray_icon_event(|tray, event| match event {
                    TrayIconEvent::Click {
                        button: MouseButton::Left,
                        button_state: MouseButtonState::Up,
                        ..
                    } => {
                        println!("your gay");
                        let gap = tray.app_handle();
                        if let Some(window) = gap.get_webview_window("main") {
                            let _ = window.unminimize();
                            let _ = window.show();
                            let _ = window.set_focus();
                        }
                    }
                    _ => {}
                })
                .on_menu_event(|app, event| match event.id().as_ref() {
                    "exit_app" => {
                        app.exit(0);
                    }
                    _ => {}
                })
                .build(app)?;

            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
