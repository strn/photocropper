#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rpErrorHandler
import Tkinter
#------------------------------------------------------------------------------#
#                                                                              #
#                                 Preferences                                  #
#                                                                              #
#------------------------------------------------------------------------------#
class Preferences(Tkinter.Frame):
    def __init__(self,Master=None,*pos,**kw):
        #
        #Your code here
        #

        apply(Tkinter.Frame.__init__,(self,Master),kw)

        #
        #Your code here
        #
    #
    #Start of event handler methods
    #

    #
    #Start of non-Rapyd user code
    #


pass #---end-of-form---
#------------------------------------------------------------------------------#
#                                                                              #
#                                 ScanCropper                                  #
#                                                                              #
#------------------------------------------------------------------------------#
class ScanCropper(Tkinter.Frame):
    def __init__(self,Master=None,*pos,**kw):
        kw['borderwidth'] = '5'
        kw['height'] = '1'
        kw['width'] = '1'
        #
        #Your code here
        #

        apply(Tkinter.Frame.__init__,(self,Master),kw)
        self.bind('<Configure>',self.on_ScanCropper_Config)
        self.frameFiles = Tkinter.Frame(self)
        self.frameFiles.pack(anchor='nw',fill='y',side='left')
        self.sbFiles = Tkinter.Scrollbar(self.frameFiles)
        self.sbFiles.pack(anchor='nw',fill='y',side='right')
        self.lbFiles = Tkinter.Listbox(self.frameFiles,takefocus=1)
        self.lbFiles.pack(anchor='nw',fill='y',side='right')
        self.lbFiles.bind('<ButtonRelease-1>',self.on_lbFiles_mouseClick_1)
        self.frameMain = Tkinter.Frame(self,borderwidth='1')
        self.frameMain.pack(expand='yes',fill='both',side='left')
        self.framePicture = Tkinter.Frame(self.frameMain,borderwidth='1'
            ,relief='raised')
        self.framePicture.pack(anchor='nw',expand='yes',fill='both',side='top')
        self.canvas = Tkinter.Canvas(self.framePicture,borderwidth='1'
            ,takefocus=1)
        self.canvas.pack(anchor='nw',expand='yes',fill='both',side='bottom')
        self.canvas.bind('<B1-Motion>',self.canvas_mouseb1move_callback)
        self.canvas.bind('<Button-1>',self.canvas_mouse1_callback)
        self.canvas.bind('<ButtonRelease-1>',self.canvas_mouseup1_callback)
        self.canvas.bind('<KeyRelease-Down>',self.canvas_KeyRel_ArrowDown)
        self.canvas.bind('<KeyRelease-KP_Next>' \
            ,self.on_canvas_KeyRel_KeyPad_PageDown)
        self.canvas.bind('<KeyRelease-KP_Prior>' \
            ,self.on_canvas_KeyRel_KeyPad_PageUp)
        self.canvas.bind('<KeyRelease-Left>',self.canvas_KeyRel_ArrowLeft)
        self.canvas.bind('<KeyRelease-Next>',self.on_canvas_KeyRel_PageDown)
        self.canvas.bind('<KeyRelease-Prior>',self.on_canvas_KeyRel_PageUp)
        self.canvas.bind('<KeyRelease-Right>',self.canvas_KeyRel_ArrowRight)
        self.canvas.bind('<KeyRelease-Up>',self.canvas_KeyRel_ArrowUp)
        self.canvas.bind('<Shift-KeyRelease-Up>' \
            ,self.canvas_KeyRel_ArrowUp_Shift)
        self.canvas.bind('<KeyRelease-space>',self.canvas_KeyRel_space)
        self.frameButtons = Tkinter.Frame(self.frameMain,borderwidth='1'
            ,height='1')
        self.frameButtons.pack(anchor='nw',fill='x',side='top')
        self.resetButton = Tkinter.Button(self.frameButtons
            ,activebackground='#F00',command=self.reset,text='Reset')
        self.resetButton.pack(anchor='sw',expand='yes',fill='x',side='left')
        self.undoButton = Tkinter.Button(self.frameButtons
            ,activebackground='#FF0',command=self.undo_last,text='Undo')
        self.undoButton.pack(anchor='sw',expand='yes',fill='x',side='left')
        self.zoomButton = Tkinter.Checkbutton(self.frameButtons
            ,command=self.zoom_mode,text='Zoom')
        self.zoomButton.pack(anchor='sw',expand='yes',fill='x',side='left')
        self.unzoomButton = Tkinter.Button(self.frameButtons
            ,activebackground='#00F',command=self.unzoom_image,text='<-|->')
        self.unzoomButton.pack(anchor='sw',expand='yes',fill='x',side='left')
        self.plusButton = Tkinter.Button(self.frameButtons,command=self.plus_box
            ,text='+')
        self.plusButton.pack(anchor='sw',expand='yes',fill='x',side='left')
        self.goButton = Tkinter.Button(self.frameButtons,activebackground='#0F0'
            ,command=self.start_cropping,text='Crops')
        self.goButton.pack(anchor='sw',expand='yes',fill='x',side='left')
        self.quitButton = Tkinter.Button(self.frameButtons
            ,activebackground='#F00',command=self.quit,text='Quit')
        self.quitButton.pack(anchor='sw',expand='yes',fill='x',side='left')
        #
        #Your code here
        #
        self.quitButton_ttp = CreateToolTip(self.quitButton, "Exit")
        self.resetButton_ttp = CreateToolTip(self.resetButton, "Reset all rectangles")
        self.undoButton_ttp = CreateToolTip(self.undoButton, "Undo last rectangle")
        self.zoomButton_ttp = CreateToolTip(self.zoomButton, "On/Off Zoom mode")
        self.unzoomButton_ttp = CreateToolTip(self.unzoomButton, "Unzoom, view all image")
        self.plusButton_ttp = CreateToolTip(self.plusButton, "Plus box, extent rectangle")
        self.goButton_ttp = CreateToolTip(self.goButton, "Go, begin cropping")
        self.croprect_start = None
        self.croprect_end = None
        self.crop_count = 0
        self.canvas_rects = []
        self.crop_rects = []
        self.current_rect = None
        self.zoommode = False
        self.w = 1
        self.h = 1
        self.x0 = 0
        self.y0 = 0
        self.n = 0
        self.config = None
        self.delimiters = ' |,|\t|#|\|'
        self._after_id = None
        self.filename = None
        self.lbIndex = None # Keeps item index in listbox
    #
    #Start of event handler methods
    #


    def canvas_KeyRel_ArrowDown(self, event=None):
        print("Pressed Canvas Arrow Down")

    def canvas_KeyRel_ArrowLeft(self, event=None):
        print("Pressed Canvas Arrow Left")

    def canvas_KeyRel_ArrowRight(self, event=None):
        print('Pressed Canvas Arrow Right')

    def canvas_KeyRel_ArrowUp(self, event=None):
        print('Pressed Canvas Arrow Up')

    def canvas_KeyRel_ArrowUp_Shift(self, event=None):
        # Shift + ArrowUp
        print('Pressed Canvas Shift Arrow Up')

    def canvas_KeyRel_space(self, event=None):
        print('Pressed Canvas SPACE')

    def canvas_mouse1_callback(self, event=None):
        self.croprect_start = (event.x, event.y)

    def canvas_mouseb1move_callback(self, event=None):
        if self.current_rect:
            self.canvas.delete(self.current_rect)
        x1 = self.croprect_start[0]
        y1 = self.croprect_start[1]
        x2 = event.x
        y2 = event.y
        bbox = (x1, y1, x2, y2)
        cr = self.canvas.create_rectangle(bbox)
        self.current_rect = cr

    def canvas_mouseup1_callback(self, event=None):
        self.croprect_end = (event.x, event.y)
        self.set_crop_area()
        self.canvas.delete(self.current_rect)
        self.current_rect = None

    def on_ScanCropper_Config(self, event=None):
        if self._after_id:
            self.after_cancel(self._after_id)
        self._after_id = self.after(1200, self.draw_after_resize)

    def on_canvas_KeyRel_KeyPad_PageDown(self,Event=None):
        self.pressPage(self.PAGE_DOWN)

    def on_canvas_KeyRel_KeyPad_PageUp(self,Event=None):
        self.pressPage(self.PAGE_UP)

    def on_canvas_KeyRel_PageDown(self, event=None):
        self.pressPage(self.PAGE_DOWN)

    def on_canvas_KeyRel_PageUp(self, event=None):
        self.pressPage(self.PAGE_UP)

    def on_lbFiles_mouseClick_1(self, event=None):
        self.lbIndex = self.lbFiles.curselection()[0]
        self.load_lbFiles_image(self.lbFiles.get(tk.ACTIVE))
    #
    #Start of non-Rapyd user code
    #
    
    PAGE_UP = -1
    PAGE_DOWN = 1
    
    def pressPage(self, direction=0):
        index = self.lbFiles.curselection()[0] + direction
        self.lbFiles.selection_clear(0, tk.END)
        self.lbSelect(index)

    # Programmatically select image in a listbox
    def lbSelect(self, index):
        if index < 0:
            index = 0
        elif index == self.lbFiles.size():
            index = self.lbFiles.size()-1  
        self.lbFiles.select_set(index)
        self.lbFiles.activate(index)
        if index != self.lbIndex:
            self.load_lbFiles_image(self.lbFiles.get(tk.ACTIVE))
            self.lbIndex = index
        
    def draw_after_resize(self):
        # Check if there is a selection in file list
        if self.filename:
            self.loadimage()
 
    def load_lbFiles_image(self, imagePath):
        self.filename = os.path.join(self.config['input-directory'], imagePath)
        if os.path.exists(self.filename):
            self.loadimage()
       
    def set_crop_area(self):
        r = Rect(self.croprect_start, self.croprect_end)

        # adjust dimensions
        r.clip_to(self.image_thumb_rect)

        # ignore rects smaller than this size
        if min(r.h, r.w) < 10:
            return

        ra = r
        ra = ra.scale_rect(self.scale)
        ra = ra.move_rect(self.x0, self.y0)
        ra = ra.valid_rect(self.w, self.h)
        if self.zoommode:
            self.canvas.delete(tk.ALL)
            self.x0 = ra.left
            self.y0 = ra.top
            za = (ra.left, ra.top, ra.right, ra.bottom)
            self.image_thumb = self.image.crop(za)
            self.image_thumb.thumbnail(thumbsize)
            self.image_thumb_rect = Rect(self.image_thumb.size)
            self.image_thumb_rect.set_thumboffset(int(self.config['thumboffset']))
            self.displayimage()
            x_scale = float(ra.w) / self.image_thumb_rect.w
            y_scale = float(ra.h) / self.image_thumb_rect.h
            self.scale = (x_scale, y_scale)
            self.redraw_rect()
            self.zoommode = False
            self.zoomButton.deselect()
        else:
            self.drawrect(r)
            self.crop_rects.append(ra)
            self.n = self.n + 1

    def zoom_mode(self):
        if self.zoommode:
            self.zoommode = False
        else:
            self.zoommode = True

    def unzoom_image(self):
        self.canvas.delete(tk.ALL)
        self.zoommode = False
        self.zoomButton.deselect()
        self.x0 = 0
        self.y0 = 0
        self.image_thumb = self.image.copy()
        self.image_thumb.thumbnail(thumbsize)
        self.image_thumb_rect = Rect(self.image_thumb.size)
        self.image_thumb_rect.set_thumboffset(int(self.config['thumboffset']))
        self.displayimage()
        x_scale = float(self.image_rect.w) / self.image_thumb_rect.w
        y_scale = float(self.image_rect.h) / self.image_thumb_rect.h
        self.scale = (x_scale, y_scale)
        self.redraw_rect()

    def plus_box(self):
        if self.n > 1:
            self.canvas.delete(tk.ALL)
            if self.crop_rects:
                ra = self.crop_rects[self.n - 1]
                self.crop_rects.pop()
                self.n = self.n - 1
                ra0 = self.crop_rects[self.n - 1]
                ra0 = ra0.plus_rect(ra)
                self.crop_rects[self.n - 1] = ra0
                self.displayimage()
                self.redraw_rect()
                self.zoommode = False
                self.zoomButton.deselect()

    def redraw_rect(self):
        for croparea in self.crop_rects:
            self.drawrect(croparea.rescale_rect(self.scale, self.x0, self.y0))

    def undo_last(self):
        if self.canvas_rects:
            r = self.canvas_rects.pop()
            self.canvas.delete(r)

        if self.crop_rects:
            self.crop_rects.pop()

    def drawrect(self, rect):
        bbox = (rect.left, rect.top, rect.right, rect.bottom)
        cr = self.canvas.create_rectangle(
            bbox, activefill='', fill='red', stipple='gray25')
        self.canvas_rects.append(cr)

    def reset(self):
        self.canvas.delete(tk.ALL)
        self.zoommode = False
        self.zoomButton.deselect()
        self.canvas_rects = []
        self.crop_rects = []
        self.displayimage()
        
    def displayimage(self):
        self.photoimage = ImageTk.PhotoImage(self.image_thumb)
        w, h = self.image_thumb.size
        
        self.canvas.create_image(
            int(self.config['thumboffset']),
            int(self.config['thumboffset']),
            anchor=tk.NW,
            image=self.photoimage)

    def loadimage(self):
        self.image = Image.open(self.filename)
        self.image_rect = Rect(self.image.size)
        self.image_rect.set_thumboffset(int(self.config['thumboffset']))
        self.w = self.image_rect.w
        self.h = self.image_rect.h
        # TODO: needed? borderwidth = self.canvas.config()['borderwidth'][4]
        
        self.image_thumb = self.image.copy()
        self.image_thumb.thumbnail(
            [ self.canvas.winfo_width() - int(self.config['thumboffset']),
              self.canvas.winfo_height() - int(self.config['thumboffset']) ]
        )
        self.image_thumb_rect = Rect(self.image_thumb.size)
        self.image_thumb_rect.set_thumboffset(int(self.config['thumboffset']))

        self.displayimage()
        x_scale = float(self.image_rect.w) / self.image_thumb_rect.w
        y_scale = float(self.image_rect.h) / self.image_thumb_rect.h
        self.scale = (x_scale, y_scale)

    def newfilename(self, filenum):
        f, e = os.path.splitext(self.filename)
        return '%s_crop_%s%s' % (f, filenum, e)

    def start_cropping(self):
        cropcount = 0
        for croparea in self.crop_rects:
            cropcount += 1
            f = self.newfilename(cropcount)
            print f, croparea
            self.crop(croparea, f)
        self.quit()

    def crop(self, croparea, filename):
        ca = (croparea.left, croparea.top, croparea.right, croparea.bottom)
        newimg = self.image.crop(ca)
        newimg.save(filename)
        
    def load_image_list(self):
        if self.config is not None:
            self.lbFiles.delete(0, tk.END)
            suffixtuple = tuple(re.split(self.delimiters, self.config['image-extensions']))
            for item in os.listdir(self.config['input-directory']):
                if os.path.isfile(os.path.join(self.config['input-directory'], item)):
                    if item.lower().endswith(suffixtuple): # The arg can be a tuple of suffixes to look for
                        self.lbFiles.insert(tk.END, item)
            self.update_idletasks()
            # If there are items in listbox, select the 1st one
            if self.lbFiles.size() > 0:
                self.lbFiles.select_set(0)
                #self.lbFiles.activate(0)
                self.load_lbFiles_image(self.lbFiles.get(tk.ACTIVE))
                self.canvas.focus_set()


