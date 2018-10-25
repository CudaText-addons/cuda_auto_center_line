import os
from cudatext import *

fn_config = os.path.join(app_path(APP_DIR_SETTINGS), 'cuda_typewriter.ini')

def bool_to_str(v): return '1' if v else '0'
def str_to_bool(s): return s=='1'

class Command:
    
    def on(self):
    
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
        h = ed.get_prop(PROP_VISIBLE_LINES)
        
        pos = max(0, y-h//2)
        
        if ed.get_prop(PROP_WRAP)!=0:
            w = ed.get_wrapinfo()
            for n in reversed(range(len(w))):
                wi = w[n]
                if wi['line']==y and wi['char']-1<=x:
                    pos = max(0, n-h//2)
                    break
        
        ed.set_prop(PROP_SCROLL_VERT, pos)
