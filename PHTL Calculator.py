import tkinter as tk


HEIGTH = 800
WIDTH = 800

root = tk.Tk()

root.title("PHTL Master Calculator 2.0.3----Justin Smith---2020")

canvas = tk.Canvas(root, height=HEIGTH, width=WIDTH, bg='#a9b1b6', relief='raised' )
canvas.pack()

ocimage = tk.PhotoImage(file='ocean.ppm')


new_color = '#74add0'
bgcolor = '#74add0'


frame = tk.Frame(root, bg ='#74add0', relief='solid')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

mainlabel = tk.Label(frame, text="PHTL Master Calculator", fg='#0c161c', bg ='#74add0', font=('fixedsys', 24))
mainlabel.place(relx=0.1, rely=0.1, relwidth=0.8)

colorlabel = tk.Label(frame, text="Change Background Color", fg='#0c161c', bg ='#74add0', font=('fixedsys', 8))
colorlabel.place(height=50, width=200, x=0, y=600)

def blumains():
    frame.configure(bg='#74add0')
    mainlabel.configure(bg='#74add0')
    colorlabel.configure(bg='#74add0')

def redmains():
    frame.configure(bg='#ea6565')
    mainlabel.configure(bg='#ea6565')
    colorlabel.configure(bg='#ea6565')

def grnmains():
    frame.configure(bg='#7ff287')
    mainlabel.configure(bg='#7ff287')
    colorlabel.configure(bg='#7ff287')

def stlmains():
    frame.configure(bg='#999999')
    mainlabel.configure(bg='#999999')
    colorlabel.configure(bg='#999999')

def ocmains():
    
    oclabel = tk.Label(canvas, image=ocimage)
    oclabel.place(x=0, y=0, relwidth=1, relheight=1)
    

blumain = tk.Button(frame, text="Blue", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=blumains)
blumain.place(height=50, width=80, x=200, y=600)

redmain = tk.Button(frame, text="Red", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=redmains)
redmain.place(height=50, width=80, x=280, y=600)

grnmain = tk.Button(frame, text="Green", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=grnmains)
grnmain.place(height=50, width=80, x=360, y=600)

stlmain = tk.Button(frame, text="Steel", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=stlmains)
stlmain.place(height=50, width=80, x=440, y=600)

ocmain = tk.Button(frame, text="Ocean", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=ocmains)
ocmain.place(height=50, width=80, x=520, y=600)









