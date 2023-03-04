import os
from cudatext import *

fn_config = os.path.join(app_path(APP_DIR_SETTINGS), 'plugins.ini')
SECTION = 'auto_center_line'

def bool_to_str(v): return '1' if v else '0'
def str_to_bool(s): return s=='1'

class Command:
    h = 50
    
    def config(self):

        ini_write(fn_config, SECTION, 'h', str(self.h))
        file_open(fn_config)

    def on(self):
    
        self.h = int(ini_read(fn_config, SECTION, 'h', str(self.h)))
        app_proc(PROC_SET_EVENTS, 'cuda_auto_center_line;on_caret;;')
        msg_status('Auto Center Line activated')

    def off(self):

        app_proc(PROC_SET_EVENTS, 'cuda_auto_center_line;;;')
        msg_status('Auto Center Line deactivated')

    def on_caret(self, ed_self):
    
        carets = ed.get_carets()
        if len(carets)!=1:
            return
            
        x, y, x1, y1 = carets[0]
        if y1>=0:
            return
        
        # handle mouse selection
        st = app_proc(PROC_GET_KEYSTATE, '')
        if 'L' in st or 'R' in st:
            return
        
        h = ed.get_prop(PROP_VISIBLE_LINES)
        h_delta = h * self.h // 100
        pos = max(0, y-h_delta)
        
        if ed.get_prop(PROP_WRAP)!=0:
            w = ed.get_wrapinfo()
            for n in reversed(range(len(w))):
                wi = w[n]
                if wi['line']==y and wi['char']-1<=x:
                    pos = max(0, n-h_delta)
                    break
        
        ed.set_prop(PROP_SCROLL_VERT, pos)
