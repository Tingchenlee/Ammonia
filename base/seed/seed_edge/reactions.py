#!/usr/bin/env python
# encoding: utf-8

name = "seed_edge"
shortDesc = ""
longDesc = """

"""
autoGenerated=True
entry(
    index = 0,
    label = "X + X + H2 <=> H_X + H_X",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.046, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/CPOX_Pt/Deutschmann2006
""",
)

entry(
    index = 1,
    label = "X + X + CH4 <=> H_X + CH3X",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.0009, n=0, Ea=(72000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/CPOX_Pt/Deutschmann2006
""",
)

entry(
    index = 2,
    label = "X + OX + CH4 <=> OHX + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(5e+18,'cm^5/(mol^2*s)'), n=0.7, Ea=(42000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/CPOX_Pt/Deutschmann2006
""",
)

entry(
    index = 3,
    label = "X + OHX + CH4 <=> H2O_X + CH3X",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=1, n=0, Ea=(10000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/CPOX_Pt/Deutschmann2006
""",
)

entry(
    index = 4,
    label = "X + CO2 <=> CO2X",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.005, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/CPOX_Pt/Deutschmann2006
""",
)

entry(
    index = 5,
    label = "X + CO <=> OCX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.84, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/CPOX_Pt/Deutschmann2006
""",
)

entry(
    index = 6,
    label = "OX + CX <=> X + OCX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.7e+19,'cm^2/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/CPOX_Pt/Deutschmann2006
""",
)

entry(
    index = 7,
    label = "OX + OCX <=> X + CO2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.7e+21,'cm^2/(mol*s)'), n=0, Ea=(117600,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/CPOX_Pt/Deutschmann2006
""",
)

entry(
    index = 8,
    label = "H_X + CO2X <=> OHX + OCX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1e+19,'cm^2/(mol*s)'), n=0, Ea=(8400,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/CPOX_Pt/Deutschmann2006
""",
)

entry(
    index = 9,
    label = "H_X + CH2X <=> X + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.09e+22,'cm^2/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/CPOX_Pt/Deutschmann2006
""",
)

entry(
    index = 10,
    label = "H_X + CHX <=> X + CH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.09e+22,'cm^2/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/CPOX_Pt/Deutschmann2006
""",
)

entry(
    index = 11,
    label = "X + CHX <=> H_X + CX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.09e+22,'cm^2/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/CPOX_Pt/Deutschmann2006
""",
)

entry(
    index = 12,
    label = "H2 + CX <=> CH2X",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.04, n=0, Ea=(29700,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/CPOX_Pt/Deutschmann2006
""",
)

entry(
    index = 13,
    label = "X + NH2(D) <=> NH2_X",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=1, n=0, Ea=(0,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K'), comment="""Matched reaction 21 X + H2N <=> H2NX in Surface_Adsorption_Single/training
    This reaction matched rate rule [N;VacantSite]
    family: Surface_Adsorption_Single
    metal: None
    facet: None
    site: None"""),
    longDesc = 
"""
Matched reaction 21 X + H2N <=> H2NX in Surface_Adsorption_Single/training
This reaction matched rate rule [N;VacantSite]
family: Surface_Adsorption_Single
metal: None
facet: None
site: None
""",
)

entry(
    index = 14,
    label = "X + H <=> H_X",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.384, n=1.832, Ea=(0,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K'), comment="""Matched reaction 11 X + H <=> HX in Surface_Adsorption_Single/training
    This reaction matched rate rule [H;VacantSite]
    family: Surface_Adsorption_Single
    metal: None
    facet: None
    site: None"""),
    longDesc = 
"""
Matched reaction 11 X + H <=> HX in Surface_Adsorption_Single/training
This reaction matched rate rule [H;VacantSite]
family: Surface_Adsorption_Single
metal: None
facet: None
site: None
""",
)

entry(
    index = 15,
    label = "X + X + NH2NH2 <=> NH2_X + NH2_X",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.0304631, n=0.077, Ea=(18.828,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [Adsorbate;VacantSite1;VacantSite2] for rate rule [N;VacantSite1;VacantSite2]
    Euclidian distance = 1.0
    family: Surface_Adsorption_Dissociative"""),
    longDesc = 
"""
Estimated using template [Adsorbate;VacantSite1;VacantSite2] for rate rule [N;VacantSite1;VacantSite2]
Euclidian distance = 1.0
family: Surface_Adsorption_Dissociative
""",
)