def speed():
    speedtop = tk.Toplevel(root, bg ='#74add0', height=600, width=600)
    speedtop.title("Universal Speed Calculator")

    freqlabel = tk.Label(speedtop, text="Enter Frequency (kHz)", font=('fixedsys', 12), fg='#0c161c', bg ='#74add0')
    freqlabel.place(height=50, width=175, x=10, y=10)
    freqentry = tk.Entry(speedtop, font=('fixedsys', 24) )
    freqentry.place(height=50, width=175, x=10, y=50)
    dpilabel = tk.Label(speedtop, text="Enter Resolution (DPI)", font=('fixedsys', 12), fg='#0c161c', bg ='#74add0')
    dpilabel.place(height=50, width=175, x=10, y=90)
    dpientry = tk.Entry(speedtop, font=('fixedsys', 24))
    dpientry.place(height=50, width=175, x=10, y=130)

    colorlabels = tk.Label(speedtop, text="Change Background Color", fg='#0c161c', bg ='#74add0', font=('fixedsys', 8))
    colorlabels.place(height=50, width=200, x=0, y=500)

    def bluspeeds():
        speedtop.configure(bg='#74add0')
        freqlabel.configure(bg='#74add0')
        dpilabel.configure(bg='#74add0')
        colorlabels.configure(bg='#74add0')

    def grnspeeds():
        speedtop.configure(bg='#7ff287')
        freqlabel.configure(bg='#7ff287')
        dpilabel.configure(bg='#7ff287')
        colorlabels.configure(bg='#7ff287')

    def redspeeds():
        speedtop.configure(bg='#ea6565')
        freqlabel.configure(bg='#ea6565')
        dpilabel.configure(bg='#ea6565')
        colorlabels.configure(bg='#ea6565')

    def stlspeeds():
        speedtop.configure(bg='#999999')
        freqlabel.configure(bg='#999999')
        dpilabel.configure(bg='#999999')
        colorlabels.configure(bg='#999999')

    
        

    bluspeed = tk.Button(speedtop, text="Blue", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=bluspeeds)
    bluspeed.place(height=50, width=80, x=200, y=500)

    grnspeed = tk.Button(speedtop, text="Green", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=grnspeeds)
    grnspeed.place(height=50, width=80, x=360, y=500)

    redspeed = tk.Button(speedtop, text="Red", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=redspeeds)
    redspeed.place(height=50, width=80, x=280, y=500)

    stlspeed = tk.Button(speedtop, text="Steel", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=stlspeeds)
    stlspeed.place(height=50, width=80, x=440, y=500)


    def speedexit():
        speedtop.destroy()

    speedback = tk.Button(speedtop, text="Back", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 4),
                            command=speedexit)
    speedback.place(height=25, width=40, x=550, y=10)

    

    

    


    

    def speedcalc(self):
        freq = int(freqentry.get())
        dpi = int(dpientry.get())

        speedform = ((freq*1000) / dpi)
        webform = speedform * 5
        sledlabel = tk.Label(speedtop, text="Platen Speed = " + str(round(speedform, 2)) + " inches per second", font=('fixedsys', 16), fg='#0c161c', relief='solid')
        sledlabel.place(height=50, width=450, x=50, y=325)
        weblabel = tk.Label(speedtop, text="Web Speed = " + str(round(webform, 1)) + " feet per minute",
                             font=('fixedsys', 16), fg='#0c161c', relief='solid')
        weblabel.place(height=50, width=450, x=50, y=375)


        

    speedsub = tk.Button(speedtop, text="Submit", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 12),
                            command=speedcalc)
    speedsub.place(height=50, width=175, x=10, y=190)

    speedtop.bind('<Return>', speedcalc)
    

    def helpspeed():
        helptop = tk.Toplevel(speedtop, bg ='#74add0', height=250, width=250)
        helptop.title("Universal Speed Calculator---HELP")
        helplabel = tk.Label(helptop, text="Enter Print Frequency in kHz and Print (Process) Resolution in DPI. \n Hit Submit to Calculate Platen Speed in IPS or Webdrive Speed in FPM", font=('fixedsys', 16), fg='#0c161c', pady=50)
        helplabel.pack()

    speedhelp = tk.Button(speedtop, text="Help", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 12),
                            command=helpspeed)
    speedhelp.place(height=50, width=175, x=10, y=250)

    



