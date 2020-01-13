file = 'C:\\Modelling\\Hampton Court\\TUFLOW\\model\\mi\\2d_zpt_wbthfm_001.mif' #Change the file location DO NOT FORGET to change '\' to '\\' (python thinks '\' is the end of a line)
legend = iface.legendInterface() #get the legend - list of loaded layers
vlayer =iface.addVectorLayer(file, "", "ogr") #load my file into the map
legend.setLayerVisible(vlayer, False) #turn off my layer 