class CreateToolTip(object):
    """
    create a tooltip for a given widget
    """
    def __init__(self, widget, text='widget info'):
        self.waittime = 500     #miliseconds
        self.wraplength = 180   #pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = tk.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
            background="#ffffff", relief='solid', borderwidth=1,
            wraplength = self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()
            
class Rect(object):
    def __init__(self, *args):
        self.set_points(*args)
        self.thumboffset = 0

    def set_points(self, *args):
        if len(args) == 2:
            pt1 = args[0]
            pt2 = args[1]
        elif len(args) == 1:
            pt1 = (0, 0)
            pt2 = args[0]
        elif len(args) == 0:
            pt1 = (0, 0)
            pt2 = (0, 0)

        x1, y1 = pt1
        x2, y2 = pt2

        self.left = min(x1, x2)
        self.top = min(y1, y2)
        self.right = max(x1, x2)
        self.bottom = max(y1, y2)

        self._update_dims()

    def clip_to(self, containing_rect):
        cr = containing_rect
        self.top = max(self.top, cr.top + self.thumboffset)
        self.bottom = min(self.bottom, cr.bottom + self.thumboffset)
        self.left = max(self.left, cr.left + self.thumboffset)
        self.right = min(self.right, cr.right + self.thumboffset)
        self._update_dims()

    def _update_dims(self):
        """added to provide w and h dimensions."""

        self.w = self.right - self.left
        self.h = self.bottom - self.top

    def scale_rect(self, scale):
        x_scale = scale[0]
        y_scale = scale[1]

        r = Rect()
        r.top = int((self.top - self.thumboffset) * y_scale)
        r.bottom = int((self.bottom - self.thumboffset) * y_scale)
        r.right = int((self.right - self.thumboffset) * x_scale)
        r.left = int((self.left - self.thumboffset) * x_scale)
        r._update_dims()

        return r

    def move_rect(self, x0, y0):
        r = Rect()
        r.top = int(self.top + y0)
        r.bottom = int(self.bottom + y0)
        r.right = int(self.right + x0)
        r.left = int(self.left + x0)
        r._update_dims()
        return r

    def rescale_rect(self, scale, x0, y0):
        x_scale = scale[0]
        y_scale = scale[1]

        r = Rect()
        r.top = int((self.top - y0) / y_scale + self.thumboffset)
        r.bottom = int((self.bottom - y0) / y_scale + self.thumboffset)
        r.right = int((self.right - x0) / x_scale + self.thumboffset)
        r.left = int((self.left - x0) / x_scale + self.thumboffset)
        r._update_dims()
        return r

    def plus_rect(self, r0):
        r = Rect()
        r.top = min(self.top, r0.top)
        r.bottom = max(self.bottom, r0.bottom)
        r.right = max(self.right, r0.right)
        r.left = min(self.left, r0.left)
        r._update_dims()
        return r

    def valid_rect(self, w, h):
        r = Rect()
        r.top = self.top
        if r.top < 0:
            r.top = 0
        if r.top > h - 1:
            r.top = h - 1
        r.bottom = self.bottom
        if r.bottom < 1:
            r.bottom = 1
        if r.bottom > h:
            r.bottom = h
        r.right = self.right
        if r.right < 1:
            r.right = 1
        if r.right > w:
            r.right = w
        r.left = self.left
        if r.left < 0:
            r.left = 0
        if r.left > w - 1:
            r.left = w - 1
        r._update_dims()
        return r

    def set_thumboffset(self, thumboffset=0):
        self.thumboffset = thumboffset

    def __repr__(self):
        return '(%d,%d)-(%d,%d)' % (self.left, self.top, self.right, self.bottom)

