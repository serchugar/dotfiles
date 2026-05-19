local wezterm = require("wezterm")
local config = wezterm.config_builder()

-------------------------------------------------------------------------------
-- 1. GENERAL AND SYSTEM CONFIGURATION
-------------------------------------------------------------------------------
if wezterm.target_triple:find("windows") then
	config.default_prog = { "powershell.exe", "-NoLogo" }
else
	config.default_prog = { "bash" }
end
config.front_end = "OpenGL"
config.window_close_confirmation = "NeverPrompt"

-------------------------------------------------------------------------------
-- 2. FONTS AND TYPOGRAPHY
-------------------------------------------------------------------------------
config.font = wezterm.font("Inconsolata Nerd Font")
config.font_size = 12.0
config.line_height = 1.0

-------------------------------------------------------------------------------
-- 3. WINDOW DIMENSIONS AND DESIGN
-------------------------------------------------------------------------------
config.initial_cols = 140
config.initial_rows = 35

config.window_decorations = "INTEGRATED_BUTTONS"
config.use_fancy_tab_bar = true
config.tab_max_width = 40
config.win32_system_backdrop = "Auto"

config.window_padding = {
	left = 8,
	right = 8,
	top = 8,
	bottom = 8,
}

-------------------------------------------------------------------------------
-- 4. KEYBINDINGS
-------------------------------------------------------------------------------
config.keys = {
	{
		key = "F11",
		action = wezterm.action.ToggleFullScreen,
	},
	{
		key = "w",
		mods = "SHIFT",
		action = wezterm.action.CloseCurrentTab({ confirm = false }),
	},
}

-------------------------------------------------------------------------------
-- 5. STYLE AND COLOR PALETTE
-------------------------------------------------------------------------------
config.window_frame = {
	active_titlebar_bg = "#232326",
	inactive_titlebar_bg = "#232326",
}

config.colors = {
	-- Primary colors
	background = "#232326",
	foreground = "#a7aab0",

	-- Cursor
	cursor_bg = "#57a5e5",
	cursor_fg = "#232326",

	-- Text selection
	selection_bg = "#35363b",
	selection_fg = "#abb2bf",

	-- Standard ANSI color palette
	ansi = {
		"#101012", -- black
		"#de5d68", -- red
		"#8fb573", -- green
		"#dbb671", -- yellow
		"#57a5e5", -- blue
		"#bb70d2", -- magenta
		"#51a8b3", -- cyan
		"#a7aab0", -- white
	},

	-- Bright ANSI color palette
	brights = {
		"#5a5b5e", -- black
		"#de5d68", -- red
		"#8fb573", -- green
		"#c49060", -- yellow
		"#68aee8", -- blue
		"#bb70d2", -- magenta
		"#51a8b3", -- cyan
		"#818387", -- white
	},

	-- Copy/Search mode colors
	copy_mode_inactive_highlight_bg = { Color = "#3e4451" }, -- Normal matches (background)
	copy_mode_inactive_highlight_fg = { Color = "#abb2bf" }, -- Normal matches (foreground)
	copy_mode_active_highlight_bg = { Color = "#e5c07b" }, -- Focused match (background)
	copy_mode_active_highlight_fg = { Color = "#282c34" }, -- Focused match (foreground)

	tab_bar = {
		background = "#232323",
		active_tab = {
			bg_color = "#171717",
			fg_color = "#dbdbdb",
			intensity = "Normal",
			underline = "None",
		},
		inactive_tab = {
			bg_color = "#232326",
			fg_color = "#a7aab0",
		},
		new_tab = {
			bg_color = "#232326",
			fg_color = "#a7aab0",
		},
	},
}

return config
