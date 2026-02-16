# Automatic Projection Tool Script

This is a tool that projects all data from the target folder into the desired shapefile spatial reference.

## How it works:
Using ArcPy methods we are able to automate the process of the project tool by setting our parameters workspace to the target folder and selecting the correct feature layer spatial reference. Then by settings the range of the folder we can iterate through each shapefile, projecting if needed.
* In lines 4-13, setting up parameters.
* In lines 20-27, contained is an error handling that checks to see if the "_Projected" string has been concatenated onto the new files.
* In lines 27-41, loop that iterates over each shapefile and reprojects if it is different from the one selected to the correct reference.

## Outputs in ArcGIS Pro:
### Output Message 1
