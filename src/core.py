import threading
import pygame
import time
import os

class SoundController():
    
    def __init__(self,index:int):
        self.index = index
        self.loopThread: loopThread
        self.fade_out_timer = 0
        self.fade_in_timer = 0
        self.is_loop = False
        self.channel = pygame.mixer.Channel(index)
        self.sound = None
        self.volume = 0
        self.sound_name = ""
    
    def reproducir_audio(self,volume):
        if self.sound :
            self.volume = float(volume)/100
            self.channel.set_volume(self.volume*self.volume)
            self.channel.play(self.sound)
            
            
    def cambiar_volumen(self,volumen):
        if self.sound :
            self.volume= float(volumen)/100
            self.channel.set_volume(self.volume*self.volume)
            
            
    def parar_audio(self):
        if self.sound :
           self.channel.stop()
           
    def set_fade_out_timer(self,valor):
        self.fade_out_timer = (valor*5) / 10 
        
    def fade_out(self):
        if self.sound:
            self.channel.fadeout(int(self.fade_out_timer*1000))
            self.loopThread.loop_off()
            self.loop_check.setChecked(False)
        
    
    #def fade_out_t(self,timer):
    #    print("fade out t")
    #    print(timer)
    #    self.channel.fadeout(int(timer))
    #    self.loopThread.loop_off()
    #    self.loop_check.setChecked(False)

    def set_fade_in_timer(self,valor):
        self.fade_in_timer = (valor*5) / 10 

    def fade_in(self):
        if self.sound:
            time = int(self.fade_in_timer*1000)
            if time != 0:
                self.channel.set_volume(self.volume*self.volume)
                self.channel.play(self.sonido,0,0,time)
            else:
                self.channel.set_volume(self.volume*self.volume)
                self.channel.play(self.sonido,0,0)

            self.playCheckedThread.start()
        
        
    #def fade_in_t(self,timer):
    #    if self.sound:
    #        time = int(timer)
    #        if time != 0:
    #            volumen_float = float(self.barra_volumen.value())/100
    #            self.channel.set_volume(volumen_float*volumen_float)
    #            self.channel.play(self.sonido,0,0,time)
    #            self.boton_reproducir.setChecked(True)
    #        else:
    #            volumen_float = float(self.barra_volumen.value())/100
    #            self.channel.set_volume(volumen_float*volumen_float)
    #            self.channel.play(self.sonido,0,0)
    #            self.boton_reproducir.setChecked(True)
#
    #        self.playCheckedThread = playCheckedThread(self)
    #        self.playCheckedThread.start()
    
        
 
    def load_sound(self,ruta):
        self.sound = pygame.mixer.Sound(ruta)
        

    def set_loop(self):
        try:
            loop = self.loop_check.isChecked()
            if loop :
                self.loopThread= loopThread(self)
                self.loopThread.start()
            else:
                self.loopThread.loop_off()
        except:
            self.loopThread.loop_off()
        
        
# Hilo para el control del check de una channel      
class playCheckedThread(threading.Thread):
    def __init__(self, channelController: SoundController ):
        threading.Thread.__init__(self)
        self.channelController = channelController

    def run(self):
        try:
            while self.channelController.channel.get_busy():
                time.sleep(0.5)
            self.channelController.boton_reproducir.setChecked(False)
        except:
            pass


# Hilo para el control del loop  
class loopThread(threading.Thread):
    def __init__(self, channelController: SoundController ):
        threading.Thread.__init__(self)
        self.channelController = channelController
        self._stop = False

    def run(self):
        try:
            while not self._stop:
                time.sleep(1)
                if not self.channelController.channel.get_busy():
                    self.channelController.reproducir_audio(True)
            while self.channelController.channel.get_busy():
                pass
            self.channelController.boton_reproducir.setChecked(False)
        except:
            self.loop_off()
             

    def loop_off(self):
        try:
            self._stop = True
        except:
            pass