def mass():
    masstop = tk.Toplevel(root, bg ='#74add0', height=600, width=600)
    masstop.title("Universal Dropmass Calculator")

    jetlabel = tk.Label(masstop, text="Number of Jets", font=('fixedsys', 12), fg='#0c161c', bg ='#74add0')
    jetlabel.place(height=50, width=175, x=10, y=10)
    jetentry = tk.Entry(masstop, font=('fixedsys', 24))
    jetentry.place(height=50, width=175, x=10, y=50)
    jetoutlabel = tk.Label(masstop, text="Number of Jets Out", font=('fixedsys', 12), fg='#0c161c', bg ='#74add0')
    jetoutlabel.place(height=50, width=175, x=10, y=90)
    jetoutentry = tk.Entry(masstop, font=('fixedsys', 24))
    jetoutentry.place(height=50, width=175, x=10, y=130)
    copylabel = tk.Label(masstop, text="Number of Copies/Fires", font=('fixedsys', 12), fg='#0c161c', bg ='#74add0')
    copylabel.place(height=50, width=175, x=10, y=170)
    copyentry = tk.Entry(masstop, font=('fixedsys', 24))
    copyentry.place(height=50, width=175, x=10, y=210)
    pixellabel = tk.Label(masstop, text="Number of Pixels", font=('fixedsys', 12), fg='#0c161c', bg ='#74add0')
    pixellabel.place(height=50, width=175, x=10, y=250)
    pixelentry = tk.Entry(masstop, font=('fixedsys', 24))
    pixelentry.place(height=50, width=175, x=10, y=290)
    gramlabel = tk.Label(masstop, text="Mass in Grams:", font=('fixedsys', 12), fg='#0c161c', bg ='#74add0')
    gramlabel.place(height=50, width=175, x=10, y=330)
    gramentry = tk.Entry(masstop, font=('fixedsys', 24))
    gramentry.place(height=50, width=175, x=10, y=370)

    colorlabelm = tk.Label(masstop, text="Change Background Color", fg='#0c161c', bg ='#74add0', font=('fixedsys', 8))
    colorlabelm.place(height=50, width=200, x=0, y=500)


    def blumasses():
        masstop.configure(bg='#74add0')
        jetlabel.configure(bg='#74add0')
        jetoutlabel.configure(bg='#74add0')
        copylabel.configure(bg='#74add0')
        pixellabel.configure(bg='#74add0')
        gramlabel.configure(bg='#74add0')
        colorlabelm.configure(bg='#74add0')

    def grnmasses():
        masstop.configure(bg='#7ff287')
        jetlabel.configure(bg='#7ff287')
        jetoutlabel.configure(bg='#7ff287')
        copylabel.configure(bg='#7ff287')
        pixellabel.configure(bg='#7ff287')
        gramlabel.configure(bg='#7ff287')
        colorlabelm.configure(bg='#7ff287')

    def redmasses():
        masstop.configure(bg='#ea6565')
        jetlabel.configure(bg='#ea6565')
        jetoutlabel.configure(bg='#ea6565')
        copylabel.configure(bg='#ea6565')
        pixellabel.configure(bg='#ea6565')
        gramlabel.configure(bg='#ea6565')
        colorlabelm.configure(bg='#ea6565')

    def stlmasses():
        masstop.configure(bg='#999999')
        jetlabel.configure(bg='#999999')
        jetoutlabel.configure(bg='#999999')
        copylabel.configure(bg='#999999')
        pixellabel.configure(bg='#999999')
        gramlabel.configure(bg='#999999')
        colorlabelm.configure(bg='#999999')

    



    blumass = tk.Button(masstop, text="Blue", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=blumasses)
    blumass.place(height=50, width=80, x=200, y=500)

    grnmass = tk.Button(masstop, text="Green", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=grnmasses)
    grnmass.place(height=50, width=80, x=360, y=500)

    redmass = tk.Button(masstop, text="Red", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=redmasses)
    redmass.place(height=50, width=80, x=280, y=500)

    stlmass = tk.Button(masstop, text="Steel", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=stlmasses)
    stlmass.place(height=50, width=80, x=440, y=500)


    def massexit():
        masstop.destroy()

    massback = tk.Button(masstop, text="Back", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 4),
                            command=massexit)
    massback.place(height=25, width=40, x=550, y=10)


    def masscalc(self):
        jets = int(jetentry.get())
        jetsout = int(jetoutentry.get())
        fires = int(copyentry.get())
        pixels = int(pixelentry.get())
        grams = float(gramentry.get())
        hadm = (grams * 1000000000) / ((jets - jetsout) * pixels * fires)

        hadmlabel = tk.Label(masstop, text="HADM: " + str(round(hadm, 2)) + " ng", font=('fixedsys', 20), fg='#0c161c', relief='solid')
        hadmlabel.place(height=50, width=300, x=230, y=210)






    masssub = tk.Button(masstop, text="Submit", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 12),
                         command=masscalc)
    masssub.place(height=50, width=175, x=10, y=430)
    masstop.bind('<Return>', masscalc)

    def helpmass():
        helpmtop = tk.Toplevel(masstop, bg ='#74add0', height=250, width=250)
        helpmtop.title("Universal Dropmass Calculator---HELP")
        helpmlabel = tk.Label(helpmtop, text="Enter Total # of Jets In Printhead \n\n Enter # of Jets Out in Printhead \n\n Enter Copies/Fires to be Printed/Fired \n\n Enter Pixels in Dropmass Image (if on Char, Enter 1) \n\n Take Mass Measurement and Enter Mass in Grams \n\n Hit Submit to Calculate Head Average Drop Mass in ng.", font=('fixedsys', 16), fg='#0c161c', pady=50)
        helpmlabel.pack()

    masshelp = tk.Button(masstop, text="Help", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 12),
                            command=helpmass)
    masshelp.place(height=50, width=175, x=195, y=430)



