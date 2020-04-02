# cmap2png
Useful script to convert a color map definition to PNG image file.

## Usage
```
cmap2png.py [-h] cmapType cmapId min max tick label output

positional arguments:
  cmapType    Colormap type: [cpt, h2g or matplotlib]
  cmapId      Colormap identifier or path to colormap file
  min         Legend minimum value
  max         Legend maximum value
  tick        Legend tick frequency
  label       Legend label
  output      Result output path

optional arguments:
  -h, --help  show this help message and exit
```
 
 ## Examples
```bash
cmap2png.py matplotlib Greys -55.0 72.0 10.0 "Brightness Temperature ($^{\circ}$C)" legend-celsius-en.png
```
```bash
cmap2png.py cpt WVCOLOR35.cpt -100.0 100.0 20.0 "My awesome label" legend.png
```

![](legends/goes-aod-pt-br.png)                                                    
![](legends/goes-ch01-ref-pt-br.png)                                               
![](legends/goes-ch02-ref-pt-br.png)                                               
![](legends/goes-ch03-ref-pt-br.png)                                               
![](legends/goes-ch04-ref-pt-br.png)                                               
![](legends/goes-ch05-ref-pt-br.png)                                               
![](legends/goes-ch06-ref-pt-br.png)                                               
![](legends/goes-ch07-celsius-pt-br.png)                                           
![](legends/goes-ch08-celsius-pt-br.png)                                           
![](legends/goes-ch08-WVCOLOR35-celsius-pt-br.png)                                 
![](legends/goes-ch09-celsius-pt-br.png)                                           
![](legends/goes-ch09-WVCOLOR35-celsius-pt-br.png)                                 
![](legends/goes-ch10-celsius-pt-br.png)                                           
![](legends/goes-ch10-WVCOLOR35-celsius-pt-br.png)                                 
![](legends/goes-ch11-celsius-pt-br.png)                                           
![](legends/goes-ch12-celsius-pt-br.png)                                           
![](legends/goes-ch13-celsius-pt-br.png)                                           
![](legends/goes-ch13-dsa-celsius-pt-br.png)                                       
![](legends/goes-ch13-IR4AVHRR6-celsius-pt-br.png)                                 
![](legends/goes-ch14-celsius-pt-br.png)                                           
![](legends/goes-ch15-celsius-pt-br.png)                                           
![](legends/goes-ch16-celsius-pt-br.png)                                           
![](legends/goes-rrqpef-pt-br.png)                                                 
![](legends/goes-sstf-celsius-pt-br.png)                                                            
