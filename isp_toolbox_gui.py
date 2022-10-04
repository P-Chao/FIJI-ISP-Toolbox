from ij.gui import GenericDialog
from java.awt.event   import ActionListener

from ij               import IJ
from ij               import ImagePlus
from ijopencv.ij      import ImagePlusMatConverter
from ijopencv.opencv  import MatImagePlusConverter
from org.bytedeco.javacpp.opencv_core	import Scalar, Mat, subtract


def blc_gui():
    gui = GenericDialog("Black Level Correction")
    gui.addChoice("Patten", ["RGGB", "BGGR", "GRBG", "GBRG"], "RGGB")
    gui.addNumericField(" R", 0)
    gui.addNumericField("GR", 0)
    gui.addNumericField("GB", 0)
    gui.addNumericField(" B", 0)
    gui.showDialog()
    
    if gui.wasOKed():
        pattern = gui.getNextChoice()
        bl_r    = gui.getNextNumber()
        bl_gr   = gui.getNextNumber()
        bl_gb   = gui.getNextNumber()
        bl_b    = gui.getNextNumber()
        
        imp = IJ.getImage()
        title = imp.getTitle()
        imp2mat = ImagePlusMatConverter()
        ImMat = imp2mat.toMat(imp.getProcessor())
        
        #if pattern == "RGGB":
        #    ImMat = ImMat - 64
        
        mat2ip = MatImagePlusConverter()
        NewIP  = mat2ip.toImageProcessor(ImMat)
        NewImp = ImagePlus(title + "_BLC", NewIP)
        
        NewImp.show()


class ButtonClic(ActionListener):
    """Class which unique function is to handle the button clics"""

    def actionPerformed(self, event): # self (or this in Java) to state that the method will be associated to the class instances

        # Check from where comes the event 
        source = event.getSource() # returns the Button object
        #print source 

        # Do an action depending on the button clicked
        if source.label == "BLC":
            blc_gui()

        elif source.label == "B":
            print "You clicked B\n"
            
        else:
            print source.label + " is not supported."

func = ButtonClic()

# Create an instance of GenericDialog
gui = GenericDialog("ISP Toolbox")
gui.hideCancelButton()

# isp basic operation (Raw)
gui.setLocation(0,0)
gui.addButton('BLC', func)
gui.addToSameRow()
gui.addButton('BPC', func)
gui.addToSameRow()
gui.addButton('WBC', func)
gui.addToSameRow()
gui.addButton('LSC', func)
gui.addToSameRow()
gui.addButton('Demosaicing', func)

gui.addButton('CCM', func)
gui.addToSameRow()
gui.addButton('Gamma', func)
gui.addToSameRow()
gui.addButton('GTM', func)
gui.addToSameRow()
gui.addButton('LTM', func)
gui.addToSameRow()
gui.addButton('2D LUT', func)
gui.addToSameRow()
gui.addButton('3D LUT', func)
gui.addButton('Denoise', func)
gui.addToSameRow()
gui.addButton('Sharpen', func)
gui.addToSameRow()
gui.addButton('Dehaze', func)
gui.addToSameRow()
gui.addButton('Super Resolution', func)
#gui.setInsets(0,0,0)
gui.addButton('QBC Remosaic', func)
gui.addToSameRow()
gui.addButton('QBC Demosaic', func)

# Warp (Raw && RGB)
gui.addButton('Calibration', func)
gui.addToSameRow()
gui.addButton('Undistortion', func)
gui.addToSameRow()
gui.addButton('Registration', func)
gui.addToSameRow()
gui.addButton('Merge', func)

# Multiframe (Raw && RGB)
gui.addButton('MultiFrame Denoise', func)
gui.addToSameRow()
gui.addButton('MultiFrame Demosaic', func)
gui.addToSameRow()
gui.addButton('MultiFrame Super Resolution', func)
gui.addToSameRow()
gui.addButton('MultiFrame HDR', func)

# Post Process
gui.addButton('Face Recognition', func)
gui.addToSameRow()
gui.addButton('Portrait Segmentation', func)
gui.addToSameRow()
gui.addButton('Portrait Enlighten', func)

# Add a Help button in addition to the default OK/Cancel
#gui.addHelp(r"https://imagej.net/scripting/generic-dialog") # clicking the help button will open the provided URL in the default browser

# Show dialog, the rest of the code is not executed before OK or Cancel is clicked
gui.showDialog() # dont forget to actually display the dialog at some point
