# Data

<!-- * Stripe82 co-add, [Annis+14](https://ui.adsabs.harvard.edu/abs/2014ApJ...794..120A/abstract) -->
* Stripe82 morphology, [Bottrell+19](https://ui.adsabs.harvard.edu/abs/2019MNRAS.486..390B/abstract)
* SDSS DR7 group catalog, [Yang+07](https://ui.adsabs.harvard.edu/abs/2007ApJ...671..153Y/abstract)
    - [download](https://gax.sjtu.edu.cn/data/Group.html)

<!-- * Stripe82 photometric redshift catalogs [Reis+12]()
    - [download](http://das.sdss.org/va/coadd_galaxies/) -->


## Sample selection
### LSBG vs. HSBG



<!-- 1. Complete limit
    - Based on Annis+14: Figure 8, Table 5
    - THE SLOAN DIGITAL SKY SURVEY COADD: 275 deg2 OF DEEP SLOAN DIGITAL SKY SURVEY IMAGING ON STRIPE 82
    
2. Mag limit
    - brighter than Mr = -19.8 from Perez-Montano & Sodi 2019
    
3. Stellar mass
    - https://salims.pages.iu.edu/gswlc/
    - Salim+18, Dust Attenuation Curves in the Local Universe: Demographics and New Laws for Star-forming Galaxies and High-redshift Analogs
    - Stellar parameters, i.e., stellar masses (M*) and SFRs, are
taken from Galaxy Evolution Explorer (GALEX)?SDSS?
WISE Legacy Catalog 2 (Salim et al. 2018). They follow a
Bayesian approach to SED fitting on the combination of
GALEX and SDSS data of all galaxies (0.7 million) with
z < 0.3. -->

<!-- ### LSS
*  -->

<!-- ### Inclination


Cervantes-Sodi et al.(2008, 2012)와 Perez-Montano et al.(2019, 2022) 등을 살펴 보았는데, 결론적으로 inclination angle의 criterion이 포함된 것은 Perez-Montano et al.(2019), 하나 뿐입니다. -->


<!-- ## Previous study
* [Pérez-Montaño+19][]
    - galaxy sample: KIAS Value-Added Catalog based on SDSS DR7
    - structural information from the Simard et al. 2011, fixed sersic index $n_{b} = 4$ for the bulge component
    - volume-limited sample
        - $M_{r} = 19.8$ mag within a $0.01 < z < 0.1$
        - nearly face-on to avoid extiction correction/spiral galaxies, $q > 0.4$
        - #fracDev < 0.9$: late-type galaxies 
    - match with ALFALFA $\alpha 100$ catalog with $25 < inclination < 75$

* [Pérez-Montaño+22][]
    - IllustriTNG100 

* [Cervantes-Sodi+08][]

* [Cervantes-Sodi+12][]

* [Kim & Lee 2013][]


<!-- References -->
<!-- [Pérez-Montaño+19]: https://ui.adsabs.harvard.edu/abs/2019MNRAS.490.3772P/abstract

[Pérez-Montaño+22]: https://ui.adsabs.harvard.edu/abs/2022MNRAS.514.5840P/abstract

[Cervantes-Sodi+08]: https://ui.adsabs.harvard.edu/abs/2008MNRAS.388..863C/abstract

[Cervantes-Sodi+12]: https://ui.adsabs.harvard.edu/abs/2012MNRAS.426.1606C/abstract

[Kim & Lee 2013]: https://ui.adsabs.harvard.edu/abs/2013MNRAS.432.1701K/abstract -->


<!-- ## Notes on Cosmicflow-4

* [Tully+23](https://ui.adsabs.harvard.edu/abs/2023ApJ...944...94T/abstract)
    - distances for $55877$ galaxies gathered into $38065$ groups
        - $8$ methodologies; Tully-Fisher (TF), Fundamental Plane (FP), type Ia SNe, surface brightness fluctuations of elliptical galaxies, core-collapse supernovae (SNe II), Cepheid period-luminosity, tip of the red giant branch (TRGB), stellar parallax
    - galaxy groups
        - `` -->


<!-- ## Filament catalog
* [Tempel+14](https://ui.adsabs.harvard.edu/abs/2014MNRAS.438.3465T/abstract)
    - [data](https://vizier.cds.unistra.fr/viz-bin/VizieR?-source=J/MNRAS/438/3465)


magnitude conversion
- https://arxiv.org/pdf/1007.4014.pdf
- https://arxiv.org/pdf/1811.04569.pdf
- Kim & Lee 2013, How Does the Surface Density and Size of Disk Galaxies Measured in Hydrodynamic Simulations Correlate with the Halo SpinParameter?

Things to check

- redshift range
- volume limited (preferred) vs. magnitude limited
- surface brightness distribution as a function of redshift
- comepleteness?
- How to convert sdss filter sets into UBVRI
- inclination -->
<!-- 
# zeropoint = 30
#  -2.5 * np.log10(tbl_ps['f_g'][:10])+ 30 = tbl_ps['g2dmag_g'][:10]

# path = './bottrell/stz855_supplemental_files/Stripe82_DeepMorphologies_TXT/'
# tbl_n4 = ascii.read(path + 'sdss_s82_morph_gr_n4.txt')

Halo mass to virial radius

$$M_{200} = \frac{100}{G} r^{3}_{200} H^{2}(t)$$

Hs = cosmo.H(grps['z']).value
h =  cosmo.H(0).value / 100
 
G = 4.2e-3 * 1e-6 # Mpc M_sun-1 (km/s)^2

r200 = (( 10**(grps['hm1']) * G / 100 / Hs**2 )**(1/3)).value #mpc -->