entry(
    index = 16,
    label = "X + H2N-NH2_ads <=> NH2_X + NH2_X",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(6.61e+17,'cm^2/(mol*s)'), n=1.589, Ea=(66578,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K'), comment="""Matched reaction 29 X_4 + H4N2X-2 <=> NH2_X + H2NX in Surface_Dissociation_vdW/training
    This reaction matched rate rule [Combined;VacantSite]
    family: Surface_Dissociation_vdW
    metal: None
    facet: None
    site: None"""),
    longDesc = 
"""
Matched reaction 29 X_4 + H4N2X-2 <=> NH2_X + H2NX in Surface_Dissociation_vdW/training
This reaction matched rate rule [Combined;VacantSite]
family: Surface_Dissociation_vdW
metal: None
facet: None
site: None
""",
)

entry(
    index = 17,
    label = "X + HN-NH2_ads <=> NH_X + NH2_X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.87e+16,'cm^2/(mol*s)'), n=2.065, Ea=(86841,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K'), comment="""Matched reaction 52 X_4 + H3N2X-2 <=> NHX_1 + H2NX in Surface_Dissociation/training
    This reaction matched rate rule [N;VacantSite]
    family: Surface_Dissociation
    metal: None
    facet: None
    site: None"""),
    longDesc = 
"""
Matched reaction 52 X_4 + H3N2X-2 <=> NHX_1 + H2NX in Surface_Dissociation/training
This reaction matched rate rule [N;VacantSite]
family: Surface_Dissociation
metal: None
facet: None
site: None
""",
)

entry(
    index = 18,
    label = "H_X + H2N-OH_ads <=> H2O_X + NH2_X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(9.48698e+16,'m^2/(mol*s)'), n=0.0693333, Ea=(36.7735,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [N-R;Abstracting] for rate rule [N-O;Abstracting]
    Euclidian distance = 1.0
    family: Surface_Abstraction_Single_vdW"""),
    longDesc = 
"""
Estimated using template [N-R;Abstracting] for rate rule [N-O;Abstracting]
Euclidian distance = 1.0
family: Surface_Abstraction_Single_vdW
""",
)

