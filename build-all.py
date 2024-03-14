# -*- coding: utf-8 -*-

__author__ = 'Douglas Uba'
__email__  = 'douglas.uba@inpe.br'

from cmap2png import cmap2png

# VIS/NIR
cmap2png('matplotlib', 'gray', 0.0, 100.0, 10.0, '0,47$\mu$m Refletância (%)', './legends/goes-ch01-ref-pt-br.png')
cmap2png('matplotlib', 'gray', 0.0, 100.0, 10.0, '0,64$\mu$m Refletância (%)', './legends/goes-ch02-ref-pt-br.png')
cmap2png('matplotlib', 'gray', 0.0, 100.0, 10.0, '0,86$\mu$m Refletância (%)', './legends/goes-ch03-ref-pt-br.png')
cmap2png('matplotlib', 'gray', 0.0, 100.0, 10.0, '1,37$\mu$m Refletância (%)', './legends/goes-ch04-ref-pt-br.png')
cmap2png('matplotlib', 'gray', 0.0, 100.0, 10.0, '1,60$\mu$m Refletância (%)', './legends/goes-ch05-ref-pt-br.png')
cmap2png('matplotlib', 'gray', 0.0, 100.0, 10.0, '2,20$\mu$m Refletância (%)', './legends/goes-ch06-ref-pt-br.png')

# IR #
cmap2png('matplotlib', 'Greys', -80.0, 55.0, 20.0, '3,90$\mu$m Temperatura de Brilho ($^{\circ}$C)', './legends/goes-ch07-celsius-pt-br.png')

# WV
cmap2png('matplotlib', 'Greys', -80.0, 0.0, 20.0, '6,19$\mu$m Temperatura de Brilho ($^{\circ}$C)', './legends/goes-ch08-celsius-pt-br.png')
cmap2png('matplotlib', 'Greys', -80.0, 0.0, 20.0, '6,95$\mu$m Temperatura de Brilho ($^{\circ}$C)', './legends/goes-ch09-celsius-pt-br.png')
cmap2png('matplotlib', 'Greys', -80.0, 0.0, 20.0, '7,34$\mu$m Temperatura de Brilho ($^{\circ}$C)', './legends/goes-ch10-celsius-pt-br.png')

# IR
cmap2png('matplotlib', 'Greys', -80.0, 55.0, 20.0, '8,50$\mu$m Temperatura de Brilho ($^{\circ}$C)', './legends/goes-ch11-celsius-pt-br.png')
cmap2png('matplotlib', 'Greys', -80.0, 55.0, 20.0, '9,61$\mu$m Temperatura de Brilho ($^{\circ}$C)', './legends/goes-ch12-celsius-pt-br.png')
cmap2png('matplotlib', 'Greys', -80.0, 55.0, 20.0, '10,35$\mu$m Temperatura de Brilho ($^{\circ}$C)', './legends/goes-ch13-celsius-pt-br.png')
cmap2png('matplotlib', 'Greys', -80.0, 55.0, 20.0, '11,20$\mu$m Temperatura de Brilho ($^{\circ}$C)', './legends/goes-ch14-celsius-pt-br.png')
cmap2png('matplotlib', 'Greys', -80.0, 55.0, 20.0, '12,30$\mu$m Temperatura de Brilho ($^{\circ}$C)', './legends/goes-ch15-celsius-pt-br.png')
cmap2png('matplotlib', 'Greys', -80.0, 55.0, 20.0, '13,30$\mu$m Temperatura de Brilho ($^{\circ}$C)', './legends/goes-ch16-celsius-pt-br.png')

# Realces
cmap2png('cpt', './resources/cpt/WVCOLOR35.cpt', -100.0, 100.0, 20.0, '6,19$\mu$m Temperatura de Brilho ($^{\circ}$C)', './legends/goes-ch08-WVCOLOR35-celsius-pt-br.png')
cmap2png('cpt', './resources/cpt/WVCOLOR35.cpt', -100.0, 100.0, 20.0, '6,95$\mu$m Temperatura de Brilho ($^{\circ}$C)', './legends/goes-ch09-WVCOLOR35-celsius-pt-br.png')
cmap2png('cpt', './resources/cpt/WVCOLOR35.cpt', -100.0, 100.0, 20.0, '7,34$\mu$m Temperatura de Brilho ($^{\circ}$C)', './legends/goes-ch10-WVCOLOR35-celsius-pt-br.png')
cmap2png('cpt', './resources/cpt/IR4AVHRR6.cpt', -100.0, 100.0, 20.0, '10,35$\mu$m Temperatura de Brilho ($^{\circ}$C)', './legends/goes-ch13-IR4AVHRR6-celsius-pt-br.png')
cmap2png('cpt', './resources/cpt/ir_realce_dsa_kelvin.cpt', -80.0, 40.0, 20.0, '10,35$\mu$m Temperatura de Brilho ($^{\circ}$C)', './legends/goes-ch13-dsa-celsius-pt-br.png')

# L2 Products
cmap2png('cpt', './resources/cpt/bcyr.cpt', 0.0, 1.0, 0.2, 'Profundidade Ótica Aerosol (AOD)', './legends/goes-aod-pt-br.png')
cmap2png('cpt', './resources/cpt/bcyr.cpt', 1.0, 60.0, 10.0, 'Precipitação (mm/h) (RRQPE)', './legends/goes-rrqpef-pt-br.png')
cmap2png('cpt', './resources/cpt/bcyr.cpt', -5.0, 35.0, 10.0, 'Temperatura Sup. Mar ($^{\circ}$C) (SST)', './legends/goes-sstf-celsius-pt-br.png')

# RADAR
cmap2png('rgbs', './resources/cpt/radar.rgbs', minvalue=5, maxvalue=65,
     tickFreq=None, label='Refletividade (dBZ)', output='./legends/radar-pt-br.png', ticks=[5,10,20,35,50,65])
