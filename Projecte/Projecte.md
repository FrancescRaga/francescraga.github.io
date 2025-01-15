# Projecte

## Study on the Presence of Dark Matter in the Milky Way

### Introduction
The presence of dark matter in the Milky Way has been a subject of extensive study and debate. Dark matter is a form of matter that does not emit, absorb, or reflect light, making it invisible and detectable only through its gravitational effects. This study aims to explore the evidence for dark matter in our galaxy by analyzing the rotation curves and mass distribution.

### Rotation Curves
One of the key pieces of evidence for dark matter comes from the rotation curves of galaxies. A rotation curve plots the orbital velocity of stars and gas in a galaxy against their distance from the galactic center. According to mechanics, we would expect the velocity to decrease with distance from the center, as the gravitational force weakens; otherwise the galaxy would fly apart. This velocity is known as the escape velocity, and it is given by the equation[1]:

\[
v_{esc} = \sqrt{\frac{2GM}{r}}
\]

where \(v_{esc}\) is the escape velocity, \(G\) is the gravitational constant, \(M\) is the mass enclosed within the radius \(r\), and \(r\) is the distance from the center.

Therefore, the greater the distance from the center, the lower the velocity should be. However, this is only applicable considering that the mass os the galaxy \(M\) is mainly concentrated in the center, which should be the case for the Milky Way (at least for the region we are located in)[2].

#### Alternative Explanation

If contrary to what we expect the velocity remains constant or even increases with distance from the center, this can only be explained by the presence of additional mass in the galaxy that is not accounted for by the visible matter, i.e., dark matter. This additional mass would provide the necessary gravitational force to keep the stars and gas in their orbits, resulting in a flat or increasing rotation curve.

Additionaly, by analyzing the specific shape that the rotation curve has, we can infer the distribution of these dark matter in the galaxy. This is because the shape of the rotation curve is directly related to the mass distribution of the galaxy, and by comparing the theoretical rotation curve with the observed one, we can determine the amount and distribution of dark matter.

### Data Analysis

To analyze the presence of dark matter in the Milky Way, we use data from RAVE and UCAC4. We used the Radial Velocity Experiment (RAVE) Data Release 5 (DR5)[3], from where we take the radial velocities and distances of stars. We also used the UCAC4 Astrograph Catalog[4] to obtain the proper motions of stars. With this data, we can calculate the rotation curve of the Milky Way and compare it with theoretical models.

The rotation curve of the Milky Way is shown in Figure 1. As we can see, the velocity remains relatively constant with distance from the center, discarting the posibility of the mass being concentrated in the center as suggested by the visible matter. This is a strong indication of the presence of dark matter in the galaxy.

<iframe src="figures/RotCurve.html" width="1000" height="400"></iframe>
*Figure 1: Rotation curve of the Milky Way*

#### Theoretical component

To further investigate the presence of dark matter, we can add to the rotation curve the theoretical contribution of the visible matter in the galaxy. This is done by calculating the potential of the galaxy using the mass distribution of the visible matter. The potenmtial is a combination of the gravitational potential of:
- <span style="color:grey">The bulge</span>, which represents the central concentration of mass in the very center of the galaxy.
- <span style="color:lightblue">The disk</span>, which represents the mass distributed in the disk of the galaxy.
Each component has a different mass distribution and contributes differently to the total potential of the galaxy.

The model in Figure 2 shows the rotation curve of the Milky Way with the theoretical contributions of the bulge and disk. The parameters of each potential component were adjusted to fit the observations[2]. Additionally, the graph incorporates a third component representing the <span style="color:green">dark matter</span>, distributed in a spherical halo around the galaxy. To try to fit the observed rotation curve, the mass of the dark matter halo was adjusted to 16 times the mass of the visible matter.

<iframe src="figures/RotCurveComponents.html" width="1000" height="400"></iframe>
*Figure 2: Rotation curve of the Milky Way divided by component*

As we can see, the theoretical model don't ajust perfectly with the observed rotation curve. Meaning that the proposed mass distribution is not able to explain the observed rotation curve. This suggests that the mass distribution of the galaxy is more complex than the model we used. However, the graph do allow us to determine that <span style="color:green">dark matter</span> is necessary to explain the observed rotation curve, as **the visible matter alone is not enough to account for the observed velocity**.

#### Interactive Model

Having seen that the presence of dark matter is necessary to explain the rotation curve of the Milky Way, but that the solution is not as simple as just adding mass in a halo, it is the moment to realize that at this point we have a lot of freedom to explore different scenarios. Since the dark matter is still an ungoing research topic, we can't be sure of the exact distribution of dark matter in the galaxy. Therefore, untill further evidence is provided, your gess is as good as mine when it comes to the distribution of dark matter in the Milky Way.

Therefore, we have created an interactive model that allows you to explore different mass distributions of the galaxy and see how they affect the rotation curve. You can adjust the mass of the <span style="color:grey">bulge</span>, <span style="color:lightblue">disk</span>, and <span style="color:green">dark matter halo</span>, as well as their shape and scale lengths, and see how the rotation curve changes. This will help you understand the impact of dark matter on the rotation curve and the complexity of the mass distribution in the galaxy.

This model requires constant calculations and therefore cannot be enbeded in this document. However, you can access it in this [Google Colab notebook](https://colab.research.google.com/drive/1LeOCqU1tu573g2BQBTo96x3h3emR7yH0?usp=sharing) and explore the different scenarios.

<iframe src="https://colab.research.google.com/drive/1LeOCqU1tu573g2BQBTo96x3h3emR7yH0?usp=sharing" width="1000" height="600"></iframe>

### Conclusion
The constant velocity observed in the rotation curves strongly suggests the presence of an unseen mass, which we attribute to dark matter. However, the exact distribution of this dark matter is still uncertain, and further research is needed to determine its properties. The interactive model allows you to explore different mass distributions and see how they affect the rotation curve, providing a better understanding of the complexity of the mass distribution in the Milky Way.

However, the most important conclusion to extract is that nomatter the proposed distribution, **visible matter alone is not enough to explain the observed rotation curve**, meaning that dark matter is necessary to account for the observed velocities. This is a strong indication of the presence of dark matter in the Milky Way.

### References
- [1] Breithaupt, J (2000). New Understanding Physics for Advanced Level. Nelson Thornes. p. 231. ISBN 978-0-7487-4314-8. Alternatively, the formula can be obtained from the second law of Newton, F = ma, and the universal law of gravitation, F = GMm/r^2, where F is the force, m is the mass of the object, and a is the acceleration.
- [2] McMillan, P.J. (2017) The mass distribution and gravitational potential of the Milky Way, Monthly Notices of the Royal Astronomical Society, Volume 465, Issue 1, 11 February 2017, Pages 76–94, https://doi.org/10.1093/mnras/stw2759.
- [3] Kordopatis, G., Steinmetz, M., et al. (2017) The Radial Velocity Experiment (RAVE): Fifth Data Release, The Astronomical Journal, Volume 153, Number 2, 2017, https://doi.org/10.3847/1538-3881/153/2/75.
- [4] Zacharias, N., Finch, C., Girard, T. M., et al. (2013) The Fourth US Naval Observatory CCD Astrograph Catalog (UCAC4), The Astronomical Journal, Volume 145, Number 2, 2013, https://doi.org/10.1088/0004-6256/145/2/44.