# Class that handles configuration
class ScanConfig(object):

    def __init__(self, configFile=None):
        self.section = self.__class__.__name__.upper()
        self.get_default_config()

        if configFile is None:
            # Create default configuration in OS-independent "home" directory
            configPath = os.path.join(os.path.expanduser('~'), '.config', self.__class__.__name__.lower())
            if not os.path.exists(configPath):
                os.makedirs(configPath)
            self.configFile = os.path.join(configPath, 'config.ini')
            if os.path.exists(self.configFile):
                self.config = confpars.SafeConfigParser()
                self.config.read(self.configFile)
            else:
                self.config = self.default_config
                with open(self.configFile, 'wb') as cf:
                    self.config.write(cf)
        elif os.path.exists(configFile):
            self.configFile = os.path.normpath(configFile)
            self.config = confpars.SafeConfigParser()
            self.config.read(self.configFile)
        else:
            # Path given, but does not exist
            raise Exception("Configuration file '{0}' does not exist".format(configFile))
    
    # Gets default configuration
    def get_default_config(self):
        self.default_config = confpars.SafeConfigParser()
        self.default_config.add_section(self.section)
        # Position and size of main window
        self.default_config.set(self.section, 'geometry', '1024x768+10+10')
        # Directory with pictures to process
        self.default_config.set(self.section, 'input-directory', os.path.expanduser('~'))
        # Directory to write resulting pictures into
        self.default_config.set(self.section, 'output-directory', os.path.expanduser('~'))
        # Extensions of files considered to be pictures
        self.default_config.set(self.section, 'image-extensions', 'tif tiff jpg jpeg gif png')
        # Thumbnail offset
        self.default_config.set(self.section, 'thumboffset', '4')
        
    def __getitem__(self, key):
        try:
            return self.config.get(self.section, key)
        except confpars.NoOptionError:
            try:
                return self.default_config.get(self.section, key)
            except confpars.NoOptionError:
                return None

    def __del__(self):
        with open(self.configFile, 'wb') as cf:
            self.config.write(cf)


