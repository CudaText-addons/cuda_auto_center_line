Plugin for CudaText.
When active, it changes vertical scroll position, so that line 
with caret is always centered in the editor window.

"Centered" position can be changed via config file - option "h"
(in percents, default is 50), in the settings/plugins.ini,
section [auto_center_line].

Plugin gives command "Toggle" in the menu "Plugins / Auto Center Line"
(plugin is not active until you call "Toggle").
Plugin is not activated on CudaText restart.
Plugin is passive when multi-carets are placed.

Author: Alexey Torgashin (CudaText)
License: MIT
