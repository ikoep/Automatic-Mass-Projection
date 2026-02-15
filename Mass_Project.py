import arcpy

#Setting param = folder workspace. Grabbing selected folder
folder = arcpy.GetParameterAsText(0)
arcpy.env.workspace = folder
arcpy.AddMessage(f"Your workspace is set to {folder}")

#Setting variable name = the correct feature layer coord system
correctSR = arcpy.GetParameterAsText(1)

correctDesc = arcpy.Describe(correctSR)
correctSRF = correctDesc.SpatialReference
arcpy.AddMessage(f"The correct coordinate system you selected is {correctSRF.name}")

#Getting num feature classes in folder
fcs = arcpy.ListFeatureClasses()

arcpy.AddMessage(str(len(fcs)) + " Items in folder: " + str(fcs) + "\n") #Counts and lists file names
# Checks to see if data already projected to the same coordinate system
for i in fcs:
    if "_Projected" in i: #If contains _Projected extension exit program
        arcpy.AddMessage("All of your data is already projected")
        exit()
    else:
        continue
#Loop through folder
for fc in fcs:

    #Current item
    desc = arcpy.Describe(fc)
    srf = desc.SpatialReference

    #If mismatch, reproject to correct
    if (srf.name != correctSRF.name):
        rft = fc.replace(".shp", "")
        output = f"{rft}_Projected"
        arcpy.management.Project(fc, output, correctSRF)
        arcpy.AddMessage(f"The coordinate systems do not match.\n Your spatial reference: {srf.name} in the feature class: {fc} was projected to {correctSRF.name}")
    #If no mismatch, print
    else:
        arcpy.AddMessage(f"The coordinate systems match, no projected is necessary for {fc}")