pass #---end-of-form---

def window_close():
    Root.destroy()

try:
    #--------------------------------------------------------------------------#
    # User code should go after this comment so it is inside the "try".        #
    #     This allows rpErrorHandler to gain control on an error so it         #
    #     can properly display a Rapyd-aware error message.                    #
    #--------------------------------------------------------------------------#

    #Adjust sys.path so we can find other modules of this project
    import sys
    if '.' not in sys.path:
        sys.path.append('.')
    #Put lines to import other modules of this project here
    import argparse    
    import tkFileDialog
    import os
    import re
    try:
        # for Python2
        import ConfigParser as confpars
    except ImportError:
        # for Python3
        import configparser as confpars
    #
    from PIL import Image, ImageTk
    tk = Tkinter
 
    if __name__ == '__main__':
        # Parse arguments
        parser = argparse.ArgumentParser(description='Picture cropper')
        parser.add_argument('-c', '--config', '--config-file', dest='configFile', default=None, help='Configuration file path')
        parser.add_argument('-d', '--debug', default=0, help='Debug level')
        args = parser.parse_args()

        # Load configuration
        conf = ScanConfig(args.configFile)

        Root = Tkinter.Tk()
        Tkinter.CallWrapper = rpErrorHandler.CallWrapper
        App = ScanCropper(Root)
        App.pack(expand='yes',fill='both')

        # Set window
        Root.geometry(conf['geometry'])
        # Allow closing windows by clicking "X"
        Root.protocol("WM_DELETE_WINDOW", window_close)
        Root.title('Scan Cropper')
        App.config = conf
        App.load_image_list()
        Root.mainloop()
    #--------------------------------------------------------------------------#
    # User code should go above this comment.                                  #
    #--------------------------------------------------------------------------#
except:
    rpErrorHandler.RunError()