# -*- coding: utf-8 -*-

__author__ = 'Douglas Uba'
__email__  = 'douglas.uba@inpe.br'

import argparse
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from os.path import exists

def LoadCPT(path):
    '''
    LoadCPT(path):
    From https://github.com/j08lue/pycpt
    Python tools to load and handle cpt (GMT format) color maps for use with matplotlib.
    '''
    try:
        f = open(path)
    except:
        print('CPT file', path, 'not found')
        return None

    lines = f.readlines()
    
    f.close()
    
    x = []
    r = []
    g = []
    b = []
    
    colorModel = 'RGB'
    
    for l in lines:
        ls = l.split()
        if l[0] == '#':
            if ls[-1] == 'HSV':
                colorModel = 'HSV'
                continue
            else:
                continue
        if ls[0] == 'B' or ls[0] == 'F' or ls[0] == 'N':
            pass
        else:
            if len(ls) == 8: # read tuple (r,g,b)
                x.append(float(ls[0]))
                r.append(float(ls[1]))
                g.append(float(ls[2]))
                b.append(float(ls[3]))
                xtemp = float(ls[4])
                rtemp = float(ls[5])
                gtemp = float(ls[6])
                btemp = float(ls[7])
            elif len(ls) == 4: # read gray (g,g,g)
                x.append(float(ls[0]))
                r.append(float(ls[1]))
                g.append(float(ls[1]))
                b.append(float(ls[1]))
                xtemp = float(ls[2])
                rtemp = float(ls[3])
                gtemp = float(ls[3])
                btemp = float(ls[3])

        x.append(xtemp)
        r.append(rtemp)
        g.append(gtemp)
        b.append(btemp)

    x = np.array(x, np.float)
    r = np.array(r, np.float)
    g = np.array(g, np.float)
    b = np.array(b, np.float)
    
    if colorModel == 'HSV':
        for i in range(r.shape[0]):
            rr, gg, bb = colorsys.hsv_to_rgb(r[i]/360.,g[i],b[i])
        r[i] = rr ; g[i] = gg ; b[i] = bb
        
    if colorModel == 'RGB':
        r = r/255.0
        g = g/255.0
        b = b/255.0
        
    xNorm = (x - x[0])/(x[-1] - x[0])

    red   = []
    blue  = []
    green = []
    
    for i in range(len(x)):
        red.append([xNorm[i],r[i],r[i]])
        green.append([xNorm[i],g[i],g[i]])
        blue.append([xNorm[i],b[i],b[i]])
        
    cpt = {'red': red, 'green': green, 'blue': blue}
    
    cmap = mpl.colors.LinearSegmentedColormap('cpt', cpt)  

    return cmap

def LoadH2GColorMap(path):
    colors = []
    levels = []
    
    if exists(path) is False:
        raise Exception('Color file ' + path + ' does not exist')
        
    f = open(path, 'r')
    
    for line in f:
        if line.find('#') == -1 and line.find('/') == -1:
            entry = line.split()
        
            # Get color
            red = int(entry[1])/255.0
            green = int(entry[2])/255.0
            blue = int(entry[3])/255.0
            
            # Do not consider 'nodata value'
            if red == 0.0 and green == 0.0 and blue == 0.0:
                continue
            
            # Get index
            levels.append(eval(entry[0]))
            
            # Add to colormap
            colors.append((red, green, blue))
       
    f.close()

    cmap = mpl.colors.LinearSegmentedColormap.from_list('colorbar', colors, N=len(levels), gamma=1.0)
    
    return cmap

def cmap2png(cmapType, cmapId, minvalue, maxvalue, tickFreq, label, output):
    # Build color map
    cmap = None
    if cmapType == 'cpt':
        cmap = LoadCPT(cmapId)
    elif cmapType == 'h2g':
        cmap = LoadH2GColorMap(cmapId)
    elif cmapType == 'matplotlib':
        cmap = plt.cm.get_cmap(cmapId)
    else:
        raise Exception('Colormap type not supported')
        
    # Make a figure and axe with dimensions as desired
    fig = plt.figure(figsize=(2.5, 0.61)) # 271 x 60 (for while, legend size hard-coded)
    ax = fig.add_axes([0.05, 0.35, 0.9, 0.35])
    fig.patch.set_visible(False)
    
    norm = mpl.colors.Normalize(vmin=minvalue, vmax=maxvalue)
        
    # Create colorbar
    cb = mpl.colorbar.ColorbarBase(ax, cmap=cmap, norm=norm, orientation='horizontal')
    
    # Adjust ticks
    ticks = np.arange(minvalue, maxvalue + 1, tickFreq)
    cb.set_ticks(ticks)
    ax.xaxis.set_tick_params(labelsize=7)
    
    # Set label
    cb.set_label(label, size=9)
    cb.ax.xaxis.set_label_position('top')
    
    # Export result
    plt.savefig(output)
    
    # Show result
    #plt.show()

    plt.close()

if __name__ == '__main__':
    # Command-line tool
    # Call example:
    # cmap2png.py matplotlib Greys -55.0 72.0 10.0 "3.7$\mu$m Brightness Temperature ($^{\circ}$C)"" viirs-svm12-celsius-en.png
    # Argument parser
    parser = argparse.ArgumentParser()
    
    # Define colormap type argument
    parser.add_argument('cmapType', type=str, help='Colormap type: [cpt, h2g or matplotlib]')
    
    # Define colormap identifier argument
    parser.add_argument('cmapId', type=str, help='Colormap identifier')
    
    # Define legend min value argument
    parser.add_argument('min', type=float, help='Legend minimum value')
    
    # Define legend max value argument
    parser.add_argument('max', type=float, help='Legend maximum value')
    
    # Define legend tick frequency
    parser.add_argument('tick', type=float, help='Legend tick frequency')
    
    # Define legend label argument
    parser.add_argument('label', type=str, help='Legend label')
    
    # Define result output path argument
    parser.add_argument('output', type=str, help='Result output path')
    
    # Parse input arguments
    args = parser.parse_args()
    
    # Run!
    cmap2png(args.cmapType, args.cmapId, args.min, args.max, args.tick, args.label, args.output)