def calibrate():
    calitop = tk.Toplevel(root, bg ='#74add0', height=600, width=600)
    calitop.title("Mass Calibrate Calculator")
    v1label = tk.Label(calitop, text="Voltage # 1 (low)", font=('fixedsys', 12), fg='#0c161c', bg ='#74add0')
    v1label.place(height=50, width=175, x=10, y=10)
    v1entry = tk.Entry(calitop, font=('fixedsys', 24))
    v1entry.place(height=50, width=175, x=10, y=50)
    v2label = tk.Label(calitop, text="Voltage # 2 (mid)", font=('fixedsys', 12), fg='#0c161c', bg ='#74add0')
    v2label.place(height=50, width=175, x=10, y=90)
    v2entry = tk.Entry(calitop, font=('fixedsys', 24))
    v2entry.place(height=50, width=175, x=10, y=130)
    v3label = tk.Label(calitop, text="Voltage # 3 (high)", font=('fixedsys', 12), fg='#0c161c', bg ='#74add0')
    v3label.place(height=50, width=175, x=10, y=170)
    v3entry = tk.Entry(calitop, font=('fixedsys', 24))
    v3entry.place(height=50, width=175, x=10, y=210)
    targetlabel = tk.Label(calitop, text="Target Mass (ng)", font=('fixedsys', 12), fg='#0c161c', bg ='#74add0')
    targetlabel.place(height=50, width=175, x=10, y=250)
    targetentry = tk.Entry(calitop, font=('fixedsys', 24))
    targetentry.place(height=50, width=175, x=10, y=290)
    m1label = tk.Label(calitop, text="Voltage 1 Mass (ng)", font=('fixedsys', 12), fg='#0c161c', bg ='#74add0')
    m1label.place(height=50, width=175, x=300, y=10)
    m1entry = tk.Entry(calitop, font=('fixedsys', 24))
    m1entry.place(height=50, width=175, x=300, y=50)
    m2label = tk.Label(calitop, text="Voltage 2 Mass (ng)", font=('fixedsys', 12), fg='#0c161c', bg ='#74add0')
    m2label.place(height=50, width=175, x=300, y=90)
    m2entry = tk.Entry(calitop, font=('fixedsys', 24))
    m2entry.place(height=50, width=175, x=300, y=130)
    m3label = tk.Label(calitop, text="Voltage 3 Mass (ng)", font=('fixedsys', 12), fg='#0c161c', bg ='#74add0')
    m3label.place(height=50, width=175, x=300, y=170)
    m3entry = tk.Entry(calitop, font=('fixedsys', 24))
    m3entry.place(height=50, width=175, x=300, y=210)

    colorlabelc = tk.Label(calitop, text="Change Background Color", fg='#0c161c', bg ='#74add0', font=('fixedsys', 8))
    colorlabelc.place(height=50, width=200, x=0, y=500)

    def blucali():
        calitop.configure(bg='#74add0')
        v1label.configure(bg='#74add0')
        v2label.configure(bg='#74add0')
        v3label.configure(bg='#74add0')
        targetlabel.configure(bg='#74add0')
        m1label.configure(bg='#74add0')
        m2label.configure(bg='#74add0')
        m3label.configure(bg='#74add0')
        colorlabelc.configure(bg='#74add0')

    def grncali():
        calitop.configure(bg='#7ff287')
        v1label.configure(bg='#7ff287')
        v2label.configure(bg='#7ff287')
        v3label.configure(bg='#7ff287')
        targetlabel.configure(bg='#7ff287')
        m1label.configure(bg='#7ff287')
        m2label.configure(bg='#7ff287')
        m3label.configure(bg='#7ff287')
        colorlabelc.configure(bg='#7ff287')

    def redcali():
        calitop.configure(bg='#ea6565')
        v1label.configure(bg='#ea6565')
        v2label.configure(bg='#ea6565')
        v3label.configure(bg='#ea6565')
        targetlabel.configure(bg='#ea6565')
        m1label.configure(bg='#ea6565')
        m2label.configure(bg='#ea6565')
        m3label.configure(bg='#ea6565')
        colorlabelc.configure(bg='#ea6565')

    def stlcali():
        calitop.configure(bg='#999999')
        v1label.configure(bg='#999999')
        v2label.configure(bg='#999999')
        v3label.configure(bg='#999999')
        targetlabel.configure(bg='#999999')
        m1label.configure(bg='#999999')
        m2label.configure(bg='#999999')
        m3label.configure(bg='#999999')
        colorlabelc.configure(bg='#999999')


    blucali = tk.Button(calitop, text="Blue", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=blucali)
    blucali.place(height=50, width=80, x=200, y=500)

    grncali = tk.Button(calitop, text="Green", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=grncali)
    grncali.place(height=50, width=80, x=360, y=500)

    redcali = tk.Button(calitop, text="Red", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=redcali)
    redcali.place(height=50, width=80, x=280, y=500)

    stlcali = tk.Button(calitop, text="Steel", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=stlcali)
    stlcali.place(height=50, width=80, x=440, y=500)


    def caliexit():
        calitop.destroy()

    caliback = tk.Button(calitop, text="Back", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 4),
                            command=caliexit)
    caliback.place(height=25, width=40, x=550, y=10)

    

    def calibrated(self):
        v1 = int(v1entry.get())

        v3 = int(v3entry.get())
        m1 = float(m1entry.get())
        m3 = float(m3entry.get())
        slope = (m3 - m1) / (v3 - v1)
        target = float(targetentry.get())
        intercept = m1 - slope * v1

        vtarget = (target - intercept) / slope
        vollabel = tk.Label(calitop, text="Try " + str(round(vtarget, 1)) + " volts", font=('fixedsys', 20), fg='#0c161c',
                             relief='solid')
        vollabel.place(height=50, width=300, x=200, y=400)

    calsub = tk.Button(calitop, text="Submit", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 12),
                        command=calibrated)
    calsub.place(height=50, width=175, x=10, y=350)

    calitop.bind('<Return>', calibrated)

    def helpcal():
        calhtop = tk.Toplevel(calitop, bg ='#74add0', height=250, width=250)
        calhtop.title("Mass Calibrate Calculator---HELP")
        helpclabel = tk.Label(calhtop, text="Use this Calculator with the Universal Dropmass Calculator \n\n Pick Three Stable Voltages to Perform Dropmass at \n\n Enter the Voltages, Lowest to Highest \n\n Enter the Dropmass Target in ng. \n\n Perform Dropmasses at Each Voltage and Enter the HADM (ng) in for Each Respective Voltage \n\n Click Submit to Calculate a Predicted Voltage to Achieve the Requested Target.", font=('fixedsys', 16), fg='#0c161c', pady=50)
        helpclabel.pack()

    calhelp = tk.Button(calitop, text="Help", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 12),
                            command=helpcal)
    calhelp.place(height=50, width=175, x=10, y=425)




    
    

    

    

    
    

    



speedbutton = tk.Button(frame, text="Universal Speed", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 12), command=speed)
speedbutton.place(height=50, width=175, x=240, y=200,)

massbutton = tk.Button(frame, text="Universal Dropmass", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 12), command=mass)
massbutton.place(height=50, width=175, x=240, y=300,)

calbutton = tk.Button(frame, text="Mass Calibrate", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 12), command=calibrate)
calbutton.place(height=50, width=175, x=240, y=400,)






root.mainloop()