entry(
    index = 19,
    label = "N2O_X + NH2_X <=> NH_X + [Pt]NN=O",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.22e+21,'cm^2/(mol*s)'), n=0, Ea=(78.1569,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K'), comment="""Estimated using template [Abstracting;*-N-H] for rate rule [N=*;*-N-H]
    Euclidian distance = 2.0
    Multiplied by reaction path degeneracy 2.0
    family: Surface_Abstraction"""),
    longDesc = 
"""
Estimated using template [Abstracting;*-N-H] for rate rule [N=*;*-N-H]
Euclidian distance = 2.0
Multiplied by reaction path degeneracy 2.0
family: Surface_Abstraction
""",
)

entry(
    index = 20,
    label = "NX + NH2NO <=> N2O_X + NH2_X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.17675e+14,'m^2/(mol*s)'), n=0.208794, Ea=(118.607,'kJ/mol'), T0=(1,'K'), Tmin=(303.03,'K'), Tmax=(2000,'K'), comment="""Estimated using template [N-R;*#N] for rate rule [N-N;*#N]
    Euclidian distance = 1.0
    family: Surface_Abstraction_vdW"""),
    longDesc = 
"""
Estimated using template [N-R;*#N] for rate rule [N-N;*#N]
Euclidian distance = 1.0
family: Surface_Abstraction_vdW
""",
)

entry(
    index = 21,
    label = "NH_X + H2_ads <=> H_X + NH2_X",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(1.44095e+13,'m^2/(mol*s)'), n=0.894608, Ea=(85.384,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [AdsorbateVdW;*=NH] for rate rule [H-H;*=NH]
    Euclidian distance = 1.0
    Multiplied by reaction path degeneracy 2.0
    family: Surface_Abstraction_vdW"""),
    longDesc = 
"""
Estimated using template [AdsorbateVdW;*=NH] for rate rule [H-H;*=NH]
Euclidian distance = 1.0
Multiplied by reaction path degeneracy 2.0
family: Surface_Abstraction_vdW
""",
)

entry(
    index = 22,
    label = "X + HN-NH_ads <=> NH_X + NH_X",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(3.87e+21,'cm^2/(mol*s)'), n=0, Ea=(70437.7,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K'), comment="""Matched reaction 9 X_4 + H2N2X <=> HNX-2 + HNX in Surface_Dissociation_Double_vdW/training
    This reaction matched rate rule [AdsorbateVdW;VacantSite]
    family: Surface_Dissociation_Double_vdW
    metal: None
    facet: None
    site: None"""),
    longDesc = 
"""
Matched reaction 9 X_4 + H2N2X <=> HNX-2 + HNX in Surface_Dissociation_Double_vdW/training
This reaction matched rate rule [AdsorbateVdW;VacantSite]
family: Surface_Dissociation_Double_vdW
metal: None
facet: None
site: None
""",
)

entry(
    index = 23,
    label = "NH_X + H2O_X <=> H_X + HN-OH_ads",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(1.44095e+13,'m^2/(mol*s)'), n=0.894608, Ea=(157.389,'kJ/mol'), T0=(1,'K'), comment="""Estimated using an average for rate rule [AdsorbateVdW;*=NH]
    Euclidian distance = 0
    Multiplied by reaction path degeneracy 2.0
    family: Surface_Abstraction_vdW
    Ea raised from 156.4 to 157.4 kJ/mol to match endothermicity of reaction."""),
    longDesc = 
"""
Estimated using an average for rate rule [AdsorbateVdW;*=NH]
Euclidian distance = 0
Multiplied by reaction path degeneracy 2.0
family: Surface_Abstraction_vdW
Ea raised from 156.4 to 157.4 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 24,
    label = "NX + [Pt]NN=O <=> N2O_X + NH_X",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(3.53491e+17,'m^2/(mol*s)'), n=-0.0171111, Ea=(59.0521,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [Abstracting;Donating] for rate rule [:N#*;*N-N]
    Euclidian distance = 3.605551275463989
    family: Surface_Abstraction"""),
    longDesc = 
"""
Estimated using template [Abstracting;Donating] for rate rule [:N#*;*N-N]
Euclidian distance = 3.605551275463989
family: Surface_Abstraction
""",
)

entry(
    index = 25,
    label = "NX + [Pt]NN=O <=> N2O_X + NH_X",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(3.53491e+17,'m^2/(mol*s)'), n=-0.0171111, Ea=(59.0521,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [Abstracting;Donating] for rate rule [:N#*;*N-N]
    Euclidian distance = 3.605551275463989
    family: Surface_Abstraction"""),
    longDesc = 
"""
Estimated using template [Abstracting;Donating] for rate rule [:N#*;*N-N]
Euclidian distance = 3.605551275463989
family: Surface_Abstraction
""",
)

entry(
    index = 26,
    label = "NX + H2_ads <=> H_X + NH_X",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(1.18106e+13,'m^2/(mol*s)'), n=0.618666, Ea=(106.039,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [AdsorbateVdW;*#N] for rate rule [H-H;*#N]
    Euclidian distance = 1.0
    Multiplied by reaction path degeneracy 2.0
    family: Surface_Abstraction_vdW"""),
    longDesc = 
"""
Estimated using template [AdsorbateVdW;*#N] for rate rule [H-H;*#N]
Euclidian distance = 1.0
Multiplied by reaction path degeneracy 2.0
family: Surface_Abstraction_vdW
""",
)

entry(
    index = 27,
    label = "N2O_X + H2O_X <=> OHX + [Pt]NN=O",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.49624e+12,'m^2/(mol*s)'), n=0.968861, Ea=(79.0883,'kJ/mol'), T0=(1,'K'), Tmin=(303.03,'K'), Tmax=(2000,'K'), comment="""Estimated using an average for rate rule [O-R;*=N]
    Euclidian distance = 0
    Multiplied by reaction path degeneracy 2.0
    family: Surface_Abstraction_vdW"""),
    longDesc = 
"""
Estimated using an average for rate rule [O-R;*=N]
Euclidian distance = 0
Multiplied by reaction path degeneracy 2.0
family: Surface_Abstraction_vdW
""",
)

entry(
    index = 28,
    label = "N2O_X + H2O_X <=> H_X + ON(N=O)[Pt]",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(7.25014e+12,'m^2/(mol*s)'), n=0.972954, Ea=(153.327,'kJ/mol'), T0=(1,'K'), comment="""Estimated using an average for rate rule [AdsorbateVdW;*=N]
    Euclidian distance = 0
    Multiplied by reaction path degeneracy 2.0
    family: Surface_Abstraction_vdW
    Ea raised from 152.2 to 153.3 kJ/mol to match endothermicity of reaction."""),
    longDesc = 
"""
Estimated using an average for rate rule [AdsorbateVdW;*=N]
Euclidian distance = 0
Multiplied by reaction path degeneracy 2.0
family: Surface_Abstraction_vdW
Ea raised from 152.2 to 153.3 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 29,
    label = "H_X + H2O_X <=> OHX + H2_ads",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(4e+19,'cm^2/(mol*s)'), n=0, Ea=(128.686,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K'), comment="""From training reaction 12 used for H2O;Abstracting
    Exact match found for rate rule [H2O;Abstracting]
    Euclidian distance = 0
    Multiplied by reaction path degeneracy 2.0
    family: Surface_Abstraction_Single_vdW"""),
    longDesc = 
"""
From training reaction 12 used for H2O;Abstracting
Exact match found for rate rule [H2O;Abstracting]
Euclidian distance = 0
Multiplied by reaction path degeneracy 2.0
family: Surface_Abstraction_Single_vdW
""",
)

entry(
    index = 30,
    label = "NX + HN-O_ads <=> N2O_X + H_X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(5.90531e+12,'m^2/(mol*s)'), n=0.618666, Ea=(106.039,'kJ/mol'), T0=(1,'K'), comment="""Estimated using an average for rate rule [AdsorbateVdW;*#N]
    Euclidian distance = 0
    family: Surface_Abstraction_vdW"""),
    longDesc = 
"""
Estimated using an average for rate rule [AdsorbateVdW;*#N]
Euclidian distance = 0
family: Surface_Abstraction_vdW
""",
)

entry(
    index = 31,
    label = "X + [Pt]NN=O <=> N2O_X + H_X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.34e+17,'cm^2/(mol*s)'), n=1.942, Ea=(121.577,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K'), comment="""From training reaction 49 used for N;VacantSite
    Exact match found for rate rule [N;VacantSite]
    Euclidian distance = 0
    family: Surface_Dissociation"""),
    longDesc = 
"""
From training reaction 49 used for N;VacantSite
Exact match found for rate rule [N;VacantSite]
Euclidian distance = 0
family: Surface_Dissociation
""",
)

entry(
    index = 32,
    label = "X + N2 <=> NN_ads",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=5.5e-05, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K'), comment="""Matched reaction 22 X + N2 <=> N2X in Surface_Adsorption_vdW/training
    This reaction matched rate rule [N#N;VacantSite]
    family: Surface_Adsorption_vdW
    metal: None
    facet: None
    site: None"""),
    longDesc = 
"""
Matched reaction 22 X + N2 <=> N2X in Surface_Adsorption_vdW/training
This reaction matched rate rule [N#N;VacantSite]
family: Surface_Adsorption_vdW
metal: None
facet: None
site: None
""",
)

entry(
    index = 33,
    label = "X + N2O <=> N2O",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=1, n=0, Ea=(32806.6,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K'), comment="""Matched reaction 6 X + N2O <=> N2OX in Surface_Adsorption_vdW/training
    This reaction matched rate rule [N2O;VacantSite]
    family: Surface_Adsorption_vdW
    metal: None
    facet: None
    site: None"""),
    longDesc = 
"""
Matched reaction 6 X + N2O <=> N2OX in Surface_Adsorption_vdW/training
This reaction matched rate rule [N2O;VacantSite]
family: Surface_Adsorption_vdW
metal: None
facet: None
site: None
""",
)

