---
hide:
  - navigation
---

<script>
// Toggle open all details elements, onload
// Regardless of their initial status
// StackOverflow 43008609
const expandElements = shouldExpand => {
    let detailsElements = document.querySelectorAll("details");

    detailsElements = [...detailsElements];

    if (shouldExpand) {
        detailsElements.map(item => item.setAttribute("open", shouldExpand));
    } else {
        detailsElements.map(item => item.removeAttribute("open"));
    }
};
</script>

#  **A Living Review of Machine Learning for Particle Physics**

*Modern machine learning techniques, including deep learning, is rapidly being applied, adapted, and developed for high energy physics.  The goal of this document is to provide a nearly comprehensive list of citations for those developing and applying these approaches to experimental, phenomenological, or theoretical analyses.  As a living document, it will be updated as often as possible to incorporate the latest developments.  A list of proper (unchanging) reviews can be found within.  Papers are grouped into a small set of topics to be as useful as possible.  Suggestions are most welcome.*

[![download](https://img.shields.io/badge/download-review-blue.svg)](https://iml-wg.github.io/HEPML-LivingReview/assets/hepml_review.pdf)
[![github](https://badges.aleen42.com/src/github.svg)](https://github.com/iml-wg/HEPML-LivingReview)

<p align="center"><img src="assets/per_year.png#only-light" width="75%", alt="Publications per Year"></p>
<p align="center"><img src="assets/dark_per_year.png#only-dark" width="75%", alt="Publications per Year"></p>


<a class="md-button" onClick="expandElements(true)">Expand all sections</a>
<a class="md-button" onClick="expandElements(false)">Collapse all sections</a>
##  Reviews

??? example "Modern reviews"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Modern reviews
    </div>

    * [Snowmass 2021 Computational Frontier CompF03 Topical Group Report: Machine Learning](https://arxiv.org/abs/2209.07559) (2022)
    * [Artificial Intelligence and Machine Learning in Nuclear Physics](https://arxiv.org/abs/2112.02309) [[DOI](https://doi.org/10.1103/RevModPhys.94.031003)] (2021)
    * [Machine Learning in the Search for New Fundamental Physics](https://arxiv.org/abs/2112.03769) (2021)
    * [Modern Machine Learning and Particle Physics](https://arxiv.org/abs/2103.12226) [[DOI](https://doi.org/10.1162/99608f92.beeb1183)] (2021)
    * [Machine and Deep Learning Applications in Particle Physics](https://arxiv.org/abs/1912.08245) [[DOI](https://doi.org/10.1142/S0217751X19300199)] (2019)
    * [Machine learning and the physical sciences](https://arxiv.org/abs/1903.10563) [[DOI](https://doi.org/10.1103/RevModPhys.91.045002)] (2019)
    * [Machine learning at the energy and intensity frontiers of particle physics](https://doi.org/10.1038/s41586-018-0361-2) (2018)
    * [Machine Learning in High Energy Physics Community White Paper](https://arxiv.org/abs/1807.02876) [[DOI](https://doi.org/10.1088/1742-6596/1085/2/022008)] (2018)
    * [Deep Learning and its Application to LHC Physics](https://arxiv.org/abs/1806.11484) [[DOI](https://doi.org/10.1146/annurev-nucl-101917-021019)] (2018)
    * [Jet Substructure at the Large Hadron Collider: A Review of Recent Advances in Theory and Machine Learning](https://arxiv.org/abs/1709.04464) [[DOI](https://doi.org/10.1016/j.physrep.2019.11.001)] (2017)


??? example "Specialized reviews"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Specialized reviews
    </div>

    * [CaloChallenge 2022: A Community Challenge for Fast Calorimeter Simulation](https://arxiv.org/abs/2410.21611) (2024)
    * [Exploring jets: substructure and flavour tagging in CMS and ATLAS](https://arxiv.org/abs/2410.14330) (2024)
    * [Novel machine learning applications at the LHC](https://arxiv.org/abs/2409.20413) (2024)
    * [Unveiling the Secrets of New Physics Through Top Quark Tagging](https://arxiv.org/abs/2409.12085) (2024)
    * [TASI Lectures on Physics for Machine Learning](https://arxiv.org/abs/2408.00082) (2024)
    * [QCD Masterclass Lectures on Jet Physics and Machine Learning](https://arxiv.org/abs/2407.04897) (2024)
    * [Top-philic Machine Learning](https://arxiv.org/abs/2407.00183) [[DOI](https://doi.org/10.1140/epjs/s11734-024-01237-9)] (2024)
    * [A Comprehensive Evaluation of Generative Models in Calorimeter Shower Simulation](https://arxiv.org/abs/2406.12898) (2024)
    * [The Landscape of Unfolding with Machine Learning](https://arxiv.org/abs/2404.18807) (2024)
    * [Machine Learning in High Energy Physics: A review of heavy-flavor jet tagging at the LHC](https://arxiv.org/abs/2404.01071) [[DOI](https://doi.org/10.1140/epjs/s11734-024-01234-y)] (2024)
    * [Unsupervised and lightly supervised learning in particle physics](https://arxiv.org/abs/2403.13676) [[DOI](https://doi.org/10.1140/epjs/s11734-024-01235-x)] (2024)
    * [High-energy physics image classification: A Survey of Jet Applications](https://arxiv.org/abs/2403.11934) (2024)
    * [The SMARTHEP European Training Network](https://arxiv.org/abs/2401.13484) [[DOI](https://doi.org/10.1051/epjconf/202429508022)] (2024)
    * [Les Houches guide to reusable ML models in LHC analyses](https://arxiv.org/abs/2312.14575) (2023)
    * [Machine Learning for Anomaly Detection in Particle Physics](https://arxiv.org/abs/2312.14190) [[DOI](https://doi.org/10.1016/j.revip.2024.100091)] (2023)
    * [Deep Generative Models for Detector Signature Simulation: An Analytical Taxonomy](https://arxiv.org/abs/2312.09597) [[DOI](https://doi.org/10.1016/j.revip.2024.100092)] (2023)
    * [Artificial Intelligence for the Electron Ion Collider (AI4EIC)](https://arxiv.org/abs/2307.08593) [[DOI](https://doi.org/10.1007/s41781-024-00113-4)] (2023)
    * [Overview: Jet quenching with machine learning](https://arxiv.org/abs/2308.10035) (2023)
    * [Graph neural networks at the Large Hadron Collider](https://doi.org/10.1038/s42254-023-00569-0) (2023)
    * [Exploring QCD matter in extreme conditions with Machine Learning](https://arxiv.org/abs/2303.15136) [[DOI](https://doi.org/10.1016/j.ppnp.2023.104084)] (2023)
    * [Snowmass Neutrino Frontier Report](https://arxiv.org/abs/2211.08641) (2022)
    * [FAIR for AI: An interdisciplinary, international, inclusive, and diverse community building perspective](https://arxiv.org/abs/2210.08973) [[DOI](https://doi.org/10.1038/s41597-023-02298-6)] (2022)
    * [Bridging Machine Learning and Sciences: Opportunities and Challenges](https://arxiv.org/abs/2210.13441) (2022)
    * [Modern Machine Learning for LHC Physicists](https://arxiv.org/abs/2211.01421) (2022)
    * [Interpretable Uncertainty Quantification in AI for HEP](https://arxiv.org/abs/2208.03284) [[DOI](https://doi.org/10.2172/1886020)] (2022)
    * [Data Science and Machine Learning in Education](https://arxiv.org/abs/2207.09060) (2022)
    * [Boosted decision trees](https://arxiv.org/abs/2206.09645) [[DOI](https://doi.org/10.1142/9789811234033_0002)] (2022)
    * [Physics Community Needs, Tools, and Resources for Machine Learning](https://arxiv.org/abs/2203.16255) (2022)
    * [Graph Neural Networks in Particle Physics: Implementations, Innovations, and Challenges](https://arxiv.org/abs/2203.12852) (2022)
    * [New directions for surrogate models and differentiable programming for High Energy Physics detector simulation](https://arxiv.org/abs/2203.08806) (2022)
    * [Machine Learning and Cosmology](https://arxiv.org/abs/2203.08056) (2022)
    * [Machine Learning and LHC Event Generation](https://arxiv.org/abs/2203.07460) [[DOI](https://doi.org/10.21468/SciPostPhys.14.4.079)] (2022)
    * [Symmetry Group Equivariant Architectures for Physics](https://arxiv.org/abs/2203.06153) (2022)
    * [Solving Simulation Systematics in and with AI/ML](https://arxiv.org/abs/2203.06112) (2022)
    * [Deep Learning From Four Vectors](https://arxiv.org/abs/2203.03067) (2022)
    * [A survey of machine learning-based physics event generation](https://arxiv.org/abs/2106.00643) [[DOI](https://doi.org/10.24963/ijcai.2021/588)] (2021)
    * [Sequence-based Machine Learning Models in Jet Physics](https://arxiv.org/abs/2102.06128) (2021)
    * [Quantum Machine Learning in High Energy Physics](https://arxiv.org/abs/2005.08582) [[DOI](https://doi.org/10.1088/2632-2153/abc17d)] (2020)
    * [Image-Based Jet Analysis](https://arxiv.org/abs/2012.09719) (2020)
    * [Machine Learning scientific competitions and datasets](https://arxiv.org/abs/2012.08520) (2020)
    * [The frontier of simulation-based inference](https://arxiv.org/abs/1911.01429) [[DOI](https://doi.org/10.1073/pnas.1912789117)] (2019)
    * [Distributed Training and Optimization Of Neural Networks](https://arxiv.org/abs/2012.01839) [[DOI](https://doi.org/10.1142/9789811234033_0008)] (2020)
    * [Graph Neural Networks for Particle Tracking and Reconstruction](https://arxiv.org/abs/2012.01249) [[DOI](https://doi.org/10.1142/9789811234033_0012)] (2020)
    * [Anomaly Detection for Physics Analysis and Less than Supervised Learning](https://arxiv.org/abs/2010.14554) (2020)
    * [Simulation-based inference methods for particle physics](https://arxiv.org/abs/2010.06439) (2020)
    * [Parton distribution functions](https://arxiv.org/abs/2008.12305) (2020)
    * [Generative Networks for LHC events](https://arxiv.org/abs/2008.08558) (2020)
    * [A Review on Machine Learning for Neutrino Experiments](https://arxiv.org/abs/2008.01242) [[DOI](https://doi.org/10.1142/S0217751X20430058)] (2020)
    * [Graph Neural Networks in Particle Physics](https://arxiv.org/abs/2007.13681) [[DOI](https://doi.org/10.1088/2632-2153/abbf9a)] (2020)
    * [Dealing with Nuisance Parameters using Machine Learning in High Energy Physics: a Review](https://arxiv.org/abs/2007.09121) (2020)
    * [The Machine Learning Landscape of Top Taggers](https://arxiv.org/abs/1902.09914) [[DOI](https://doi.org/10.21468/SciPostPhys.7.1.014)] (2019)


??? example "Classical papers"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Classical papers
    </div>

    * [Finding Gluon Jets With a Neural Trigger](https://doi.org/10.1103/PhysRevLett.65.1321) (1990)
    * [Neural Networks and Cellular Automata in Experimental High-energy Physics](https://doi.org/10.1016/0010-4655(88)90004-5) (1988)


??? example "Datasets"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Datasets
    </div>

    * [CaloChallenge 2022: A Community Challenge for Fast Calorimeter Simulation](https://arxiv.org/abs/2410.21611) (2024)
    * [FAIR Universe HiggsML Uncertainty Challenge Competition](https://arxiv.org/abs/2410.02867) (2024)
    * [RODEM Jet Datasets](https://arxiv.org/abs/2408.11616) (2024)
    * [Electron Energy Regression in the CMS High-Granularity Calorimeter Prototype](https://arxiv.org/abs/2309.06582) (2023)
    * [Public Kaggle Competition ''IceCube -- Neutrinos in Deep Ice''](https://arxiv.org/abs/2307.15289) (2023)
    * [Particle Transformer for Jet Tagging](https://arxiv.org/abs/2202.03772) (2022)
    * [A FAIR and AI-ready Higgs Boson Decay Dataset](https://arxiv.org/abs/2108.02214) [[DOI](https://doi.org/10.1038/s41597-021-01109-0)] (2021)
    * [LHC physics dataset for unsupervised New Physics detection at 40 MHz](https://arxiv.org/abs/2107.02157) [[DOI](https://doi.org/10.1038/s41597-022-01187-8)] (2021)
    * [Shared Data and Algorithms for Deep Learning in Fundamental Physics](https://arxiv.org/abs/2107.00656) [[DOI](https://doi.org/10.1007/s41781-022-00082-6)] (2021)
    * [The Dark Machines Anomaly Score Challenge: Benchmark Data and Model Independent Event Classification for the Large Hadron Collider](https://arxiv.org/abs/2105.14027) [[DOI](https://doi.org/10.21468/SciPostPhys.12.1.043)] (2021)
    * [The LHC Olympics 2020: A Community Challenge for Anomaly Detection in High Energy Physics](https://arxiv.org/abs/2101.08320) [[DOI](https://doi.org/10.1088/1361-6633/ac36b9)] (2021)

##  Classification

??? example "Parameterized classifiers"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Parameterized classifiers
    </div>

    * [Boosting likelihood learning with event reweighting](https://arxiv.org/abs/2308.05704) [[DOI](https://doi.org/10.1007/JHEP03(2024)117)] (2023)
    * [E Pluribus Unum Ex Machina: Learning from Many Collider Events at Once](https://arxiv.org/abs/2101.07263) [[DOI](https://doi.org/10.1103/PhysRevD.103.116013)] (2021)
    * [Approximating Likelihood Ratios with Calibrated Discriminative  Classifiers](https://arxiv.org/abs/1506.02169) (2015)
    * [Parameterized neural networks for high-energy physics](https://arxiv.org/abs/1601.07913) [[DOI](https://doi.org/10.1140/epjc/s10052-016-4099-4)] (2016)


??? example "Representations"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ### Representations
    </div>

    ####  Jet images

    * [High-energy physics image classification: A Survey of Jet Applications](https://arxiv.org/abs/2403.11934) (2024)
    * [A Guide to Diagnosing Colored Resonances at Hadron Colliders](https://arxiv.org/abs/2306.00079) [[DOI](https://doi.org/10.1007/JHEP08(2023)173)] (2023)
    * [Automatic detection of boosted Higgs and top quark jets in event image](https://arxiv.org/abs/2302.13460) [[DOI](https://doi.org/10.1103/PhysRevD.108.116002)] (2023)
    * [Identifying the Quantum Properties of Hadronic Resonances using Machine Learning](https://arxiv.org/abs/2105.04582) (2021)
    * [Deep learning jet modifications in heavy-ion collisions](https://arxiv.org/abs/2012.07797) [[DOI](https://doi.org/10.1007/JHEP03(2021)206)] (2020)
    * [Learning to Isolate Muons](https://arxiv.org/abs/2102.02278) [[DOI](https://doi.org/10.1007/JHEP10(2021)200)] (2021)
    * [Quark-Gluon Jet Discrimination Using Convolutional Neural Networks](https://arxiv.org/abs/2012.02531) [[DOI](https://doi.org/10.3938/jkps.74.219)] (2020)
    * [An Attention Based Neural Network for Jet Tagging](https://arxiv.org/abs/2009.00170) (2020)
    * [Reconstructing boosted Higgs jets from event image segmentation](https://arxiv.org/abs/2008.13529) [[DOI](https://doi.org/10.1007/JHEP04(2021)156)] (2020)
    * [Pulling Out All the Tops with Computer Vision and Deep Learning](https://arxiv.org/abs/1803.00107) [[DOI](https://doi.org/10.1007/JHEP10(2018)121)] (2018)
    * [Deep-learning Top Taggers or The End of QCD?](https://arxiv.org/abs/1701.08784) [[DOI](https://doi.org/10.1007/JHEP05(2017)006)] (2017)
    * [Deep learning in color: towards automated quark/gluon](https://arxiv.org/abs/1612.01551) [[DOI](https://doi.org/10.1007/JHEP01(2017)110)] (2016)
    * [Parton Shower Uncertainties in Jet Substructure Analyses with Deep Neural Networks](https://arxiv.org/abs/1609.00607) [[DOI](https://doi.org/10.1103/PhysRevD.95.014018)] (2016)
    * [Learning to classify from impure samples with high-dimensional data](https://arxiv.org/abs/1801.10158) [[DOI](https://doi.org/10.1103/PhysRevD.98.011502)] (2018)
    * [Boosting $H\to b\bar b$ with Machine Learning](https://arxiv.org/abs/1807.10768) [[DOI](https://doi.org/10.1007/JHEP10(2018)101)] (2018)
    * [Quark versus Gluon Jet Tagging Using Jet Images with the ATLAS Detector](http://cds.cern.ch/record/2275641) (2017)
    * [Jet-images — deep learning edition](https://arxiv.org/abs/1511.05190) [[DOI](https://doi.org/10.1007/JHEP07(2016)069)] (2015)
    * [Playing Tag with ANN: Boosted Top Identification with Pattern Recognition](https://arxiv.org/abs/1501.05968) [[DOI](https://doi.org/10.1007/JHEP07(2015)086)] (2015)
    * [Jet-Images: Computer Vision Inspired Techniques for Jet Tagging](https://arxiv.org/abs/1407.5675) [[DOI](https://doi.org/10.1007/JHEP02(2015)118)] (2014)
    * [How to tell quark jets from gluon jets](https://doi.org/10.1103/PhysRevD.44.2025) (1991)

    ####  Event images

    * [A novel machine learning method to detect double-$\Lambda$ hypernuclear events in nuclear emulsions](https://arxiv.org/abs/2409.01657) (2024)
    * [Exploring the Synergy of Kinematics and Dynamics for Collider Physics](https://arxiv.org/abs/2311.16674) (2023)
    * [A Neural Network Approach for Orienting Heavy-Ion Collision Events](https://arxiv.org/abs/2308.15796) [[DOI](https://doi.org/10.1016/j.physletb.2023.138359)] (2023)
    * [Large-Scale Deep Learning for Multi-Jet Event Classification](https://arxiv.org/abs/2207.11710) (2022)
    * [Jet Single Shot Detection](https://arxiv.org/abs/2105.05785) [[DOI](https://doi.org/10.1051/epjconf/202125104027)] (2021)
    * [End-to-End Jet Classification of Boosted Top Quarks with the CMS Open Data](https://arxiv.org/abs/2104.14659) [[DOI](https://doi.org/10.1051/epjconf/202125104030)] (2021)
    * [Identifying the nature of the QCD transition in relativistic collision of heavy nuclei with deep learning](https://arxiv.org/abs/1910.11530) [[DOI](https://doi.org/10.1140/epjc/s10052-020-8030-7)] (2019)
    * [Disentangling Boosted Higgs Boson Production Modes with Machine Learning](https://arxiv.org/abs/2009.05930) [[DOI](https://doi.org/10.1088/1748-0221/16/07/P07002)] (2020)
    * [End-to-End Physics Event Classification with the CMS Open Data: Applying Image-based Deep Learning on Detector Data to Directly Classify Collision Events at the LHC](https://arxiv.org/abs/1807.11916) [[DOI](https://doi.org/10.1007/s41781-020-00038-8)] (2018)
    * [Boosting $H\to b\bar b$ with Machine Learning](https://arxiv.org/abs/1807.10768) [[DOI](https://doi.org/10.1007/JHEP10(2018)101)] (2018)
    * [Convolutional Neural Networks with Event Images for Pileup Mitigation with the ATLAS Detector](http://cds.cern.ch/record/2684070) (2019)
    * [Topology classification with deep learning to improve real-time event selection at the LHC](https://arxiv.org/abs/1807.00083) [[DOI](https://doi.org/10.1007/s41781-019-0028-1)] (2018)

    ####  Sequences

    * [Identification of Jets Containing $b$-Hadrons with Recurrent Neural Networks at the ATLAS Experiment](http://cdsweb.cern.ch/record/2255226) (2017)
    * [Sequence-based Machine Learning Models in Jet Physics](https://arxiv.org/abs/2102.06128) (2021)
    * [Development of a Vertex Finding Algorithm using Recurrent Neural Network](https://arxiv.org/abs/2101.11906) [[DOI](https://doi.org/10.1016/j.nima.2022.167836)] (2021)
    * [Jet Flavour Classification Using DeepJet](https://arxiv.org/abs/2008.10519) [[DOI](https://doi.org/10.1088/1748-0221/15/12/P12012)] (2020)
    * [Topology classification with deep learning to improve real-time event selection at the LHC](https://arxiv.org/abs/1807.00083) [[DOI](https://doi.org/10.1007/s41781-019-0028-1)] (2018)
    * [Jet Flavor Classification in High-Energy Physics with Deep Neural Networks](https://arxiv.org/abs/1607.08633) [[DOI](https://doi.org/10.1103/PhysRevD.94.112002)] (2016)

    ####  Trees

    * [Searches for the BSM scenarios at the LHC using decision tree based machine learning algorithms: A comparative study and review of Random Forest, Adaboost, XGboost and LightGBM frameworks](https://arxiv.org/abs/2405.06040) (2024)
    * [Photon Classification with Gradient Boosted Trees at CLAS12](https://arxiv.org/abs/2402.13105) [[DOI](https://doi.org/10.1088/1748-0221/19/06/C06006)] (2024)
    * [Back To The Roots: Tree-Based Algorithms for Weakly Supervised Anomaly Detection](https://arxiv.org/abs/2309.13111) [[DOI](https://doi.org/10.1103/PhysRevD.109.034033)] (2023)
    * [Boosting dark matter searches at muon colliders with Machine Learning: the mono-Higgs channel as a case study](https://arxiv.org/abs/2309.11241) [[DOI](https://doi.org/10.1093/ptep/ptad144)] (2023)
    * [Applying Machine Learning Techniques to Searches for Lepton-Partner Pair-Production with Intermediate Mass Gaps at the Large Hadron Collider](https://arxiv.org/abs/2309.10197) [[DOI](https://doi.org/10.1103/PhysRevD.109.075018)] (2023)
    * [Introduction and analysis of a method for the investigation of QCD-like tree data](https://arxiv.org/abs/2112.01809) [[DOI](https://doi.org/10.3390/e24010104)] (2021)
    * [Recursive Neural Networks in Quark/Gluon Tagging](https://arxiv.org/abs/1711.02633) [[DOI](https://doi.org/10.1007/s41781-018-0007-y)] (2017)
    * [QCD-Aware Recursive Neural Networks for Jet Physics](https://arxiv.org/abs/1702.00748) [[DOI](https://doi.org/10.1007/JHEP01(2019)057)] (2017)

    ####  Graphs

    * [HGPflow: Extending Hypergraph Particle Flow to Collider Event Reconstruction](https://arxiv.org/abs/2410.23236) (2024)
    * [Observation of a rare beta decay of the charmed baryon with a Graph Neural Network](https://arxiv.org/abs/2410.13515) (2024)
    * [Measurements of decay branching fractions of the Higgs boson to hadronic final states at the CEPC](https://arxiv.org/abs/2410.04465) (2024)
    * [Search for light long-lived particles decaying to displaced jets in proton-proton collisions at $\sqrt{s}$](https://arxiv.org/abs/2409.10806) (2024)
    * [EggNet: An Evolving Graph-based Graph Attention Network for Particle Track Reconstruction](https://arxiv.org/abs/2407.13925) (2024)
    * [Graph Neural Network-Based Track Finding in the LHCb Vertex Detector](https://arxiv.org/abs/2407.12119) (2024)
    * [Accelerating Graph-based Tracking Tasks with Symbolic Regression](https://arxiv.org/abs/2406.16752) (2024)
    * [Using graph neural networks to reconstruct charged pion showers in the CMS High Granularity Calorimeter](https://arxiv.org/abs/2406.11937) (2024)
    * [Advancing Set-Conditional Set Generation: Graph Diffusion for Fast Simulation of Reconstructed Particles](https://arxiv.org/abs/2405.10106) (2024)
    * [NuGraph2: A Graph Neural Network for Neutrino Physics Event Reconstruction](https://arxiv.org/abs/2403.11872) [[DOI](https://doi.org/10.1103/PhysRevD.110.032008)] (2024)
    * [A case study of sending graph neural networks back to the test bench for applications in high-energy particle physics](https://arxiv.org/abs/2402.17386) [[DOI](https://doi.org/10.1007/s41781-024-00122-3)] (2024)
    * [A new graph-neural-network flavor tagger for Belle II and measurement of $\sin 2\phi_1$ in $B^0 \to J/\psi K^0_\text{S}$ decays](https://arxiv.org/abs/2402.17260) [[DOI](https://doi.org/10.1103/PhysRevD.110.012001)] (2024)
    * [Reconstruction of Short-Lived Particles using Graph-Hypergraph Representation Learning](https://arxiv.org/abs/2402.10149) (2024)
    * [Application of Graph Neural Networks in Dark Photon Search with Visible Decays at Future Beam Dump Experiment](https://arxiv.org/abs/2401.15477) [[DOI](https://doi.org/10.1007/978-981-97-0065-3_19)] (2024)
    * [Neutrino Reconstruction in TRIDENT Based on Graph Neural Network](https://arxiv.org/abs/2401.15324) [[DOI](https://doi.org/10.1007/978-981-97-0065-3_20)] (2024)
    * [Combined track finding with GNN \& CKF](https://arxiv.org/abs/2401.16016) (2024)
    * [Rotation-equivariant graph neural network for learning hadronic SMEFT effects](https://arxiv.org/abs/2401.10323) [[DOI](https://doi.org/10.1103/PhysRevD.109.076012)] (2024)
    * [Hypergraphs in LHC Phenomenology -- The Next Frontier of IRC-Safe Feature Extraction](https://arxiv.org/abs/2309.17351) [[DOI](https://doi.org/10.1007/JHEP01(2024)113)] (2023)
    * [Graph Structure from Point Clouds: Geometric Attention is All You Need](https://arxiv.org/abs/2307.16662) (2023)
    * [LLPNet: Graph Autoencoder for Triggering Light Long-Lived Particles at HL-LHC](https://arxiv.org/abs/2308.13611) (2023)
    * [Jet energy calibration with deep learning as a Kubeflow pipeline](https://arxiv.org/abs/2308.12724) [[DOI](https://doi.org/10.1007/s41781-023-00103-y)] (2023)
    * [Photon Reconstruction in the Belle II Calorimeter Using Graph Neural Networks](https://arxiv.org/abs/2306.04179) [[DOI](https://doi.org/10.1007/s41781-023-00105-w)] (2023)
    * [Flavour tagging with graph neural networks with the ATLAS detector](https://arxiv.org/abs/2306.04415) (2023)
    * [GNN for Deep Full Event Interpretation and hierarchical reconstruction of heavy-hadron decays in proton-proton collisions](https://arxiv.org/abs/2304.08610) [[DOI](https://doi.org/10.1007/s41781-023-00107-8)] (2023)
    * [Hierarchical Graph Neural Networks for Particle Track Reconstruction](https://arxiv.org/abs/2303.01640) (2023)
    * [Domain-adversarial graph neural networks for \ensuremath{\Lambda} hyperon identification with CLAS12](https://arxiv.org/abs/2302.05481) [[DOI](https://doi.org/10.1088/1748-0221/18/06/P06002)] (2023)
    * [Determination of impact parameter for CEE with Digi-input neural networks](https://arxiv.org/abs/2307.15355) [[DOI](https://doi.org/10.1088/1748-0221/19/05/P05009)] (2023)
    * [Real-time Graph Building on FPGAs for Machine Learning Trigger Applications in Particle Physics](https://arxiv.org/abs/2307.07289) [[DOI](https://doi.org/10.1007/s41781-024-00117-0)] (2023)
    * [Improved selective background Monte Carlo simulation at Belle II with graph attention networks and weighted events](https://arxiv.org/abs/2307.06434) (2023)
    * [Equivariant Graph Neural Networks for Charged Particle Tracking](https://arxiv.org/abs/2304.05293) (2023)
    * [Topological Reconstruction of Particle Physics Processes using Graph Neural Networks](https://arxiv.org/abs/2303.13937) [[DOI](https://doi.org/10.1103/PhysRevD.107.116019)] (2023)
    * [On the BSM reach of four top production at the LHC](https://arxiv.org/abs/2302.08281) [[DOI](https://doi.org/10.1103/PhysRevD.108.035001)] (2023)
    * [Deep Learning Symmetries and Their Lie Groups, Algebras, and Subalgebras from First Principles](https://arxiv.org/abs/2301.05638) [[DOI](https://doi.org/10.1088/2632-2153/acd989)] (2023)
    * [Heterogeneous Graph Neural Network for identifying hadronically decayed tau leptons at the High Luminosity LHC](https://arxiv.org/abs/2301.00501) [[DOI](https://doi.org/10.1088/1748-0221/18/07/P07001)] (2023)
    * [Do graph neural networks learn traditional jet substructure?](https://arxiv.org/abs/2211.09912) (2022)
    * [Reconstructing particles in jets using set transformer and hypergraph prediction networks](https://arxiv.org/abs/2212.01328) [[DOI](https://doi.org/10.1140/epjc/s10052-023-11677-7)] (2022)
    * [Climbing four tops with graph networks, transformers and pairwise features](https://arxiv.org/abs/2211.05143) (2022)
    * [PELICAN: Permutation Equivariant and Lorentz Invariant or Covariant Aggregator Network for Particle Physics](https://arxiv.org/abs/2211.00454) (2022)
    * [A jet tagging algorithm of graph network with HaarPooling message passing](https://arxiv.org/abs/2210.13869) [[DOI](https://doi.org/10.1103/PhysRevD.108.072007)] (2022)
    * [End-to-end multi-particle reconstruction in high occupancy imaging calorimeters with graph neural networks](https://arxiv.org/abs/2204.01681) [[DOI](https://doi.org/10.1140/epjc/s10052-022-10665-7)] (2022)
    * [An Efficient Lorentz Equivariant Graph Neural Network for Jet Tagging](https://arxiv.org/abs/2201.08187) [[DOI](https://doi.org/10.1007/JHEP07(2022)030)] (2022)
    * [Machine Learning for Particle Flow Reconstruction at CMS](https://arxiv.org/abs/2203.00330) [[DOI](https://doi.org/10.1088/1742-6596/2438/1/012100)] (2022)
    * [Graph Neural Networks for Charged Particle Tracking on FPGAs](https://arxiv.org/abs/2112.02048) [[DOI](https://doi.org/10.3389/fdata.2022.828666)] (2021)
    * [Particle Graph Autoencoders and Differentiable, Learned Energy Mover's Distance](https://arxiv.org/abs/2111.12849) (2021)
    * [Improved Constraints on Effective Top Quark Interactions using Edge Convolution Networks](https://arxiv.org/abs/2111.01838) [[DOI](https://doi.org/10.1007/JHEP04(2022)137)] (2021)
    * [Energy-weighted Message Passing: an infra-red and collinear safe graph neural network algorithm](https://arxiv.org/abs/2109.14636) [[DOI](https://doi.org/10.1007/JHEP02(2022)060)] (2021)
    * [Anomaly detection with Convolutional Graph Neural Networks](https://arxiv.org/abs/2105.07988) [[DOI](https://doi.org/10.1007/JHEP08(2021)080)] (2021)
    * [Segmentation of EM showers for neutrino experiments with deep graph neural networks](https://arxiv.org/abs/2104.02040) [[DOI](https://doi.org/10.1088/1748-0221/16/12/P12035)] (2021)
    * [Graph Generative Models for Fast Detector Simulations in High Energy Physics](https://arxiv.org/abs/2104.01725) (2021)
    * [Jet characterization in Heavy Ion Collisions by QCD-Aware Graph Neural Networks](https://arxiv.org/abs/2103.14906) (2021)
    * [Charged particle tracking via edge-classifying interaction networks](https://arxiv.org/abs/2103.16701) [[DOI](https://doi.org/10.1007/s41781-021-00073-z)] (2021)
    * [Instance Segmentation GNNs for One-Shot Conformal Tracking at the LHC](https://arxiv.org/abs/2103.06509) (2021)
    * [Graph Neural Network for Object Reconstruction in Liquid Argon Time Projection Chambers](https://arxiv.org/abs/2103.06233) [[DOI](https://doi.org/10.1051/epjconf/202125103054)] (2021)
    * [Deep Learning strategies for ProtoDUNE raw data denoising](https://arxiv.org/abs/2103.01596) [[DOI](https://doi.org/10.1007/s41781-021-00077-9)] (2021)
    * [Towards a realistic track reconstruction algorithm based on graph neural networks for the HL-LHC](https://arxiv.org/abs/2103.00916) [[DOI](https://doi.org/10.1051/epjconf/202125103047)] (2021)
    * [MLPF: Efficient machine-learned particle-flow reconstruction using graph neural networks](https://arxiv.org/abs/2101.08578) [[DOI](https://doi.org/10.1140/epjc/s10052-021-09158-w)] (2021)
    * [Vertex and Energy Reconstruction in JUNO with Machine Learning Methods](https://arxiv.org/abs/2101.04839) [[DOI](https://doi.org/10.1016/j.nima.2021.165527)] (2021)
    * [Jet tagging in the Lund plane with graph networks](https://arxiv.org/abs/2012.08526) [[DOI](https://doi.org/10.1007/JHEP03(2021)052)] (2020)
    * [Particle Track Reconstruction using Geometric Deep Learning](https://arxiv.org/abs/2012.08515) (2020)
    * [Accelerated Charged Particle Tracking with Graph Neural Networks on FPGAs](https://arxiv.org/abs/2012.01563) (2020)
    * [The Boosted Higgs Jet Reconstruction via Graph Neural Network](https://arxiv.org/abs/2010.05464) [[DOI](https://doi.org/10.1103/PhysRevD.103.116025)] (2020)
    * [Graph neural network for 3D classification of ambiguities and optical crosstalk in scintillator-based neutrino detectors](https://arxiv.org/abs/2009.00688) [[DOI](https://doi.org/10.1103/PhysRevD.103.032005)] (2020)
    * [Track Seeding and Labelling with Embedded-space Graph Neural Networks](https://arxiv.org/abs/2007.00149) (2020)
    * [Supervised Jet Clustering with Graph Neural Networks for Lorentz Boosted Bosons](https://arxiv.org/abs/2008.06064) [[DOI](https://doi.org/10.1103/PhysRevD.102.075014)] (2020)
    * [Distance-Weighted Graph Neural Networks on FPGAs for Real-Time Particle Reconstruction in High Energy Physics](https://arxiv.org/abs/2008.03601) [[DOI](https://doi.org/10.3389/fdata.2020.598927)] (2020)
    * [Graph Neural Networks in Particle Physics](https://arxiv.org/abs/2007.13681) [[DOI](https://doi.org/10.1088/2632-2153/abbf9a)] (2020)
    * [Casting a graph net to catch dark showers](https://arxiv.org/abs/2006.08639) [[DOI](https://doi.org/10.21468/SciPostPhys.10.2.046)] (2020)
    * [Probing triple Higgs coupling with machine learning at the LHC](https://arxiv.org/abs/2005.11086) [[DOI](https://doi.org/10.1103/PhysRevD.104.056003)] (2020)
    * [Neural Network-based Top Tagger with Two-Point Energy Correlations and Geometry of Soft Emissions](https://arxiv.org/abs/2003.11787) [[DOI](https://doi.org/10.1007/JHEP07(2020)111)] (2020)
    * [Towards a Computer Vision Particle Flow](https://arxiv.org/abs/2003.08863) [[DOI](https://doi.org/10.1140/epjc/s10052-021-08897-0)] (2020)
    * [Interpretable deep learning for two-prong jet classification with jet spectra](https://arxiv.org/abs/1904.02092) [[DOI](https://doi.org/10.1007/JHEP07(2019)135)] (2019)
    * [Learning representations of irregular particle-detector geometry with distance-weighted graph networks](https://arxiv.org/abs/1902.07987) [[DOI](https://doi.org/10.1140/epjc/s10052-019-7113-9)] (2019)
    * [JEDI-net: a jet identification algorithm based on interaction networks](https://arxiv.org/abs/1908.05318) [[DOI](https://doi.org/10.1140/epjc/s10052-020-7608-4)] (2019)
    * [Unveiling CP property of top-Higgs coupling with graph neural networks at the LHC](https://arxiv.org/abs/1901.05627) [[DOI](https://doi.org/10.1016/j.physletb.2020.135198)] (2019)
    * [Pileup mitigation at the Large Hadron Collider with graph neural networks](https://arxiv.org/abs/1810.07988) [[DOI](https://doi.org/10.1140/epjp/i2019-12710-3)] (2018)
    * [Probing stop pair production at the LHC with graph neural networks](https://arxiv.org/abs/1807.09088) [[DOI](https://doi.org/10.1007/JHEP08(2019)055)] (2018)
    * [Graph Neural Networks for Particle Reconstruction in High Energy Physics detectors](https://arxiv.org/abs/2003.11603) (2020)
    * [Neural Message Passing for Jet Physics](https://dl4physicalsciences.github.io/files/nips_dlps_2017_29.pdf) (2017)

    ####  Sets (point clouds)

    * [Point cloud-based diffusion models for the Electron-Ion Collider](https://arxiv.org/abs/2410.22421) (2024)
    * [Is Tokenization Needed for Masked Particle Modelling?](https://arxiv.org/abs/2409.12589) (2024)
    * [Moments of Clarity: Streamlining Latent Spaces in Machine Learning using Moment Pooling](https://arxiv.org/abs/2403.08854) [[DOI](https://doi.org/10.1103/PhysRevD.110.074020)] (2024)
    * [Sets are All You Need: Ultrafast Jet Classification on FPGAs for HL-LHC](https://arxiv.org/abs/2402.01876) [[DOI](https://doi.org/10.1088/2632-2153/ad5f10)] (2024)
    * [Multi-scale cross-attention transformer encoder for event classification](https://arxiv.org/abs/2401.00452) [[DOI](https://doi.org/10.1007/JHEP03(2024)144)] (2024)
    * [PAIReD jet: A multi-pronged resonance tagging strategy across all Lorentz boosts](https://arxiv.org/abs/2311.11011) [[DOI](https://doi.org/10.1007/JHEP09(2024)128)] (2023)
    * [The Optimal use of Segmentation for Sampling Calorimeters](https://arxiv.org/abs/2310.04442) [[DOI](https://doi.org/10.1088/1748-0221/19/06/P06002)] (2023)
    * [EPiC-ly Fast Particle Cloud Generation with Flow-Matching and Diffusion](https://arxiv.org/abs/2310.00049) (2023)
    * [A data-driven and model-agnostic approach to solving combinatorial assignment problems in searches for new physics](https://arxiv.org/abs/2309.05728) [[DOI](https://doi.org/10.1103/PhysRevD.109.L011702)] (2023)
    * [Attention to Mean-Fields for Particle Cloud Generation](https://arxiv.org/abs/2305.15254) (2023)
    * [Is infrared-collinear safe information all you need for jet classification?](https://arxiv.org/abs/2305.08979) [[DOI](https://doi.org/10.1007/JHEP07(2024)257)] (2023)
    * [Comparing Point Cloud Strategies for Collider Event Classification](https://arxiv.org/abs/2212.10659) [[DOI](https://doi.org/10.1103/PhysRevD.108.012001)] (2022)
    * [Point Cloud Generation using Transformer Encoders and Normalising Flows](https://arxiv.org/abs/2211.13623) (2022)
    * [Particle Transformer for Jet Tagging](https://arxiv.org/abs/2202.03772) (2022)
    * [Deep Sets based Neural Networks for Impact Parameter Flavour Tagging in ATLAS](https://cds.cern.ch/record/2718948) (2020)
    * [Particle Convolution for High Energy Physics](https://arxiv.org/abs/2107.02908) (2021)
    * [SPANet: Generalized Permutationless Set Assignment for Particle Physics using Symmetry Preserving Attention](https://arxiv.org/abs/2106.03898) [[DOI](https://doi.org/10.21468/SciPostPhys.12.5.178)] (2021)
    * [Point Cloud Transformers applied to Collider Physics](https://arxiv.org/abs/2102.05073) [[DOI](https://doi.org/10.1088/2632-2153/ac07f6)] (2021)
    * [Learning to Isolate Muons](https://arxiv.org/abs/2102.02278) [[DOI](https://doi.org/10.1007/JHEP10(2021)200)] (2021)
    * [Zero-Permutation Jet-Parton Assignment using a Self-Attention Network](https://arxiv.org/abs/2012.03542) [[DOI](https://doi.org/10.1007/s40042-024-01037-3)] (2020)
    * [Permutationless Many-Jet Event Reconstruction with Symmetry Preserving Attention Networks](https://arxiv.org/abs/2010.09206) [[DOI](https://doi.org/10.1103/PhysRevD.105.112008)] (2020)
    * [Equivariant Energy Flow Networks for Jet Tagging](https://arxiv.org/abs/2012.00964) [[DOI](https://doi.org/10.1103/PhysRevD.103.074022)] (2020)
    * [Secondary Vertex Finding in Jets with Neural Networks](https://arxiv.org/abs/2008.02831) [[DOI](https://doi.org/10.1140/epjc/s10052-021-09342-y)] (2020)
    * [ABCNet: An attention-based method for particle tagging](https://arxiv.org/abs/2001.05311) [[DOI](https://doi.org/10.1140/epjp/s13360-020-00497-3)] (2020)
    * [ParticleNet: Jet Tagging via Particle Clouds](https://arxiv.org/abs/1902.08570) [[DOI](https://doi.org/10.1103/PhysRevD.101.056019)] (2019)
    * [Energy Flow Networks: Deep Sets for Particle Jets](https://arxiv.org/abs/1810.05165) [[DOI](https://doi.org/10.1007/JHEP01(2019)121)] (2018)

    ####  Physics-inspired basis

    * [Advancing Physics Data Analysis through Machine Learning and Physics-Informed Neural Networks](https://arxiv.org/abs/2410.14760) (2024)
    * [Universal New Physics Latent Space](https://arxiv.org/abs/2407.20315) (2024)
    * [Physics-informed machine learning approaches to reactor antineutrino detection](https://arxiv.org/abs/2407.06139) (2024)
    * [Exotic and physics-informed support vector machines for high energy physics](https://arxiv.org/abs/2407.03538) (2024)
    * [Exploring the Truth and Beauty of Theory Landscapes with Machine Learning](https://arxiv.org/abs/2401.11513) [[DOI](https://doi.org/10.1016/j.physletb.2024.138941)] (2024)
    * [JetLOV: Enhancing Jet Tree Tagging through Neural Network Learning of Optimal LundNet Variables](https://arxiv.org/abs/2311.14654) (2023)
    * [Jet Rotational Metrics](https://arxiv.org/abs/2311.06686) [[DOI](https://doi.org/10.1007/JHEP08(2024)049)] (2023)
    * [Learning Broken Symmetries with Resimulation and Encouraged Invariance](https://arxiv.org/abs/2311.05952) (2023)
    * [Retrieval of Boost Invariant Symbolic Observables via Feature Importance](https://arxiv.org/abs/2306.13496) (2023)
    * [Jet SIFT-ing: a new scale-invariant jet clustering algorithm for the substructure era](https://arxiv.org/abs/2302.08609) [[DOI](https://doi.org/10.1103/PhysRevD.108.016005)] (2023)
    * [Decay-aware neural network for event classification in collider physics](https://arxiv.org/abs/2212.08759) (2022)
    * [Resurrecting $b\bar{b}h$ with kinematic shapes](https://arxiv.org/abs/2011.13945) [[DOI](https://doi.org/10.1007/JHEP04(2021)139)] (2020)
    * [Deep-learned Top Tagging with a Lorentz Layer](https://arxiv.org/abs/1707.08966) [[DOI](https://doi.org/10.21468/SciPostPhys.5.3.028)] (2017)
    * [Energy flow polynomials: A complete linear basis for jet substructure](https://arxiv.org/abs/1712.07124) [[DOI](https://doi.org/10.1007/JHEP04(2018)013)] (2017)
    * [Novel Jet Observables from Machine Learning](https://arxiv.org/abs/1710.01305) [[DOI](https://doi.org/10.1007/JHEP03(2018)086)] (2017)
    * [How Much Information is in a Jet?](https://arxiv.org/abs/1704.08249) [[DOI](https://doi.org/10.1007/JHEP06(2017)073)] (2017)
    * [Automating the Construction of Jet Observables with Machine Learning](https://arxiv.org/abs/1902.07180) [[DOI](https://doi.org/10.1103/PhysRevD.100.095016)] (2019)


??? example "Targets"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ### Targets
    </div>

    ####  $W/Z$ tagging

    * [Measurements of decay branching fractions of the Higgs boson to hadronic final states at the CEPC](https://arxiv.org/abs/2410.04465) (2024)
    * [Interplay of Traditional Methods and Machine Learning Algorithms for Tagging Boosted Objects](https://arxiv.org/abs/2408.01138) [[DOI](https://doi.org/10.1140/epjs/s11734-024-01256-6)] (2024)
    * [Explainable Equivariant Neural Networks for Particle Physics: PELICAN](https://arxiv.org/abs/2307.16506) [[DOI](https://doi.org/10.1007/JHEP03(2024)113)] (2023)
    * [Application of Machine Learning Based Top Quark and W Jet Tagging to Hadronic Four-Top Final States Induced by SM as well as BSM Processes](https://arxiv.org/abs/2310.13009) (2023)
    * [Amplitude-assisted tagging of longitudinally polarised bosons using wide neural networks](https://arxiv.org/abs/2306.07726) [[DOI](https://doi.org/10.1140/epjc/s10052-023-11931-y)] (2023)
    * [Is infrared-collinear safe information all you need for jet classification?](https://arxiv.org/abs/2305.08979) [[DOI](https://doi.org/10.1007/JHEP07(2024)257)] (2023)
    * [Gradient Boosting MUST taggers for highly-boosted jets](https://arxiv.org/abs/2305.04957) (2023)
    * [Role of polarizations and spin-spin correlations of W's in e-e+\textrightarrow{}W-W+ at s](https://arxiv.org/abs/2212.12973) [[DOI](https://doi.org/10.1103/PhysRevD.107.073004)] (2022)
    * [A $W^\pm$ polarization analyzer from Deep Neural Networks](https://arxiv.org/abs/2102.05124) (2021)
    * [Jet tagging in the Lund plane with graph networks](https://arxiv.org/abs/2012.08526) [[DOI](https://doi.org/10.1007/JHEP03(2021)052)] (2020)
    * [Supervised Jet Clustering with Graph Neural Networks for Lorentz Boosted Bosons](https://arxiv.org/abs/2008.06064) [[DOI](https://doi.org/10.1103/PhysRevD.102.075014)] (2020)
    * [Boosted $W$ and $Z$ tagging with jet charge and deep learning](https://arxiv.org/abs/1908.08256) [[DOI](https://doi.org/10.1103/PhysRevD.101.053001)] (2019)
    * [Identification of heavy, energetic, hadronically decaying particles using machine-learning techniques](https://arxiv.org/abs/2004.08262) [[DOI](https://doi.org/10.1088/1748-0221/15/06/P06005)] (2020)
    * [QCD-Aware Recursive Neural Networks for Jet Physics](https://arxiv.org/abs/1702.00748) [[DOI](https://doi.org/10.1007/JHEP01(2019)057)] (2017)
    * [Parton Shower Uncertainties in Jet Substructure Analyses with Deep Neural Networks](https://arxiv.org/abs/1609.00607) [[DOI](https://doi.org/10.1103/PhysRevD.95.014018)] (2016)
    * [Jet-images — deep learning edition](https://arxiv.org/abs/1511.05190) [[DOI](https://doi.org/10.1007/JHEP07(2016)069)] (2015)

    ####  $H\rightarrow b\bar{b}$

    * [Application of Particle Transformer to quark flavor tagging in the ILC project](https://arxiv.org/abs/2410.11322) (2024)
    * [Measurements of decay branching fractions of the Higgs boson to hadronic final states at the CEPC](https://arxiv.org/abs/2410.04465) (2024)
    * [Higgs tagging with the Lund jet plane](https://arxiv.org/abs/2105.03989) [[DOI](https://doi.org/10.1103/PhysRevD.104.055043)] (2021)
    * [Learning to increase matching efficiency in identifying additional b-jets in the $\text{t}\bar{\text{t}}\text{b}\bar{\text{b}}$ process](https://arxiv.org/abs/2103.09129) [[DOI](https://doi.org/10.1140/epjp/s13360-022-03024-8)] (2021)
    * [Extracting Signals of Higgs Boson From Background Noise Using Deep Neural Networks](https://arxiv.org/abs/2010.08201) (2020)
    * [The Boosted Higgs Jet Reconstruction via Graph Neural Network](https://arxiv.org/abs/2010.05464) [[DOI](https://doi.org/10.1103/PhysRevD.103.116025)] (2020)
    * [Benchmarking Machine Learning Techniques with Di-Higgs Production at the LHC](https://arxiv.org/abs/2009.06754) (2020)
    * [Disentangling Boosted Higgs Boson Production Modes with Machine Learning](https://arxiv.org/abs/2009.05930) [[DOI](https://doi.org/10.1088/1748-0221/16/07/P07002)] (2020)
    * [Identification of heavy, energetic, hadronically decaying particles using machine-learning techniques](https://arxiv.org/abs/2004.08262) [[DOI](https://doi.org/10.1088/1748-0221/15/06/P06005)] (2020)
    * [Interpretable deep learning for two-prong jet classification with jet spectra](https://arxiv.org/abs/1904.02092) [[DOI](https://doi.org/10.1007/JHEP07(2019)135)] (2019)
    * [Interaction networks for the identification of boosted $H \rightarrow b\overline{b}$ decays](https://arxiv.org/abs/1909.12285) [[DOI](https://doi.org/10.1103/PhysRevD.102.012010)] (2019)
    * [Boosting $H\to b\bar b$ with Machine Learning](https://arxiv.org/abs/1807.10768) [[DOI](https://doi.org/10.1007/JHEP10(2018)101)] (2018)
    * [Automating the Construction of Jet Observables with Machine Learning](https://arxiv.org/abs/1902.07180) [[DOI](https://doi.org/10.1103/PhysRevD.100.095016)] (2019)

    ####  quarks and gluons

    * [The Fundamental Limit of Jet Tagging](https://arxiv.org/abs/2411.02628) (2024)
    * [A Lorentz-Equivariant Transformer for All of the LHC](https://arxiv.org/abs/2411.00446) (2024)
    * [Application of Particle Transformer to quark flavor tagging in the ILC project](https://arxiv.org/abs/2410.11322) (2024)
    * [Jet Tagging with More-Interaction Particle Transformer](https://arxiv.org/abs/2407.08682) [[DOI](https://doi.org/10.1088/1674-1137/ad7f3d)] (2024)
    * [A multicategory jet image classification framework using deep neural network](https://arxiv.org/abs/2407.03524) (2024)
    * [Jet Flavour Tagging at FCC-ee with a Transformer-based Neural Network: DeepJetTransformer](https://arxiv.org/abs/2406.08590) (2024)
    * [Quark-versus-gluon tagging in CMS Open Data with CWoLa and TopicFlow](https://arxiv.org/abs/2312.03434) (2023)
    * [Hierarchical High-Point Energy Flow Network for Jet Tagging](https://arxiv.org/abs/2308.08300) [[DOI](https://doi.org/10.1007/JHEP09(2023)135)] (2023)
    * [Quark/Gluon Discrimination and Top Tagging with Dual Attention Transformer](https://arxiv.org/abs/2307.04723) [[DOI](https://doi.org/10.1140/epjc/s10052-023-12293-1)] (2023)
    * [Is infrared-collinear safe information all you need for jet classification?](https://arxiv.org/abs/2305.08979) [[DOI](https://doi.org/10.1007/JHEP07(2024)257)] (2023)
    * [Jet substructure observables for jet quenching in Quark Gluon Plasma: a Machine Learning driven analysis](https://arxiv.org/abs/2304.07196) [[DOI](https://doi.org/10.21468/SciPostPhys.16.1.015)] (2023)
    * [Systematic Quark/Gluon Identification with Ratios of Likelihoods](https://arxiv.org/abs/2207.12411) [[DOI](https://doi.org/10.1007/JHEP12(2022)021)] (2022)
    * [Quarks and gluons in the Lund plane](https://arxiv.org/abs/2112.09140) [[DOI](https://doi.org/10.1007/JHEP08(2022)177)] (2021)
    * [Identifying the Quantum Properties of Hadronic Resonances using Machine Learning](https://arxiv.org/abs/2105.04582) (2021)
    * [Safety of Quark/Gluon Jet Classification](https://arxiv.org/abs/2103.09103) (2021)
    * [Jet tagging in the Lund plane with graph networks](https://arxiv.org/abs/2012.08526) [[DOI](https://doi.org/10.1007/JHEP03(2021)052)] (2020)
    * [Quark-Gluon Jet Discrimination Using Convolutional Neural Networks](https://arxiv.org/abs/2012.02531) [[DOI](https://doi.org/10.3938/jkps.74.219)] (2020)
    * [Quark Gluon Jet Discrimination with Weakly Supervised Learning](https://arxiv.org/abs/2012.02540) [[DOI](https://doi.org/10.3938/jkps.75.652)] (2020)
    * [Towards Machine Learning Analytics for Jet Substructure](https://arxiv.org/abs/2007.04319) [[DOI](https://doi.org/10.1007/JHEP09(2020)195)] (2020)
    * [Quark-Gluon Tagging: Machine Learning vs Detector](https://arxiv.org/abs/1812.09223) [[DOI](https://doi.org/10.21468/SciPostPhys.6.6.069)] (2018)
    * [JEDI-net: a jet identification algorithm based on interaction networks](https://arxiv.org/abs/1908.05318) [[DOI](https://doi.org/10.1140/epjc/s10052-020-7608-4)] (2019)
    * [Probing heavy ion collisions using quark and gluon jet substructure](https://arxiv.org/abs/1803.03589) (2018)
    * [DeepJet: Generic physics object based jet multiclass classification for LHC experiments](https://dl4physicalsciences.github.io/files/nips_dlps_2017_10.pdf) (2017)
    * [Recursive Neural Networks in Quark/Gluon Tagging](https://arxiv.org/abs/1711.02633) [[DOI](https://doi.org/10.1007/s41781-018-0007-y)] (2017)
    * [Deep learning in color: towards automated quark/gluon](https://arxiv.org/abs/1612.01551) [[DOI](https://doi.org/10.1007/JHEP01(2017)110)] (2016)
    * [Quark versus Gluon Jet Tagging Using Jet Images with the ATLAS Detector](http://cds.cern.ch/record/2275641) (2017)

    ####  top quark tagging

    * [A Lorentz-Equivariant Transformer for All of the LHC](https://arxiv.org/abs/2411.00446) (2024)
    * [Systematic Interpretability and the Likelihood for Boosted Top Quark Identification](https://arxiv.org/abs/2411.00104) (2024)
    * [Application of Machine Learning Based Top Quark and W Jet Tagging to Hadronic Four-Top Final States Induced by SM and BSM Processes](https://arxiv.org/abs/2410.13904) (2024)
    * [Unveiling the Secrets of New Physics Through Top Quark Tagging](https://arxiv.org/abs/2409.12085) (2024)
    * [Hadronic Top Quark Polarimetry with ParticleNet](https://arxiv.org/abs/2407.01663) (2024)
    * [The Phase Space Distance Between Collider Events](https://arxiv.org/abs/2405.16698) [[DOI](https://doi.org/10.1007/JHEP09(2024)054)] (2024)
    * [Interpretable deep learning models for the inference and classification of LHC data](https://arxiv.org/abs/2312.12330) [[DOI](https://doi.org/10.1007/JHEP05(2024)004)] (2023)
    * [Jet Classification Using High-Level Features from Anatomy of Top Jets](https://arxiv.org/abs/2312.11760) [[DOI](https://doi.org/10.1007/JHEP07(2024)146)] (2023)
    * [Scaling Laws in Jet Classification](https://arxiv.org/abs/2312.02264) (2023)
    * [Efficient and Robust Jet Tagging at the LHC with Knowledge Distillation](https://arxiv.org/abs/2311.14160) (2023)
    * [19 Parameters Is All You Need: Tiny Neural Networks for Particle Physics](https://arxiv.org/abs/2310.16121) (2023)
    * [Application of Machine Learning Based Top Quark and W Jet Tagging to Hadronic Four-Top Final States Induced by SM as well as BSM Processes](https://arxiv.org/abs/2310.13009) (2023)
    * [ML-Based Top Taggers: Performance, Uncertainty and Impact of Tower \& Tracker Data Integration](https://arxiv.org/abs/2309.01568) (2023)
    * [Investigating the Violation of Charge-parity Symmetry Through Top-quark ChromoElectric Dipole Moments by Using Machine Learning Techniques](https://arxiv.org/abs/2306.11683) [[DOI](https://doi.org/10.5506/APhysPolB.54.5-A4)] (2023)
    * [Hierarchical High-Point Energy Flow Network for Jet Tagging](https://arxiv.org/abs/2308.08300) [[DOI](https://doi.org/10.1007/JHEP09(2023)135)] (2023)
    * [Explainable Equivariant Neural Networks for Particle Physics: PELICAN](https://arxiv.org/abs/2307.16506) [[DOI](https://doi.org/10.1007/JHEP03(2024)113)] (2023)
    * [Quark/Gluon Discrimination and Top Tagging with Dual Attention Transformer](https://arxiv.org/abs/2307.04723) [[DOI](https://doi.org/10.1140/epjc/s10052-023-12293-1)] (2023)
    * [Machine Learning in Top Physics in the ATLAS and CMS Collaborations](https://arxiv.org/abs/2301.09534) (2023)
    * [Automatic detection of boosted Higgs and top quark jets in event image](https://arxiv.org/abs/2302.13460) [[DOI](https://doi.org/10.1103/PhysRevD.108.116002)] (2023)
    * [Boosted top tagging and its interpretation using Shapley values](https://arxiv.org/abs/2212.11606) (2022)
    * [BIP: Boost Invariant Polynomials for Efficient Jet Tagging](https://arxiv.org/abs/2207.08272) [[DOI](https://doi.org/10.1088/2632-2153/aca9ca)] (2022)
    * [Application of deep learning in top pair and single top quark production at the LHC](https://arxiv.org/abs/2203.12871) [[DOI](https://doi.org/10.1140/epjp/s13360-023-04409-z)] (2022)
    * [Leveraging universality of jet taggers through transfer learning](https://arxiv.org/abs/2203.06210) [[DOI](https://doi.org/10.1140/epjc/s10052-022-10469-9)] (2022)
    * [End-to-End Jet Classification of Boosted Top Quarks with the CMS Open Data](https://arxiv.org/abs/2104.14659) [[DOI](https://doi.org/10.1051/epjconf/202125104030)] (2021)
    * [Pulling the Higgs and Top needles from the jet stack with Feature Extended Supervised Tagging](https://arxiv.org/abs/2102.01667) [[DOI](https://doi.org/10.1140/epjc/s10052-021-09530-w)] (2021)
    * [Jet tagging in the Lund plane with graph networks](https://arxiv.org/abs/2012.08526) [[DOI](https://doi.org/10.1007/JHEP03(2021)052)] (2020)
    * [Morphology for Jet Classification](https://arxiv.org/abs/2010.13469) [[DOI](https://doi.org/10.1103/PhysRevD.105.014004)] (2020)
    * [Boosted Top Quark Tagging and Polarization Measurement using Machine Learning](https://arxiv.org/abs/2010.11778) [[DOI](https://doi.org/10.1103/PhysRevD.105.042005)] (2020)
    * [Pulling Out All the Tops with Computer Vision and Deep Learning](https://arxiv.org/abs/1803.00107) [[DOI](https://doi.org/10.1007/JHEP10(2018)121)] (2018)
    * [Deep-learning Top Taggers or The End of QCD?](https://arxiv.org/abs/1701.08784) [[DOI](https://doi.org/10.1007/JHEP05(2017)006)] (2017)
    * [Deep-learned Top Tagging with a Lorentz Layer](https://arxiv.org/abs/1707.08966) [[DOI](https://doi.org/10.21468/SciPostPhys.5.3.028)] (2017)
    * [CapsNets Continuing the Convolutional Quest](https://arxiv.org/abs/1906.11265) [[DOI](https://doi.org/10.21468/SciPostPhys.8.2.023)] (2019)
    * [Neural Network-based Top Tagger with Two-Point Energy Correlations and Geometry of Soft Emissions](https://arxiv.org/abs/2003.11787) [[DOI](https://doi.org/10.1007/JHEP07(2020)111)] (2020)
    * [The Machine Learning Landscape of Top Taggers](https://arxiv.org/abs/1902.09914) [[DOI](https://doi.org/10.21468/SciPostPhys.7.1.014)] (2019)
    * [DeepJet: Generic physics object based jet multiclass classification for LHC experiments](https://dl4physicalsciences.github.io/files/nips_dlps_2017_10.pdf) (2017)
    * [Playing Tag with ANN: Boosted Top Identification with Pattern Recognition](https://arxiv.org/abs/1501.05968) [[DOI](https://doi.org/10.1007/JHEP07(2015)086)] (2015)

    ####  strange jets

    * [New Physics Through Flavor Tagging at FCC-ee](https://arxiv.org/abs/2411.02485) (2024)
    * [Application of Particle Transformer to quark flavor tagging in the ILC project](https://arxiv.org/abs/2410.11322) (2024)
    * [From strange-quark tagging to fragmentation tagging with machine learning](https://arxiv.org/abs/2408.12377) (2024)
    * [Study of anomalous $W^-W^+\gamma/Z$ couplings using polarizations and spin correlations in $e^-e^+\to W^-W^+$ with polarized beams](https://arxiv.org/abs/2305.15106) [[DOI](https://doi.org/10.1140/epjc/s10052-023-12292-2)] (2023)
    * [Maximum performance of strange-jet tagging at hadron colliders](https://arxiv.org/abs/2011.10736) [[DOI](https://doi.org/10.1088/1748-0221/16/08/P08039)] (2020)
    * [A tagger for strange jets based on tracking information using long short-term memory](https://arxiv.org/abs/1907.07505) [[DOI](https://doi.org/10.1088/1748-0221/15/01/P01021)] (2019)
    * [Strange Jet Tagging](https://arxiv.org/abs/2003.09517) (2020)

    ####  $b$-tagging

    * [Exploring jets: substructure and flavour tagging in CMS and ATLAS](https://arxiv.org/abs/2410.14330) (2024)
    * [DNN-based identification of additional b jets for a differential $t\bar{t}b\bar{b}$ cross section measurement](https://arxiv.org/abs/2401.07626) (2024)
    * [Vertex Reconstruction with MaskFormers](https://arxiv.org/abs/2312.12272) [[DOI](https://doi.org/10.1140/epjc/s10052-024-13374-5)] (2023)
    * [Neural networks for boosted di-$\tau$ identification](https://arxiv.org/abs/2312.08276) [[DOI](https://doi.org/10.1088/1748-0221/19/07/P07004)] (2023)
    * [Fast $b$-tagging at the high-level trigger of the ATLAS experiment in LHC Run 3](https://arxiv.org/abs/2306.09738) [[DOI](https://doi.org/10.1088/1748-0221/18/11/P11006)] (2023)
    * [Improving robustness of jet tagging algorithms with adversarial training: exploring the loss surface](https://arxiv.org/abs/2303.14511) (2023)
    * [Performance studies of jet flavor tagging and measurement of $R_b$ using ParticleNet at CEPC](https://arxiv.org/abs/2208.13503) [[DOI](https://doi.org/10.1142/S0217751X23501683)] (2022)
    * [Deep Sets based Neural Networks for Impact Parameter Flavour Tagging in ATLAS](https://cds.cern.ch/record/2718948) (2020)
    * [Identification of Jets Containing $b$-Hadrons with Recurrent Neural Networks at the ATLAS Experiment](http://cdsweb.cern.ch/record/2255226) (2017)
    * [Jet Flavour Classification Using DeepJet](https://arxiv.org/abs/2008.10519) [[DOI](https://doi.org/10.1088/1748-0221/15/12/P12012)] (2020)
    * [Identifying Heavy-Flavor Jets Using Vectors of Locally Aggregated Descriptors](https://arxiv.org/abs/2005.01842) [[DOI](https://doi.org/10.1088/1748-0221/16/03/P03017)] (2020)
    * [The Full Event Interpretation}: {An Exclusive Tagging Algorithm for the Belle II Experiment](https://arxiv.org/abs/1807.08680) [[DOI](https://doi.org/10.1007/s41781-019-0021-8)] (2018)
    * [Jet Flavor Classification in High-Energy Physics with Deep Neural Networks](https://arxiv.org/abs/1607.08633) [[DOI](https://doi.org/10.1103/PhysRevD.94.112002)] (2016)
    * [Identification of heavy-flavour jets with the CMS detector in pp collisions at 13 TeV](https://arxiv.org/abs/1712.07158) [[DOI](https://doi.org/10.1088/1748-0221/13/05/P05011)] (2017)

    ####  Flavor physics

    * [Reinforcement learning-based statistical search strategy for an axion model from flavor](https://arxiv.org/abs/2409.10023) (2024)
    * [Holographic complex potential of a quarkonium from deep learning](https://arxiv.org/abs/2406.06285) (2024)
    * [Exploring Transport Properties of Quark-Gluon Plasma with a Machine-Learning assisted Holographic Approach](https://arxiv.org/abs/2404.18217) (2024)
    * [Meson mass and width: Deep learning approach](https://arxiv.org/abs/2404.00448) [[DOI](https://doi.org/10.1103/PhysRevD.110.054011)] (2024)
    * [A Deep Learning Framework for Disentangling Triangle Singularity and Pole-Based Enhancements](https://arxiv.org/abs/2403.18265) (2024)
    * [Heavy quarkonium spectral function in an anisotropic background](https://arxiv.org/abs/2403.04966) [[DOI](https://doi.org/10.1103/PhysRevD.109.086010)] (2024)
    * [Cluster Counting Algorithm for the CEPC Drift Chamber using LSTM and DGCNN](https://arxiv.org/abs/2402.16493) (2024)
    * [Differentiable Vertex Fitting for Jet Flavour Tagging](https://arxiv.org/abs/2310.12804) [[DOI](https://doi.org/10.1103/PhysRevD.110.052010)] (2023)
    * [Exploring the flavor structure of quarks and leptons with reinforcement learning](https://arxiv.org/abs/2304.14176) [[DOI](https://doi.org/10.1007/JHEP12(2023)021)] (2023)
    * [Revealing the nature of hidden charm pentaquarks with machine learning](https://arxiv.org/abs/2301.05364) [[DOI](https://doi.org/10.1016/j.scib.2023.04.018)] (2023)
    * [Predicting Exotic Hadron Masses with Data Augmentation Using Multilayer Perceptron](https://arxiv.org/abs/2208.09538) [[DOI](https://doi.org/10.1142/S0217751X23500033)] (2022)
    * ['Deep' Dive into $b \to c$ Anomalies: Standardized and Future-proof Model Selection Using Self-normalizing Neural Networks](https://arxiv.org/abs/2008.04316) (2020)

    ####  BSM particles and models

    * [Pseudo-observables and Deep Neural Network for mixed CP -- H to tau tau decays at LHC](https://arxiv.org/abs/2411.06216) (2024)
    * [Improving smuon searches with Neural Networks](https://arxiv.org/abs/2411.04526) (2024)
    * [Machine-Learning Analysis of Radiative Decays to Dark Matter at the LHC](https://arxiv.org/abs/2410.13799) (2024)
    * [Machine learning tagged boosted dark photon: A signature of fermionic portal matter at the LHC](https://arxiv.org/abs/2410.06925) (2024)
    * [Multiple testing for signal-agnostic searches of new physics with machine learning](https://arxiv.org/abs/2408.12296) (2024)
    * [Graph Reinforcement Learning for Exploring BSM Model Spaces](https://arxiv.org/abs/2407.07203) (2024)
    * [Learning to see R-parity violating scalar top decays](https://arxiv.org/abs/2406.03096) [[DOI](https://doi.org/10.1103/PhysRevD.110.056006)] (2024)
    * [Boosting probes of CP violation in the top Yukawa coupling with Deep Learning](https://arxiv.org/abs/2405.16499) (2024)
    * [Leptoquark Searches at TeV Scale Using Neural Networks at Hadron Collider](https://arxiv.org/abs/2405.08090) (2024)
    * [Reconstruction of Short-Lived Particles using Graph-Hypergraph Representation Learning](https://arxiv.org/abs/2402.10149) (2024)
    * [Deep Learning to Improve the Sensitivity of Di-Higgs Searches in the $4b$ Channel](https://arxiv.org/abs/2401.14198) [[DOI](https://doi.org/10.1007/JHEP09(2024)139)] (2024)
    * [Machine Learning for Prediction of Unitarity and Bounded from Below Constraints](https://arxiv.org/abs/2401.09130) [[DOI](https://doi.org/10.22323/1.449.0494)] (2024)
    * [Analysis of the $gg\to H\to hh\to4\tau$ process in the 2HDM lepton specific model at the LHC](https://arxiv.org/abs/2401.07289) (2024)
    * [Search for Long-lived Particles at Future Lepton Colliders Using Deep Learning Techniques](https://arxiv.org/abs/2401.05094) (2024)
    * [Multi-scale cross-attention transformer encoder for event classification](https://arxiv.org/abs/2401.00452) [[DOI](https://doi.org/10.1007/JHEP03(2024)144)] (2024)
    * [Quantum Metric Learning for New Physics Searches at the LHC](https://arxiv.org/abs/2311.16866) (2023)
    * [Optimize the event selection strategy the study the anomalous quartic gauge couplings at muon colliders using the support vector machine](https://arxiv.org/abs/2311.15280) [[DOI](https://doi.org/10.1140/epjc/s10052-024-13208-4)] (2023)
    * [Probing Light Fermiophobic Higgs Boson via diphoton jets at the HL-LHC](https://arxiv.org/abs/2310.17741) [[DOI](https://doi.org/10.1103/PhysRevD.109.015017)] (2023)
    * [Machine Learning Classification of Sphalerons and Black Holes at the LHC](https://arxiv.org/abs/2310.15227) [[DOI](https://doi.org/10.1140/epjc/s10052-024-12790-x)] (2023)
    * [LLPNet: Graph Autoencoder for Triggering Light Long-Lived Particles at HL-LHC](https://arxiv.org/abs/2308.13611) (2023)
    * [Improving sensitivity of trilinear RPV SUSY searches using machine learning at the LHC](https://arxiv.org/abs/2308.02697) [[DOI](https://doi.org/10.1103/PhysRevD.109.035001)] (2023)
    * [Sharpening the $A\to Z^{(*)}h $ Signature of the Type-II 2HDM at the LHC through Advanced Machine Learning](https://arxiv.org/abs/2305.13781) [[DOI](https://doi.org/10.1007/JHEP11(2023)020)] (2023)
    * [Leveraging on-shell interference to search for FCNCs of the top quark and the Z boson](https://arxiv.org/abs/2305.12172) [[DOI](https://doi.org/10.1140/epjc/s10052-023-11982-1)] (2023)
    * [Gradient Boosting MUST taggers for highly-boosted jets](https://arxiv.org/abs/2305.04957) (2023)
    * [Searching for dark jets with displaced vertices using weakly supervised machine learning](https://arxiv.org/abs/2305.04372) [[DOI](https://doi.org/10.1103/PhysRevD.108.035036)] (2023)
    * [Uncovering doubly charged scalars with dominant three-body decays using machine learning](https://arxiv.org/abs/2304.09195) [[DOI](https://doi.org/10.1007/JHEP11(2023)009)] (2023)
    * [Probing Dark QCD Sector through the Higgs Portal with Machine Learning at the LHC](https://arxiv.org/abs/2304.03237) [[DOI](https://doi.org/10.1007/JHEP08(2023)187)] (2023)
    * [Search for vector-like leptons at a Muon Collider](https://arxiv.org/abs/2304.01885) [[DOI](https://doi.org/10.1088/1674-1137/ace5a7)] (2023)
    * [Searching for anomalous quartic gauge couplings at muon colliders using principle component analysis](https://arxiv.org/abs/2304.01505) [[DOI](https://doi.org/10.1140/epjc/s10052-023-11719-0)] (2023)
    * [Invariant mass reconstruction of heavy gauge bosons decaying to $\tau$ leptons using machine learning techniques](https://arxiv.org/abs/2304.01126) [[DOI](https://doi.org/10.1140/epjc/s10052-024-12527-w)] (2023)
    * [Optimal Mass Variables for Semivisible Jets](https://arxiv.org/abs/2303.16253) [[DOI](https://doi.org/10.21468/SciPostPhysCore.6.4.067)] (2023)
    * [Probing Heavy Neutrinos at the LHC from Fat-jet using Machine Learning](https://arxiv.org/abs/2303.15920) (2023)
    * [Probing Electroweak Phase Transition in Singlet scalar extension of Standard Model at HL-LHC through $bbZZ$ channel using parameterized machine learning](https://arxiv.org/abs/2302.04191) [[DOI](https://doi.org/10.1088/1361-6471/ad4fab)] (2023)
    * [Search for a new scalar resonance in flavour-changing neutral-current top-quark decays $t \rightarrow qX$ ($q](https://arxiv.org/abs/2301.03902) [[DOI](https://doi.org/10.1007/JHEP07(2023)199)] (2023)
    * [Search for Electroweak Production of Supersymmetric Particles in Compressed Mass Spectra With the ATLAS Detector at the LHC](https://arxiv.org/abs/2211.11642) (2022)
    * [Search for supersymmetry in final states with a single electron or muon using angular correlations and heavy-object identification in proton-proton collisions at $\sqrt{s}$](https://arxiv.org/abs/2211.08476) [[DOI](https://doi.org/10.1007/JHEP09(2023)149)] (2022)
    * [Search for supersymmetry in final states with missing transverse momentum and three or more b-jets in 139 fb$^{-1}$ of proton\textendash{}proton collisions at $\sqrt{s}](https://arxiv.org/abs/2211.08028) [[DOI](https://doi.org/10.1140/epjc/s10052-023-11543-6)] (2022)
    * [Searching for exotic Higgs bosons from top quark decays at the HL-LHC](https://arxiv.org/abs/2212.09061) [[DOI](https://doi.org/10.1140/epjc/s10052-024-13274-8)] (2022)
    * [Machine learning-enhanced search for a vectorlike-singlet $\mathbf B$ quark decaying to a singlet scalar or pseudoscalar](https://arxiv.org/abs/2212.02442) [[DOI](https://doi.org/10.1103/PhysRevD.107.115001)] (2022)
    * [Associated production of Higgs and single top at the LHC in presence of the SMEFT operators](https://arxiv.org/abs/2211.05450) [[DOI](https://doi.org/10.1007/JHEP08(2023)015)] (2022)
    * [Learning to Identify Semi-Visible Jets](https://arxiv.org/abs/2208.10062) [[DOI](https://doi.org/10.1007/JHEP12(2022)132)] (2022)
    * [Machine-enhanced CP-asymmetries in the electroweak sector](https://arxiv.org/abs/2209.05143) [[DOI](https://doi.org/10.1103/PhysRevD.107.016008)] (2022)
    * [VBF vs. GGF Higgs with Full-Event Deep Learning: Towards a Decay-Agnostic Tagger](https://arxiv.org/abs/2209.05518) [[DOI](https://doi.org/10.1103/PhysRevD.107.016014)] (2022)
    * [Probing a $\mathrm{Z}^{\prime}$ with non-universal fermion couplings through top quark fusion, decays to bottom quarks, and machine learning techniques](https://arxiv.org/abs/2210.15813) [[DOI](https://doi.org/10.1140/epjc/s10052-023-11506-x)] (2022)
    * [Machine learning the trilinear and light-quark Yukawa couplings from Higgs pair kinematic shapes](https://arxiv.org/abs/2207.04157) [[DOI](https://doi.org/10.1007/JHEP11(2022)045)] (2022)
    * [Measuring the anomalous quartic gauge couplings in the $W^+W^-\to W^+W^-$ process at muon collider using artificial neural networks](https://arxiv.org/abs/2204.10034) [[DOI](https://doi.org/10.1007/JHEP09(2022)074)] (2022)
    * [Probing highly collimated photon-jets with deep learning](https://arxiv.org/abs/2203.16703) [[DOI](https://doi.org/10.1088/1742-6596/2438/1/012114)] (2022)
    * [Deep Learning Jet Image as a Probe of Light Higgsino Dark Matter at the LHC](https://arxiv.org/abs/2203.14569) [[DOI](https://doi.org/10.1103/PhysRevD.106.055008)] (2022)
    * [Active learning BSM parameter spaces](https://arxiv.org/abs/2204.13950) [[DOI](https://doi.org/10.1140/epjc/s10052-023-11368-3)] (2022)
    * [Phenomenology at the Large Hadron Collider with Deep Learning: the case of vector-like quarks decaying to light jets](https://arxiv.org/abs/2204.12542) [[DOI](https://doi.org/10.1140/epjc/s10052-022-10799-8)] (2022)
    * [Solving Combinatorial Problems at Particle Colliders Using Machine Learning](https://arxiv.org/abs/2201.02205) [[DOI](https://doi.org/10.1103/PhysRevD.106.016001)] (2022)
    * [Influence of QCD parton shower in deep learning invisible Higgs through vector boson fusion](https://arxiv.org/abs/2201.01040) [[DOI](https://doi.org/10.1103/PhysRevD.105.113003)] (2022)
    * [Improving heavy Dirac neutrino prospects at future hadron colliders using machine learning](https://arxiv.org/abs/2112.15312) [[DOI](https://doi.org/10.1007/JHEP09(2022)141)] (2021)
    * [Event-level variables for semivisible jets using anomalous jet tagging](https://arxiv.org/abs/2111.12156) (2021)
    * [How to use Machine Learning to improve the discrimination between signal and background at particle colliders](https://arxiv.org/abs/2110.15099) [[DOI](https://doi.org/10.3390/app112211076)] (2021)
    * [Boosted decision trees in the era of new physics: a smuon analysis case study](https://arxiv.org/abs/2109.11815) [[DOI](https://doi.org/10.1007/JHEP04(2022)015)] (2021)
    * [Machine Learning Optimized Search for the $Z'$ from $U(1)_{L_\mu-L_\tau}$ at the LHC](https://arxiv.org/abs/2109.07674) (2021)
    * [Probing Higgs exotic decay at the LHC with machine learning](https://arxiv.org/abs/2109.03294) [[DOI](https://doi.org/10.1103/PhysRevD.105.035008)] (2021)
    * [Deep Learning Searches for Vector-Like Leptons at the LHC and Electron/Muon Colliders](https://arxiv.org/abs/2108.03926) [[DOI](https://doi.org/10.1140/epjc/s10052-023-11314-3)] (2021)
    * [Beyond Cuts in Small Signal Scenarios - Enhanced Sneutrino Detectability Using Machine Learning](https://arxiv.org/abs/2108.03125) [[DOI](https://doi.org/10.1140/epjc/s10052-023-11532-9)] (2021)
    * [Extract the energy scale of anomalous $\gamma\gamma \to W^+W^-$ scattering in the vector boson scattering process using artificial neural networks](https://arxiv.org/abs/2107.13624) [[DOI](https://doi.org/10.1007/JHEP09(2021)085)] (2021)
    * [Unsupervised Hadronic SUEP at the LHC](https://arxiv.org/abs/2107.12379) [[DOI](https://doi.org/10.1007/JHEP12(2021)129)] (2021)
    * [Detecting an axion-like particle with machine learning at the LHC](https://arxiv.org/abs/2106.07018) [[DOI](https://doi.org/10.1007/JHEP11(2021)138)] (2021)
    * [Top squark signal significance enhancement by different Machine Learning Algorithms](https://arxiv.org/abs/2106.06813) [[DOI](https://doi.org/10.1142/S0217751X22501974)] (2021)
    * [Towards a method to anticipate dark matter signals with deep learning at the LHC](https://arxiv.org/abs/2105.12018) [[DOI](https://doi.org/10.21468/SciPostPhys.12.2.063)] (2021)
    * [Advanced Multi-Variate Analysis Methods for New Physics Searches at the Large Hadron Collider](https://arxiv.org/abs/2105.07530) [[DOI](https://doi.org/10.1016/j.revip.2021.100063)] (2021)
    * [Exploring the standard model EFT in VH production with machine learning](https://arxiv.org/abs/1902.05803) [[DOI](https://doi.org/10.1103/PhysRevD.100.035040)] (2019)
    * [WIMPs or else? Using Machine Learning to disentangle LHC signatures](https://arxiv.org/abs/1910.06058) [[DOI](https://doi.org/10.21468/SciPostPhys.10.6.151)] (2019)
    * [Phenomenology of vector-like leptons with Deep Learning at the Large Hadron Collider](https://arxiv.org/abs/2010.01307) [[DOI](https://doi.org/10.1007/JHEP01(2021)076)] (2020)
    * [Sensing Higgs cascade decays through memory](https://arxiv.org/abs/2008.08611) [[DOI](https://doi.org/10.1103/PhysRevD.102.095027)] (2020)
    * [Invisible Higgs search through Vector Boson Fusion: A deep learning approach](https://arxiv.org/abs/2008.05434) [[DOI](https://doi.org/10.1140/epjc/s10052-020-08629-w)] (2020)
    * [Comparing Traditional and Deep-Learning Techniques of Kinematic Reconstruction for polarisation Discrimination in Vector Boson Scattering](https://arxiv.org/abs/2008.05316) [[DOI](https://doi.org/10.1140/epjc/s10052-020-08713-1)] (2020)
    * [Deep learnig analysis of the inverse seesaw in a 3-3-1 model at the LHC](https://arxiv.org/abs/2008.03409) [[DOI](https://doi.org/10.1016/j.physletb.2020.135931)] (2020)
    * [Distinguishing $W'$ Signals at Hadron Colliders Using Neural Networks](https://arxiv.org/abs/2007.14586) [[DOI](https://doi.org/10.1103/PhysRevD.103.036016)] (2020)
    * [Casting a graph net to catch dark showers](https://arxiv.org/abs/2006.08639) [[DOI](https://doi.org/10.21468/SciPostPhys.10.2.046)] (2020)
    * [Fast convolutional neural networks for identifying long-lived particles in a high-granularity calorimeter](https://arxiv.org/abs/2004.10744) [[DOI](https://doi.org/10.1088/1748-0221/15/12/P12006)] (2020)
    * [A deep neural network to search for new long-lived particles decaying to jets](https://arxiv.org/abs/1912.12238) [[DOI](https://doi.org/10.1088/2632-2153/ab9023)] (2019)
    * [Interpretable deep learning for two-prong jet classification with jet spectra](https://arxiv.org/abs/1904.02092) [[DOI](https://doi.org/10.1007/JHEP07(2019)135)] (2019)
    * [Searching for Exotic Particles in High-Energy Physics with Deep Learning](https://arxiv.org/abs/1402.4735) [[DOI](https://doi.org/10.1038/ncomms5308)] (2014)
    * [Automating the Construction of Jet Observables with Machine Learning](https://arxiv.org/abs/1902.07180) [[DOI](https://doi.org/10.1103/PhysRevD.100.095016)] (2019)

    ####  Particle identification

    * [Transformers for Charged Particle Track Reconstruction in High Energy Physics](https://arxiv.org/abs/2411.07149) (2024)
    * [Detecting highly collimated photon-jets from Higgs boson exotic decays with deep learning](https://arxiv.org/abs/2401.15690) (2024)
    * [Machine-learning-based particle identification with missing data](https://arxiv.org/abs/2401.01905) [[DOI](https://doi.org/10.1140/epjc/s10052-024-13047-3)] (2024)
    * [Study of residual artificial neural network for particle identification in the CEPC high-granularity calorimeter prototype](https://arxiv.org/abs/2310.09489) [[DOI](https://doi.org/10.1088/1748-0221/19/04/P04033)] (2023)
    * [Particle identification with machine learning in ALICE Run 3](https://arxiv.org/abs/2309.07768) [[DOI](https://doi.org/10.1051/epjconf/202429509029)] (2023)
    * [Improved calorimetric particle identification in NA62 using machine learning techniques](https://arxiv.org/abs/2304.10580) [[DOI](https://doi.org/10.1007/JHEP11(2023)138)] (2023)
    * [Particle identification with the Belle II calorimeter using machine learning](https://arxiv.org/abs/2301.11654) [[DOI](https://doi.org/10.1088/1742-6596/2438/1/012111)] (2023)
    * [Identification of light leptons and pions in the electromagnetic calorimeter of Belle II](https://arxiv.org/abs/2301.05074) [[DOI](https://doi.org/10.1016/j.nima.2023.168630)] (2023)
    * [Particle-flow based tau identification at future $\textrm{e}^{+}\textrm{e}^{-}$ colliders](https://arxiv.org/abs/2307.07747) [[DOI](https://doi.org/10.1016/j.cpc.2024.109095)] (2023)
    * [Inclusive, prompt and non-prompt $\rm{J}/\psi$ identification in proton-proton collisions at the Large Hadron Collider using machine learning](https://arxiv.org/abs/2308.00329) [[DOI](https://doi.org/10.1103/PhysRevD.109.014005)] (2023)
    * [Machine learning method for $^{12}$C event classification and reconstruction in the active target time-projection chamber](https://arxiv.org/abs/2304.13233) [[DOI](https://doi.org/10.1016/j.nima.2023.168528)] (2023)
    * [Separation of electrons from pions in GEM TRD using deep learning](https://arxiv.org/abs/2303.10776) (2023)
    * [Robust Neural Particle Identification Models](https://arxiv.org/abs/2212.07274) [[DOI](https://doi.org/10.1088/1742-6596/2438/1/012119)] (2022)
    * [Using Artificial Intelligence in the Reconstruction of Signals from the PADME Electromagnetic Calorimeter](https://arxiv.org/abs/2210.00811) [[DOI](https://doi.org/10.3390/instruments6040046)] (2022)
    * [Artificial Intelligence for Imaging Cherenkov Detectors at the EIC](https://arxiv.org/abs/2204.08645) [[DOI](https://doi.org/10.1088/1748-0221/17/07/C07011)] (2022)
    * [Using Machine Learning for Particle Identification in ALICE](https://arxiv.org/abs/2204.06900) [[DOI](https://doi.org/10.1088/1748-0221/17/07/C07016)] (2022)
    * [A Neural-Network-defined Gaussian Mixture Model for particle identification applied to the LHCb fixed-target programme](https://arxiv.org/abs/2110.10259) [[DOI](https://doi.org/10.1088/1748-0221/17/02/P02018)] (2021)
    * [Shower Identification in Calorimeter using Deep Learning](https://arxiv.org/abs/2103.16247) (2021)
    * [Learning to Identify Electrons](https://arxiv.org/abs/2011.01984) [[DOI](https://doi.org/10.1103/PhysRevD.103.116028)] (2020)
    * [Learning representations of irregular particle-detector geometry with distance-weighted graph networks](https://arxiv.org/abs/1902.07987) [[DOI](https://doi.org/10.1140/epjc/s10052-019-7113-9)] (2019)
    * [Calorimetry with Deep Learning: Particle Simulation and Reconstruction for Collider Physics](https://arxiv.org/abs/1912.06794) [[DOI](https://doi.org/10.1140/epjc/s10052-020-8251-9)] (2019)
    * [The Full Event Interpretation}: {An Exclusive Tagging Algorithm for the Belle II Experiment](https://arxiv.org/abs/1807.08680) [[DOI](https://doi.org/10.1007/s41781-019-0021-8)] (2018)
    * [Calorimetry with Deep Learning: Particle Classification, Energy Regression, and Simulation for High-Energy Physics](https://dl4physicalsciences.github.io/files/nips_dlps_2017_15.pdf) (2017)
    * [Survey of Machine Learning Techniques for High Energy Electromagnetic Shower Classification](https://dl4physicalsciences.github.io/files/nips_dlps_2017_24.pdf) (2017)
    * [Electromagnetic Showers Beyond Shower Shapes](https://arxiv.org/abs/1806.05667) [[DOI](https://doi.org/10.1016/j.nima.2019.162879)] (2018)

    ####  Neutrino Detectors

    * [Machine Learning-Powered Data Cleaning for LEGEND](https://arxiv.org/abs/2410.14701) (2024)
    * [Learning Efficient Representations of Neutrino Telescope Events](https://arxiv.org/abs/2410.13148) (2024)
    * [Real-time Position Reconstruction for the KamLAND-Zen Experiment using Hardware-AI Co-design](https://arxiv.org/abs/2410.02991) (2024)
    * [Enhancing Events in Neutrino Telescopes through Deep Learning-Driven Super-Resolution](https://arxiv.org/abs/2408.08474) (2024)
    * [Improving Neutrino Energy Reconstruction with Machine Learning](https://arxiv.org/abs/2405.15867) (2024)
    * [RELICS: a REactor neutrino LIquid xenon Coherent elastic Scattering experiment](https://arxiv.org/abs/2405.05554) [[DOI](https://doi.org/10.1103/PhysRevD.110.072011)] (2024)
    * [Measurement of atmospheric neutrino oscillation parameters using convolutional neural networks with 9.3 years of data in IceCube DeepCore](https://arxiv.org/abs/2405.02163) (2024)
    * [NuGraph2: A Graph Neural Network for Neutrino Physics Event Reconstruction](https://arxiv.org/abs/2403.11872) [[DOI](https://doi.org/10.1103/PhysRevD.110.032008)] (2024)
    * [Using machine learning to separate Cherenkov and scintillation light in hybrid neutrino detector](https://arxiv.org/abs/2403.05184) [[DOI](https://doi.org/10.1088/1748-0221/19/04/P04027)] (2024)
    * [Neutrino Reconstruction in TRIDENT Based on Graph Neural Network](https://arxiv.org/abs/2401.15324) [[DOI](https://doi.org/10.1007/978-981-97-0065-3_20)] (2024)
    * [Trigger-Level Event Reconstruction for Neutrino Telescopes Using Sparse Submanifold Convolutional Neural Networks](https://arxiv.org/abs/2303.08812) [[DOI](https://doi.org/10.22323/1.444.1004)] (2023)
    * [Assessment of few-hits machine learning classification algorithms for low energy physics in liquid argon detectors](https://arxiv.org/abs/2305.09744) [[DOI](https://doi.org/10.1140/epjp/s13360-024-05287-9)] (2023)
    * [Probing the mixing parameter |V\ensuremath{\tau}N|2 for heavy neutrinos](https://arxiv.org/abs/2211.00309) [[DOI](https://doi.org/10.1103/PhysRevD.107.095008)] (2022)
    * [Graph Neural Networks for low-energy event classification \& reconstruction in IceCube](https://arxiv.org/abs/2209.03042) [[DOI](https://doi.org/10.1088/1748-0221/17/11/P11003)] (2022)
    * [GraphNeT: Graph neural networks for neutrino telescope event reconstruction](https://arxiv.org/abs/2210.12194) [[DOI](https://doi.org/10.21105/joss.04971)] (2022)
    * [Partition Pooling for Convolutional Graph Network Applications in Particle Physics](https://arxiv.org/abs/2208.05952) [[DOI](https://doi.org/10.1088/1748-0221/17/10/P10004)] (2022)
    * [Application of Transfer Learning to Neutrino Interaction Classification](https://arxiv.org/abs/2207.03139) [[DOI](https://doi.org/10.1140/epjc/s10052-022-11066-6)] (2022)
    * [Towards Designing and Exploiting Generative Networks for Neutrino Physics Experiments using Liquid Argon Time Projection Chambers](https://arxiv.org/abs/2204.02496) (2022)
    * [Separation of track- and shower-like energy deposits in ProtoDUNE-SP using a convolutional neural network](https://arxiv.org/abs/2203.17053) [[DOI](https://doi.org/10.1140/epjc/s10052-022-10791-2)] (2022)
    * [Improvement of the NOvA Near Detector Event Reconstruction and Primary Vertexing through the Application of Machine Learning Methods](https://arxiv.org/abs/2112.01494) (2021)
    * [Wire-Cell 3D Pattern Recognition Techniques for Neutrino Event Reconstruction in Large LArTPCs: Algorithm Description and Quantitative Evaluation with MicroBooNE Simulation](https://arxiv.org/abs/2110.13961) [[DOI](https://doi.org/10.1088/1748-0221/17/01/P01037)] (2021)
    * [Electromagnetic Shower Reconstruction and Energy Validation with Michel Electrons and $\pi^0$ Samples for the Deep-Learning-Based Analyses in MicroBooNE](https://arxiv.org/abs/2110.11874) [[DOI](https://doi.org/10.1088/1748-0221/16/12/T12017)] (2021)
    * [Convolutional Neural Networks for Shower Energy Prediction in Liquid Argon Time Projection Chambers](https://arxiv.org/abs/2110.10766) [[DOI](https://doi.org/10.1088/1748-0221/17/02/P02022)] (2021)
    * [Deep learning reconstruction in ANTARES](https://arxiv.org/abs/2107.13654) [[DOI](https://doi.org/10.1088/1748-0221/16/09/C09018)] (2021)
    * [The use of Boosted Decision Trees for Energy Reconstruction in JUNO experiment](https://arxiv.org/abs/2106.02907) [[DOI](https://doi.org/10.1051/epjconf/202125103014)] (2021)
    * [CNNs for enhanced background discrimination in DSNB searches in large-scale water-Gd detectors](https://arxiv.org/abs/2104.13426) [[DOI](https://doi.org/10.1088/1475-7516/2021/11/051)] (2021)
    * [Segmentation of EM showers for neutrino experiments with deep graph neural networks](https://arxiv.org/abs/2104.02040) [[DOI](https://doi.org/10.1088/1748-0221/16/12/P12035)] (2021)
    * [A deep-learning based raw waveform region-of-interest finder for the liquid argon time projection chamber](https://arxiv.org/abs/2103.06391) [[DOI](https://doi.org/10.1088/1748-0221/17/01/P01018)] (2021)
    * [Graph Neural Network for Object Reconstruction in Liquid Argon Time Projection Chambers](https://arxiv.org/abs/2103.06233) [[DOI](https://doi.org/10.1051/epjconf/202125103054)] (2021)
    * [Deep Learning strategies for ProtoDUNE raw data denoising](https://arxiv.org/abs/2103.01596) [[DOI](https://doi.org/10.1007/s41781-021-00077-9)] (2021)
    * [Scalable, End-to-End, Deep-Learning-Based Data Reconstruction Chain for Particle Imaging Detectors](https://arxiv.org/abs/2102.01033) (2021)
    * [A Convolutional Neural Network based Cascade Reconstruction for the IceCube Neutrino Observatory](https://arxiv.org/abs/2101.11589) [[DOI](https://doi.org/10.1088/1748-0221/16/07/P07041)] (2021)
    * [Vertex and Energy Reconstruction in JUNO with Machine Learning Methods](https://arxiv.org/abs/2101.04839) [[DOI](https://doi.org/10.1016/j.nima.2021.165527)] (2021)
    * [Quantum Convolutional Neural Networks for High Energy Physics Data Analysis](https://arxiv.org/abs/2012.12177) [[DOI](https://doi.org/10.1103/PhysRevResearch.4.013231)] (2020)
    * [Semantic Segmentation with a Sparse Convolutional Neural Network for Event Reconstruction in MicroBooNE](https://arxiv.org/abs/2012.08513) [[DOI](https://doi.org/10.1103/PhysRevD.103.052012)] (2020)
    * [Deep-Learning-Based Kinematic Reconstruction for DUNE](https://arxiv.org/abs/2012.06181) (2020)
    * [Study of using machine learning for level 1 trigger decision in JUNO experiment](https://arxiv.org/abs/2011.08847) [[DOI](https://doi.org/10.1109/TNS.2021.3085428)] (2020)
    * [A Convolutional Neural Network for Multiple Particle Identification in the MicroBooNE Liquid Argon Time Projection Chamber](https://arxiv.org/abs/2010.08653) [[DOI](https://doi.org/10.1103/PhysRevD.103.092003)] (2020)
    * [Graph neural network for 3D classification of ambiguities and optical crosstalk in scintillator-based neutrino detectors](https://arxiv.org/abs/2009.00688) [[DOI](https://doi.org/10.1103/PhysRevD.103.032005)] (2020)
    * [A Review on Machine Learning for Neutrino Experiments](https://arxiv.org/abs/2008.01242) [[DOI](https://doi.org/10.1142/S0217751X20430058)] (2020)
    * [Augmented signal processing in Liquid Argon Time Projection Chambers with a deep neural network](https://arxiv.org/abs/2007.12743) [[DOI](https://doi.org/10.1088/1748-0221/16/01/P01036)] (2020)
    * [Scalable, Proposal-free Instance Segmentation Network for 3D Pixel Clustering and Particle Trajectory Reconstruction in Liquid Argon Time Projection Chambers](https://arxiv.org/abs/2007.03083) (2020)
    * [Clustering of electromagnetic showers and particle interactions with graph neural networks in liquid argon time projection chambers](https://arxiv.org/abs/2007.01335) [[DOI](https://doi.org/10.1103/PhysRevD.104.072004)] (2020)
    * [Neutrino interaction classification with a convolutional neural network in the DUNE far detector](https://arxiv.org/abs/2006.15052) [[DOI](https://doi.org/10.1103/PhysRevD.102.092003)] (2020)
    * [Point Proposal Network for Reconstructing 3D Particle Positions with Sub-Pixel Precision in Liquid Argon Time Projection Chambers](https://arxiv.org/abs/2006.14745) [[DOI](https://doi.org/10.1103/PhysRevD.104.032004)] (2020)
    * [PILArNet: Public Dataset for Particle Imaging Liquid Argon Detectors in High Energy Physics](https://arxiv.org/abs/2006.01993) (2020)
    * [Event reconstruction for KM3NeT/ORCA using convolutional neural networks](https://arxiv.org/abs/2004.08254) [[DOI](https://doi.org/10.1088/1748-0221/15/10/P10005)] (2020)
    * [Scalable deep convolutional neural networks for sparse, locally dense liquid argon time projection chamber data](https://arxiv.org/abs/1903.05663) [[DOI](https://doi.org/10.1103/PhysRevD.102.012005)] (2019)
    * [Deep neural network for pixel-level electromagnetic particle identification in the MicroBooNE liquid argon time projection chamber](https://arxiv.org/abs/1808.07269) [[DOI](https://doi.org/10.1103/PhysRevD.99.092001)] (2018)
    * [Convolutional Neural Networks for Electron Neutrino and Electron Shower Energy Reconstruction in the NO$\nu$A Detectors](https://dl4physicalsciences.github.io/files/nips_dlps_2017_7.pdf) (2017)
    * [Convolutional Neural Networks Applied to Neutrino Events in a Liquid Argon Time Projection Chamber](https://arxiv.org/abs/1611.05531) [[DOI](https://doi.org/10.1088/1748-0221/12/03/P03011)] (2016)
    * [A Convolutional Neural Network Neutrino Event Classifier](https://arxiv.org/abs/1604.01444) [[DOI](https://doi.org/10.1088/1748-0221/11/09/P09001)] (2016)

    ####  Direct Dark Matter Detectors

    * [Bayesian technique to combine independently-trained Machine-Learning models applied to direct dark matter detection](https://arxiv.org/abs/2407.21008) (2024)
    * [Deep Probabilistic Direction Prediction in 3D with Applications to Directional Dark Matter Detectors](https://arxiv.org/abs/2403.15949) [[DOI](https://doi.org/10.1088/2632-2153/ad5f13)] (2024)
    * [Detector signal characterization with a Bayesian network in XENONnT](https://arxiv.org/abs/2304.05428) [[DOI](https://doi.org/10.1103/PhysRevD.108.012016)] (2023)
    * [Assessment of few-hits machine learning classification algorithms for low energy physics in liquid argon detectors](https://arxiv.org/abs/2305.09744) [[DOI](https://doi.org/10.1140/epjp/s13360-024-05287-9)] (2023)
    * [Improving the machine learning based vertex reconstruction for large liquid scintillator detectors with multiple types of PMTs](https://arxiv.org/abs/2205.04039) [[DOI](https://doi.org/10.1007/s41365-022-01078-y)] (2022)
    * [Domain-informed neural networks for interaction localization within astroparticle experiments](https://arxiv.org/abs/2112.07995) [[DOI](https://doi.org/10.3389/frai.2022.832909)] (2021)
    * [Signal-agnostic dark matter searches in direct detection data with machine learning](https://arxiv.org/abs/2110.12248) [[DOI](https://doi.org/10.1088/1475-7516/2022/02/039)] (2021)
    * [Machine-learning techniques applied to three-year exposure of ANAIS-112](https://arxiv.org/abs/2110.10649) [[DOI](https://doi.org/10.1088/1742-6596/2156/1/012036)] (2021)
    * [Scanning the landscape of axion dark matter detectors: applying gradient descent to experimental design](https://arxiv.org/abs/2108.13894) [[DOI](https://doi.org/10.1103/PhysRevD.105.083010)] (2021)
    * [Deep Learning for direct Dark Matter search with nuclear emulsions](https://arxiv.org/abs/2106.11995) [[DOI](https://doi.org/10.1016/j.cpc.2022.108312)] (2021)
    * [Convolutional Neural Networks for Direct Detection of Dark Matter](https://arxiv.org/abs/1911.09210) [[DOI](https://doi.org/10.1088/1361-6471/ab8e94)] (2019)
    * [Improving sensitivity to low-mass dark matter in LUX using a novel electrode background mitigation technique](https://arxiv.org/abs/2011.09602) [[DOI](https://doi.org/10.1103/PhysRevD.104.012011)] (2020)
    * Boosted decision trees approach to neck alpha events discrimination in DEAP-3600 experiment (2020)

    ####  Cosmology, Astro Particle, and Cosmic Ray physics

    * [An Extended Closure Relation by LightGBM for Neutrino Radiation Transport in Core-collapse Supernovae](https://arxiv.org/abs/2409.02719) (2024)
    * [$\overline{\text{D}}$arkRayNet: Emulation of cosmic-ray antideuteron fluxes from dark matter](https://arxiv.org/abs/2406.18642) (2024)
    * [Holographic reconstruction of black hole spacetime: machine learning and entanglement entropy](https://arxiv.org/abs/2406.07395) (2024)
    * [Neural Networks Assisted Metropolis-Hastings for Bayesian Estimation of Critical Exponent on Elliptic Black Hole Solution in 4D Using Quantum Perturbation Theory](https://arxiv.org/abs/2406.04310) [[DOI](https://doi.org/10.1088/1475-7516/2024/09/015)] (2024)
    * [Preheating with deep learning](https://arxiv.org/abs/2405.08901) [[DOI](https://doi.org/10.1088/1475-7516/2024/08/031)] (2024)
    * [Sibyll★](https://arxiv.org/abs/2404.02636) [[DOI](https://doi.org/10.1016/j.astropartphys.2024.102964)] (2024)
    * [The Measurement and Modelling of Cosmic Ray Muons at KM3NeT Detectors](https://arxiv.org/abs/2402.02620) (2024)
    * [Towards Uncovering Dark Matter Effects on Neutron Star Properties: A Machine Learning Approach](https://arxiv.org/abs/2401.07773) [[DOI](https://doi.org/10.3390/particles7010005)] (2024)
    * [Insights into neutron star equation of state by machine learning](https://arxiv.org/abs/2309.11227) [[DOI](https://doi.org/10.3847/1538-4357/ad2e8d)] (2023)
    * [Sequential Monte Carlo with Cross-validated Neural Networks for Complexity of Hyperbolic Black Hole Solutions in 4D](https://arxiv.org/abs/2308.07907) [[DOI](https://doi.org/10.1140/epjc/s10052-023-12284-2)] (2023)
    * [A Deep Learning Approach to Extracting Nuclear Matter Properties from Neutron Star Observations](https://arxiv.org/abs/2303.17146) [[DOI](https://doi.org/10.3390/sym15051123)] (2023)
    * [Core States of Neutron Stars from Anatomizing Their Scaled Structure Equations](https://arxiv.org/abs/2306.08202) [[DOI](https://doi.org/10.3847/1538-4357/acdef0)] (2023)
    * [Decoding Neutron Star Observations: Revealing Composition through Bayesian Neural Networks](https://arxiv.org/abs/2306.06929) [[DOI](https://doi.org/10.1103/PhysRevD.108.043031)] (2023)
    * [Nonparametric Model for the Equations of State of a Neutron Star from Deep Neural Network](https://arxiv.org/abs/2305.03323) [[DOI](https://doi.org/10.3847/1538-4357/acd335)] (2023)
    * [Probing Cosmological Particle Production and Pairwise Hotspots with Deep Neural Networks](https://arxiv.org/abs/2303.08869) [[DOI](https://doi.org/10.1103/PhysRevD.108.043525)] (2023)
    * [Progress in Nuclear Astrophysics: a multi-disciplinary field with still many open questions](https://arxiv.org/abs/2212.02156) [[DOI](https://doi.org/10.1088/1742-6596/2586/1/012104)] (2022)
    * [Uncovering dark matter density profiles in dwarf galaxies with graph neural networks](https://arxiv.org/abs/2208.12825) [[DOI](https://doi.org/10.1103/PhysRevD.107.043015)] (2022)
    * [Inferring subhalo effective density slopes from strong lensing observations with neural likelihood-ratio estimation](https://arxiv.org/abs/2208.13796) [[DOI](https://doi.org/10.1093/mnras/stac3014)] (2022)
    * [Cosmic Inflation and Genetic Algorithms](https://arxiv.org/abs/2208.13804) [[DOI](https://doi.org/10.1002/prop.202200161)] (2022)
    * [Modeling early-universe energy injection with Dense Neural Networks](https://arxiv.org/abs/2207.06425) [[DOI](https://doi.org/10.1103/PhysRevD.107.063541)] (2022)
    * [BlaST -- A Machine-Learning Estimator for the Synchrotron Peak of Blazars](https://arxiv.org/abs/2207.03813) [[DOI](https://doi.org/10.1016/j.ascom.2022.100646)] (2022)
    * [Estimating the warm dark matter mass from strong lensing images with truncated marginal neural ratio estimation](https://arxiv.org/abs/2205.09126) [[DOI](https://doi.org/10.1093/mnras/stac3215)] (2022)
    * [Deep learning techniques for Imaging Air Cherenkov Telescopes](https://arxiv.org/abs/2206.05296) [[DOI](https://doi.org/10.1103/PhysRevD.107.083026)] (2022)
    * [Novel pre-burst stage of gamma-ray bursts from machine learning](https://arxiv.org/abs/1910.08043) [[DOI](https://doi.org/10.1016/j.jheap.2021.09.002)] (2019)
    * [Inference of cosmic-ray source properties by conditional invertible neural networks](https://arxiv.org/abs/2110.09493) [[DOI](https://doi.org/10.1140/epjc/s10052-022-10138-x)] (2021)
    * [A neural simulation-based inference approach for characterizing the Galactic Center $\gamma$-ray excess](https://arxiv.org/abs/2110.06931) [[DOI](https://doi.org/10.1103/PhysRevD.105.063017)] (2021)
    * [Inferring dark matter substructure with astrometric lensing beyond the power spectrum](https://arxiv.org/abs/2110.01620) [[DOI](https://doi.org/10.1088/2632-2153/ac494a)] (2021)
    * [Probing Ultra-light Axion Dark Matter from 21cm Tomography using Convolutional Neural Networks](https://arxiv.org/abs/2108.07972) [[DOI](https://doi.org/10.1088/1475-7516/2022/01/020)] (2021)
    * [Constraining dark matter annihilation with cosmic ray antiprotons using neural networks](https://arxiv.org/abs/2107.12395) [[DOI](https://doi.org/10.1088/1475-7516/2021/12/037)] (2021)
    * [Dim but not entirely dark: Extracting the Galactic Center Excess' source-count distribution with neural nets](https://arxiv.org/abs/2107.09070) [[DOI](https://doi.org/10.1103/PhysRevD.104.123022)] (2021)
    * [Using Convolutional Neural Networks for the Helicity Classification of Magnetic Fields](https://arxiv.org/abs/2106.06718) [[DOI](https://doi.org/10.22323/1.395.0906)] (2021)
    * [Machine Learning improved fits of the sound horizon at the baryon drag epoch](https://arxiv.org/abs/2106.00428) [[DOI](https://doi.org/10.1103/PhysRevD.104.043521)] (2021)
    * [Development of Convolutional Neural Networks for an Electron-Tracking Compton Camera](https://arxiv.org/abs/2105.02512) [[DOI](https://doi.org/10.1093/ptep/ptab091)] (2021)
    * [Via Machinae: Searching for Stellar Streams using Unsupervised Machine Learning](https://arxiv.org/abs/2104.12789) [[DOI](https://doi.org/10.1093/mnras/stab3372)] (2021)
    * [Machine Learning the 6th Dimension: Stellar Radial Velocities from 5D Phase-Space Correlations](https://arxiv.org/abs/2103.14039) [[DOI](https://doi.org/10.3847/2041-8213/ac09ef)] (2021)
    * [Novel null tests for the spatial curvature and homogeneity of the Universe and their machine learning reconstructions](https://arxiv.org/abs/2103.06789) [[DOI](https://doi.org/10.1103/PhysRevD.103.103539)] (2021)
    * [Bayesian nonparametric inference of neutron star equation of state via neural network](https://arxiv.org/abs/2103.05408) [[DOI](https://doi.org/10.3847/1538-4357/ac11f8)] (2021)
    * [A neural network classifier for electron identification on the DAMPE experiment](https://arxiv.org/abs/2102.05534) [[DOI](https://doi.org/10.1088/1748-0221/16/07/P07036)] (2021)
    * [A convolutional-neural-network estimator of CMB constraints on dark matter energy injection](https://arxiv.org/abs/2101.10360) [[DOI](https://doi.org/10.1088/1475-7516/2021/06/025)] (2021)
    * [Muon identification in a compact single-layered water Cherenkov detector and gamma/hadron discrimination using Machine Learning techniques](https://arxiv.org/abs/2101.10109) [[DOI](https://doi.org/10.1140/epjc/s10052-021-09312-4)] (2021)
    * [Tackling the muon identification in water Cherenkov detectors problem for the future Southern Wide-field Gamma-ray Observatory by means of Machine Learning](https://arxiv.org/abs/2101.11924) (2021)
    * [A comparison of optimisation algorithms for high-dimensional particle and astrophysics applications](https://arxiv.org/abs/2101.04525) [[DOI](https://doi.org/10.1007/JHEP05(2021)108)] (2021)
    * [Deep-Learning based Reconstruction of the Shower Maximum $X_{\mathrm{max}}$ using the Water-Cherenkov Detectors of the Pierre Auger Observatory](https://arxiv.org/abs/2101.02946) [[DOI](https://doi.org/10.1088/1748-0221/16/07/P07019)] (2021)
    * [Particle Track Reconstruction using Geometric Deep Learning](https://arxiv.org/abs/2012.08515) (2020)
    * [Inverting cosmic ray propagation by Convolutional Neural Networks](https://arxiv.org/abs/2011.11930) [[DOI](https://doi.org/10.1088/1475-7516/2022/03/044)] (2020)
    * [Mining for Dark Matter Substructure: Inferring subhalo population properties from strong lenses with machine learning](https://arxiv.org/abs/1909.02005) [[DOI](https://doi.org/10.3847/1538-4357/ab4c41)] (2019)
    * [Detecting Subhalos in Strong Gravitational Lens Images with Image Segmentation](https://arxiv.org/abs/2009.06663) [[DOI](https://doi.org/10.1051/0004-6361/202142030)] (2020)

    ####  Tracking

    * [TrackFormers: In Search of Transformer-Based Particle Tracking for the High-Luminosity LHC Era](https://arxiv.org/abs/2407.07179) (2024)
    * [Improving tracking algorithms with machine learning: a case for line-segment tracking at the High Luminosity LHC](https://arxiv.org/abs/2403.13166) (2024)
    * [Real-Time Charged Track Reconstruction for CLAS12](https://arxiv.org/abs/2403.04020) [[DOI](https://doi.org/10.1088/1748-0221/19/05/C05050)] (2024)
    * [A Language Model for Particle Tracking](https://arxiv.org/abs/2402.10239) (2024)
    * [Ranking-based neural network for ambiguity resolution in ACTS](https://arxiv.org/abs/2312.05070) [[DOI](https://doi.org/10.1051/epjconf/202429503022)] (2023)
    * [Auto-tuning capabilities of the ACTS track reconstruction suite](https://arxiv.org/abs/2312.05123) (2023)
    * [HyperTrack: Neural Combinatorics for High Energy Physics](https://arxiv.org/abs/2309.14113) [[DOI](https://doi.org/10.1051/epjconf/202429509021)] (2023)
    * [Comparing and improving hybrid deep learning algorithms for identifying and locating primary vertices](https://arxiv.org/abs/2304.02423) (2023)
    * [Deep Learning-Based Spatiotemporal Multi-Event Reconstruction for Delay Line Detectors](https://arxiv.org/abs/2306.09359) [[DOI](https://doi.org/10.1088/2632-2153/ad3d2d)] (2023)
    * [Reconstruction of fast neutron direction in segmented organic detectors using deep learning](https://arxiv.org/abs/2301.10796) [[DOI](https://doi.org/10.1016/j.nima.2023.168024)] (2023)
    * [Charged Particle Tracking with Machine Learning on FPGAs](https://arxiv.org/abs/2212.02348) (2022)
    * [Fast muon tracking with machine learning implemented in FPGA](https://arxiv.org/abs/2202.04976) [[DOI](https://doi.org/10.1016/j.nima.2022.167546)] (2022)
    * [Track Reconstruction using Geometric Deep Learning in the Straw Tube Tracker (STT) at the PANDA Experiment](https://arxiv.org/abs/2208.12178) (2022)
    * [Deep learning for track recognition in pixel and strip-based particle detectors](https://arxiv.org/abs/2210.00599) [[DOI](https://doi.org/10.1088/1748-0221/17/12/P12023)] (2022)
    * [Artificial intelligence for improved fitting of trajectories of elementary particles in inhomogeneous dense materials immersed in a magnetic field](https://arxiv.org/abs/2211.04890) [[DOI](https://doi.org/10.1038/s42005-023-01239-4)] (2022)
    * [Reconstruction of Large Radius Tracks with the Exa.TrkX pipeline](https://arxiv.org/abs/2203.08800) [[DOI](https://doi.org/10.1088/1742-6596/2438/1/012117)] (2022)
    * [Ariadne: PyTorch Library for Particle Track Reconstruction Using Deep Learning](https://arxiv.org/abs/2109.08982) [[DOI](https://doi.org/10.1063/5.0063300)] (2021)
    * [Machine learning for surface prediction in ACTS](https://arxiv.org/abs/2108.03068) [[DOI](https://doi.org/10.1051/epjconf/202125103053)] (2021)
    * [Optical Inspection of the Silicon Micro-strip Sensors for the CBM Experiment employing Artificial Intelligence](https://arxiv.org/abs/2107.07714) [[DOI](https://doi.org/10.1016/j.nima.2021.165932)] (2021)
    * [Using Machine Learning to Select High-Quality Measurements](https://arxiv.org/abs/2106.08891) [[DOI](https://doi.org/10.1088/1748-0221/16/08/T08010)] (2021)
    * [Charged particle tracking via edge-classifying interaction networks](https://arxiv.org/abs/2103.16701) [[DOI](https://doi.org/10.1007/s41781-021-00073-z)] (2021)
    * [Physics and Computing Performance of the Exa.TrkX TrackML Pipeline](https://arxiv.org/abs/2103.06995) [[DOI](https://doi.org/10.1140/epjc/s10052-021-09675-8)] (2021)
    * [Instance Segmentation GNNs for One-Shot Conformal Tracking at the LHC](https://arxiv.org/abs/2103.06509) (2021)
    * [Progress in developing a hybrid deep learning algorithm for identifying and locating primary vertices](https://arxiv.org/abs/2103.04962) [[DOI](https://doi.org/10.1051/epjconf/202125104012)] (2021)
    * [Towards a realistic track reconstruction algorithm based on graph neural networks for the HL-LHC](https://arxiv.org/abs/2103.00916) [[DOI](https://doi.org/10.1051/epjconf/202125103047)] (2021)
    * [Development of a Vertex Finding Algorithm using Recurrent Neural Network](https://arxiv.org/abs/2101.11906) [[DOI](https://doi.org/10.1016/j.nima.2022.167836)] (2021)
    * [Hashing and metric learning for charged particle tracking](https://arxiv.org/abs/2101.06428) (2021)
    * [Beyond 4D Tracking: Using Cluster Shapes for Track Seeding](https://arxiv.org/abs/2012.04533) [[DOI](https://doi.org/10.1088/1748-0221/16/05/P05001)] (2020)
    * [First application of machine learning algorithms to the position reconstruction in Resistive Silicon Detectors](https://arxiv.org/abs/2011.02410) [[DOI](https://doi.org/10.1088/1748-0221/16/03/P03019)] (2020)
    * [Track Seeding and Labelling with Embedded-space Graph Neural Networks](https://arxiv.org/abs/2007.00149) (2020)
    * [Secondary Vertex Finding in Jets with Neural Networks](https://arxiv.org/abs/2008.02831) [[DOI](https://doi.org/10.1140/epjc/s10052-021-09342-y)] (2020)
    * [An updated hybrid deep learning algorithm for identifying and locating primary vertices](https://arxiv.org/abs/2007.01023) (2020)
    * [Graph Neural Networks for Particle Reconstruction in High Energy Physics detectors](https://arxiv.org/abs/2003.11603) (2020)
    * [The Tracking Machine Learning challenge : Accuracy phase](https://arxiv.org/abs/1904.06778) [[DOI](https://doi.org/10.1007/978-3-030-29135-8\_9)] (2019)
    * [Novel deep learning methods for track reconstruction](https://arxiv.org/abs/1810.06111) (2018)
    * [Particle Track Reconstruction with Deep Learning](https://dl4physicalsciences.github.io/files/nips_dlps_2017_28.pdf) (2017)

    ####  Heavy Ions / Nuclear Physics

    * [A novel machine learning method to detect double-$\Lambda$ hypernuclear events in nuclear emulsions](https://arxiv.org/abs/2409.01657) (2024)
    * [Electron-nucleus cross sections from transfer learning](https://arxiv.org/abs/2408.09936) (2024)
    * [Bayesian Inference analysis of jet quenching using inclusive jet and hadron suppression measurements](https://arxiv.org/abs/2408.08247) (2024)
    * [AI for Nuclear Physics: the EXCLAIM project](https://arxiv.org/abs/2408.00163) (2024)
    * [Effects of saturation and fluctuating hotspots for flow observables in ultrarelativistic heavy-ion collisions](https://arxiv.org/abs/2407.01338) [[DOI](https://doi.org/10.1103/PhysRevC.110.034911)] (2024)
    * [Pole structure of $P_\psi^N(4312)^+$ via machine learning and uniformized S-matrix](https://arxiv.org/abs/2405.11906) (2024)
    * [A machine learning-based study of open-charm hadrons in proton-proton collisions at the Large Hadron Collider](https://arxiv.org/abs/2404.09839) [[DOI](https://doi.org/10.1103/PhysRevD.110.034017)] (2024)
    * [Deep learning for flow observables in high energy heavy-ion collisions](https://arxiv.org/abs/2404.02602) [[DOI](https://doi.org/10.1051/epjconf/202429602002)] (2024)
    * [Multiplicity Based Background Subtraction for Jets in Heavy Ion Collisions](https://arxiv.org/abs/2402.10945) (2024)
    * [Physics-informed Meta-instrument for eXperiments (PiMiX) with applications to fusion energy](https://arxiv.org/abs/2401.08390) (2024)
    * [Neural Network Emulation of Spontaneous Fission](https://arxiv.org/abs/2310.01608) [[DOI](https://doi.org/10.1103/PhysRevC.109.044305)] (2023)
    * [Neural Network Solutions of Bosonic Quantum Systems in One Dimension](https://arxiv.org/abs/2309.02352) [[DOI](https://doi.org/10.1103/PhysRevC.109.034004)] (2023)
    * [Artificial Intelligence for the Electron Ion Collider (AI4EIC)](https://arxiv.org/abs/2307.08593) [[DOI](https://doi.org/10.1007/s41781-024-00113-4)] (2023)
    * [Generative modeling of nucleon-nucleon interactions](https://arxiv.org/abs/2306.13007) (2023)
    * [Analysis of a Skyrme energy density functional with deep learning](https://arxiv.org/abs/2306.11314) [[DOI](https://doi.org/10.1103/PhysRevC.108.034311)] (2023)
    * [Constraining the Woods-Saxon potential in fusion reactions based on a physics-informed neural network](https://arxiv.org/abs/2306.11236) [[DOI](https://doi.org/10.1103/PhysRevC.109.024601)] (2023)
    * [IMSRG-Net: A machine learning-based solver for In-Medium Similarity Renormalization Group](https://arxiv.org/abs/2306.08878) [[DOI](https://doi.org/10.1103/PhysRevC.108.044303)] (2023)
    * [Generative deep-learning reveals collective variables of Fermionic systems](https://arxiv.org/abs/2306.08348) [[DOI](https://doi.org/10.1103/PhysRevC.109.064612)] (2023)
    * [Neutron-Gamma Pulse Shape Discrimination for Organic Scintillation Detector using 2D CNN based Image Classification](https://arxiv.org/abs/2306.09356) (2023)
    * [Nuclear mass predictions based on deep neural network and finite-range droplet model (2012)](https://arxiv.org/abs/2306.04171) [[DOI](https://doi.org/10.1088/1674-1137/ad021c)] (2023)
    * [Label-free timing analysis of modularized nuclear detectors with physics-constrained deep learning](https://arxiv.org/abs/2304.11930) [[DOI](https://doi.org/10.1088/2632-2153/acfd09)] (2023)
    * [Machine learning transforms the inference of the nuclear equation of state](https://arxiv.org/abs/2305.16686) [[DOI](https://doi.org/10.1007/s11467-023-1313-3)] (2023)
    * [A machine learning study to identify collective flow in small and large colliding systems](https://arxiv.org/abs/2305.09937) [[DOI](https://doi.org/10.1103/PhysRevC.110.024910)] (2023)
    * [Neural network predictions of inclusive electron-nucleus cross sections](https://arxiv.org/abs/2305.08217) [[DOI](https://doi.org/10.1103/PhysRevC.107.065501)] (2023)
    * [Predicting nuclear masses with product-unit networks](https://arxiv.org/abs/2305.04675) [[DOI](https://doi.org/10.1016/j.physletb.2024.138608)] (2023)
    * [Demonstration of Sub-micron UCN Position Resolution using Room-temperature CMOS Sensor](https://arxiv.org/abs/2305.09562) [[DOI](https://doi.org/10.1016/j.nima.2023.168769)] (2023)
    * [Nuclear corrections on the charged hadron fragmentation functions in a Neural Network global QCD analysis](https://arxiv.org/abs/2305.02664) [[DOI](https://doi.org/10.1140/epjp/s13360-024-05571-8)] (2023)
    * [$\Sigma$ Resonances from a Neural Network-based Partial Wave Analysis on $K^-p$ Scattering](https://arxiv.org/abs/2305.01852) (2023)
    * [Estimation of collision centrality in terms of the number of participating nucleons in heavy-ion collisions using deep learning](https://arxiv.org/abs/2305.00493) [[DOI](https://doi.org/10.1140/epja/s10050-023-01087-4)] (2023)
    * [Jet substructure observables for jet quenching in Quark Gluon Plasma: a Machine Learning driven analysis](https://arxiv.org/abs/2304.07196) [[DOI](https://doi.org/10.21468/SciPostPhys.16.1.015)] (2023)
    * [Exploring QCD matter in extreme conditions with Machine Learning](https://arxiv.org/abs/2303.15136) [[DOI](https://doi.org/10.1016/j.ppnp.2023.104084)] (2023)
    * [High energy nuclear physics meets Machine Learning](https://arxiv.org/abs/2303.06752) [[DOI](https://doi.org/10.1007/s41365-023-01233-z)] (2023)
    * [Machine Learning based KNO-scaling of charged hadron multiplicities with Hijing++](https://arxiv.org/abs/2303.05422) (2023)
    * [Deep learning for flow observables in ultrarelativistic heavy-ion collisions](https://arxiv.org/abs/2303.04517) [[DOI](https://doi.org/10.1103/PhysRevC.108.034905)] (2023)
    * [Improving nuclear data evaluations with predictive reaction theory and indirect measurements](https://arxiv.org/abs/2304.10034) [[DOI](https://doi.org/10.1051/epjconf/202328403012)] (2023)
    * [Bayesian averaging for ground state masses of atomic nuclei in a Machine Learning approach](https://arxiv.org/abs/2304.08546) [[DOI](https://doi.org/10.3389/fphy.2023.1198572)] (2023)
    * [Mitigating Green's function Monte Carlo signal-to-noise problems using contour deformations](https://arxiv.org/abs/2304.03229) [[DOI](https://doi.org/10.1103/PhysRevC.109.034317)] (2023)
    * [Bayesian inference of nucleus resonance and neutron skin](https://arxiv.org/abs/2301.07884) [[DOI](https://doi.org/10.7538/yzk.2022.youxian.0759)] (2023)
    * [Machine learning in nuclear physics at low and intermediate energies](https://arxiv.org/abs/2301.06396) [[DOI](https://doi.org/10.1007/s11433-023-2116-0)] (2023)
    * [Deep learning predicted elliptic flow of identified particles in heavy-ion collisions at the RHIC and LHC energies](https://arxiv.org/abs/2301.10426) [[DOI](https://doi.org/10.1103/PhysRevD.107.094001)] (2023)
    * [Separating signal from combinatorial jets in a high background environment](https://arxiv.org/abs/2301.09148) [[DOI](https://doi.org/10.1103/PhysRevC.108.024909)] (2023)
    * [Dilute neutron star matter from neural-network quantum states](https://arxiv.org/abs/2212.04436) [[DOI](https://doi.org/10.1103/PhysRevResearch.5.033062)] (2022)
    * [Estimating elliptic flow coefficient in heavy ion collisions using deep learning](https://arxiv.org/abs/2203.01246) [[DOI](https://doi.org/10.1103/PhysRevD.105.114022)] (2022)
    * [Progress in Nuclear Astrophysics: a multi-disciplinary field with still many open questions](https://arxiv.org/abs/2212.02156) [[DOI](https://doi.org/10.1088/1742-6596/2586/1/012104)] (2022)
    * [Predicting \ensuremath{\beta}-decay energy with machine learning](https://arxiv.org/abs/2211.17136) [[DOI](https://doi.org/10.1103/PhysRevC.107.034308)] (2022)
    * [Deep-neural-network approach to solving the ab initio nuclear structure problem](https://arxiv.org/abs/2211.13998) [[DOI](https://doi.org/10.1103/PhysRevC.107.034320)] (2022)
    * [Solving the nuclear pairing model with neural network quantum states](https://arxiv.org/abs/2211.04614) [[DOI](https://doi.org/10.1103/PhysRevE.107.025310)] (2022)
    * [A Kohn-Sham scheme based neural network for nuclear systems](https://arxiv.org/abs/2212.02093) [[DOI](https://doi.org/10.1016/j.physletb.2023.137870)] (2022)
    * [Optimization of the generator coordinate method with machine-learning techniques for nuclear spectra and neutrinoless double-\ensuremath{\beta} decay: Ridge regression for nuclei with axial deformation](https://arxiv.org/abs/2211.02797) [[DOI](https://doi.org/10.1103/PhysRevC.107.024304)] (2022)
    * [Testing of KNO-scaling of charged hadron multiplicities within a Machine Learning based approach](https://arxiv.org/abs/2210.10548) [[DOI](https://doi.org/10.22323/1.414.1188)] (2022)
    * [Machine learning-based jet and event classification at the Electron-Ion Collider with applications to hadron structure and spin physics](https://arxiv.org/abs/2210.06450) [[DOI](https://doi.org/10.1007/JHEP03(2023)085)] (2022)
    * [Machine Learning model driven prediction of the initial geometry in Heavy-Ion Collision experiments](https://arxiv.org/abs/2203.15433) [[DOI](https://doi.org/10.1103/PhysRevC.106.014901)] (2022)
    * [Identify Hadronic Molecule States by Neural Network](https://arxiv.org/abs/2205.03572) [[DOI](https://doi.org/10.1140/epjc/s10052-023-11170-1)] (2022)
    * [AI-assisted Optimization of the ECCE Tracking System at the Electron Ion Collider](https://arxiv.org/abs/2205.09185) [[DOI](https://doi.org/10.1016/j.nima.2022.167748)] (2022)
    * [Identifying quenched jets in heavy ion collisions with machine learning](https://arxiv.org/abs/2206.01628) [[DOI](https://doi.org/10.1007/JHEP04(2023)140)] (2022)
    * [Efficient emulation of relativistic heavy ion collisions with transfer learning](https://arxiv.org/abs/2201.07302) [[DOI](https://doi.org/10.1103/PhysRevC.105.034910)] (2022)
    * [New tool for kinematic regime estimation in semi-inclusive deep-inelastic scattering](https://arxiv.org/abs/2201.12197) [[DOI](https://doi.org/10.1007/JHEP04(2022)084)] (2022)
    * [Particle ratios with in Hadron Resonance Gas (HRG) and Artificial Neural Network (ANN) models](https://arxiv.org/abs/2201.04444) (2022)
    * [Neural network reconstruction of the dense matter equation of state from neutron star observables](https://arxiv.org/abs/2201.01756) [[DOI](https://doi.org/10.1088/1475-7516/2022/08/071)] (2022)
    * [Determination of impact parameter in high-energy heavy-ion collisions via deep learning](https://arxiv.org/abs/2112.03824) [[DOI](https://doi.org/10.1088/1674-1137/ac6490)] (2021)
    * [Jet tomography in hot QCD medium with deep learning](https://arxiv.org/abs/2112.00679) [[DOI](https://doi.org/10.22323/1.398.0302)] (2021)
    * [Classification of quark and gluon jets in hot QCD medium with deep learning](https://arxiv.org/abs/2112.00681) [[DOI](https://doi.org/10.22323/1.380.0224)] (2021)
    * [The information content of jet quenching and machine learning assisted observable design](https://arxiv.org/abs/2111.14589) [[DOI](https://doi.org/10.1007/JHEP10(2022)011)] (2021)
    * [Studying Hadronization by Machine Learning Techniques](https://arxiv.org/abs/2111.15655) (2021)
    * [Entropy per rapidity in Pb-Pb central collisions using Thermal and Artificial neural network(ANN) models at LHC energies](https://arxiv.org/abs/2110.15026) [[DOI](https://doi.org/10.1088/1674-1137/ac5f9d)] (2021)
    * [Deep Learning Exotic Hadrons](https://arxiv.org/abs/2110.13742) [[DOI](https://doi.org/10.1103/PhysRevD.105.L091501)] (2021)
    * [Implementation of machine learning techniques to predict impact parameter and transverse spherocity in heavy-ion collisions at the LHC](https://arxiv.org/abs/2110.04026) [[DOI](https://doi.org/10.22323/1.397.0265)] (2021)
    * [Multiparton Interactions in pp collisions from Machine Learning](https://arxiv.org/abs/2110.01748) [[DOI](https://doi.org/10.22323/1.397.0347)] (2021)
    * [Particles Multiplicity Based on Rapidity in Landau and Artificial Neural Network(ANN) Models](https://arxiv.org/abs/2109.07191) [[DOI](https://doi.org/10.1142/S0217751X22500026)] (2021)
    * [Machine-learning-based identification for initial clustering structure in relativistic heavy-ion collisions](https://arxiv.org/abs/2109.06277) [[DOI](https://doi.org/10.1103/PhysRevC.104.044902)] (2021)
    * [Modeling of charged-particle multiplicity and transverse-momentum distributions in pp collisions using a DNN](https://arxiv.org/abs/2108.06102) [[DOI](https://doi.org/10.1038/s41598-022-11618-6)] (2021)
    * [Probing criticality with deep learning in relativistic heavy-ion collisions](https://arxiv.org/abs/2107.11828) [[DOI](https://doi.org/10.1016/j.physletb.2022.137001)] (2021)
    * [An equation-of-state-meter for CBM using PointNet](https://arxiv.org/abs/2107.05590) [[DOI](https://doi.org/10.1007/JHEP10(2021)184)] (2021)
    * [Jet tomography in heavy ion collisions with deep learning](https://arxiv.org/abs/2106.11271) [[DOI](https://doi.org/10.1103/PhysRevLett.128.012301)] (2021)
    * [inclusiveAI: A machine learning representation of the $F_2$ structure function over all charted $Q^2$ and $x$ range](https://arxiv.org/abs/2106.06390) [[DOI](https://doi.org/10.1103/PhysRevC.104.064321)] (2021)
    * [Deep Learning for the Classification of Quenched Jets](https://arxiv.org/abs/2106.08869) [[DOI](https://doi.org/10.1007/JHEP11(2021)219)] (2021)
    * [Application of radial basis functions neutral networks in spectral functions](https://arxiv.org/abs/2106.08168) [[DOI](https://doi.org/10.1103/PhysRevD.104.076011)] (2021)
    * [Classifying near-threshold enhancement using deep neural network](https://arxiv.org/abs/2106.03453) [[DOI](https://doi.org/10.1007/s00601-021-01642-z)] (2021)
    * [Detecting Chiral Magnetic Effect via Deep Learning](https://arxiv.org/abs/2105.13761) [[DOI](https://doi.org/10.1103/PhysRevC.106.L051901)] (2021)
    * [Constraining nuclear effects in Argon using machine learning algorithms](https://arxiv.org/abs/2105.12733) (2021)
    * [Estimation of Impact Parameter and Transverse Spherocity in heavy-ion collisions at the LHC energies using Machine Learning](https://arxiv.org/abs/2103.01736) [[DOI](https://doi.org/10.1103/PhysRevD.103.094031)] (2021)
    * [Identifying the nature of the QCD transition in relativistic collision of heavy nuclei with deep learning](https://arxiv.org/abs/1910.11530) [[DOI](https://doi.org/10.1140/epjc/s10052-020-8030-7)] (2019)
    * [Deep learning jet modifications in heavy-ion collisions](https://arxiv.org/abs/2012.07797) [[DOI](https://doi.org/10.1007/JHEP03(2021)206)] (2020)
    * [Probing heavy ion collisions using quark and gluon jet substructure](https://arxiv.org/abs/1803.03589) (2018)
    * [An equation-of-state-meter of quantum chromodynamics transition from deep learning](https://arxiv.org/abs/1612.04262) [[DOI](https://doi.org/10.1038/s41467-017-02726-3)] (2016)


??? example "Learning strategies"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ### Learning strategies
    </div>

    ####  Hyperparameters

    * [Auto-tuning capabilities of the ACTS track reconstruction suite](https://arxiv.org/abs/2312.05123) (2023)
    * [Event Generator Tuning Incorporating Systematic Uncertainty](https://arxiv.org/abs/2310.07566) [[DOI](https://doi.org/10.1051/epjconf/202429506010)] (2023)
    * [Principles for Initialization and Architecture Selection in Graph Neural Networks with ReLU Activations](https://arxiv.org/abs/2306.11668) (2023)
    * [Support vector machines and generalisation in HEP](https://arxiv.org/abs/1702.04686) [[DOI](https://doi.org/10.1088/1742-6596/898/7/072021)] (2017)
    * [Application of Deep Learning Technique to an Analysis of Hard Scattering Processes at Colliders](https://arxiv.org/abs/2109.08520) [[DOI](https://doi.org/10.22323/1.410.0012)] (2021)
    * [Evolutionary algorithms for hyperparameter optimization in machine learning for application in high energy physics](https://arxiv.org/abs/2011.04434) [[DOI](https://doi.org/10.1140/epjc/s10052-021-08950-y)] (2020)

    ####  Weak/Semi supervision

    * [Trials Factor for Semi-Supervised NN Classifiers in Searches for Narrow Resonances at the LHC](https://arxiv.org/abs/2404.07822) (2024)
    * [Improving the performance of weak supervision searches using transfer and meta-learning](https://arxiv.org/abs/2312.06152) [[DOI](https://doi.org/10.1007/JHEP02(2024)138)] (2023)
    * [Learning to Isolate Muons in Data](https://arxiv.org/abs/2306.15737) [[DOI](https://doi.org/10.1103/PhysRevD.108.092008)] (2023)
    * [Searching for dark jets with displaced vertices using weakly supervised machine learning](https://arxiv.org/abs/2305.04372) [[DOI](https://doi.org/10.1103/PhysRevD.108.035036)] (2023)
    * [TopicFlow: Disentangling quark and gluon jets with normalizing flows](https://arxiv.org/abs/2211.16053) [[DOI](https://doi.org/10.1103/PhysRevD.107.114003)] (2022)
    * [Going off topics to demix quark and gluon jets in \ensuremath{\alpha}$_{S}$ extractions](https://arxiv.org/abs/2206.10642) [[DOI](https://doi.org/10.1007/JHEP02(2023)150)] (2022)
    * [Boosting mono-jet searches with model-agnostic machine learning](https://arxiv.org/abs/2204.11889) [[DOI](https://doi.org/10.1007/JHEP08(2022)015)] (2022)
    * [Semi-supervised Graph Neural Networks for Pileup Noise Removal](https://arxiv.org/abs/2203.15823) [[DOI](https://doi.org/10.1140/epjc/s10052-022-11083-5)] (2022)
    * [Disentangling Quarks and Gluons with CMS Open Data](https://arxiv.org/abs/2205.04459) [[DOI](https://doi.org/10.1103/PhysRevD.106.094021)] (2022)
    * [An investigation of over-training within semi-supervised machine learning models in the search for heavy resonances at the LHC](https://arxiv.org/abs/2109.07287) (2021)
    * [Quark Gluon Jet Discrimination with Weakly Supervised Learning](https://arxiv.org/abs/2012.02540) [[DOI](https://doi.org/10.3938/jkps.75.652)] (2020)
    * [Machine learning approach for the search of resonances with topological features at the Large Hadron Collider](https://arxiv.org/abs/2011.09863) [[DOI](https://doi.org/10.1142/S0217751X21502419)] (2020)
    * [Data-driven quark and gluon jet modification in heavy-ion collisions](https://arxiv.org/abs/2008.08596) [[DOI](https://doi.org/10.1103/PhysRevC.103.L021901)] (2020)
    * [Tag N' Train: A Technique to Train Improved Classifiers on Unlabeled Data](https://arxiv.org/abs/2002.12376) [[DOI](https://doi.org/10.1007/JHEP01(2021)153)] (2020)
    * [Dijet resonance search with weak supervision using 13 TeV pp collisions in the ATLAS detector](https://arxiv.org/abs/2005.02983) [[DOI](https://doi.org/10.1103/PhysRevLett.125.131801)] (2020)
    * [Jet Topics: Disentangling Quarks and Gluons at Colliders](https://arxiv.org/abs/1802.00008) [[DOI](https://doi.org/10.1103/PhysRevLett.120.241602)] (2018)
    * [An operational definition of quark and gluon jets](https://arxiv.org/abs/1809.01140) [[DOI](https://doi.org/10.1007/JHEP11(2018)059)] (2018)
    * [(Machine) Learning to Do More with Less](https://arxiv.org/abs/1706.09451) [[DOI](https://doi.org/10.1007/JHEP02(2018)034)] (2017)
    * [Machine Learning on data with sPlot background subtraction](https://arxiv.org/abs/1905.11719) [[DOI](https://doi.org/10.1088/1748-0221/14/08/P08020)] (2019)
    * [Extending the search for new resonances with machine learning](https://arxiv.org/abs/1902.02634) [[DOI](https://doi.org/10.1103/PhysRevD.99.014038)] (2019)
    * [Anomaly Detection for Resonant New Physics with Machine Learning](https://arxiv.org/abs/1805.02664) [[DOI](https://doi.org/10.1103/PhysRevLett.121.241803)] (2018)
    * [Learning to classify from impure samples with high-dimensional data](https://arxiv.org/abs/1801.10158) [[DOI](https://doi.org/10.1103/PhysRevD.98.011502)] (2018)
    * [Classification without labels: Learning from mixed samples in high energy physics](https://arxiv.org/abs/1708.02949) [[DOI](https://doi.org/10.1007/JHEP10(2017)174)] (2017)
    * [Weakly Supervised Classification in High Energy Physics](https://arxiv.org/abs/1702.00414) [[DOI](https://doi.org/10.1007/JHEP05(2017)145)] (2017)

    ####  Unsupervised

    * [MACK: Mismodeling Addressed with Contrastive Knowledge](https://arxiv.org/abs/2410.13947) (2024)
    * [The Phase Space Distance Between Collider Events](https://arxiv.org/abs/2405.16698) [[DOI](https://doi.org/10.1007/JHEP09(2024)054)] (2024)
    * [PASCL: Supervised Contrastive Learning with Perturbative Augmentation for Particle Decay Reconstruction](https://arxiv.org/abs/2402.11538) (2024)
    * [Pre-training strategy using real particle collision data for event classification in collider physics](https://arxiv.org/abs/2312.06909) (2023)
    * [A data-driven and model-agnostic approach to solving combinatorial assignment problems in searches for new physics](https://arxiv.org/abs/2309.05728) [[DOI](https://doi.org/10.1103/PhysRevD.109.L011702)] (2023)
    * [NuCLR: Nuclear Co-Learned Representations](https://arxiv.org/abs/2306.06099) (2023)
    * [Unsupervised Domain Transfer for Science: Exploring Deep Learning Methods for Translation between LArTPC Detector Simulations with Differing Response Models](https://arxiv.org/abs/2304.12858) (2023)
    * [Symmetries, Safety, and Self-Supervision](https://arxiv.org/abs/2108.04253) [[DOI](https://doi.org/10.21468/SciPostPhys.12.6.188)] (2021)
    * [Foundations of a Fast, Data-Driven, Machine-Learned Simulator](https://arxiv.org/abs/2101.08944) [[DOI](https://doi.org/10.1038/s41598-022-10966-7)] (2021)
    * [Linearized Optimal Transport for Collider Events](https://arxiv.org/abs/2008.08604) [[DOI](https://doi.org/10.1103/PhysRevD.102.116019)] (2020)
    * [Uncovering latent jet substructure](https://arxiv.org/abs/1904.04200) [[DOI](https://doi.org/10.1103/PhysRevD.100.056002)] (2019)
    * [Learning the latent structure of collider events](https://arxiv.org/abs/2005.12319) [[DOI](https://doi.org/10.1007/JHEP10(2020)206)] (2020)
    * [Metric Space of Collider Events](https://arxiv.org/abs/1902.02346) [[DOI](https://doi.org/10.1103/PhysRevLett.123.041801)] (2019)
    * [Fuzzy Jets](https://arxiv.org/abs/1509.02216) [[DOI](https://doi.org/10.1007/JHEP06(2016)010)] (2015)

    ####  Reinforcement Learning

    * [Reinforcement learning-based statistical search strategy for an axion model from flavor](https://arxiv.org/abs/2409.10023) (2024)
    * [Optimal operation of cryogenic calorimeters through deep reinforcement learning](https://arxiv.org/abs/2311.15147) [[DOI](https://doi.org/10.1007/s41781-024-00119-y)] (2023)
    * [Lattice real-time simulations with learned optimal kernels](https://arxiv.org/abs/2310.08053) [[DOI](https://doi.org/10.1103/PhysRevD.109.L031502)] (2023)
    * [Exploring the flavor structure of quarks and leptons with reinforcement learning](https://arxiv.org/abs/2304.14176) [[DOI](https://doi.org/10.1007/JHEP12(2023)021)] (2023)
    * [Simplifying Polylogarithms with Machine Learning](https://arxiv.org/abs/2206.04115) [[DOI](https://doi.org/10.1142/S2810939223500028)] (2022)
    * [A machine learning pipeline for autonomous numerical analytic continuation of Dyson-Schwinger equations](https://arxiv.org/abs/2112.13011) [[DOI](https://doi.org/10.1051/epjconf/202225809003)] (2021)
    * [Reframing Jet Physics with New Computational Methods](https://arxiv.org/abs/2105.10512) [[DOI](https://doi.org/10.1051/epjconf/202125103059)] (2021)
    * [Particle Physics Model Building with Reinforcement Learning](https://arxiv.org/abs/2103.04759) [[DOI](https://doi.org/10.1007/JHEP08(2021)161)] (2021)
    * [Real-time Artificial Intelligence for Accelerator Control: A Study at the Fermilab Booster](https://arxiv.org/abs/2011.07371) [[DOI](https://doi.org/10.1103/PhysRevAccelBeams.24.104601)] (2020)
    * [Hierarchical clustering in particle physics through reinforcement learning](https://arxiv.org/abs/2011.08191) (2020)
    * [Jet grooming through reinforcement learning](https://arxiv.org/abs/1903.09644) [[DOI](https://doi.org/10.1103/PhysRevD.100.014014)] (2019)

    ####  Quantum Machine Learning

    * [Hybrid quantum-classical approach for combinatorial problems at hadron colliders](https://arxiv.org/abs/2410.22417) (2024)
    * [A novel quantum machine learning classifier to search for new physics](https://arxiv.org/abs/2410.18847) (2024)
    * [Evaluating Modifications to Classifiers for Identification of Higgs Bosons](https://arxiv.org/abs/2409.10902) (2024)
    * [Detect anomalous quartic gauge couplings at muon colliders with quantum kernel k-means](https://arxiv.org/abs/2409.07010) (2024)
    * [New Pathways in Neutrino Physics via Quantum-Encoded Data Analysis](https://arxiv.org/abs/2402.19306) (2024)
    * [Jet Discrimination with Quantum Complete Graph Neural Network](https://arxiv.org/abs/2403.04990) (2024)
    * [CaloQVAE : Simulating high-energy particle-calorimeter interactions using hybrid quantum-classical generative models](https://arxiv.org/abs/2312.03179) (2023)
    * [Quantum Metric Learning for New Physics Searches at the LHC](https://arxiv.org/abs/2311.16866) (2023)
    * [Precise Image Generation on Current Noisy Quantum Computing Devices](https://arxiv.org/abs/2307.05253) [[DOI](https://doi.org/10.1088/2058-9565/ad0389)] (2023)
    * [Unravelling physics beyond the standard model with classical and quantum anomaly detection](https://arxiv.org/abs/2301.10787) [[DOI](https://doi.org/10.1088/2632-2153/ad07f7)] (2023)
    * [Quantum anomaly detection in the latent space of proton collision events at the LHC](https://arxiv.org/abs/2301.10780) (2023)
    * [Generative Invertible Quantum Neural Networks](https://arxiv.org/abs/2302.12906) [[DOI](https://doi.org/10.21468/SciPostPhys.16.6.146)] (2023)
    * [Reconstructing charged particle track segments with a quantum-enhanced support vector machine](https://arxiv.org/abs/2212.07279) [[DOI](https://doi.org/10.1103/PhysRevD.109.052002)] (2022)
    * [Quantum-probabilistic Hamiltonian learning for generative modelling \& anomaly detection](https://arxiv.org/abs/2211.03803) [[DOI](https://doi.org/10.1103/PhysRevA.108.062422)] (2022)
    * [Fitting a Collider in a Quantum Computer: Tackling the Challenges of Quantum Machine Learning for Big Datasets](https://arxiv.org/abs/2211.03233) [[DOI](https://doi.org/10.3389/frai.2023.1268852)] (2022)
    * [Quantum Anomaly Detection for Collider Physics](https://arxiv.org/abs/2206.08391) [[DOI](https://doi.org/10.1007/JHEP02(2023)220)] (2022)
    * [Unsupervised Quantum Circuit Learning in High Energy Physics](https://arxiv.org/abs/2203.03578) [[DOI](https://doi.org/10.1103/PhysRevD.106.096006)] (2022)
    * [Classical versus Quantum: comparing Tensor Network-based Quantum Circuits on LHC data](https://arxiv.org/abs/2202.10471) [[DOI](https://doi.org/10.1103/PhysRevA.106.062423)] (2022)
    * [Completely Quantum Neural Networks](https://arxiv.org/abs/2202.11727) [[DOI](https://doi.org/10.1103/PhysRevA.106.022601)] (2022)
    * [Quantum Machine Learning for $b$-jet identification](https://arxiv.org/abs/2202.13943) [[DOI](https://doi.org/10.1007/JHEP08(2022)014)] (2022)
    * [Anomaly detection in high-energy physics using a quantum autoencoder](https://arxiv.org/abs/2112.04958) [[DOI](https://doi.org/10.1103/PhysRevD.105.095004)] (2021)
    * [Leveraging Quantum Annealer to identify an Event-topology at High Energy Colliders](https://arxiv.org/abs/2111.07806) (2021)
    * [Style-based quantum generative adversarial networks for Monte Carlo events](https://arxiv.org/abs/2110.06933) [[DOI](https://doi.org/10.22331/q-2022-08-17-777)] (2021)
    * [Quantum-inspired event reconstruction with Tensor Networks: Matrix Product States](https://arxiv.org/abs/2106.08334) [[DOI](https://doi.org/10.1007/JHEP08(2021)112)] (2021)
    * [Higgs analysis with quantum classifiers](https://arxiv.org/abs/2104.07692) [[DOI](https://doi.org/10.1051/epjconf/202125103070)] (2021)
    * [Application of Quantum Machine Learning using the Quantum Kernel Algorithm on High Energy Physics Analysis at the LHC](https://arxiv.org/abs/2104.05059) [[DOI](https://doi.org/10.1103/PhysRevResearch.3.033221)] (2021)
    * [Quantum Support Vector Machines for Continuum Suppression in B Meson Decays](https://arxiv.org/abs/2103.12257) [[DOI](https://doi.org/10.1007/s41781-021-00075-x)] (2021)
    * [Unsupervised Event Classification with Graphs on Classical and Photonic Quantum Computers](https://arxiv.org/abs/2103.03897) [[DOI](https://doi.org/10.1007/JHEP08(2021)170)] (2021)
    * [Hybrid Quantum-Classical Graph Convolutional Network](https://arxiv.org/abs/2101.06189) (2021)
    * [Quantum Machine Learning in High Energy Physics](https://arxiv.org/abs/2005.08582) [[DOI](https://doi.org/10.1088/2632-2153/abc17d)] (2020)
    * [Application of Quantum Machine Learning using the Quantum Variational Classifier Method to High Energy Physics Analysis at the LHC on IBM Quantum Computer Simulator and Hardware with 10 qubits](https://arxiv.org/abs/2012.11560) [[DOI](https://doi.org/10.1088/1361-6471/ac1391)] (2020)
    * [Quantum Convolutional Neural Networks for High Energy Physics Data Analysis](https://arxiv.org/abs/2012.12177) [[DOI](https://doi.org/10.1103/PhysRevResearch.4.013231)] (2020)
    * [Event Classification with Quantum Machine Learning in High-Energy Physics](https://arxiv.org/abs/2002.09935) [[DOI](https://doi.org/10.1007/s41781-020-00047-7)] (2020)
    * [Quantum Machine Learning for Particle Physics using a Variational Quantum Classifier](https://arxiv.org/abs/2010.07335) [[DOI](https://doi.org/10.1007/JHEP02(2021)212)] (2020)
    * [Quantum adiabatic machine learning with zooming](https://arxiv.org/abs/1908.04480) [[DOI](https://doi.org/10.1103/PhysRevA.102.062405)] (2019)
    * [Solving a Higgs optimization problem with quantum annealing for machine learning](https://doi.org/10.1038/nature24047) (2017)

    ####  Feature ranking

    * [Feature Selection with Distance Correlation](https://arxiv.org/abs/2212.00046) [[DOI](https://doi.org/10.1103/PhysRevD.109.054009)] (2022)
    * [Resurrecting $b\bar{b}h$ with kinematic shapes](https://arxiv.org/abs/2011.13945) [[DOI](https://doi.org/10.1007/JHEP04(2021)139)] (2020)
    * [Mapping Machine-Learned Physics into a Human-Readable Space](https://arxiv.org/abs/2010.11998) [[DOI](https://doi.org/10.1103/PhysRevD.103.036020)] (2020)

    ####  Attention

    * [Attention to Mean-Fields for Particle Cloud Generation](https://arxiv.org/abs/2305.15254) (2023)
    * [Assessment of few-hits machine learning classification algorithms for low energy physics in liquid argon detectors](https://arxiv.org/abs/2305.09744) [[DOI](https://doi.org/10.1140/epjp/s13360-024-05287-9)] (2023)
    * [Parton Labeling without Matching: Unveiling Emergent Labelling Capabilities in Regression Models](https://arxiv.org/abs/2304.09208) [[DOI](https://doi.org/10.1140/epjc/s10052-023-11809-z)] (2023)
    * [Learning the language of QCD jets with transformers](https://arxiv.org/abs/2303.07364) [[DOI](https://doi.org/10.1007/JHEP06(2023)184)] (2023)
    * [Development of a Vertex Finding Algorithm using Recurrent Neural Network](https://arxiv.org/abs/2101.11906) [[DOI](https://doi.org/10.1016/j.nima.2022.167836)] (2021)

    ####  Regularization

    * [Support vector machine classification on a biased training set: Multi-jet background rejection at hadron colliders](https://arxiv.org/abs/1407.0317) [[DOI](https://doi.org/10.1016/j.nima.2013.04.046)] (2014)
    * [Combine and Conquer: Event Reconstruction with Bayesian Ensemble Neural Networks](https://arxiv.org/abs/2102.01078) [[DOI](https://doi.org/10.1007/JHEP04(2021)296)] (2021)

    ####  Optimal Transport

    * [Chained Quantile Morphing with Normalizing Flows](https://arxiv.org/abs/2309.15912) (2023)
    * [Measurements of multijet event isotropies using optimal transport with the ATLAS detector](https://arxiv.org/abs/2305.16930) [[DOI](https://doi.org/10.1007/JHEP10(2023)060)] (2023)
    * [Optimal transport for a global event description at high-intensity hadron colliders](https://arxiv.org/abs/2211.02029) [[DOI](https://doi.org/10.1103/PhysRevD.108.096003)] (2022)
    * [Background Modeling for Double Higgs Boson Production: Density Ratios and Optimal Transport](https://arxiv.org/abs/2208.02807) (2022)
    * [Which Metric on the Space of Collider Events?](https://arxiv.org/abs/2111.03670) [[DOI](https://doi.org/10.1103/PhysRevD.105.076003)] (2021)
    * [Transport away your problems: Calibrating stochastic simulations with optimal transport](https://arxiv.org/abs/2107.08648) [[DOI](https://doi.org/10.1016/j.nima.2021.166119)] (2021)
    * [Use of a Generalized Energy Mover's Distance in the Search for Rare Phenomena at Colliders](https://arxiv.org/abs/2004.09360) [[DOI](https://doi.org/10.1140/epjc/s10052-021-08891-6)] (2020)
    * [Linearized Optimal Transport for Collider Events](https://arxiv.org/abs/2008.08604) [[DOI](https://doi.org/10.1103/PhysRevD.102.116019)] (2020)
    * [Metric Space of Collider Events](https://arxiv.org/abs/1902.02346) [[DOI](https://doi.org/10.1103/PhysRevLett.123.041801)] (2019)


??? example "Fast inference / deployment"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ### Fast inference / deployment
    </div>

    ####  Software

    * [Learning Efficient Representations of Neutrino Telescope Events](https://arxiv.org/abs/2410.13148) (2024)
    * [Machine learning opportunities for online and offline tagging of photo-induced and diffractive events in continuous readout experiments](https://arxiv.org/abs/2410.06983) (2024)
    * [Implementing dynamic high-performance computing supported workflows on Scanning Transmission Electron Microscope](https://arxiv.org/abs/2406.11018) (2024)
    * [Robust Independent Validation of Experiment and Theory: Rivet version 4 release note](https://arxiv.org/abs/2404.15984) (2024)
    * [RootInteractive tool for multidimensional statistical analysis, machine learning and analytical model validation](https://arxiv.org/abs/2403.19330) [[DOI](https://doi.org/10.1051/epjconf/202429506019)] (2024)
    * [Software Compensation for Highly Granular Calorimeters using Machine Learning](https://arxiv.org/abs/2403.04632) [[DOI](https://doi.org/10.1088/1748-0221/19/04/P04037)] (2024)
    * [Physics analysis for the HL-LHC: concepts and pipelines in practice with the Analysis Grand Challenge](https://arxiv.org/abs/2401.02766) [[DOI](https://doi.org/10.1051/epjconf/202429506016)] (2024)
    * [Machine Learning for Columnar High Energy Physics Analysis](https://arxiv.org/abs/2401.01802) [[DOI](https://doi.org/10.1051/epjconf/202429508011)] (2024)
    * [Distilling particle knowledge for fast reconstruction at high-energy physics experiments](https://arxiv.org/abs/2311.12551) [[DOI](https://doi.org/10.1088/2632-2153/ad43b1)] (2023)
    * [Configurable calorimeter simulation for AI applications](https://arxiv.org/abs/2303.02101) [[DOI](https://doi.org/10.1088/2632-2153/acf186)] (2023)
    * [Data Preservation in High Energy Physics -- DPHEP Global Report 2022](https://arxiv.org/abs/2302.03583) [[DOI](https://doi.org/10.1140/epjc/s10052-023-11885-1)] (2023)
    * [Deep learning level-3 electron trigger for CLAS12](https://arxiv.org/abs/2302.07635) [[DOI](https://doi.org/10.1016/j.cpc.2023.108783)] (2023)
    * [MLAnalysis: An open-source program for high energy physics analyses](https://arxiv.org/abs/2305.00964) [[DOI](https://doi.org/10.1016/j.cpc.2023.108957)] (2023)
    * [FAIR AI Models in High Energy Physics](https://arxiv.org/abs/2212.05081) [[DOI](https://doi.org/10.1088/2632-2153/ad12e3)] (2022)
    * [Exploration of different parameter optimization algorithms within the context of ACTS software framework](https://arxiv.org/abs/2211.00764) (2022)
    * [Deep machine learning for the PANDA software trigger](https://arxiv.org/abs/2211.15390) [[DOI](https://doi.org/10.1140/epjc/s10052-023-11494-y)] (2022)
    * [Event Classification with Multi-step Machine Learning](https://arxiv.org/abs/2106.02301) [[DOI](https://doi.org/10.1051/epjconf/202125103036)] (2021)
    * [Ariadne: PyTorch Library for Particle Track Reconstruction Using Deep Learning](https://arxiv.org/abs/2109.08982) [[DOI](https://doi.org/10.1063/5.0063300)] (2021)
    * [Jet Single Shot Detection](https://arxiv.org/abs/2105.05785) [[DOI](https://doi.org/10.1051/epjconf/202125104027)] (2021)
    * [The Tracking Machine Learning challenge : Throughput phase](https://arxiv.org/abs/2105.01160) [[DOI](https://doi.org/10.1007/s41781-023-00094-w)] (2021)
    * [Towards an Interpretable Data-driven Trigger System for High-throughput Physics Facilities](https://arxiv.org/abs/2104.06622) (2021)
    * [Reduced Precision Strategies for Deep Learning: A High Energy Physics Generative Adversarial Network Use Case](https://arxiv.org/abs/2103.10142) [[DOI](https://doi.org/10.5220/0010245002510258)] (2021)
    * [A comparison of optimisation algorithms for high-dimensional particle and astrophysics applications](https://arxiv.org/abs/2101.04525) [[DOI](https://doi.org/10.1007/JHEP05(2021)108)] (2021)
    * [Fast convolutional neural networks for identifying long-lived particles in a high-granularity calorimeter](https://arxiv.org/abs/2004.10744) [[DOI](https://doi.org/10.1088/1748-0221/15/12/P12006)] (2020)
    * [Using holistic event information in the trigger](https://arxiv.org/abs/1808.00711) (2018)
    * [Topology classification with deep learning to improve real-time event selection at the LHC](https://arxiv.org/abs/1807.00083) [[DOI](https://doi.org/10.1007/s41781-019-0028-1)] (2018)
    * [Deep topology classifiers for a more efficient trigger selection at the LHC](https://dl4physicalsciences.github.io/files/nips_dlps_2017_3.pdf) (2017)
    * [Efficient, reliable and fast high-level triggering using a bonsai boosted decision tree](https://arxiv.org/abs/1210.6861) [[DOI](https://doi.org/10.1088/1748-0221/8/02/P02013)] (2012)
    * [On the impact of modern deep-learning techniques to the performance and time-requirements of classification models in experimental high-energy physics](https://arxiv.org/abs/2002.01427) [[DOI](https://doi.org/10.1088/2632-2153/ab983a)] (2020)

    ####  Hardware/firmware

    * [Performance of the CMS high-level trigger during LHC Run 2](https://arxiv.org/abs/2410.17038) (2024)
    * [Real-time Position Reconstruction for the KamLAND-Zen Experiment using Hardware-AI Co-design](https://arxiv.org/abs/2410.02991) (2024)
    * [Intelligent Pixel Detectors: Towards a Radiation Hard ASIC with On-Chip Machine Learning in 28 nm CMOS](https://arxiv.org/abs/2410.02945) (2024)
    * [Nanosecond hardware regression trees in FPGA at the LHC](https://arxiv.org/abs/2409.20506) (2024)
    * [Ultra-low latency quantum-inspired machine learning predictors implemented on FPGA](https://arxiv.org/abs/2409.16075) (2024)
    * [Comparison of Geometrical Layouts for Next-Generation Large-volume Cherenkov Neutrino Telescopes](https://arxiv.org/abs/2407.19010) (2024)
    * [A Bayesian Framework to Investigate Radiation Reaction in Strong Fields](https://arxiv.org/abs/2406.19420) (2024)
    * [Smart Pixels: In-pixel AI for on-sensor data filtering](https://arxiv.org/abs/2406.14860) [[DOI](https://doi.org/10.1109/NSS/MIC/RTSD57108.2024.10655003)] (2024)
    * [Comprehensive Machine Learning Model Comparison for Cherenkov and Scintillation Light Separation due to Particle Interactions](https://arxiv.org/abs/2406.09191) (2024)
    * [The Neural Network First-Level Hardware Track Trigger of the Belle II Experiment](https://arxiv.org/abs/2402.14962) (2024)
    * [Portable acceleration of CMS computing workflows with coprocessors as a service](https://arxiv.org/abs/2402.15366) [[DOI](https://doi.org/10.1007/s41781-024-00124-1)] (2024)
    * [Smartpixels: Towards on-sensor inference of charged particle track parameters and uncertainties](https://arxiv.org/abs/2312.11676) (2023)
    * [Applications of Lipschitz neural networks to the Run 3 LHCb trigger system](https://arxiv.org/abs/2312.14265) [[DOI](https://doi.org/10.1051/epjconf/202429509005)] (2023)
    * [Testing a Neural Network for Anomaly Detection in the CMS Global Trigger Test Crate during Run 3](https://arxiv.org/abs/2312.10009) [[DOI](https://doi.org/10.1088/1748-0221/19/03/C03029)] (2023)
    * [Neural Network Methods for Radiation Detectors and Imaging](https://arxiv.org/abs/2311.05726) [[DOI](https://doi.org/10.3389/fphy.2024.1334298)] (2023)
    * [Two Watts is All You Need: Enabling In-Detector Real-Time Machine Learning for Neutrino Telescopes Via Edge Computing](https://arxiv.org/abs/2311.04983) [[DOI](https://doi.org/10.1088/1475-7516/2024/06/026)] (2023)
    * [Triggerless data acquisition pipeline for Machine Learning based statistical anomaly detection](https://arxiv.org/abs/2311.02038) [[DOI](https://doi.org/10.1051/epjconf/202429502033)] (2023)
    * [Smart pixel sensors: towards on-sensor filtering of pixel clusters with deep learning](https://arxiv.org/abs/2310.02474) [[DOI](https://doi.org/10.1088/2632-2153/ad6a00)] (2023)
    * [Development of the Topological Trigger for LHCb Run 3](https://arxiv.org/abs/2306.09873) (2023)
    * [Comparing machine learning models for tau triggers](https://arxiv.org/abs/2306.06743) (2023)
    * [Tetris-inspired detector with neural network for radiation mapping](https://arxiv.org/abs/2302.07099) [[DOI](https://doi.org/10.1038/s41467-024-47338-w)] (2023)
    * [Real-time Graph Building on FPGAs for Machine Learning Trigger Applications in Particle Physics](https://arxiv.org/abs/2307.07289) [[DOI](https://doi.org/10.1007/s41781-024-00117-0)] (2023)
    * [Fast Neural Network Inference on FPGAs for Triggering on Long-Lived Particles at Colliders](https://arxiv.org/abs/2307.05152) [[DOI](https://doi.org/10.1088/2632-2153/ad087a)] (2023)
    * [Implementation of a framework for deploying AI inference engines in FPGAs](https://arxiv.org/abs/2305.19455) (2023)
    * [Accelerating Machine Learning Inference with GPUs in ProtoDUNE Data Processing](https://arxiv.org/abs/2301.04633) [[DOI](https://doi.org/10.1007/s41781-023-00101-0)] (2023)
    * [Neural-network-based level-1 trigger upgrade for the SuperCDMS experiment at SNOLAB](https://arxiv.org/abs/2212.07864) [[DOI](https://doi.org/10.1088/1748-0221/18/06/P06012)] (2022)
    * [Charged Particle Tracking with Machine Learning on FPGAs](https://arxiv.org/abs/2212.02348) (2022)
    * [Nanosecond machine learning regression with deep boosted decision trees in FPGA for high energy physics](https://arxiv.org/abs/2207.05602) [[DOI](https://doi.org/10.1088/1748-0221/17/09/P09039)] (2022)
    * [Ultra-low latency recurrent neural network inference on FPGAs for physics applications with hls4ml](https://arxiv.org/abs/2207.00559) [[DOI](https://doi.org/10.1088/2632-2153/acc0d7)] (2022)
    * [Fast muon tracking with machine learning implemented in FPGA](https://arxiv.org/abs/2202.04976) [[DOI](https://doi.org/10.1016/j.nima.2022.167546)] (2022)
    * [Ephemeral Learning -- Augmenting Triggers with Online-Trained Normalizing Flows](https://arxiv.org/abs/2202.09375) [[DOI](https://doi.org/10.21468/SciPostPhys.13.4.087)] (2022)
    * [Accelerating Deep Neural Networks for Real-time Data Selection for High-resolution Imaging Particle Detectors](https://arxiv.org/abs/2201.04740) [[DOI](https://doi.org/10.1109/NYSDS.2019.8909784)] (2022)
    * [Graph Neural Networks for Charged Particle Tracking on FPGAs](https://arxiv.org/abs/2112.02048) [[DOI](https://doi.org/10.3389/fdata.2022.828666)] (2021)
    * [Autoencoders on FPGAs for real-time, unsupervised new physics detection at 40 MHz at the Large Hadron Collider](https://arxiv.org/abs/2108.03986) [[DOI](https://doi.org/10.1038/s42256-022-00441-3)] (2021)
    * [Muon trigger with fast Neural Networks on FPGA, a demonstrator](https://arxiv.org/abs/2105.04428) [[DOI](https://doi.org/10.1088/1742-6596/2374/1/012099)] (2021)
    * [A reconfigurable neural network ASIC for detector front-end data compression at the HL-LHC](https://arxiv.org/abs/2105.01683) [[DOI](https://doi.org/10.1109/TNS.2021.3087100)] (2021)
    * [Nanosecond machine learning event classification with boosted decision trees in FPGA for high energy physics](https://arxiv.org/abs/2104.03408) [[DOI](https://doi.org/10.1088/1748-0221/16/08/P08016)] (2021)
    * [Sparse Deconvolution Methods for Online Energy Estimation in Calorimeters Operating in High Luminosity Conditions](https://arxiv.org/abs/2103.12467) [[DOI](https://doi.org/10.1088/1748-0221/16/09/P09008)] (2021)
    * [Ps and Qs: Quantization-aware pruning for efficient low latency neural network inference](https://arxiv.org/abs/2102.11289) [[DOI](https://doi.org/10.3389/frai.2021.676564)] (2021)
    * [Fast convolutional neural networks on FPGAs with hls4ml](https://arxiv.org/abs/2101.05108) [[DOI](https://doi.org/10.1088/2632-2153/ac0ea1)] (2021)
    * [PDFFlow: hardware accelerating parton density access](https://arxiv.org/abs/2012.08221) [[DOI](https://doi.org/10.5821/zenodo.4286175)] (2020)
    * [Accelerated Charged Particle Tracking with Graph Neural Networks on FPGAs](https://arxiv.org/abs/2012.01563) (2020)
    * [FPGAs-as-a-Service Toolkit (FaaST)](https://arxiv.org/abs/2010.08556) [[DOI](https://doi.org/10.1109/H2RC51942.2020.00010)] (2020)
    * [PDFFlow: parton distribution functions on GPU](https://arxiv.org/abs/2009.06635) [[DOI](https://doi.org/10.1016/j.cpc.2021.107995)] (2020)
    * [Studying the potential of Graphcore IPUs for applications in Particle Physics](https://arxiv.org/abs/2008.09210) [[DOI](https://doi.org/10.1007/s41781-021-00057-z)] (2020)
    * [Distance-Weighted Graph Neural Networks on FPGAs for Real-Time Particle Reconstruction in High Energy Physics](https://arxiv.org/abs/2008.03601) [[DOI](https://doi.org/10.3389/fdata.2020.598927)] (2020)
    * [GPU coprocessors as a service for deep learning inference in high energy physics](https://arxiv.org/abs/2007.10359) [[DOI](https://doi.org/10.1088/2632-2153/abec21)] (2020)
    * [Fast inference of Boosted Decision Trees in FPGAs for particle physics](https://arxiv.org/abs/2002.02534) [[DOI](https://doi.org/10.1088/1748-0221/15/05/P05026)] (2020)
    * [Compressing deep neural networks on FPGAs to binary and ternary precision with HLS4ML](https://arxiv.org/abs/2003.06308) [[DOI](https://doi.org/10.1088/2632-2153/aba042)] (2020)
    * [Fast inference of deep neural networks in FPGAs for particle physics](https://arxiv.org/abs/1804.06913) [[DOI](https://doi.org/10.1088/1748-0221/13/07/P07027)] (2018)

    ####  Deployment

    * [HEP ML Lab: An end-to-end framework for applying machine learning into phenomenology studies](https://arxiv.org/abs/2405.02888) (2024)
    * [Classifier Surrogates: Sharing AI-based Searches with the World](https://arxiv.org/abs/2402.15558) [[DOI](https://doi.org/10.1140/epjc/s10052-024-13353-w)] (2024)
    * [Optimizing High Throughput Inference on Graph Neural Networks at Shared Computing Facilities with the NVIDIA Triton Inference Server](https://arxiv.org/abs/2312.06838) [[DOI](https://doi.org/10.1007/s41781-024-00123-2)] (2023)
    * [Jet energy calibration with deep learning as a Kubeflow pipeline](https://arxiv.org/abs/2308.12724) [[DOI](https://doi.org/10.1007/s41781-023-00103-y)] (2023)
    * [Distributed training and scalability for the particle clustering method UCluster](https://arxiv.org/abs/2109.00264) [[DOI](https://doi.org/10.1051/epjconf/202125102054)] (2021)
    * [MLaaS4HEP: Machine Learning as a Service for HEP](https://arxiv.org/abs/2007.14781) [[DOI](https://doi.org/10.1007/s41781-021-00061-3)] (2020)

##  Regression

??? example "Pileup"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Pileup
    </div>

    * [Variational inference for pile-up removal at hadron colliders with diffusion models](https://arxiv.org/abs/2410.22074) (2024)
    * [High Pileup Particle Tracking with Object Condensation](https://arxiv.org/abs/2312.03823) (2023)
    * [Restoring original signals from pile-up using deep learning](https://arxiv.org/abs/2304.14496) [[DOI](https://doi.org/10.1016/j.nima.2023.168492)] (2023)
    * [Towards an automated data cleaning with deep learning in CRESST](https://arxiv.org/abs/2211.00564) [[DOI](https://doi.org/10.1140/epjp/s13360-023-03674-2)] (2022)
    * [Semi-supervised Graph Neural Networks for Pileup Noise Removal](https://arxiv.org/abs/2203.15823) [[DOI](https://doi.org/10.1140/epjc/s10052-022-11083-5)] (2022)
    * [Pile-Up Mitigation using Attention](https://arxiv.org/abs/2107.02779) [[DOI](https://doi.org/10.1088/2632-2153/ac7198)] (2021)
    * [Jet grooming through reinforcement learning](https://arxiv.org/abs/1903.09644) [[DOI](https://doi.org/10.1103/PhysRevD.100.014014)] (2019)
    * [Pileup mitigation at the Large Hadron Collider with graph neural networks](https://arxiv.org/abs/1810.07988) [[DOI](https://doi.org/10.1140/epjp/i2019-12710-3)] (2018)
    * [Convolutional Neural Networks with Event Images for Pileup Mitigation with the ATLAS Detector](http://cds.cern.ch/record/2684070) (2019)
    * [Pileup Mitigation with Machine Learning (PUMML)](https://arxiv.org/abs/1707.08600) [[DOI](https://doi.org/10.1007/JHEP12(2017)051)] (2017)


??? example "Calibration"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Calibration
    </div>

    * [Reweighting simulated events using machine-learning techniques in the CMS experiment](https://arxiv.org/abs/2411.03023) (2024)
    * [Vertex Imaging Hadron Calorimetry Using AI/ML Tools](https://arxiv.org/abs/2408.15385) (2024)
    * [ML-based Calibration and Control of the GlueX Central Drift Chamber](https://arxiv.org/abs/2403.13823) (2024)
    * [A Comparison of Deep Learning Models for Proton Background Rejection with the AMS Electromagnetic Calorimeter](https://arxiv.org/abs/2402.16285) (2024)
    * [Machine learning based event reconstruction for the MUonE experiment](https://arxiv.org/abs/2402.02913) [[DOI](https://doi.org/10.7494/csci.2024.25.1.5690)] (2024)
    * [Using deep neural networks to improve the precision of fast-sampled particle timing detectors](https://arxiv.org/abs/2312.05883) [[DOI](https://doi.org/10.7494/csci.2024.25.1.5784)] (2023)
    * [The Optimal use of Segmentation for Sampling Calorimeters](https://arxiv.org/abs/2310.04442) [[DOI](https://doi.org/10.1088/1748-0221/19/06/P06002)] (2023)
    * [Refining fast simulation using machine learning](https://arxiv.org/abs/2309.12919) [[DOI](https://doi.org/10.1051/epjconf/202429509032)] (2023)
    * [Jet energy calibration with deep learning as a Kubeflow pipeline](https://arxiv.org/abs/2308.12724) [[DOI](https://doi.org/10.1007/s41781-023-00103-y)] (2023)
    * [A first application of machine and deep learning for background rejection in the ALPS II TES detector](https://arxiv.org/abs/2304.08406) [[DOI](https://doi.org/10.1002/andp.202200545)] (2023)
    * [Correction of the baseline fluctuations in the GEM-based ALICE TPC](https://arxiv.org/abs/2304.03881) [[DOI](https://doi.org/10.1088/1748-0221/18/11/P11021)] (2023)
    * [New techniques for jet calibration with the ATLAS detector](https://arxiv.org/abs/2303.17312) [[DOI](https://doi.org/10.1140/epjc/s10052-023-11837-9)] (2023)
    * [Removing Noise From Simulated Events at The Main Drift Chamber of BESIII Using Convolutional Neural Networks](https://arxiv.org/abs/2303.12202) (2023)
    * [$\nu^2$-Flows: Fast and improved neutrino reconstruction in multi-neutrino final states with conditional normalizing flows](https://arxiv.org/abs/2307.02405) [[DOI](https://doi.org/10.1103/PhysRevD.109.012005)] (2023)
    * [Nuclear corrections on the charged hadron fragmentation functions in a Neural Network global QCD analysis](https://arxiv.org/abs/2305.02664) [[DOI](https://doi.org/10.1140/epjp/s13360-024-05571-8)] (2023)
    * [Fast kernel methods for Data Quality Monitoring as a goodness-of-fit test](https://arxiv.org/abs/2303.05413) [[DOI](https://doi.org/10.1088/2632-2153/acebb7)] (2023)
    * [A fast and flexible machine learning approach to data quality monitoring](https://arxiv.org/abs/2301.08917) (2023)
    * [Estimation of collision centrality in terms of the number of participating nucleons in heavy-ion collisions using deep learning](https://arxiv.org/abs/2305.00493) [[DOI](https://doi.org/10.1140/epja/s10050-023-01087-4)] (2023)
    * [A neural network for beam background decomposition in Belle~II at SuperKEKB](https://arxiv.org/abs/2301.06170) [[DOI](https://doi.org/10.1016/j.nima.2023.168112)] (2023)
    * [Restoring the saturation response of a PMT using pulse shape and artificial neural networks](https://arxiv.org/abs/2302.06170) [[DOI](https://doi.org/10.1093/ptep/ptad047)] (2023)
    * [Firmware implementation of a recurrent neural network for the computation of the energy deposited in the liquid argon calorimeter of the ATLAS experiment](https://arxiv.org/abs/2302.07555) [[DOI](https://doi.org/10.1088/1748-0221/18/05/P05017)] (2023)
    * [Machine learning approaches for parameter reweighting for MC samples of top quark production in CMS](https://arxiv.org/abs/2211.07355) [[DOI](https://doi.org/10.22323/1.414.1045)] (2022)
    * [A new method for the $q^2$ reconstruction in semileptonic decays at LHCb based on machine learning](https://arxiv.org/abs/2208.02145) [[DOI](https://doi.org/10.1155/2023/8127604)] (2022)
    * [Machine Learned Particle Detector Simulations](https://arxiv.org/abs/2207.11254) (2022)
    * [$\nu$-Flows: conditional neutrino regression](https://arxiv.org/abs/2207.00664) [[DOI](https://doi.org/10.21468/SciPostPhys.14.6.159)] (2022)
    * [Deep learning techniques for energy clustering in the CMS ECAL](https://arxiv.org/abs/2204.10277) [[DOI](https://doi.org/10.1088/1742-6596/2438/1/012077)] (2022)
    * [Bias and Priors in Machine Learning Calibrations for High Energy Physics](https://arxiv.org/abs/2205.05084) [[DOI](https://doi.org/10.1103/PhysRevD.106.036011)] (2022)
    * [Learning Uncertainties the Frequentist Way: Calibration and Correlation in High Energy Physics](https://arxiv.org/abs/2205.03413) [[DOI](https://doi.org/10.1103/PhysRevLett.129.082001)] (2022)
    * [Deep learning applications for quality control in particle detector construction](https://arxiv.org/abs/2203.08969) (2022)
    * [A Holistic Approach to Predicting Top Quark Kinematic Properties with the Covariant Particle Transformer](https://arxiv.org/abs/2203.05687) [[DOI](https://doi.org/10.1103/PhysRevD.107.114029)] (2022)
    * [Reconstruction of Missing Resonances Combining Nearest Neighbors Regressors and Neural Network Classifiers](https://arxiv.org/abs/2203.03662) [[DOI](https://doi.org/10.1140/epjc/s10052-022-10714-1)] (2022)
    * [Deep Regression of Muon Energy with a K-Nearest Neighbor Algorithm](https://arxiv.org/abs/2203.02841) (2022)
    * [Machine-learning-based prediction of parameters of secondaries in hadronic showers using calorimetric observables](https://arxiv.org/abs/2205.12534) [[DOI](https://doi.org/10.1088/1748-0221/17/10/P10031)] (2022)
    * [Machine Learning for Particle Flow Reconstruction at CMS](https://arxiv.org/abs/2203.00330) [[DOI](https://doi.org/10.1088/1742-6596/2438/1/012100)] (2022)
    * [Reconstructing partonic kinematics at colliders with Machine Learning](https://arxiv.org/abs/2112.05043) [[DOI](https://doi.org/10.21468/SciPostPhysCore.5.4.049)] (2021)
    * [Implicit Quantile Neural Networks for Jet Simulation and Correction](https://arxiv.org/abs/2111.11415) (2021)
    * [Reconstructing the Kinematics of Deep Inelastic Scattering with Deep Learning](https://arxiv.org/abs/2110.05505) [[DOI](https://doi.org/10.1016/j.nima.2021.166164)] (2021)
    * [Using Convolutional Neural Networks to Reconstruct Energy of GeV Scale IceCube Neutrinos](https://arxiv.org/abs/2109.08152) [[DOI](https://doi.org/10.1088/1748-0221/16/09/C09019)] (2021)
    * [Energy reconstruction in a liquid argon calorimeter cell using convolutional neural networks](https://arxiv.org/abs/2109.05124) [[DOI](https://doi.org/10.1088/1748-0221/17/01/P01002)] (2021)
    * [Deeply Learning Deep Inelastic Scattering Kinematics](https://arxiv.org/abs/2108.11638) [[DOI](https://doi.org/10.1140/epjc/s10052-022-10964-z)] (2021)
    * [Perspectives on the Calibration of CNN Energy Reconstruction in Highly Granular Calorimeters](https://arxiv.org/abs/2108.10963) (2021)
    * [Object condensation: one-stage grid-free multi-object reconstruction in physics detectors, graph and image data](https://arxiv.org/abs/2002.03605) [[DOI](https://doi.org/10.1140/epjc/s10052-020-08461-2)] (2020)
    * [On the Use of Neural Networks for Energy Reconstruction in High-granularity Calorimeters](https://arxiv.org/abs/2107.10207) [[DOI](https://doi.org/10.1088/1748-0221/16/12/P12036)] (2021)
    * [Transport away your problems: Calibrating stochastic simulations with optimal transport](https://arxiv.org/abs/2107.08648) [[DOI](https://doi.org/10.1016/j.nima.2021.166119)] (2021)
    * [Calorimetric Measurement of Multi-TeV Muons via Deep Regression](https://arxiv.org/abs/2107.02119) [[DOI](https://doi.org/10.1140/epjc/s10052-022-09993-5)] (2021)
    * [Deep learning jet modifications in heavy-ion collisions](https://arxiv.org/abs/2012.07797) [[DOI](https://doi.org/10.1007/JHEP03(2021)206)] (2020)
    * [How to GAN Higher Jet Resolution](https://arxiv.org/abs/2012.11944) [[DOI](https://doi.org/10.21468/SciPostPhys.13.3.064)] (2020)
    * [A deep neural network for simultaneous estimation of b jet energy and resolution](https://arxiv.org/abs/1912.06046) [[DOI](https://doi.org/10.1007/s41781-020-00041-z)] (2019)
    * [Per-Object Systematics using Deep-Learned Calibration](https://arxiv.org/abs/2003.11099) [[DOI](https://doi.org/10.21468/SciPostPhys.9.6.089)] (2020)
    * [Calorimetry with Deep Learning: Particle Classification, Energy Regression, and Simulation for High-Energy Physics](https://dl4physicalsciences.github.io/files/nips_dlps_2017_15.pdf) (2017)
    * [Generalized Numerical Inversion: A Neural Network Approach to Jet Calibration](http://cds.cern.ch/record/2630972) (2018)
    * [Simultaneous Jet Energy and Mass Calibrations with Neural Networks](http://cds.cern.ch/record/2706189) (2020)
    * [Parametrizing the Detector Response with Neural Networks](https://arxiv.org/abs/1910.03773) [[DOI](https://doi.org/10.1088/1748-0221/15/01/P01030)] (2019)


??? example "Recasting"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Recasting
    </div>

    * [HackAnalysis 2: A powerful and hackable recasting tool](https://arxiv.org/abs/2406.10042) (2024)
    * [Exploration of Parameter Spaces Assisted by Machine Learning](https://arxiv.org/abs/2207.09959) [[DOI](https://doi.org/10.1016/j.cpc.2023.108902)] (2022)
    * [Bayesian Neural Networks for Fast SUSY Predictions](https://arxiv.org/abs/2007.04506) [[DOI](https://doi.org/10.1016/j.physletb.2020.136041)] (2020)
    * [Accelerating the BSM interpretation of LHC data with machine learning](https://arxiv.org/abs/1611.02704) [[DOI](https://doi.org/10.1016/j.dark.2019.100293)] (2016)
    * [The BSM-AI project: SUSY-AI--generalizing LHC limits on supersymmetry with machine learning](https://arxiv.org/abs/1605.02797) [[DOI](https://doi.org/10.1140/epjc/s10052-017-4814-9)] (2016)


??? example "Matrix elements"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Matrix elements
    </div>

    * [The MadNIS Reloaded](https://arxiv.org/abs/2311.01548) [[DOI](https://doi.org/10.21468/SciPostPhys.17.1.023)] (2023)
    * [Pole-fitting for complex functions: Enhancing standard techniques by artificial-neural-network classifiers and regressors](https://arxiv.org/abs/2309.08358) [[DOI](https://doi.org/10.1016/j.cpc.2023.108998)] (2023)
    * [One-loop matrix element emulation with factorisation awareness](https://arxiv.org/abs/2302.04005) [[DOI](https://doi.org/10.1007/JHEP05(2023)159)] (2023)
    * [Unweighting multijet event generation using factorisation-aware neural networks](https://arxiv.org/abs/2301.13562) [[DOI](https://doi.org/10.21468/SciPostPhys.15.3.107)] (2023)
    * [Loop Amplitudes from Precision Networks](https://arxiv.org/abs/2206.14831) [[DOI](https://doi.org/10.21468/SciPostPhysCore.6.2.034)] (2022)
    * [Simplifying Polylogarithms with Machine Learning](https://arxiv.org/abs/2206.04115) [[DOI](https://doi.org/10.1142/S2810939223500028)] (2022)
    * [SYMBA: Symbolic Computation of Squared Amplitudes in High Energy Physics with Machine ALearning](https://arxiv.org/abs/2206.08901) [[DOI](https://doi.org/10.1088/2632-2153/acb2b2)] (2022)
    * [Fast and precise model calculation for KATRIN using a neural network](https://arxiv.org/abs/2201.04523) [[DOI](https://doi.org/10.1140/epjc/s10052-022-10384-z)] (2022)
    * [Targeting Multi-Loop Integrals with Neural Networks](https://arxiv.org/abs/2112.09145) [[DOI](https://doi.org/10.21468/SciPostPhys.12.4.129)] (2021)
    * [Accelerating Monte Carlo event generation -- rejection sampling using neural network event-weight estimates](https://arxiv.org/abs/2109.11964) [[DOI](https://doi.org/10.21468/SciPostPhys.12.5.164)] (2021)
    * [A factorisation-aware Matrix element emulator](https://arxiv.org/abs/2107.06625) [[DOI](https://doi.org/10.1007/JHEP11(2021)066)] (2021)
    * [Optimising simulations for diphoton production at hadron colliders using amplitude neural networks](https://arxiv.org/abs/2106.09474) [[DOI](https://doi.org/10.1007/JHEP08(2021)066)] (2021)
    * [Model independent analysis of coupled-channel scattering: a deep learning approach](https://arxiv.org/abs/2105.04898) [[DOI](https://doi.org/10.1103/PhysRevD.104.036001)] (2021)
    * [Unveiling the pole structure of S-matrix using deep learning](https://arxiv.org/abs/2104.14182) [[DOI](https://doi.org/10.31349/SuplRevMexFis.3.0308067)] (2021)
    * [Matrix Element Regression with Deep Neural Networks -- breaking the CPU barrier](https://arxiv.org/abs/2008.10949) [[DOI](https://doi.org/10.1007/JHEP04(2021)020)] (2020)
    * [$\textsf{Xsec}$: the cross-section evaluation code](https://arxiv.org/abs/2006.16273) [[DOI](https://doi.org/10.1140/epjc/s10052-020-08635-y)] (2020)
    * [(Machine) Learning Amplitudes for Faster Event Generation](https://arxiv.org/abs/1912.11055) [[DOI](https://doi.org/10.1103/PhysRevD.107.L071901)] (2019)
    * [Using neural networks for efficient evaluation of high multiplicity scattering amplitudes](https://arxiv.org/abs/2002.07516) [[DOI](https://doi.org/10.1007/JHEP06(2020)114)] (2020)


??? example "Parameter estimation"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Parameter estimation
    </div>

    * [Estimating event-by-event multiplicity by a Machine Learning Method for Hadronization Studies](https://arxiv.org/abs/2408.17130) (2024)
    * [Reconstruction of electromagnetic showers in calorimeters using Deep Learning](https://arxiv.org/abs/2311.17914) [[DOI](https://doi.org/10.1140/epjc/s10052-024-12978-1)] (2023)
    * [Training Deep 3D Convolutional Neural Networks to Extract BSM Physics Parameters Directly from HEP Data: a Proof-of-Concept Study Using Monte Carlo Simulations](https://arxiv.org/abs/2311.13060) (2023)
    * [First attempt of directionality reconstruction for atmospheric neutrinos in a large homogeneous liquid scintillator detector](https://arxiv.org/abs/2310.06281) [[DOI](https://doi.org/10.1103/PhysRevD.109.052005)] (2023)
    * [Improving the temporal resolution of event-based electron detectors using neural network cluster analysis](https://arxiv.org/abs/2307.16666) [[DOI](https://doi.org/10.1016/j.ultramic.2023.113881)] (2023)
    * [Determination of high-energy hadronic interaction properties from observables of proton initiated extensive air showers](https://arxiv.org/abs/2304.08007) (2023)
    * [$\Sigma$ Resonances from a Neural Network-based Partial Wave Analysis on $K^-p$ Scattering](https://arxiv.org/abs/2305.01852) (2023)
    * [Neural network predictions of inclusive electron-nucleus cross sections](https://arxiv.org/abs/2305.08217) [[DOI](https://doi.org/10.1103/PhysRevC.107.065501)] (2023)
    * [Parton Labeling without Matching: Unveiling Emergent Labelling Capabilities in Regression Models](https://arxiv.org/abs/2304.09208) [[DOI](https://doi.org/10.1140/epjc/s10052-023-11809-z)] (2023)
    * [Exploration of different parameter optimization algorithms within the context of ACTS software framework](https://arxiv.org/abs/2211.00764) (2022)
    * [Machine Learning Assisted Vector Atomic Magnetometry](https://arxiv.org/abs/2301.05707) [[DOI](https://doi.org/10.1038/s41467-023-41676-x)] (2023)
    * [LHC EFT WG Report: Experimental Measurements and Observables](https://arxiv.org/abs/2211.08353) (2022)
    * [Machine learning a manifold](https://arxiv.org/abs/2112.07673) [[DOI](https://doi.org/10.1103/PhysRevD.105.096030)] (2021)
    * [Using Machine Learning techniques in phenomenological studies in flavour physics](https://arxiv.org/abs/2109.07405) [[DOI](https://doi.org/10.1007/JHEP07(2022)115)] (2021)
    * [Deep-Learned Event Variables for Collider Phenomenology](https://arxiv.org/abs/2105.10126) [[DOI](https://doi.org/10.1103/PhysRevD.107.L031904)] (2021)
    * [MCNNTUNES: tuning Shower Monte Carlo generators with machine learning](https://arxiv.org/abs/2010.02213) [[DOI](https://doi.org/10.1016/j.cpc.2021.107908)] (2020)
    * [Parametrized classifiers for optimal EFT sensitivity](https://arxiv.org/abs/2007.10356) [[DOI](https://doi.org/10.1007/JHEP05(2021)247)] (2020)
    * [Numerical analysis of neutrino physics within a high scale supersymmetry model via machine learning](https://arxiv.org/abs/2006.01495) [[DOI](https://doi.org/10.1142/S0217732320502181)] (2020)


??? example "Parton Distribution Functions (and related)"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Parton Distribution Functions (and related)
    </div>

    * [Polarized and unpolarized gluon PDFs: generative machine learning applications for lattice QCD matrix elements at short distance and large momentum](https://arxiv.org/abs/2409.17234) (2024)
    * [Explainable AI classification for parton density theory](https://arxiv.org/abs/2407.03411) (2024)
    * [Extraction of Information from Polarized Deep Exclusive Scattering with Machine Learning](https://arxiv.org/abs/2406.09258) (2024)
    * [A generalized statistical model for fits to parton distributions](https://arxiv.org/abs/2406.01664) (2024)
    * [NNPDF4.0 aN$^3$LO PDFs with QED corrections](https://arxiv.org/abs/2406.01779) (2024)
    * [Using analytic models to describe effective PDFs](https://arxiv.org/abs/2404.15175) [[DOI](https://doi.org/10.1103/PhysRevD.110.036019)] (2024)
    * [Determination of $K^0_S$ Fragmentation Functions including BESIII Measurements and using Neural Networks](https://arxiv.org/abs/2404.07334) [[DOI](https://doi.org/10.1103/PhysRevD.110.014019)] (2024)
    * [Helicity-dependent parton distribution functions at next-to-next-to-leading order accuracy from inclusive and semi-inclusive deep-inelastic scattering data](https://arxiv.org/abs/2404.04712) (2024)
    * [SIMUnet: an open-source tool for simultaneous global fits of EFT Wilson coefficients and PDFs](https://arxiv.org/abs/2402.03308) [[DOI](https://doi.org/10.1140/epjc/s10052-024-13079-9)] (2024)
    * [Using Machine Learning to Improve PDF Uncertainties](https://arxiv.org/abs/2401.13050) (2024)
    * [Unraveling generalized parton distributions through Lorentz symmetry and partial DGLAP knowledge](https://arxiv.org/abs/2401.12013) [[DOI](https://doi.org/10.1103/PhysRevD.109.096013)] (2024)
    * [Determination of the theory uncertainties from missing higher orders on NNLO parton distributions with percent accuracy](https://arxiv.org/abs/2401.10319) [[DOI](https://doi.org/10.1140/epjc/s10052-024-12772-z)] (2024)
    * [Photons in the proton: implications for the LHC](https://arxiv.org/abs/2401.08749) [[DOI](https://doi.org/10.1140/epjc/s10052-024-12731-8)] (2024)
    * [Learning PDFs through Interpretable Latent Representations in Mellin Space](https://arxiv.org/abs/2312.02278) (2023)
    * [Towards an integrated determination of proton, deuteron and nuclear PDFs](https://arxiv.org/abs/2307.05967) (2023)
    * [A Modern Global Extraction of the Sivers Function](https://arxiv.org/abs/2304.14328) [[DOI](https://doi.org/10.1103/PhysRevD.108.054007)] (2023)
    * [Research on the distribution formula of QCD strong coupling constant in medium and high energy scale region based on symbolic regression algorithm](https://arxiv.org/abs/2304.07682) [[DOI](https://doi.org/10.1088/0256-307X/41/3/031201)] (2023)
    * [The top quark legacy of the LHC Run II for PDF and SMEFT analyses](https://arxiv.org/abs/2303.06159) [[DOI](https://doi.org/10.1007/JHEP05(2023)205)] (2023)
    * [Determination of the distribution of strong coupling constant with machine learning](https://arxiv.org/abs/2303.07968) (2023)
    * [Neutrino Structure Functions from GeV to EeV Energies](https://arxiv.org/abs/2302.08527) [[DOI](https://doi.org/10.1007/JHEP05(2023)149)] (2023)
    * [Simultaneous CTEQ-TEA extraction of PDFs and SMEFT parameters from jet and $ t\overline{t} $ data](https://arxiv.org/abs/2211.01094) [[DOI](https://doi.org/10.1007/JHEP05(2023)003)] (2022)
    * [Unpolarized proton PDF at NNLO from lattice QCD with physical quark masses](https://arxiv.org/abs/2212.12569) [[DOI](https://doi.org/10.1103/PhysRevD.107.074509)] (2022)
    * [A new generation of simultaneous fits to LHC data using deep learning](https://arxiv.org/abs/2201.07240) [[DOI](https://doi.org/10.1007/JHEP05(2022)032)] (2022)
    * [Exploring the substructure of nucleons and nuclei with machine learning](https://arxiv.org/abs/2110.01924) (2021)
    * [An open-source machine learning framework for global analyses of parton distributions](https://arxiv.org/abs/2109.02671) [[DOI](https://doi.org/10.1140/epjc/s10052-021-09747-9)] (2021)
    * [The Path to Proton Structure at One-Percent Accuracy](https://arxiv.org/abs/2109.02653) [[DOI](https://doi.org/10.1140/epjc/s10052-022-10328-7)] (2021)
    * [Compressing PDF sets using generative adversarial networks](https://arxiv.org/abs/2104.04535) [[DOI](https://doi.org/10.1140/epjc/s10052-021-09338-8)] (2021)
    * [PDFFlow: hardware accelerating parton density access](https://arxiv.org/abs/2012.08221) [[DOI](https://doi.org/10.5821/zenodo.4286175)] (2020)
    * [Deep Learning Analysis of Deeply Virtual Exclusive Photoproduction](https://arxiv.org/abs/2012.04801) [[DOI](https://doi.org/10.1103/PhysRevD.104.016001)] (2020)
    * [Neural-network analysis of Parton Distribution Functions from Ioffe-time pseudodistributions](https://arxiv.org/abs/2010.03996) [[DOI](https://doi.org/10.1007/JHEP02(2021)138)] (2020)


??? example "Lattice Gauge Theory"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Lattice Gauge Theory
    </div>

    * [Diffusion models for lattice gauge field simulations](https://arxiv.org/abs/2410.19602) (2024)
    * [Continuous normalizing flows for lattice gauge theories](https://arxiv.org/abs/2410.13161) (2024)
    * [Building Hadron Potentials from Lattice QCD with Deep Neural Networks](https://arxiv.org/abs/2410.03082) (2024)
    * [A Variational Approach to Quantum Field Theory](https://arxiv.org/abs/2409.17887) (2024)
    * [Estimation of the pseudoscalar glueball mass based on a modified Transformer](https://arxiv.org/abs/2408.13280) (2024)
    * [Neural Network Modeling of Heavy-Quark Potential from Holography](https://arxiv.org/abs/2408.03784) (2024)
    * [Study of the mass of pseudoscalar glueball with a deep neural network](https://arxiv.org/abs/2407.12010) (2024)
    * [Disordered Lattice Glass $\phi^{4}$ Quantum Field Theory](https://arxiv.org/abs/2407.06569) (2024)
    * [Berezinskii--Kosterlitz--Thouless transition of the two-dimensional $XY$ model on the honeycomb lattice](https://arxiv.org/abs/2406.14812) (2024)
    * [QCD Phase Diagram at finite Magnetic Field and Chemical Potential: A Holographic Approach Using Machine Learning](https://arxiv.org/abs/2406.12772) (2024)
    * [Generating configurations of increasing lattice size with machine learning and the inverse renormalization group](https://arxiv.org/abs/2405.16288) [[DOI](https://doi.org/10.22323/1.451.0001)] (2024)
    * [Deep learning lattice gauge theories](https://arxiv.org/abs/2405.14830) [[DOI](https://doi.org/10.1103/PhysRevB.110.165133)] (2024)
    * [Building imaginary-time thermal filed theory with artificial neural networks](https://arxiv.org/abs/2405.10493) [[DOI](https://doi.org/10.1088/1674-1137/ad5f80)] (2024)
    * [Flavor dependent Critical endpoint from holographic QCD through machine learning](https://arxiv.org/abs/2405.06179) (2024)
    * [Flow-based Nonperturbative Simulation of First-order Phase Transitions](https://arxiv.org/abs/2404.18323) (2024)
    * [Multiscale Normalizing Flows for Gauge Theories](https://arxiv.org/abs/2404.10819) [[DOI](https://doi.org/10.22323/1.453.0035)] (2024)
    * [Fine grinding localized updates via gauge equivariant flows in the 2D Schwinger model](https://arxiv.org/abs/2402.12176) [[DOI](https://doi.org/10.22323/1.453.0022)] (2024)
    * [Machine learning mapping of lattice correlated data](https://arxiv.org/abs/2402.07450) [[DOI](https://doi.org/10.1016/j.physletb.2024.138894)] (2024)
    * [Real-time Dynamics of the Schwinger Model as an Open Quantum System with Neural Density Operators](https://arxiv.org/abs/2402.06607) [[DOI](https://doi.org/10.1007/JHEP06(2024)211)] (2024)
    * [Mitigating topological freezing using out-of-equilibrium simulations](https://arxiv.org/abs/2402.06561) [[DOI](https://doi.org/10.1007/JHEP04(2024)126)] (2024)
    * [Lattice simulation of $SU(2)$ dark glueball with machine learning](https://arxiv.org/abs/2402.03959) [[DOI](https://doi.org/10.1088/1674-1137/ad4e24)] (2024)
    * [Advances in algorithms for solvers and gauge generation](https://arxiv.org/abs/2401.16620) (2024)
    * [Machine learning holographic black hole from lattice QCD equation of state](https://arxiv.org/abs/2401.06417) [[DOI](https://doi.org/10.1103/PhysRevD.109.L051902)] (2024)
    * [The dependence of observables on action parameters](https://arxiv.org/abs/2401.06456) [[DOI](https://doi.org/10.22323/1.453.0020)] (2024)
    * [Machine learning a fixed point action for SU(3) gauge theory with a gauge equivariant convolutional neural network](https://arxiv.org/abs/2401.06481) [[DOI](https://doi.org/10.1103/PhysRevD.110.074502)] (2024)
    * [Exploring the Critical Points in QCD with Multi-Point Pad\'e and Machine Learning Techniques in (2+1)-flavor QCD](https://arxiv.org/abs/2401.05651) [[DOI](https://doi.org/10.1051/epjconf/202429606007)] (2024)
    * [Flow-based sampling for lattice field theories](https://arxiv.org/abs/2401.01297) (2024)
    * [Mitigating a discrete sign problem with extreme learning machines](https://arxiv.org/abs/2312.12636) (2023)
    * [MLMC: Machine Learning Monte Carlo for Lattice Gauge Theory](https://arxiv.org/abs/2312.08936) (2023)
    * [A study of topological quantities of lattice QCD by a modified DCGAN frame](https://arxiv.org/abs/2312.03023) [[DOI](https://doi.org/10.1088/1674-1137/ad2b51)] (2023)
    * [Fixed point actions from convolutional neural networks](https://arxiv.org/abs/2311.17816) [[DOI](https://doi.org/10.22323/1.453.0038)] (2023)
    * [Extraction of the microscopic properties of quasi-particles using deep neural networks](https://arxiv.org/abs/2311.15984) [[DOI](https://doi.org/10.1103/PhysRevC.110.034908)] (2023)
    * [Study of topological quantities of lattice QCD by a modified Wasserstein generative adversarial network](https://arxiv.org/abs/2311.10108) [[DOI](https://doi.org/10.1103/PhysRevD.109.074509)] (2023)
    * [Generative Diffusion Models for Lattice Field Theory](https://arxiv.org/abs/2311.03578) (2023)
    * [Equivariant Transformer is all you need](https://arxiv.org/abs/2310.13222) [[DOI](https://doi.org/10.22323/1.453.0001)] (2023)
    * [Lattice real-time simulations with learned optimal kernels](https://arxiv.org/abs/2310.08053) [[DOI](https://doi.org/10.1103/PhysRevD.109.L031502)] (2023)
    * [Learning Trivializing Flows in a $\phi^4$ theory from coarser lattices](https://arxiv.org/abs/2310.03381) [[DOI](https://doi.org/10.22323/1.453.0013)] (2023)
    * [Breaking Free with AI: The Deconfinement Transition](https://arxiv.org/abs/2309.07225) (2023)
    * [Application of the path optimization method to a discrete spin system](https://arxiv.org/abs/2309.06018) [[DOI](https://doi.org/10.1103/PhysRevD.108.094504)] (2023)
    * [Signal-to-noise improvement through neural network contour deformations for 3D $SU(2)$ lattice gauge theory](https://arxiv.org/abs/2309.00600) [[DOI](https://doi.org/10.22323/1.453.0043)] (2023)
    * [Sampling the lattice Nambu-Goto string using Continuous Normalizing Flows](https://arxiv.org/abs/2307.01107) [[DOI](https://doi.org/10.1007/JHEP02(2024)048)] (2023)
    * [Teaching to extract spectral densities from lattice correlators to a broad audience of learning-machines](https://arxiv.org/abs/2307.00808) [[DOI](https://doi.org/10.1140/epjc/s10052-024-12399-0)] (2023)
    * [Combining lattice QCD and phenomenological inputs on generalised parton distributions at moderate skewness](https://arxiv.org/abs/2306.01647) [[DOI](https://doi.org/10.1140/epjc/s10052-024-12513-2)] (2023)
    * [Sampling $U(1)$ gauge theory using a re-trainable conditional flow-based model](https://arxiv.org/abs/2306.00581) [[DOI](https://doi.org/10.1103/PhysRevD.108.074518)] (2023)
    * [Gauge-equivariant pooling layers for preconditioners in lattice QCD](https://arxiv.org/abs/2304.10438) [[DOI](https://doi.org/10.1103/PhysRevD.110.034517)] (2023)
    * [Evidence of the Schwinger mechanism from lattice QCD](https://arxiv.org/abs/2304.07800) [[DOI](https://doi.org/10.1007/s00601-023-01813-0)] (2023)
    * [A variational Monte Carlo algorithm for lattice gauge theories with continuous gauge groups: a study of (2+1)-dimensional compact QED with dynamical fermions at finite density](https://arxiv.org/abs/2304.05916) [[DOI](https://doi.org/10.1103/PhysRevResearch.5.043128)] (2023)
    * [Locality-constrained autoregressive cum conditional normalizing flow for lattice field theory simulations](https://arxiv.org/abs/2304.01798) (2023)
    * [Exotic Tetraquark states with two $\bar{b}$-quarks and $J^P](https://arxiv.org/abs/2303.17295) [[DOI](https://doi.org/10.1103/PhysRevD.107.114510)] (2023)
    * [Exploring QCD matter in extreme conditions with Machine Learning](https://arxiv.org/abs/2303.15136) [[DOI](https://doi.org/10.1016/j.ppnp.2023.104084)] (2023)
    * [Geometrical aspects of lattice gauge equivariant convolutional neural networks](https://arxiv.org/abs/2303.11448) (2023)
    * [Detecting and Mitigating Mode-Collapse for Flow-based Sampling of Lattice Field Theories](https://arxiv.org/abs/2302.14082) [[DOI](https://doi.org/10.1103/PhysRevD.108.114501)] (2023)
    * [Learning Trivializing Flows](https://arxiv.org/abs/2302.08408) [[DOI](https://doi.org/10.1140/epjc/s10052-023-11838-8)] (2023)
    * [Gauge-equivariant neural networks as preconditioners in lattice QCD](https://arxiv.org/abs/2302.05419) [[DOI](https://doi.org/10.1103/PhysRevD.108.034503)] (2023)
    * [Machine learning phases of an Abelian gauge theory](https://arxiv.org/abs/2212.14655) [[DOI](https://doi.org/10.1093/ptep/ptad096)] (2022)
    * [Deep Learning of Fermion Sign Fluctuations](https://arxiv.org/abs/2212.14606) [[DOI](https://doi.org/10.1103/PhysRevD.107.114505)] (2022)
    * [Schwinger mechanism for gluons from lattice QCD](https://arxiv.org/abs/2211.12594) [[DOI](https://doi.org/10.1016/j.physletb.2023.137906)] (2022)
    * [Unpolarized proton PDF at NNLO from lattice QCD with physical quark masses](https://arxiv.org/abs/2212.12569) [[DOI](https://doi.org/10.1103/PhysRevD.107.074509)] (2022)
    * [Learning trivializing gradient flows for lattice gauge theories](https://arxiv.org/abs/2212.08469) [[DOI](https://doi.org/10.1103/PhysRevD.107.L051504)] (2022)
    * [Learning trivializing gradient flows for lattice gauge theories](https://arxiv.org/abs/2212.08469) [[DOI](https://doi.org/10.1103/PhysRevD.107.L051504)] (2022)
    * [Simulating 2+1D Lattice Quantum Electrodynamics at Finite Density with Neural Flow Wavefunctions](https://arxiv.org/abs/2212.06835) (2022)
    * [Applications of Lattice Gauge Equivariant Neural Networks](https://arxiv.org/abs/2212.00832) [[DOI](https://doi.org/10.1051/epjconf/202227409001)] (2022)
    * [A machine learning approach to the classification of phase transitions in many flavor QCD](https://arxiv.org/abs/2211.16232) [[DOI](https://doi.org/10.22323/1.430.0027)] (2022)
    * [Error reduction using machine learning on Ising worm simulation](https://arxiv.org/abs/2212.02365) [[DOI](https://doi.org/10.22323/1.430.0018)] (2022)
    * [Persistent homology as a probe for center vortices and deconfinement in SU(2) lattice gauge theory](https://arxiv.org/abs/2211.16273) [[DOI](https://doi.org/10.22323/1.430.0387)] (2022)
    * [Gluon helicity distribution in the nucleon from lattice QCD and machine learning](https://arxiv.org/abs/2211.15587) [[DOI](https://doi.org/10.1103/PhysRevD.108.074502)] (2022)
    * [Learning trivializing flows](https://arxiv.org/abs/2211.12806) [[DOI](https://doi.org/10.22323/1.430.0001)] (2022)
    * [Massive gauge theory with quasigluon for hot SU(N): Phase transition and thermodynamics](https://arxiv.org/abs/2211.09442) [[DOI](https://doi.org/10.1103/PhysRevD.107.076005)] (2022)
    * [Deep-learning quasi-particle masses from QCD equation of state](https://arxiv.org/abs/2211.07994) [[DOI](https://doi.org/10.1016/j.physletb.2023.138088)] (2022)
    * [Fourier-flow model generating Feynman paths](https://arxiv.org/abs/2211.03470) [[DOI](https://doi.org/10.1103/PhysRevD.107.056001)] (2022)
    * [Gauge Equivariant Neural Networks for 2+1D U(1) Gauge Theory Simulations in Hamiltonian Formulation](https://arxiv.org/abs/2211.03198) (2022)
    * [Rethinking the ill-posedness of the spectral function reconstruction -- why is it fundamentally hard and how Artificial Neural Networks can help](https://arxiv.org/abs/2201.02564) [[DOI](https://doi.org/10.1016/j.cpc.2022.108547)] (2022)
    * [Equivariance and generalization in neural networks](https://arxiv.org/abs/2112.12493) [[DOI](https://doi.org/10.1051/epjconf/202225809001)] (2021)
    * [Machine learning Hadron Spectral Functions in Lattice QCD](https://arxiv.org/abs/2112.00460) [[DOI](https://doi.org/10.22323/1.396.0148)] (2021)
    * [Lattice gauge symmetry in neural networks](https://arxiv.org/abs/2111.04389) [[DOI](https://doi.org/10.22323/1.396.0185)] (2021)
    * [A regression algorithm for accelerated lattice QCD that exploits sparse inference on the D-Wave quantum annealer](https://arxiv.org/abs/1911.06267) [[DOI](https://doi.org/10.1038/s41598-020-67769-x)] (2019)
    * [Machine-learning prediction for quasiparton distribution function matrix elements](https://arxiv.org/abs/1909.10990) [[DOI](https://doi.org/10.1103/PhysRevD.101.034516)] (2019)
    * [Machine Learning Estimators for Lattice QCD Observables](https://arxiv.org/abs/1807.05971) [[DOI](https://doi.org/10.1103/PhysRevD.100.014504)] (2018)
    * [Flow-based sampling for multimodal distributions in lattice field theory](https://arxiv.org/abs/2107.00734) (2021)
    * [Heavy Quark Potential in QGP: DNN meets LQCD](https://arxiv.org/abs/2105.07862) [[DOI](https://doi.org/10.1103/PhysRevD.105.014017)] (2021)
    * [Generalization capabilities of translationally equivariant neural networks](https://arxiv.org/abs/2103.14686) [[DOI](https://doi.org/10.1103/PhysRevD.104.074504)] (2021)
    * [Lattice gauge equivariant convolutional neural networks](https://arxiv.org/abs/2012.12901) [[DOI](https://doi.org/10.1103/PhysRevLett.128.032003)] (2020)
    * [Equivariant flow-based sampling for lattice gauge theory](https://arxiv.org/abs/2003.06413) [[DOI](https://doi.org/10.1103/PhysRevLett.125.121601)] (2020)


??? example "Function Approximation"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Function Approximation
    </div>

    * [Fast Perfekt: Regression-based refinement of fast simulation](https://arxiv.org/abs/2410.15992) (2024)
    * [A Variational Approach to Quantum Field Theory](https://arxiv.org/abs/2409.17887) (2024)
    * [Calabi-Yau Links and Machine Learning](https://arxiv.org/abs/2401.11550) [[DOI](https://doi.org/10.1142/S281093922440001X)] (2024)
    * [The NFLikelihood: an unsupervised DNNLikelihood from Normalizing Flows](https://arxiv.org/abs/2309.09743) (2023)
    * [A Modern Global Extraction of the Sivers Function](https://arxiv.org/abs/2304.14328) [[DOI](https://doi.org/10.1103/PhysRevD.108.054007)] (2023)
    * [Determination of the distribution of strong coupling constant with machine learning](https://arxiv.org/abs/2303.07968) (2023)
    * [Implicit Neural Representation as a Differentiable Surrogate for Photon Propagation in a Monolithic Neutrino Detector](https://arxiv.org/abs/2211.01505) (2022)
    * [Robust and Provably Monotonic Networks](https://arxiv.org/abs/2112.00038) [[DOI](https://doi.org/10.1088/2632-2153/aced80)] (2021)
    * [Reconstructing spectral functions via automatic differentiation](https://arxiv.org/abs/2111.14760) [[DOI](https://doi.org/10.1103/PhysRevD.106.L051502)] (2021)
    * [Function Approximation for High-Energy Physics: Comparing Machine Learning and Interpolation Methods](https://arxiv.org/abs/2111.14788) [[DOI](https://doi.org/10.21468/SciPostPhys.12.6.187)] (2021)
    * [Invariant polynomials and machine learning](https://arxiv.org/abs/2104.12733) [[DOI](https://doi.org/10.17863/CAM.80156)] (2021)
    * [The DNNLikelihood: enhancing likelihood distribution with Deep Learning](https://arxiv.org/abs/1911.03305) [[DOI](https://doi.org/10.1140/epjc/s10052-020-8230-1)] (2019)
    * [Elvet -- a neural network-based differential equation and variational problem solver](https://arxiv.org/abs/2103.14575) (2021)


??? example "Symbolic Regression"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Symbolic Regression
    </div>

    * [Strategies for Machine Learning Applied to Noisy HEP Datasets: Modular Solid State Detectors from SuperCDMS](https://arxiv.org/abs/2404.10971) (2024)
    * [Research on the distribution formula of QCD strong coupling constant in medium and high energy scale region based on symbolic regression algorithm](https://arxiv.org/abs/2304.07682) [[DOI](https://doi.org/10.1088/0256-307X/41/3/031201)] (2023)
    * [Rediscovery of Numerical Luscher's Formula from the Neural Network](https://arxiv.org/abs/2210.02184) [[DOI](https://doi.org/10.1088/1674-1137/ad3b9c)] (2022)
    * [Discover the GellMann-Okubo formula with machine learning](https://arxiv.org/abs/2208.03165) [[DOI](https://doi.org/10.1088/0256-307X/39/11/111201)] (2022)
    * [Back to the Formula -- LHC Edition](https://arxiv.org/abs/2109.10414) [[DOI](https://doi.org/10.21468/SciPostPhys.16.1.037)] (2021)


??? example "Monitoring"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Monitoring
    </div>

    * [Symbolic Regression for Beyond the Standard Model Physics](https://arxiv.org/abs/2405.18471) (2024)
    * [A versatile framework for attitude tuning of beamlines at advanced light sources](https://arxiv.org/abs/2411.01278) (2024)
    * [Strategies for Machine Learning Applied to Noisy HEP Datasets: Modular Solid State Detectors from SuperCDMS](https://arxiv.org/abs/2404.10971) (2024)
    * [GAMPix: a novel fine-grained, low-noise and ultra-low power pixelated charge readout for TPCs](https://arxiv.org/abs/2402.00902) (2024)
    * [Autoencoder-based Anomaly Detection System for Online Data Quality Monitoring of the CMS Electromagnetic Calorimeter](https://arxiv.org/abs/2309.10157) [[DOI](https://doi.org/10.1007/s41781-024-00118-z)] (2023)
    * [How to Understand Limitations of Generative Networks](https://arxiv.org/abs/2305.16774) [[DOI](https://doi.org/10.21468/SciPostPhys.16.1.031)] (2023)
    * [Autoencoder-based Online Data Quality Monitoring for the CMS Electromagnetic Calorimeter](https://arxiv.org/abs/2308.16659) (2023)
    * [Magnetic field regression using artificial neural networks for cold atom experiments](https://arxiv.org/abs/2305.18822) [[DOI](https://doi.org/10.1088/1674-1056/ad0cc8)] (2023)
    * [Predicting the Future of the CMS Detector: Crystal Radiation Damage and Machine Learning at the LHC](https://arxiv.org/abs/2303.15291) (2023)
    * [Machine Learning based tool for CMS RPC currents quality monitoring](https://arxiv.org/abs/2302.02764) [[DOI](https://doi.org/10.1016/j.nima.2023.168449)] (2023)
    * [High-availability displacement sensing with multi-channel self mixing interferometry](https://arxiv.org/abs/2302.00065) [[DOI](https://doi.org/10.1364/OE.485955)] (2023)
    * [First demonstration of neural sensing and control in a kilometer-scale gravitational wave observatory](https://arxiv.org/abs/2301.06221) [[DOI](https://doi.org/10.1103/PhysRevApplied.20.064041)] (2023)

##  Equivariant networks.


??? example "Equivariant networks."

    * [A Lorentz-Equivariant Transformer for All of the LHC](https://arxiv.org/abs/2411.00446) (2024)
    * [Optimal Equivariant Architectures from the Symmetries of Matrix-Element Likelihoods](https://arxiv.org/abs/2410.18553) (2024)
    * [Learning Group Invariant Calabi-Yau Metrics by Fundamental Domain Projections](https://arxiv.org/abs/2407.06914) (2024)
    * [Equivariant neural networks for robust $\textit{CP}$ observables](https://arxiv.org/abs/2405.13524) (2024)
    * [Lorentz-Equivariant Geometric Algebra Transformers for High-Energy Physics](https://arxiv.org/abs/2405.14806) (2024)
    * [Foundations of automatic feature extraction at LHC--point clouds and graphs](https://arxiv.org/abs/2404.16207) [[DOI](https://doi.org/10.1140/epjs/s11734-024-01306-z)] (2024)
    * [CapsLorentzNet: Integrating Physics Inspired Features with Graph Convolution](https://arxiv.org/abs/2403.11826) (2024)
    * [Equivariant, Safe and Sensitive -- Graph Networks for New Physics](https://arxiv.org/abs/2402.12449) [[DOI](https://doi.org/10.1007/JHEP07(2024)245)] (2024)
    * [Rotation-equivariant graph neural network for learning hadronic SMEFT effects](https://arxiv.org/abs/2401.10323) [[DOI](https://doi.org/10.1103/PhysRevD.109.076012)] (2024)
    * [Learning New Physics from Data -- a Symmetrized Approach](https://arxiv.org/abs/2401.09530) (2024)
    * [Neural ODEs for holographic transport models without translation symmetry](https://arxiv.org/abs/2401.09946) (2024)
    * [Safe but Incalculable: Energy-weighting is not all you need](https://arxiv.org/abs/2311.07652) [[DOI](https://doi.org/10.1103/PhysRevD.110.014029)] (2023)
    * [Explainable Equivariant Neural Networks for Particle Physics: PELICAN](https://arxiv.org/abs/2307.16506) [[DOI](https://doi.org/10.1007/JHEP03(2024)113)] (2023)
    * [Equivariant Graph Neural Networks for Charged Particle Tracking](https://arxiv.org/abs/2304.05293) (2023)
    * [Gauge-equivariant pooling layers for preconditioners in lattice QCD](https://arxiv.org/abs/2304.10438) [[DOI](https://doi.org/10.1103/PhysRevD.110.034517)] (2023)
    * [Discovering Sparse Representations of Lie Groups with Machine Learning](https://arxiv.org/abs/2302.05383) [[DOI](https://doi.org/10.1016/j.physletb.2023.138086)] (2023)
    * [EPiC-GAN: Equivariant Point Cloud Generation for Particle Jets](https://arxiv.org/abs/2301.08128) [[DOI](https://doi.org/10.21468/SciPostPhys.15.4.130)] (2023)
    * [Geometrical aspects of lattice gauge equivariant convolutional neural networks](https://arxiv.org/abs/2303.11448) (2023)
    * [Deep Learning Symmetries and Their Lie Groups, Algebras, and Subalgebras from First Principles](https://arxiv.org/abs/2301.05638) [[DOI](https://doi.org/10.1088/2632-2153/acd989)] (2023)
    * [Gauge-equivariant neural networks as preconditioners in lattice QCD](https://arxiv.org/abs/2302.05419) [[DOI](https://doi.org/10.1103/PhysRevD.108.034503)] (2023)
    * [Lorentz group equivariant autoencoders](https://arxiv.org/abs/2212.07347) [[DOI](https://doi.org/10.1140/epjc/s10052-023-11633-5)] (2022)
    * [PELICAN: Permutation Equivariant and Lorentz Invariant or Covariant Aggregator Network for Particle Physics](https://arxiv.org/abs/2211.00454) (2022)
    * [Applications of Lattice Gauge Equivariant Neural Networks](https://arxiv.org/abs/2212.00832) [[DOI](https://doi.org/10.1051/epjconf/202227409001)] (2022)
    * [Symmetry Group Equivariant Architectures for Physics](https://arxiv.org/abs/2203.06153) (2022)
    * [Rethinking the ill-posedness of the spectral function reconstruction -- why is it fundamentally hard and how Artificial Neural Networks can help](https://arxiv.org/abs/2201.02564) [[DOI](https://doi.org/10.1016/j.cpc.2022.108547)] (2022)
    * [An Efficient Lorentz Equivariant Graph Neural Network for Jet Tagging](https://arxiv.org/abs/2201.08187) [[DOI](https://doi.org/10.1007/JHEP07(2022)030)] (2022)
    * [Equivariance and generalization in neural networks](https://arxiv.org/abs/2112.12493) [[DOI](https://doi.org/10.1051/epjconf/202225809001)] (2021)
    * [Lattice gauge equivariant convolutional neural networks](https://arxiv.org/abs/2012.12901) [[DOI](https://doi.org/10.1103/PhysRevLett.128.032003)] (2020)
    * [Equivariant Energy Flow Networks for Jet Tagging](https://arxiv.org/abs/2012.00964) [[DOI](https://doi.org/10.1103/PhysRevD.103.074022)] (2020)
    * [Equivariant flow-based sampling for lattice gauge theory](https://arxiv.org/abs/2003.06413) [[DOI](https://doi.org/10.1103/PhysRevLett.125.121601)] (2020)

##  Physics-informed neural networks (PINNs).


??? example "Physics-informed neural networks (PINNs)."

    * [Physics-informed neural networks viewpoint for solving the Dyson-Schwinger equations of quantum electrodynamics](https://arxiv.org/abs/2411.02177) (2024)
    * [Advancing Physics Data Analysis through Machine Learning and Physics-Informed Neural Networks](https://arxiv.org/abs/2410.14760) (2024)
    * [Modelling parametric uncertainty in PDEs models via Physics-Informed Neural Networks](https://arxiv.org/abs/2408.04690) (2024)

##  Decorrelation methods.


??? example "Decorrelation methods."

    * [Decorrelation using Optimal Transport](https://arxiv.org/abs/2307.05187) [[DOI](https://doi.org/10.1140/epjc/s10052-024-12868-6)] (2023)
    * [Partial wave analysis of $\tau^-\to\pi^-\pi^+\pi^-\nu_\tau$ at Belle](https://arxiv.org/abs/2211.11696) [[DOI](https://doi.org/10.22323/1.414.1034)] (2022)
    * [Feature Selection with Distance Correlation](https://arxiv.org/abs/2212.00046) [[DOI](https://doi.org/10.1103/PhysRevD.109.054009)] (2022)
    * [Decorrelation with conditional normalizing flows](https://arxiv.org/abs/2211.02486) (2022)
    * [Online-compatible Unsupervised Non-resonant Anomaly Detection](https://arxiv.org/abs/2111.06417) [[DOI](https://doi.org/10.1103/PhysRevD.105.055006)] (2021)
    * [Metalearning and data augmentation for mass-generalized jet taggers](https://arxiv.org/abs/2111.06047) [[DOI](https://doi.org/10.1103/PhysRevD.105.094030)] (2021)
    * [A Cautionary Tale of Decorrelating Theory Uncertainties](https://arxiv.org/abs/2109.08159) [[DOI](https://doi.org/10.1140/epjc/s10052-022-10012-w)] (2021)
    * [Enhancing searches for resonances with machine learning and moment decomposition](https://arxiv.org/abs/2010.09745) [[DOI](https://doi.org/10.1007/JHEP04(2021)070)] (2020)
    * [ABCDisCo: Automating the ABCD Method with Machine Learning](https://arxiv.org/abs/2007.14400) [[DOI](https://doi.org/10.1103/PhysRevD.103.035021)] (2020)
    * [Adversarial domain adaptation to reduce sample bias of a high energy physics classifier](https://arxiv.org/abs/2005.00568) [[DOI](https://doi.org/10.1088/2632-2153/ac3dde)] (2020)
    * [A deep neural network to search for new long-lived particles decaying to jets](https://arxiv.org/abs/1912.12238) [[DOI](https://doi.org/10.1088/2632-2153/ab9023)] (2019)
    * [New approaches for boosting to uniformity](https://arxiv.org/abs/1410.4140) [[DOI](https://doi.org/10.1088/1748-0221/10/03/T03002)] (2014)
    * [Reducing the dependence of the neural network function to systematic uncertainties in the input space](https://arxiv.org/abs/1907.11674) [[DOI](https://doi.org/10.1007/s41781-020-00037-9)] (2019)
    * [Machine Learning Uncertainties with Adversarial Neural Networks](https://arxiv.org/abs/1807.08763) [[DOI](https://doi.org/10.1140/epjc/s10052-018-6511-8)] (2018)
    * [QBDT, a new boosting decision tree method with systematical uncertainties into training for High Energy Physics](https://arxiv.org/abs/1810.08387) [[DOI](https://doi.org/10.1016/j.nima.2019.03.088)] (2018)
    * [DisCo Fever: Robust Networks Through Distance Correlation](https://arxiv.org/abs/2001.05310) [[DOI](https://doi.org/10.1103/PhysRevLett.125.122001)] (2020)
    * [Performance of mass-decorrelated jet substructure](http://cds.cern.ch/record/2630973) (2018)
    * [Mass Agnostic Jet Taggers](https://arxiv.org/abs/1908.08959) [[DOI](https://doi.org/10.21468/SciPostPhys.8.1.011)] (2019)
    * [Decorrelated Jet Substructure Tagging using Adversarial Neural Networks](https://arxiv.org/abs/1703.03507) [[DOI](https://doi.org/10.1103/PhysRevD.96.074034)] (2017)
    * [uBoost: A boosting method for producing uniform selection efficiencies from multivariate classifiers](https://arxiv.org/abs/1305.7248) [[DOI](https://doi.org/10.1088/1748-0221/8/12/P12013)] (2013)
    * [Convolved Substructure: Analytically Decorrelating Jet Substructure Observables](https://arxiv.org/abs/1710.06859) [[DOI](https://doi.org/10.1007/JHEP05(2018)002)] (2017)
    * [Thinking outside the ROCs: Designing Decorrelated Taggers (DDT) for jet substructure](https://arxiv.org/abs/1603.00027) [[DOI](https://doi.org/10.1007/JHEP05(2016)156)] (2016)
    * [Learning to Pivot with Adversarial Networks](https://arxiv.org/abs/1611.01046) [[url](https://papers.nips.cc/paper/2017/hash/48ab2f9b45957ab574cf005eb8a76760-Abstract.html)] (2016)

##  Generative models / density estimation

??? example "GANs"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  GANs
    </div>

    * [CaloChallenge 2022: A Community Challenge for Fast Calorimeter Simulation](https://arxiv.org/abs/2410.21611) (2024)
    * [Pay Attention To Mean Fields For Point Cloud Generation](https://arxiv.org/abs/2408.04997) (2024)
    * [Applying generative neural networks for fast simulations of the ALICE (CERN) experiment](https://arxiv.org/abs/2407.16704) (2024)
    * [cDVGAN: One Flexible Model for Multi-class Gravitational Wave Signal and Glitch Generation](https://arxiv.org/abs/2401.16356) [[DOI](https://doi.org/10.1103/PhysRevD.110.022004)] (2024)
    * [CALPAGAN: Calorimetry for Particles Using Generative Adversarial Networks](https://arxiv.org/abs/2401.02248) [[DOI](https://doi.org/10.1093/ptep/ptae106)] (2024)
    * [Integrating Particle Flavor into Deep Learning Models for Hadronization](https://arxiv.org/abs/2312.08453) (2023)
    * [DeepTreeGANv2: Iterative Pooling of Point Clouds](https://arxiv.org/abs/2312.00042) (2023)
    * [DeepTreeGAN: Fast Generation of High Dimensional Point Clouds](https://arxiv.org/abs/2311.12616) [[DOI](https://doi.org/10.1051/epjconf/202429509010)] (2023)
    * [CaloShowerGAN, a Generative Adversarial Networks model for fast calorimeter shower simulation](https://arxiv.org/abs/2309.06515) [[DOI](https://doi.org/10.1140/epjp/s13360-024-05397-4)] (2023)
    * [SR-GAN for SR-gamma: photon super resolution at collider experiments](https://arxiv.org/abs/2308.09025) [[DOI](https://doi.org/10.1140/epjc/s10052-023-12178-3)] (2023)
    * [Lamarr: LHCb ultra-fast simulation based on machine learning models deployed within Gauss](https://arxiv.org/abs/2303.11428) (2023)
    * [Toward a generative modeling analysis of CLAS exclusive $2\pi$ photoproduction](https://arxiv.org/abs/2307.04450) [[DOI](https://doi.org/10.1103/PhysRevD.108.094030)] (2023)
    * [Machine Learning methods for simulating particle response in the Zero Degree Calorimeter at the ALICE experiment, CERN](https://arxiv.org/abs/2306.13606) [[DOI](https://doi.org/10.1063/5.0203567)] (2023)
    * [Fitting a Deep Generative Hadronization Model](https://arxiv.org/abs/2305.17169) [[DOI](https://doi.org/10.1007/JHEP09(2023)084)] (2023)
    * [New Angles on Fast Calorimeter Shower Simulation](https://arxiv.org/abs/2303.18150) [[DOI](https://doi.org/10.1088/2632-2153/acefa9)] (2023)
    * [Generative adversarial networks for scintillation signal simulation in EXO-200](https://arxiv.org/abs/2303.06311) [[DOI](https://doi.org/10.1088/1748-0221/18/06/P06005)] (2023)
    * [Ultra-High-Resolution Detector Simulation with Intra-Event Aware GAN and Self-Supervised Relational Reasoning](https://arxiv.org/abs/2303.08046) [[DOI](https://doi.org/10.1038/s41467-024-49104-4)] (2023)
    * [Ultrafast CMOS image sensors and data-enabled super-resolution for multimodal radiographic imaging and tomography](https://arxiv.org/abs/2301.11865) [[DOI](https://doi.org/10.22323/1.420.0041)] (2023)
    * [EPiC-GAN: Equivariant Point Cloud Generation for Particle Jets](https://arxiv.org/abs/2301.08128) [[DOI](https://doi.org/10.21468/SciPostPhys.15.4.130)] (2023)
    * [Generative models uncertainty estimation](https://arxiv.org/abs/2210.09767) [[DOI](https://doi.org/10.1088/1742-6596/2438/1/012088)] (2022)
    * [Deep generative models for fast photon shower simulation in ATLAS](https://arxiv.org/abs/2210.06204) [[DOI](https://doi.org/10.1007/s41781-023-00106-9)] (2022)
    * [GAN with an Auxiliary Regressor for the Fast Simulation of the Electromagnetic Calorimeter Response](https://arxiv.org/abs/2207.06329) [[DOI](https://doi.org/10.1088/1742-6596/2438/1/012086)] (2022)
    * [Generative Surrogates for Fast Simulation: TPC Case](https://arxiv.org/abs/2207.04340) [[DOI](https://doi.org/10.1016/j.nima.2022.167743)] (2022)
    * [Towards Reliable Neural Generative Modeling of Detectors](https://arxiv.org/abs/2204.09947) [[DOI](https://doi.org/10.1088/1742-6596/2438/1/012130)] (2022)
    * [Towards a Deep Learning Model for Hadronization](https://arxiv.org/abs/2203.12660) [[DOI](https://doi.org/10.1103/PhysRevD.106.096020)] (2022)
    * [Calomplification - The Power of Generative Calorimeter Models](https://arxiv.org/abs/2202.07352) [[DOI](https://doi.org/10.1088/1748-0221/17/09/P09028)] (2022)
    * [Hadrons, Better, Faster, Stronger](https://arxiv.org/abs/2112.09709) [[DOI](https://doi.org/10.1088/2632-2153/ac7848)] (2021)
    * [SymmetryGAN: Symmetry Discovery with Deep Learning](https://arxiv.org/abs/2112.05722) [[DOI](https://doi.org/10.1103/PhysRevD.105.096031)] (2021)
    * [Non-Parametric Data-Driven Background Modelling using Conditional Probabilities](https://arxiv.org/abs/2112.00650) [[DOI](https://doi.org/10.1007/JHEP10(2022)001)] (2021)
    * [Machine Learning for the LHCb Simulation](https://arxiv.org/abs/2110.07925) (2021)
    * [Style-based quantum generative adversarial networks for Monte Carlo events](https://arxiv.org/abs/2110.06933) [[DOI](https://doi.org/10.22331/q-2022-08-17-777)] (2021)
    * [Polarization measurement for the dileptonic channel of $W^+ W^-$ scattering using generative adversarial network](https://arxiv.org/abs/2109.09924) [[DOI](https://doi.org/10.1103/PhysRevD.105.016005)] (2021)
    * [Photon detection probability prediction using one-dimensional generative neural network](https://arxiv.org/abs/2109.07277) [[DOI](https://doi.org/10.1088/2632-2153/ac58e2)] (2021)
    * [Fast Simulation of a High Granularity Calorimeter by Generative Adversarial Networks](https://arxiv.org/abs/2109.07388) [[DOI](https://doi.org/10.1140/epjc/s10052-022-10258-4)] (2021)
    * [Black-Box Optimization with Local Generative Surrogates](https://arxiv.org/abs/2002.04632) [[url](https://proceedings.neurips.cc/paper/2020/hash/a878dbebc902328b41dbf02aa87abb58-Abstract.html)] (2020)
    * [Particle Cloud Generation with Message Passing Generative Adversarial Networks](https://arxiv.org/abs/2106.11535) (2021)
    * [Latent Space Refinement for Deep Generative Models](https://arxiv.org/abs/2106.00792) (2021)
    * [The use of Generative Adversarial Networks to characterise new physics in multi-lepton final states at the LHC](https://arxiv.org/abs/2105.14933) (2021)
    * [Physics Validation of Novel Convolutional 2D Architectures for Speeding Up High Energy Physics Simulations](https://arxiv.org/abs/2105.08960) [[DOI](https://doi.org/10.1051/epjconf/202125103042)] (2021)
    * [Compressing PDF sets using generative adversarial networks](https://arxiv.org/abs/2104.04535) [[DOI](https://doi.org/10.1140/epjc/s10052-021-09338-8)] (2021)
    * [Validation of Deep Convolutional Generative Adversarial Networks for High Energy Physics Calorimeter Simulations](https://arxiv.org/abs/2103.13698) (2021)
    * [Reduced Precision Strategies for Deep Learning: A High Energy Physics Generative Adversarial Network Use Case](https://arxiv.org/abs/2103.10142) [[DOI](https://doi.org/10.5220/0010245002510258)] (2021)
    * [A Data-driven Event Generator for Hadron Colliders using Wasserstein Generative Adversarial Network](https://arxiv.org/abs/2102.11524) [[DOI](https://doi.org/10.1007/s40042-021-00095-1)] (2021)
    * [Explainable machine learning of the underlying physics of high-energy particle collisions](https://arxiv.org/abs/2012.06582) [[DOI](https://doi.org/10.1016/j.physletb.2022.137055)] (2020)
    * [Simulating the time projection chamber responses at the MPD detector using generative adversarial networks](https://arxiv.org/abs/2012.04595) [[DOI](https://doi.org/10.1140/epjc/s10052-021-09366-4)] (2020)
    * [Graph Generative Adversarial Networks for Sparse Data Generation in High Energy Physics](https://arxiv.org/abs/2012.00173) (2020)
    * [GANplifying Event Samples](https://arxiv.org/abs/2008.06545) [[DOI](https://doi.org/10.21468/SciPostPhys.10.6.139)] (2020)
    * [DCTRGAN: Improving the Precision of Generative Models with Reweighting](https://arxiv.org/abs/2009.03796) [[DOI](https://doi.org/10.1088/1748-0221/15/11/P11004)] (2020)
    * [AI-based Monte Carlo event generator for electron-proton scattering](https://arxiv.org/abs/2008.03151) [[DOI](https://doi.org/10.1103/PhysRevD.106.096002)] (2020)
    * [Getting High: High Fidelity Simulation of High Granularity Calorimeters with High Speed](https://arxiv.org/abs/2005.05334) [[DOI](https://doi.org/10.1007/s41781-021-00056-0)] (2020)
    * [A Novel Scenario in the Semi-constrained NMSSM](https://arxiv.org/abs/2002.05554) [[DOI](https://doi.org/10.1007/JHEP06(2020)078)] (2020)
    * [Calorimetry with Deep Learning: Particle Simulation and Reconstruction for Collider Physics](https://arxiv.org/abs/1912.06794) [[DOI](https://doi.org/10.1140/epjc/s10052-020-8251-9)] (2019)
    * [Calorimetry with Deep Learning: Particle Classification, Energy Regression, and Simulation for High-Energy Physics](https://dl4physicalsciences.github.io/files/nips_dlps_2017_15.pdf) (2017)
    * [Next Generation Generative Neural Networks for HEP](https://doi.org/10.1051/epjconf/201921409005) (2019)
    * [Controlling Physical Attributes in GAN-Accelerated Simulation of Electromagnetic Calorimeters](https://arxiv.org/abs/1711.08813) [[DOI](https://doi.org/10.1088/1742-6596/1085/4/042017)] (2017)
    * [Tips and Tricks for Training GANs with Physics Constraints](https://dl4physicalsciences.github.io/files/nips_dlps_2017_26.pdf) (2017)
    * [Reducing Autocorrelation Times in Lattice Simulations with Generative Adversarial Networks](https://arxiv.org/abs/1811.03533) [[DOI](https://doi.org/10.1088/2632-2153/abae73)] (2018)
    * [Precise simulation of electromagnetic calorimeter showers using a Wasserstein Generative Adversarial Network](https://arxiv.org/abs/1807.01954) [[DOI](https://doi.org/10.1007/s41781-018-0019-7)] (2018)
    * [GANs for generating EFT models](https://arxiv.org/abs/1809.02612) [[DOI](https://doi.org/10.1016/j.physletb.2020.135798)] (2018)
    * [RICH 2018](https://arxiv.org/abs/1903.11788) [[DOI](https://doi.org/10.1016/j.nima.2019.01.031)] (2019)
    * [Generative models for fast cluster simulations in the TPC for the ALICE experiment](https://doi.org/10.1051/epjconf/201921406003) (2019)
    * [Generating and refining particle detector simulations using the Wasserstein distance in adversarial networks](https://arxiv.org/abs/1802.03325) [[DOI](https://doi.org/10.1007/s41781-018-0008-x)] (2018)
    * [Fast and Accurate Simulation of Particle Detectors Using Generative Adversarial Networks](https://arxiv.org/abs/1805.00850) [[DOI](https://doi.org/10.1007/s41781-018-0015-y)] (2018)
    * [Unfolding with Generative Adversarial Networks](https://arxiv.org/abs/1806.00433) (2018)
    * [Generative models for fast simulation](https://doi.org/10.1088/1742-6596/1085/2/022005) (2018)
    * [Three dimensional Generative Adversarial Networks for fast simulation](https://doi.org/10.1088/1742-6596/1085/3/032016) (2018)
    * [Regressive and generative neural networks for scalar field theory](https://arxiv.org/abs/1810.12879) [[DOI](https://doi.org/10.1103/PhysRevD.100.011501)] (2018)
    * [Deep generative models for fast shower simulation in ATLAS](http://cds.cern.ch/record/2630433) (2018)
    * [Generative Models for Fast Calorimeter Simulation.LHCb case](https://arxiv.org/abs/1812.01319) [[DOI](https://doi.org/10.1051/epjconf/201921402034)] (2018)
    * [LHC analysis-specific datasets with Generative Adversarial Networks](https://arxiv.org/abs/1901.05282) (2019)
    * [DijetGAN: A Generative-Adversarial Network Approach for the Simulation of QCD Dijet Events at the LHC](https://arxiv.org/abs/1903.02433) [[DOI](https://doi.org/10.1007/JHEP08(2019)110)] (2019)
    * [Machine Learning Templates for QCD Factorization in the Search for Physics Beyond the Standard Model](https://arxiv.org/abs/1903.02556) [[DOI](https://doi.org/10.1007/JHEP05(2019)181)] (2019)
    * [How to GAN LHC Events](https://arxiv.org/abs/1907.03764) [[DOI](https://doi.org/10.21468/SciPostPhys.7.6.075)] (2019)
    * [Lund jet images from generative and cycle-consistent adversarial networks](https://arxiv.org/abs/1909.01359) [[DOI](https://doi.org/10.1140/epjc/s10052-019-7501-1)] (2019)
    * [Fast simulation of muons produced at the SHiP experiment using Generative Adversarial Networks](https://arxiv.org/abs/1909.04451) [[DOI](https://doi.org/10.1088/1748-0221/14/11/P11028)] (2019)
    * [3D convolutional GAN for fast simulation](https://doi.org/10.1051/epjconf/201921402010) (2019)
    * [How to GAN away Detector Effects](https://arxiv.org/abs/1912.00477) [[DOI](https://doi.org/10.21468/SciPostPhys.8.4.070)] (2019)
    * [Particle Generative Adversarial Networks for full-event simulation at the LHC and their application to pileup description](https://arxiv.org/abs/1912.02748) [[DOI](https://doi.org/10.1088/1742-6596/1525/1/012081)] (2019)
    * [How to GAN Event Subtraction](https://arxiv.org/abs/1912.08824) [[DOI](https://doi.org/10.21468/SciPostPhysCore.3.2.009)] (2019)
    * [Image-based model parameter optimization using Model-Assisted Generative Adversarial Networks](https://arxiv.org/abs/1812.00879) [[DOI](https://doi.org/10.1109/TNNLS.2020.2969327)] (2018)
    * [CaloGAN : Simulating 3D high energy particle showers in multilayer electromagnetic calorimeters with generative adversarial networks](https://arxiv.org/abs/1712.10321) [[DOI](https://doi.org/10.1103/PhysRevD.97.014021)] (2017)
    * [Accelerating Science with Generative Adversarial Networks: An Application to 3D Particle Showers in Multilayer Calorimeters](https://arxiv.org/abs/1705.02355) [[DOI](https://doi.org/10.1103/PhysRevLett.120.042003)] (2017)
    * [Learning Particle Physics by Example: Location-Aware Generative Adversarial Networks for Physics Synthesis](https://arxiv.org/abs/1701.05927) [[DOI](https://doi.org/10.1007/s41781-017-0004-6)] (2017)


??? example "(Variational) Autoencoders"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  (Variational) Autoencoders
    </div>

    * [Fast multi-geometry calorimeter simulation with conditional self-attention variational autoencoders](https://arxiv.org/abs/2411.05996) (2024)
    * [CaloChallenge 2022: A Community Challenge for Fast Calorimeter Simulation](https://arxiv.org/abs/2410.21611) (2024)
    * [Calo-VQ: Vector-Quantized Two-Stage Generative Model in Calorimeter Simulation](https://arxiv.org/abs/2405.06605) (2024)
    * [Deep Generative Models for Ultra-High Granularity Particle Physics Detector Simulation: A Voyage From Emulation to Extrapolation](https://arxiv.org/abs/2403.13825) (2024)
    * [CaloQVAE : Simulating high-energy particle-calorimeter interactions using hybrid quantum-classical generative models](https://arxiv.org/abs/2312.03179) (2023)
    * [Searching for gluon quartic gauge couplings at muon colliders using the auto-encoder](https://arxiv.org/abs/2311.16627) [[DOI](https://doi.org/10.1103/PhysRevD.109.095028)] (2023)
    * [Boosting sensitivity to new physics with unsupervised anomaly detection in dijet resonance search](https://arxiv.org/abs/2308.02671) [[DOI](https://doi.org/10.1140/epjp/s13360-024-05018-0)] (2023)
    * [Generative deep-learning reveals collective variables of Fermionic systems](https://arxiv.org/abs/2306.08348) [[DOI](https://doi.org/10.1103/PhysRevC.109.064612)] (2023)
    * [Triggering Dark Showers with Conditional Dual Auto-Encoders](https://arxiv.org/abs/2306.12955) [[DOI](https://doi.org/10.1088/2632-2153/ad652b)] (2023)
    * [Nanosecond anomaly detection with decision trees for high energy physics and real-time application to exotic Higgs decays](https://arxiv.org/abs/2304.03836) [[DOI](https://doi.org/10.1038/s41467-024-47704-8)] (2023)
    * [CaloMan: Fast generation of calorimeter showers with density estimation on learned manifolds](https://arxiv.org/abs/2211.15380) (2022)
    * [CaloDVAE : Discrete Variational Autoencoders for Fast Calorimeter Shower Simulation](https://arxiv.org/abs/2210.07430) (2022)
    * [Machine-Learning Compression for Particle Physics Discoveries](https://arxiv.org/abs/2210.11489) (2022)
    * [Modeling hadronization using machine learning](https://arxiv.org/abs/2203.04983) [[DOI](https://doi.org/10.21468/SciPostPhys.14.3.027)] (2022)
    * [Particle-based Fast Jet Simulation at the LHC with Variational Autoencoders](https://arxiv.org/abs/2203.00520) [[DOI](https://doi.org/10.1088/2632-2153/ac7c56)] (2022)
    * [Hadrons, Better, Faster, Stronger](https://arxiv.org/abs/2112.09709) [[DOI](https://doi.org/10.1088/2632-2153/ac7848)] (2021)
    * [Particle Graph Autoencoders and Differentiable, Learned Energy Mover's Distance](https://arxiv.org/abs/2111.12849) (2021)
    * [Improving Variational Autoencoders for New Physics Detection at the LHC with Normalizing Flows](https://arxiv.org/abs/2110.08508) [[DOI](https://doi.org/10.3389/fdata.2022.803685)] (2021)
    * [Sparse Data Generation for Particle-Based Simulation of Hadronic Jets in the LHC](https://arxiv.org/abs/2109.15197) (2021)
    * [An Exploration of Learnt Representations of W Jets](https://arxiv.org/abs/2109.10919) (2021)
    * [DeepRICH: Learning Deeply Cherenkov Detectors](https://arxiv.org/abs/1911.11717) [[DOI](https://doi.org/10.1088/2632-2153/ab845a)] (2019)
    * [Graph Generative Models for Fast Detector Simulations in High Energy Physics](https://arxiv.org/abs/2104.01725) (2021)
    * [{End-to-end Sinkhorn Autoencoder with Noise Generator](https://arxiv.org/abs/2006.06704) [[DOI](https://doi.org/10.1109/ACCESS.2020.3048622)] (2020)
    * [Bump Hunting in Latent Space](https://arxiv.org/abs/2103.06595) [[DOI](https://doi.org/10.1103/PhysRevD.105.115009)] (2021)
    * [Decoding Photons: Physics in the Latent Space of a BIB-AE Generative Network](https://arxiv.org/abs/2102.12491) [[DOI](https://doi.org/10.1051/epjconf/202125103003)] (2021)
    * [Foundations of a Fast, Data-Driven, Machine-Learned Simulator](https://arxiv.org/abs/2101.08944) [[DOI](https://doi.org/10.1038/s41598-022-10966-7)] (2021)
    * [Variational Autoencoders for Jet Simulation](https://arxiv.org/abs/2009.04842) (2020)
    * [Variational Autoencoders for Anomalous Jet Tagging](https://arxiv.org/abs/2007.01850) [[DOI](https://doi.org/10.1103/PhysRevD.107.016002)] (2020)
    * [Deep generative models for fast shower simulation in ATLAS](http://cds.cern.ch/record/2630433) (2018)
    * [Deep Learning as a Parton Shower](https://arxiv.org/abs/1807.03685) [[DOI](https://doi.org/10.1007/JHEP12(2018)021)] (2018)


??? example "(Continuous) Normalizing flows"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  (Continuous) Normalizing flows
    </div>

    * [CaloChallenge 2022: A Community Challenge for Fast Calorimeter Simulation](https://arxiv.org/abs/2410.21611) (2024)
    * [Signal model parameter scan using Normalizing Flow](https://arxiv.org/abs/2409.13201) [[DOI](https://doi.org/10.22323/1.458.0017)] (2024)
    * [Variational Monte Carlo with Neural Network Quantum States for Yang-Mills Matrix Model](https://arxiv.org/abs/2409.00398) (2024)
    * [Differentiable MadNIS-Lite](https://arxiv.org/abs/2408.01486) (2024)
    * [PIPPIN: Generating variable length full events from partons](https://arxiv.org/abs/2406.13074) [[DOI](https://doi.org/10.1103/PhysRevD.110.076023)] (2024)
    * [Parnassus: An Automated Approach to Accurate, Precise, and Fast Detector Simulation and Reconstruction](https://arxiv.org/abs/2406.01620) (2024)
    * [Convolutional L2LFlows: Generating Accurate Showers in Highly Granular Calorimeters Using Convolutional Normalizing Flows](https://arxiv.org/abs/2405.20407) [[DOI](https://doi.org/10.1088/1748-0221/19/09/P09003)] (2024)
    * [CaloDREAM -- Detector Response Emulation via Attentive flow Matching](https://arxiv.org/abs/2405.09629) (2024)
    * [Unifying Simulation and Inference with Normalizing Flows](https://arxiv.org/abs/2404.18992) (2024)
    * [Flow-based Nonperturbative Simulation of First-order Phase Transitions](https://arxiv.org/abs/2404.18323) (2024)
    * [Multiscale Normalizing Flows for Gauge Theories](https://arxiv.org/abs/2404.10819) [[DOI](https://doi.org/10.22323/1.453.0035)] (2024)
    * [One flow to correct them all: improving simulations in high-energy physics with a single normalising flow and a switch](https://arxiv.org/abs/2403.18582) [[DOI](https://doi.org/10.1007/s41781-024-00125-0)] (2024)
    * [CaloPointFlow II Generating Calorimeter Showers as Point Clouds](https://arxiv.org/abs/2403.15782) (2024)
    * [Normalizing Flows for Domain Adaptation when Identifying $\Lambda$ Hyperon Events](https://arxiv.org/abs/2403.14804) [[DOI](https://doi.org/10.1088/1748-0221/19/06/C06020)] (2024)
    * [End-to-end simulation of particle physics events with Flow Matching and generator Oversampling](https://arxiv.org/abs/2402.13684) [[DOI](https://doi.org/10.1088/2632-2153/ad563c)] (2024)
    * [Improving $\Lambda$ Signal Extraction with Domain Adaptation via Normalizing Flows](https://arxiv.org/abs/2403.14076) [[DOI](https://doi.org/10.22323/1.456.0043)] (2024)
    * [Accelerating HEP simulations with Neural Importance Sampling](https://arxiv.org/abs/2401.09069) [[DOI](https://doi.org/10.1007/JHEP03(2024)083)] (2024)
    * [Flow-based sampling for lattice field theories](https://arxiv.org/abs/2401.01297) (2024)
    * [Anomaly detection with flow-based fast calorimeter simulators](https://arxiv.org/abs/2312.11618) [[DOI](https://doi.org/10.1103/PhysRevD.110.035036)] (2023)
    * [Normalizing Flows for High-Dimensional Detector Simulations](https://arxiv.org/abs/2312.09290) (2023)
    * [Fast Posterior Probability Sampling with Normalizing Flows and Its Applicability in Bayesian analysis in Particle Physics](https://arxiv.org/abs/2312.02045) [[DOI](https://doi.org/10.1103/PhysRevD.109.032008)] (2023)
    * [Towards a data-driven model of hadronization using normalizing flows](https://arxiv.org/abs/2311.09296) [[DOI](https://doi.org/10.21468/SciPostPhys.17.2.045)] (2023)
    * [The MadNIS Reloaded](https://arxiv.org/abs/2311.01548) [[DOI](https://doi.org/10.21468/SciPostPhys.17.1.023)] (2023)
    * [Systematic Evaluation of Generative Machine Learning Capability to Simulate Distributions of Observables at the Large Hadron Collider](https://arxiv.org/abs/2310.08994) [[DOI](https://doi.org/10.1140/epjc/s10052-024-13284-6)] (2023)
    * [Simulation of Hadronic Interactions with Deep Generative Models](https://arxiv.org/abs/2310.07553) [[DOI](https://doi.org/10.1051/epjconf/202429509034)] (2023)
    * [Learning Trivializing Flows in a $\phi^4$ theory from coarser lattices](https://arxiv.org/abs/2310.03381) [[DOI](https://doi.org/10.22323/1.453.0013)] (2023)
    * [Chained Quantile Morphing with Normalizing Flows](https://arxiv.org/abs/2309.15912) (2023)
    * [Back To The Roots: Tree-Based Algorithms for Weakly Supervised Anomaly Detection](https://arxiv.org/abs/2309.13111) [[DOI](https://doi.org/10.1103/PhysRevD.109.034033)] (2023)
    * [Combining Resonant and Tail-based Anomaly Detection](https://arxiv.org/abs/2309.12918) [[DOI](https://doi.org/10.1103/PhysRevD.109.096031)] (2023)
    * [The NFLikelihood: an unsupervised DNNLikelihood from Normalizing Flows](https://arxiv.org/abs/2309.09743) (2023)
    * [Flows for Flows: Morphing one Dataset into another with Maximum Likelihood Estimation](https://arxiv.org/abs/2309.06472) [[DOI](https://doi.org/10.1103/PhysRevD.108.096018)] (2023)
    * [SuperCalo: Calorimeter shower super-resolution](https://arxiv.org/abs/2308.11700) [[DOI](https://doi.org/10.1103/PhysRevD.109.092009)] (2023)
    * [Inductive CaloFlow](https://arxiv.org/abs/2305.11934) [[DOI](https://doi.org/10.1103/PhysRevD.109.033006)] (2023)
    * [Sampling $U(1)$ gauge theory using a re-trainable conditional flow-based model](https://arxiv.org/abs/2306.00581) [[DOI](https://doi.org/10.1103/PhysRevD.108.074518)] (2023)
    * [Generative Machine Learning for Detector Response Modeling with a Conditional Normalizing Flow](https://arxiv.org/abs/2303.10148) [[DOI](https://doi.org/10.1088/1748-0221/19/02/P02003)] (2023)
    * [Generative modeling of nucleon-nucleon interactions](https://arxiv.org/abs/2306.13007) (2023)
    * [The Interplay of Machine Learning--based Resonant Anomaly Detection Methods](https://arxiv.org/abs/2307.11157) [[DOI](https://doi.org/10.1140/epjc/s10052-024-12607-x)] (2023)
    * [$\nu^2$-Flows: Fast and improved neutrino reconstruction in multi-neutrino final states with conditional normalizing flows](https://arxiv.org/abs/2307.02405) [[DOI](https://doi.org/10.1103/PhysRevD.109.012005)] (2023)
    * [ELSA - Enhanced latent spaces for improved collider simulations](https://arxiv.org/abs/2305.07696) [[DOI](https://doi.org/10.1140/epjc/s10052-023-11989-8)] (2023)
    * [Locality-constrained autoregressive cum conditional normalizing flow for lattice field theory simulations](https://arxiv.org/abs/2304.01798) (2023)
    * [Detecting and Mitigating Mode-Collapse for Flow-based Sampling of Lattice Field Theories](https://arxiv.org/abs/2302.14082) [[DOI](https://doi.org/10.1103/PhysRevD.108.114501)] (2023)
    * [L2LFlows: Generating High-Fidelity 3D Calorimeter Images](https://arxiv.org/abs/2302.11594) [[DOI](https://doi.org/10.1088/1748-0221/18/10/P10017)] (2023)
    * [Generative Invertible Quantum Neural Networks](https://arxiv.org/abs/2302.12906) [[DOI](https://doi.org/10.21468/SciPostPhys.16.6.146)] (2023)
    * [Learning Trivializing Flows](https://arxiv.org/abs/2302.08408) [[DOI](https://doi.org/10.1140/epjc/s10052-023-11838-8)] (2023)
    * [MadNIS -- Neural Multi-Channel Importance Sampling](https://arxiv.org/abs/2212.06172) [[DOI](https://doi.org/10.21468/SciPostPhys.15.4.141)] (2022)
    * [An unfolding method based on conditional Invertible Neural Networks (cINN) using iterative training](https://arxiv.org/abs/2212.08674) [[DOI](https://doi.org/10.21468/scipostphyscore.7.1.007)] (2022)
    * [TopicFlow: Disentangling quark and gluon jets with normalizing flows](https://arxiv.org/abs/2211.16053) [[DOI](https://doi.org/10.1103/PhysRevD.107.114003)] (2022)
    * [Point Cloud Generation using Transformer Encoders and Normalising Flows](https://arxiv.org/abs/2211.13623) (2022)
    * [JetFlow: Generating Jets with Conditioned and Mass Constrained Normalising Flows](https://arxiv.org/abs/2211.13630) (2022)
    * [CaloMan: Fast generation of calorimeter showers with density estimation on learned manifolds](https://arxiv.org/abs/2211.15380) (2022)
    * [CaloFlow for CaloChallenge Dataset 1](https://arxiv.org/abs/2210.14245) [[DOI](https://doi.org/10.21468/SciPostPhys.16.5.126)] (2022)
    * [Learning trivializing flows](https://arxiv.org/abs/2211.12806) [[DOI](https://doi.org/10.22323/1.430.0001)] (2022)
    * [Fourier-flow model generating Feynman paths](https://arxiv.org/abs/2211.03470) [[DOI](https://doi.org/10.1103/PhysRevD.107.056001)] (2022)
    * [$\nu$-Flows: conditional neutrino regression](https://arxiv.org/abs/2207.00664) [[DOI](https://doi.org/10.21468/SciPostPhys.14.6.159)] (2022)
    * [Event Generation and Density Estimation with Surjective Normalizing Flows](https://arxiv.org/abs/2205.01697) [[DOI](https://doi.org/10.21468/SciPostPhys.13.3.047)] (2022)
    * [Ephemeral Learning -- Augmenting Triggers with Online-Trained Normalizing Flows](https://arxiv.org/abs/2202.09375) [[DOI](https://doi.org/10.21468/SciPostPhys.13.4.087)] (2022)
    * [Targeting Multi-Loop Integrals with Neural Networks](https://arxiv.org/abs/2112.09145) [[DOI](https://doi.org/10.21468/SciPostPhys.12.4.129)] (2021)
    * [Generative Networks for Precision Enthusiasts](https://arxiv.org/abs/2110.13632) [[DOI](https://doi.org/10.21468/SciPostPhys.14.4.078)] (2021)
    * [CaloFlow II: Even Faster and Still Accurate Generation of Calorimeter Showers with Normalizing Flows](https://arxiv.org/abs/2110.11377) [[DOI](https://doi.org/10.1103/PhysRevD.107.113004)] (2021)
    * [Inference of cosmic-ray source properties by conditional invertible neural networks](https://arxiv.org/abs/2110.09493) [[DOI](https://doi.org/10.1140/epjc/s10052-022-10138-x)] (2021)
    * [Improving Variational Autoencoders for New Physics Detection at the LHC with Normalizing Flows](https://arxiv.org/abs/2110.08508) [[DOI](https://doi.org/10.3389/fdata.2022.803685)] (2021)
    * [Neural Empirical Bayes: Source Distribution Estimation and its Applications to Simulation-Based Inference](https://arxiv.org/abs/2011.05836) [[url](https://proceedings.mlr.press/v130/vandegar21a.html)] (2020)
    * [Black-Box Optimization with Local Generative Surrogates](https://arxiv.org/abs/2002.04632) [[url](https://proceedings.neurips.cc/paper/2020/hash/a878dbebc902328b41dbf02aa87abb58-Abstract.html)] (2020)
    * [Classifying Anomalies THrough Outer Density Estimation (CATHODE)](https://arxiv.org/abs/2109.00546) [[DOI](https://doi.org/10.1103/PhysRevD.106.055006)] (2021)
    * [Learning to discover: expressive Gaussian mixture models for multi-dimensional simulation and parameter inference in the physical sciences](https://arxiv.org/abs/2108.11481) [[DOI](https://doi.org/10.1088/2632-2153/ac4a3b)] (2021)
    * [Flow-based sampling for multimodal distributions in lattice field theory](https://arxiv.org/abs/2107.00734) (2021)
    * [CaloFlow: Fast and Accurate Generation of Calorimeter Showers with Normalizing Flows](https://arxiv.org/abs/2106.05285) [[DOI](https://doi.org/10.1103/PhysRevD.107.113003)] (2021)
    * [Latent Space Refinement for Deep Generative Models](https://arxiv.org/abs/2106.00792) (2021)
    * [Efficient sampling of constrained high-dimensional theoretical spaces with machine learning](https://arxiv.org/abs/2103.06957) [[DOI](https://doi.org/10.1140/epjc/s10052-021-09941-9)] (2021)
    * [Measuring QCD Splittings with Invertible Networks](https://arxiv.org/abs/2012.09873) [[DOI](https://doi.org/10.21468/SciPostPhys.10.6.126)] (2020)
    * [SARM: Sparse Autoregressive Model for Scalable Generation of Sparse Images in Particle Physics](https://arxiv.org/abs/2009.14017) [[DOI](https://doi.org/10.1103/PhysRevD.103.036012)] (2020)
    * [Data-driven Estimation of Background Distribution through Neural Autoregressive Flows](https://arxiv.org/abs/2008.03636) (2020)
    * [Anomaly Detection with Density Estimation](https://arxiv.org/abs/2001.04990) [[DOI](https://doi.org/10.1103/PhysRevD.101.075042)] (2020)
    * [i-flow: High-Dimensional Integration and Sampling with Normalizing Flows](https://arxiv.org/abs/2001.05486) [[DOI](https://doi.org/10.1088/2632-2153/abab62)] (2020)
    * [Event Generation with Normalizing Flows](https://arxiv.org/abs/2001.10028) [[DOI](https://doi.org/10.1103/PhysRevD.101.076002)] (2020)
    * [Exploring phase space with Neural Importance Sampling](https://arxiv.org/abs/2001.05478) [[DOI](https://doi.org/10.21468/SciPostPhys.8.4.069)] (2020)
    * [Flows for simultaneous manifold learning and density estimation](https://arxiv.org/abs/2003.13913) (2020)
    * [Equivariant flow-based sampling for lattice gauge theory](https://arxiv.org/abs/2003.06413) [[DOI](https://doi.org/10.1103/PhysRevLett.125.121601)] (2020)
    * [Invertible Networks or Partons to Detector and Back Again](https://arxiv.org/abs/2006.06685) [[DOI](https://doi.org/10.21468/SciPostPhys.9.5.074)] (2020)
    * [Flow-based generative models for Markov chain Monte Carlo in lattice field theory](https://arxiv.org/abs/1904.12072) [[DOI](https://doi.org/10.1103/PhysRevD.100.034515)] (2019)


??? example "Diffusion Models"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Diffusion Models
    </div>

    * [CaloChallenge 2022: A Community Challenge for Fast Calorimeter Simulation](https://arxiv.org/abs/2410.21611) (2024)
    * [Point cloud-based diffusion models for the Electron-Ion Collider](https://arxiv.org/abs/2410.22421) (2024)
    * [Variational inference for pile-up removal at hadron colliders with diffusion models](https://arxiv.org/abs/2410.22074) (2024)
    * [On learning higher-order cumulants in diffusion models](https://arxiv.org/abs/2410.21212) (2024)
    * [Diffusion models for lattice gauge field simulations](https://arxiv.org/abs/2410.19602) (2024)
    * [Applying generative neural networks for fast simulations of the ALICE (CERN) experiment](https://arxiv.org/abs/2407.16704) (2024)
    * [PIPPIN: Generating variable length full events from partons](https://arxiv.org/abs/2406.13074) [[DOI](https://doi.org/10.1103/PhysRevD.110.076023)] (2024)
    * [Generative Diffusion Models for Fast Simulations of Particle Collisions at CERN](https://arxiv.org/abs/2406.03233) (2024)
    * [CaloDREAM -- Detector Response Emulation via Attentive flow Matching](https://arxiv.org/abs/2405.09629) (2024)
    * [Advancing Set-Conditional Set Generation: Graph Diffusion for Fast Simulation of Reconstructed Particles](https://arxiv.org/abs/2405.10106) (2024)
    * [BUFF: Boosted Decision Tree based Ultra-Fast Flow matching](https://arxiv.org/abs/2404.18219) (2024)
    * [End-to-end simulation of particle physics events with Flow Matching and generator Oversampling](https://arxiv.org/abs/2402.13684) [[DOI](https://doi.org/10.1088/2632-2153/ad563c)] (2024)
    * [CaloGraph: Graph-based diffusion model for fast shower generation in calorimeters with irregular geometry](https://arxiv.org/abs/2402.11575) [[DOI](https://doi.org/10.1103/PhysRevD.110.072003)] (2024)
    * [Choose Your Diffusion: Efficient and flexible ways to accelerate the diffusion model in fast high energy physics simulation](https://arxiv.org/abs/2401.13162) (2024)
    * [Improving new physics searches with diffusion models for event observables and jet constituents](https://arxiv.org/abs/2312.10130) [[DOI](https://doi.org/10.1007/JHEP04(2024)109)] (2023)
    * [Kicking it Off(-shell) with Direct Diffusion](https://arxiv.org/abs/2311.17175) [[DOI](https://doi.org/10.21468/SciPostPhysCore.7.3.064)] (2023)
    * [Generative Diffusion Models for Lattice Field Theory](https://arxiv.org/abs/2311.03578) (2023)
    * [The MadNIS Reloaded](https://arxiv.org/abs/2311.01548) [[DOI](https://doi.org/10.21468/SciPostPhys.17.1.023)] (2023)
    * [Diffusion model approach to simulating electron-proton scattering events](https://arxiv.org/abs/2310.16308) [[DOI](https://doi.org/10.1103/PhysRevD.110.016030)] (2023)
    * [Full Phase Space Resonant Anomaly Detection](https://arxiv.org/abs/2310.06897) [[DOI](https://doi.org/10.1103/PhysRevD.109.055015)] (2023)
    * [EPiC-ly Fast Particle Cloud Generation with Flow-Matching and Diffusion](https://arxiv.org/abs/2310.00049) (2023)
    * [CaloClouds II: Ultra-Fast Geometry-Independent Highly-Granular Calorimeter Simulation](https://arxiv.org/abs/2309.05704) [[DOI](https://doi.org/10.1088/1748-0221/19/04/P04020)] (2023)
    * [Accelerating Markov Chain Monte Carlo sampling with diffusion models](https://arxiv.org/abs/2309.01454) [[DOI](https://doi.org/10.1016/j.cpc.2023.109059)] (2023)
    * [CaloScore v2: Single-shot Calorimeter Shower Simulation with Diffusion Models](https://arxiv.org/abs/2308.03847) [[DOI](https://doi.org/10.1088/1748-0221/19/02/P02001)] (2023)
    * [Improving Generative Model-based Unfolding with Schr\"odinger Bridges](https://arxiv.org/abs/2308.12351) [[DOI](https://doi.org/10.1103/PhysRevD.109.076011)] (2023)
    * [Renormalizing Diffusion Models](https://arxiv.org/abs/2308.12355) (2023)
    * [Refining Fast Calorimeter Simulations with a Schr\"odinger Bridge](https://arxiv.org/abs/2308.12339) (2023)
    * [CaloDiffusion with GLaM for High Fidelity Calorimeter Simulation](https://arxiv.org/abs/2308.03876) [[DOI](https://doi.org/10.1103/PhysRevD.108.072014)] (2023)
    * [Score-based Diffusion Models for Generating Liquid Argon Time Projection Chamber Images](https://arxiv.org/abs/2307.13687) [[DOI](https://doi.org/10.1103/PhysRevD.109.072011)] (2023)
    * [PC-Droid: Faster diffusion and improved quality for particle cloud generation](https://arxiv.org/abs/2307.06836) [[DOI](https://doi.org/10.1103/PhysRevD.109.012010)] (2023)
    * [Comparison of Point Cloud and Image-based Models for Calorimeter Fast Simulation](https://arxiv.org/abs/2307.04780) [[DOI](https://doi.org/10.1088/1748-0221/19/05/P05003)] (2023)
    * [High-dimensional and Permutation Invariant Anomaly Detection](https://arxiv.org/abs/2306.03933) [[DOI](https://doi.org/10.21468/SciPostPhys.16.3.062)] (2023)
    * [Jet Diffusion versus JetGPT -- Modern Networks for the LHC](https://arxiv.org/abs/2305.10475) (2023)
    * [CaloClouds: Fast Geometry-Independent Highly-Granular Calorimeter Simulation](https://arxiv.org/abs/2305.04847) [[DOI](https://doi.org/10.1088/1748-0221/18/11/P11025)] (2023)
    * [End-To-End Latent Variational Diffusion Models for Inverse Problems in High Energy Physics](https://arxiv.org/abs/2305.10399) (2023)
    * [Fast Point Cloud Generation with Diffusion Models in High Energy Physics](https://arxiv.org/abs/2304.01266) [[DOI](https://doi.org/10.1103/PhysRevD.108.036025)] (2023)
    * [PC-JeDi: Diffusion for Particle Cloud Generation in High Energy Physics](https://arxiv.org/abs/2303.05376) [[DOI](https://doi.org/10.21468/SciPostPhys.16.1.018)] (2023)
    * [Score-based Generative Models for Calorimeter Shower Simulation](https://arxiv.org/abs/2206.11898) [[DOI](https://doi.org/10.1103/PhysRevD.106.092009)] (2022)


??? example "Transformer Models"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Transformer Models
    </div>

    * [A Lorentz-Equivariant Transformer for All of the LHC](https://arxiv.org/abs/2411.00446) (2024)
    * [PIPPIN: Generating variable length full events from partons](https://arxiv.org/abs/2406.13074) [[DOI](https://doi.org/10.1103/PhysRevD.110.076023)] (2024)
    * [Lorentz-Equivariant Geometric Algebra Transformers for High-Energy Physics](https://arxiv.org/abs/2405.14806) (2024)
    * [Folded context condensation in Path Integral formalism for infinite context transformers](https://arxiv.org/abs/2405.04620) (2024)
    * [Induced Generative Adversarial Particle Transformers](https://arxiv.org/abs/2312.04757) (2023)
    * [Equivariant Transformer is all you need](https://arxiv.org/abs/2310.13222) [[DOI](https://doi.org/10.22323/1.453.0001)] (2023)
    * [$\nu^2$-Flows: Fast and improved neutrino reconstruction in multi-neutrino final states with conditional normalizing flows](https://arxiv.org/abs/2307.02405) [[DOI](https://doi.org/10.1103/PhysRevD.109.012005)] (2023)
    * [Jet Diffusion versus JetGPT -- Modern Networks for the LHC](https://arxiv.org/abs/2305.10475) (2023)
    * [Learning the language of QCD jets with transformers](https://arxiv.org/abs/2303.07364) [[DOI](https://doi.org/10.1007/JHEP06(2023)184)] (2023)


??? example "Physics-inspired"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Physics-inspired
    </div>

    * [Application of Kolmogorov-Arnold Networks in high energy physics](https://arxiv.org/abs/2409.01724) (2024)
    * [Binary Discrimination Through Next-to-Leading Order](https://arxiv.org/abs/2309.14417) [[DOI](https://doi.org/10.1007/JHEP03(2024)057)] (2023)
    * [Symmetry meets AI](https://arxiv.org/abs/2103.06115) [[DOI](https://doi.org/10.21468/SciPostPhys.11.1.014)] (2021)
    * [Explainable machine learning of the underlying physics of high-energy particle collisions](https://arxiv.org/abs/2012.06582) [[DOI](https://doi.org/10.1016/j.physletb.2022.137055)] (2020)
    * [Exploring the Possibility of a Recovery of Physics Process Properties from a Neural Network Model](https://arxiv.org/abs/2007.13110) [[DOI](https://doi.org/10.3390/e22090994)] (2020)
    * [Binary JUNIPR: an interpretable probabilistic model for discrimination](https://arxiv.org/abs/1906.10137) [[DOI](https://doi.org/10.1103/PhysRevLett.123.182001)] (2019)
    * [JUNIPR: a Framework for Unsupervised Machine Learning in Particle Physics](https://arxiv.org/abs/1804.09720) [[DOI](https://doi.org/10.1140/epjc/s10052-019-6607-9)] (2018)


??? example "Mixture Models"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Mixture Models
    </div>

    * [Mapping QGP properties in Pb--Pb and Xe--Xe collisions at the LHC](https://arxiv.org/abs/2308.16722) [[DOI](https://doi.org/10.1103/PhysRevC.108.064908)] (2023)
    * [Geometry-aware Autoregressive Models for Calorimeter Shower Simulations](https://arxiv.org/abs/2212.08233) (2022)
    * [Maximum Likelihood Reconstruction of Water Cherenkov Events With Deep Generative Neural Networks](https://arxiv.org/abs/2202.01276) [[DOI](https://doi.org/10.3389/fdata.2022.868333)] (2022)
    * [A Neural-Network-defined Gaussian Mixture Model for particle identification applied to the LHCb fixed-target programme](https://arxiv.org/abs/2110.10259) [[DOI](https://doi.org/10.1088/1748-0221/17/02/P02018)] (2021)
    * [Mixture Density Network Estimation of Continuous Variable Maximum Likelihood Using Discrete Training Samples](https://arxiv.org/abs/2103.13416) [[DOI](https://doi.org/10.1140/epjc/s10052-021-09469-y)] (2021)
    * [Data Augmentation at the LHC through Analysis-specific Fast Simulation with Deep Learning](https://arxiv.org/abs/2010.01835) (2020)


??? example "Phase space generation"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Phase space generation
    </div>

    * [Accelerating HEP simulations with Neural Importance Sampling](https://arxiv.org/abs/2401.09069) [[DOI](https://doi.org/10.1007/JHEP03(2024)083)] (2024)
    * [Learning Feynman integrals from differential equations with neural networks](https://arxiv.org/abs/2312.02067) [[DOI](https://doi.org/10.1007/JHEP07(2024)124)] (2023)
    * [Predicting the Exclusive Diffractive Electron-Ion Cross Section at small $x$ with Machine Learning in Sar$t$re](https://arxiv.org/abs/2305.15880) [[DOI](https://doi.org/10.1016/j.cpc.2023.108872)] (2023)
    * [Precision studies for the partonic kinematics calculation through Machine Learning](https://arxiv.org/abs/2305.11369) [[DOI](https://doi.org/10.31349/SuplRevMexFis.4.021134)] (2023)
    * [MadNIS -- Neural Multi-Channel Importance Sampling](https://arxiv.org/abs/2212.06172) [[DOI](https://doi.org/10.21468/SciPostPhys.15.4.141)] (2022)
    * [Machine Learning Post-Minkowskian Integrals](https://arxiv.org/abs/2209.01091) [[DOI](https://doi.org/10.1007/JHEP07(2023)181)] (2022)
    * [Multi-variable Integration with a Neural Network](https://arxiv.org/abs/2211.02834) [[DOI](https://doi.org/10.1007/JHEP03(2023)221)] (2022)
    * [A machine learning approach for efficient multi-dimensional integration](https://arxiv.org/abs/2009.06697) [[DOI](https://doi.org/10.1038/s41598-021-98392-z)] (2020)
    * [Accelerating Monte Carlo event generation -- rejection sampling using neural network event-weight estimates](https://arxiv.org/abs/2109.11964) [[DOI](https://doi.org/10.21468/SciPostPhys.12.5.164)] (2021)
    * [How to GAN Event Unweighting](https://arxiv.org/abs/2012.07873) [[DOI](https://doi.org/10.21468/SciPostPhys.10.4.089)] (2020)
    * [Phase Space Sampling and Inference from Weighted Events with Autoregressive Flows](https://arxiv.org/abs/2011.13445) [[DOI](https://doi.org/10.21468/SciPostPhys.10.2.038)] (2020)
    * [Improved Neural Network Monte Carlo Simulation](https://arxiv.org/abs/2009.07819) [[DOI](https://doi.org/10.21468/SciPostPhys.10.1.023)] (2020)
    * [A Neural Resampler for Monte Carlo Reweighting with Preserved Uncertainties](https://arxiv.org/abs/2007.11586) [[DOI](https://doi.org/10.1103/PhysRevD.102.076004)] (2020)
    * [VegasFlow: accelerating Monte Carlo simulation across multiple hardware platforms](https://arxiv.org/abs/2002.12921) [[DOI](https://doi.org/10.1016/j.cpc.2020.107376)] (2020)
    * [Neural Network-Based Approach to Phase Space Integration](https://arxiv.org/abs/1810.11509) [[DOI](https://doi.org/10.21468/SciPostPhys.9.4.053)] (2018)
    * [i-flow: High-Dimensional Integration and Sampling with Normalizing Flows](https://arxiv.org/abs/2001.05486) [[DOI](https://doi.org/10.1088/2632-2153/abab62)] (2020)
    * [Event Generation with Normalizing Flows](https://arxiv.org/abs/2001.10028) [[DOI](https://doi.org/10.1103/PhysRevD.101.076002)] (2020)
    * [Exploring phase space with Neural Importance Sampling](https://arxiv.org/abs/2001.05478) [[DOI](https://doi.org/10.21468/SciPostPhys.8.4.069)] (2020)
    * [Efficient Monte Carlo Integration Using Boosted Decision](https://arxiv.org/abs/1707.00028) (2017)


??? example "Gaussian processes"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Gaussian processes
    </div>

    * [AI-optimized detector design for the future Electron-Ion Collider: the dual-radiator RICH case](https://arxiv.org/abs/1911.05797) [[DOI](https://doi.org/10.1088/1748-0221/15/05/P05009)] (2019)
    * [$\textsf{Xsec}$: the cross-section evaluation code](https://arxiv.org/abs/2006.16273) [[DOI](https://doi.org/10.1140/epjc/s10052-020-08635-y)] (2020)
    * [Accelerating the BSM interpretation of LHC data with machine learning](https://arxiv.org/abs/1611.02704) [[DOI](https://doi.org/10.1016/j.dark.2019.100293)] (2016)
    * [Modeling Smooth Backgrounds and Generic Localized Signals with Gaussian Processes](https://arxiv.org/abs/1709.05681) (2017)


??? example "Other/hybrid"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Other/hybrid
    </div>

    * [ML-Based Top Taggers: Performance, Uncertainty and Impact of Tower \& Tracker Data Integration](https://arxiv.org/abs/2309.01568) (2023)
    * [Towards accurate real-time luminescence thermometry: an automated machine learning approach](https://arxiv.org/abs/2307.05497) (2023)
    * [Implicit Quantile Networks For Emulation in Jet Physics](https://arxiv.org/abs/2306.15053) (2023)
    * [Jet Diffusion versus JetGPT -- Modern Networks for the LHC](https://arxiv.org/abs/2305.10475) (2023)
    * [Evaluating generative models in high energy physics](https://arxiv.org/abs/2211.10295) [[DOI](https://doi.org/10.1103/PhysRevD.107.076017)] (2022)
    * [Ad-hoc Pulse Shape Simulation using Cyclic Positional U-Net](https://arxiv.org/abs/2212.04950) (2022)
    * [Conditional Generative Modelling of Reconstructed Particles at Collider Experiments](https://arxiv.org/abs/2211.06406) (2022)
    * [CaloMan: Fast generation of calorimeter showers with density estimation on learned manifolds](https://arxiv.org/abs/2211.15380) (2022)

##  Anomaly detection.


??? example "Anomaly detection."

    * [SIGMA: Single Interpolated Generative Model for Anomalies](https://arxiv.org/abs/2410.20537) (2024)
    * [Model-independent searches of new physics in DARWIN with a semi-supervised deep learning pipeline](https://arxiv.org/abs/2410.00755) (2024)
    * [Novel machine learning applications at the LHC](https://arxiv.org/abs/2409.20413) (2024)
    * [Detect anomalous quartic gauge couplings at muon colliders with quantum kernel k-means](https://arxiv.org/abs/2409.07010) (2024)
    * [ADFilter -- A Web Tool for New Physics Searches With Autoencoder-Based Anomaly Detection Using Deep Unsupervised Neural Networks](https://arxiv.org/abs/2409.03065) (2024)
    * [Semi-supervised permutation invariant particle-level anomaly detection](https://arxiv.org/abs/2408.17409) (2024)
    * [Anomaly Detection Based on Machine Learning for the CMS Electromagnetic Calorimeter Online Data Quality Monitoring](https://arxiv.org/abs/2407.20278) (2024)
    * [Accelerating template generation in resonant anomaly detection searches with optimal transport](https://arxiv.org/abs/2407.19818) (2024)
    * [Anomaly-aware summary statistic from data batches](https://arxiv.org/abs/2407.01249) (2024)
    * [Accelerating Resonance Searches via Signature-Oriented Pre-training](https://arxiv.org/abs/2405.12972) (2024)
    * [Incorporating Physical Priors into Weakly-Supervised Anomaly Detection](https://arxiv.org/abs/2405.08889) (2024)
    * [Anomaly detection with flow-based fast calorimeter simulators](https://arxiv.org/abs/2312.11618) [[DOI](https://doi.org/10.1103/PhysRevD.110.035036)] (2023)
    * [Improving new physics searches with diffusion models for event observables and jet constituents](https://arxiv.org/abs/2312.10130) [[DOI](https://doi.org/10.1007/JHEP04(2024)109)] (2023)
    * [Testing a Neural Network for Anomaly Detection in the CMS Global Trigger Test Crate during Run 3](https://arxiv.org/abs/2312.10009) [[DOI](https://doi.org/10.1088/1748-0221/19/03/C03029)] (2023)
    * [Anomaly Detection in Collider Physics via Factorized Observables](https://arxiv.org/abs/2312.00119) [[DOI](https://doi.org/10.1103/PhysRevD.110.055012)] (2023)
    * [Fast Particle-based Anomaly Detection Algorithm with Variational Autoencoder](https://arxiv.org/abs/2311.17162) (2023)
    * [Searching for gluon quartic gauge couplings at muon colliders using the auto-encoder](https://arxiv.org/abs/2311.16627) [[DOI](https://doi.org/10.1103/PhysRevD.109.095028)] (2023)
    * [Non-resonant Anomaly Detection with Background Extrapolation](https://arxiv.org/abs/2311.12924) [[DOI](https://doi.org/10.1007/JHEP04(2024)059)] (2023)
    * [Triggerless data acquisition pipeline for Machine Learning based statistical anomaly detection](https://arxiv.org/abs/2311.02038) [[DOI](https://doi.org/10.1051/epjconf/202429502033)] (2023)
    * [Anomaly Detection in Presence of Irrelevant Features](https://arxiv.org/abs/2310.13057) [[DOI](https://doi.org/10.1007/JHEP02(2024)220)] (2023)
    * [Full Phase Space Resonant Anomaly Detection](https://arxiv.org/abs/2310.06897) [[DOI](https://doi.org/10.1103/PhysRevD.109.055015)] (2023)
    * [Back To The Roots: Tree-Based Algorithms for Weakly Supervised Anomaly Detection](https://arxiv.org/abs/2309.13111) [[DOI](https://doi.org/10.1103/PhysRevD.109.034033)] (2023)
    * [Combining Resonant and Tail-based Anomaly Detection](https://arxiv.org/abs/2309.12918) [[DOI](https://doi.org/10.1103/PhysRevD.109.096031)] (2023)
    * [Autoencoder-based Anomaly Detection System for Online Data Quality Monitoring of the CMS Electromagnetic Calorimeter](https://arxiv.org/abs/2309.10157) [[DOI](https://doi.org/10.1007/s41781-024-00118-z)] (2023)
    * [Boosting sensitivity to new physics with unsupervised anomaly detection in dijet resonance search](https://arxiv.org/abs/2308.02671) [[DOI](https://doi.org/10.1140/epjp/s13360-024-05018-0)] (2023)
    * [Anomaly detection search for new resonances decaying into a Higgs boson and a generic new particle $X$ in hadronic final states using $\sqrt{s}](https://arxiv.org/abs/2306.03637) [[DOI](https://doi.org/10.1103/PhysRevD.108.052009)] (2023)
    * [GAN-AE : An anomaly detection algorithm for New Physics search in LHC data](https://arxiv.org/abs/2305.15179) [[DOI](https://doi.org/10.1140/epjc/s10052-023-12169-4)] (2023)
    * [The Interplay of Machine Learning--based Resonant Anomaly Detection Methods](https://arxiv.org/abs/2307.11157) [[DOI](https://doi.org/10.1140/epjc/s10052-024-12607-x)] (2023)
    * [High-dimensional and Permutation Invariant Anomaly Detection](https://arxiv.org/abs/2306.03933) [[DOI](https://doi.org/10.21468/SciPostPhys.16.3.062)] (2023)
    * [CURTAINs Flows For Flows: Constructing Unobserved Regions with Maximum Likelihood Estimation](https://arxiv.org/abs/2305.04646) [[DOI](https://doi.org/10.21468/SciPostPhys.17.2.046)] (2023)
    * [The Mass-ive Issue: Anomaly Detection in Jet Physics](https://arxiv.org/abs/2303.14134) (2023)
    * [Nanosecond anomaly detection with decision trees for high energy physics and real-time application to exotic Higgs decays](https://arxiv.org/abs/2304.03836) [[DOI](https://doi.org/10.1038/s41467-024-47704-8)] (2023)
    * [Unravelling physics beyond the standard model with classical and quantum anomaly detection](https://arxiv.org/abs/2301.10787) [[DOI](https://doi.org/10.1088/2632-2153/ad07f7)] (2023)
    * [Efficiently Moving Instead of Reweighting Collider Events with Machine Learning](https://arxiv.org/abs/2212.06155) (2022)
    * [Quantum-probabilistic Hamiltonian learning for generative modelling \& anomaly detection](https://arxiv.org/abs/2211.03803) [[DOI](https://doi.org/10.1103/PhysRevA.108.062422)] (2022)
    * [Anomaly Detection under Coordinate Transformations](https://arxiv.org/abs/2209.06225) [[DOI](https://doi.org/10.1103/PhysRevD.107.015009)] (2022)
    * [Resonant anomaly detection without background sculpting](https://arxiv.org/abs/2210.14924) [[DOI](https://doi.org/10.1103/PhysRevD.107.114012)] (2022)
    * [Null Hypothesis Test for Anomaly Detection](https://arxiv.org/abs/2210.02226) [[DOI](https://doi.org/10.1016/j.physletb.2023.137836)] (2022)
    * [Neural Embedding: Learning the Embedding of the Manifold of Physics Data](https://arxiv.org/abs/2208.05484) [[DOI](https://doi.org/10.1007/JHEP07(2023)108)] (2022)
    * [Mixture-of-theories Training: Can We Find New Physics and Anomalies Better by Mixing Physical Theories?](https://arxiv.org/abs/2207.07631) [[DOI](https://doi.org/10.1007/JHEP03(2023)004)] (2022)
    * [A Normalized Autoencoder for LHC Triggers](https://arxiv.org/abs/2206.14225) [[DOI](https://doi.org/10.21468/SciPostPhysCore.6.4.074)] (2022)
    * [Event Generation and Density Estimation with Surjective Normalizing Flows](https://arxiv.org/abs/2205.01697) [[DOI](https://doi.org/10.21468/SciPostPhys.13.3.047)] (2022)
    * [Boosting mono-jet searches with model-agnostic machine learning](https://arxiv.org/abs/2204.11889) [[DOI](https://doi.org/10.1007/JHEP08(2022)015)] (2022)
    * [''Flux+Mutability'': A Conditional Generative Approach to One-Class Classification and Anomaly Detection](https://arxiv.org/abs/2204.08609) [[DOI](https://doi.org/10.1088/2632-2153/ac9bcb)] (2022)
    * [Learning new physics efficiently with nonparametric methods](https://arxiv.org/abs/2204.02317) [[DOI](https://doi.org/10.1140/epjc/s10052-022-10830-y)] (2022)
    * [CURTAINs for your Sliding Window: Constructing Unobserved Regions by Transforming Adjacent Intervals](https://arxiv.org/abs/2203.09470) [[DOI](https://doi.org/10.3389/fdata.2023.899345)] (2022)
    * [Data-directed search for new physics based on symmetries of the SM](https://arxiv.org/abs/2203.07529) [[DOI](https://doi.org/10.1140/epjc/s10052-022-10454-2)] (2022)
    * [Self-supervised Anomaly Detection for New Physics](https://arxiv.org/abs/2205.10380) [[DOI](https://doi.org/10.1103/PhysRevD.106.056005)] (2022)
    * [Detecting new physics as novelty \textemdash{} Complementarity matters](https://arxiv.org/abs/2202.02165) [[DOI](https://doi.org/10.1007/JHEP10(2022)085)] (2022)
    * [Quantum Anomaly Detection for Collider Physics](https://arxiv.org/abs/2206.08391) [[DOI](https://doi.org/10.1007/JHEP02(2023)220)] (2022)
    * [What's Anomalous in LHC Jets?](https://arxiv.org/abs/2202.00686) [[DOI](https://doi.org/10.21468/SciPostPhys.15.4.168)] (2022)
    * [Taming modeling uncertainties with Mass Unspecific Supervised Tagging](https://arxiv.org/abs/2201.11143) [[DOI](https://doi.org/10.1140/epjc/s10052-022-10221-3)] (2022)
    * [Creating Simple, Interpretable Anomaly Detectors for New Physics in Jet Substructure](https://arxiv.org/abs/2203.01343) [[DOI](https://doi.org/10.1103/PhysRevD.106.035014)] (2022)
    * [Anomaly detection in high-energy physics using a quantum autoencoder](https://arxiv.org/abs/2112.04958) [[DOI](https://doi.org/10.1103/PhysRevD.105.095004)] (2021)
    * [Autoencoders for Semivisible Jet Detection](https://arxiv.org/abs/2112.02864) [[DOI](https://doi.org/10.1007/JHEP02(2022)074)] (2021)
    * [Learning New Physics from an Imperfect Machine](https://arxiv.org/abs/2111.13633) [[DOI](https://doi.org/10.1140/epjc/s10052-022-10226-y)] (2021)
    * [Event-based anomaly detection for new physics searches at the LHC using machine learning](https://arxiv.org/abs/2111.12119) [[DOI](https://doi.org/10.3390/universe8100494)] (2021)
    * [Online-compatible Unsupervised Non-resonant Anomaly Detection](https://arxiv.org/abs/2111.06417) [[DOI](https://doi.org/10.1103/PhysRevD.105.055006)] (2021)
    * [Stressed GANs snag desserts, a.k.a Spotting Symmetry Violation with Symmetric Functions](https://arxiv.org/abs/2111.00616) (2021)
    * [A method to challenge symmetries in data with self-supervised learning](https://arxiv.org/abs/2111.05442) [[DOI](https://doi.org/10.1088/1748-0221/17/08/P08024)] (2021)
    * [Anomaly detection from mass unspecific jet tagging](https://arxiv.org/abs/2111.02647) [[DOI](https://doi.org/10.1140/epjc/s10052-022-10058-w)] (2021)
    * [Signal-agnostic dark matter searches in direct detection data with machine learning](https://arxiv.org/abs/2110.12248) [[DOI](https://doi.org/10.1088/1475-7516/2022/02/039)] (2021)
    * [Improving Variational Autoencoders for New Physics Detection at the LHC with Normalizing Flows](https://arxiv.org/abs/2110.08508) [[DOI](https://doi.org/10.3389/fdata.2022.803685)] (2021)
    * [Challenges for Unsupervised Anomaly Detection in Particle Physics](https://arxiv.org/abs/2110.06948) [[DOI](https://doi.org/10.1007/JHEP03(2022)066)] (2021)
    * [Deep Set Auto Encoders for Anomaly Detection in Particle Physics](https://arxiv.org/abs/2109.01695) [[DOI](https://doi.org/10.21468/SciPostPhys.12.1.045)] (2021)
    * [Classifying Anomalies THrough Outer Density Estimation (CATHODE)](https://arxiv.org/abs/2109.00546) [[DOI](https://doi.org/10.1103/PhysRevD.106.055006)] (2021)
    * [Autoencoders on FPGAs for real-time, unsupervised new physics detection at 40 MHz at the Large Hadron Collider](https://arxiv.org/abs/2108.03986) [[DOI](https://doi.org/10.1038/s42256-022-00441-3)] (2021)
    * [The Data-Directed Paradigm for BSM searches](https://arxiv.org/abs/2107.11573) [[DOI](https://doi.org/10.1140/epjc/s10052-022-10215-1)] (2021)
    * [New Methods and Datasets for Group Anomaly Detection From Fundamental Physics](https://arxiv.org/abs/2107.02821) (2021)
    * [LHC physics dataset for unsupervised New Physics detection at 40 MHz](https://arxiv.org/abs/2107.02157) [[DOI](https://doi.org/10.1038/s41597-022-01187-8)] (2021)
    * [Rare and Different: Anomaly Scores from a combination of likelihood and out-of-distribution models to detect new physics at the LHC](https://arxiv.org/abs/2106.10164) [[DOI](https://doi.org/10.21468/SciPostPhys.12.2.077)] (2021)
    * [RanBox: Anomaly Detection in the Copula Space](https://arxiv.org/abs/2106.05747) [[DOI](https://doi.org/10.1007/JHEP01(2023)008)] (2021)
    * [The Dark Machines Anomaly Score Challenge: Benchmark Data and Model Independent Event Classification for the Large Hadron Collider](https://arxiv.org/abs/2105.14027) [[DOI](https://doi.org/10.21468/SciPostPhys.12.1.043)] (2021)
    * [Anomalous Jet Identification via Sequence Modeling](https://arxiv.org/abs/2105.09274) [[DOI](https://doi.org/10.1088/1748-0221/16/08/P08012)] (2021)
    * [Anomaly detection with Convolutional Graph Neural Networks](https://arxiv.org/abs/2105.07988) [[DOI](https://doi.org/10.1007/JHEP08(2021)080)] (2021)
    * [Via Machinae: Searching for Stellar Streams using Unsupervised Machine Learning](https://arxiv.org/abs/2104.12789) [[DOI](https://doi.org/10.1093/mnras/stab3372)] (2021)
    * [Autoencoders for unsupervised anomaly detection in high energy physics](https://arxiv.org/abs/2104.09051) [[DOI](https://doi.org/10.1007/JHEP06(2021)161)] (2021)
    * [Better Latent Spaces for Better Autoencoders](https://arxiv.org/abs/2104.08291) [[DOI](https://doi.org/10.21468/SciPostPhys.11.3.061)] (2021)
    * [Comparing Weak- and Unsupervised Methods for Resonant Anomaly Detection](https://arxiv.org/abs/2104.02092) [[DOI](https://doi.org/10.1140/epjc/s10052-021-09389-x)] (2021)
    * [Bump Hunting in Latent Space](https://arxiv.org/abs/2103.06595) [[DOI](https://doi.org/10.1103/PhysRevD.105.115009)] (2021)
    * [Unsupervised Event Classification with Graphs on Classical and Photonic Quantum Computers](https://arxiv.org/abs/2103.03897) [[DOI](https://doi.org/10.1007/JHEP08(2021)170)] (2021)
    * [Topological Obstructions to Autoencoding](https://arxiv.org/abs/2102.08380) [[DOI](https://doi.org/10.1007/JHEP04(2021)280)] (2021)
    * [Model-Independent Detection of New Physics Signals Using Interpretable Semi-Supervised Classifier Tests](https://arxiv.org/abs/2102.07679) (2021)
    * [The LHC Olympics 2020: A Community Challenge for Anomaly Detection in High Energy Physics](https://arxiv.org/abs/2101.08320) [[DOI](https://doi.org/10.1088/1361-6633/ac36b9)] (2021)
    * [Unsupervised in-distribution anomaly detection of new physics through conditional density estimation](https://arxiv.org/abs/2012.11638) (2020)
    * [Uncovering hidden patterns in collider events with Bayesian probabilistic models](https://arxiv.org/abs/2012.08579) [[DOI](https://doi.org/10.22323/1.390.0238)] (2020)
    * [Quasi Anomalous Knowledge: Searching for new physics with embedded knowledge](https://arxiv.org/abs/2011.03550) [[DOI](https://doi.org/10.1007/JHEP06(2021)030)] (2020)
    * [Combining outlier analysis algorithms to identify new physics at the LHC](https://arxiv.org/abs/2010.07940) [[DOI](https://doi.org/10.1007/JHEP09(2021)024)] (2020)
    * [Unsupervised clustering for collider physics](https://arxiv.org/abs/2010.07106) [[DOI](https://doi.org/10.1103/PhysRevD.103.092007)] (2020)
    * [Anomaly Detection With Conditional Variational Autoencoders](https://arxiv.org/abs/2010.05531) (2020)
    * [Simulation-Assisted Decorrelation for Resonant Anomaly Detection](https://arxiv.org/abs/2009.02205) [[DOI](https://doi.org/10.1103/PhysRevD.104.035003)] (2020)
    * [Mass Unspecific Supervised Tagging (MUST) for boosted jets](https://arxiv.org/abs/2008.12792) [[DOI](https://doi.org/10.1007/JHEP03(2021)012)] (2020)
    * [Decoding Dark Matter Substructure without Supervision](https://arxiv.org/abs/2008.12731) (2020)
    * [Unsupervised Outlier Detection in Heavy-Ion Collisions](https://arxiv.org/abs/2007.15830) [[DOI](https://doi.org/10.1088/1402-4896/abf214)] (2020)
    * [Anomaly Awareness](https://arxiv.org/abs/2007.14462) [[DOI](https://doi.org/10.21468/SciPostPhys.15.2.053)] (2020)
    * [Variational Autoencoders for Anomalous Jet Tagging](https://arxiv.org/abs/2007.01850) [[DOI](https://doi.org/10.1103/PhysRevD.107.016002)] (2020)
    * [Tag N' Train: A Technique to Train Improved Classifiers on Unlabeled Data](https://arxiv.org/abs/2002.12376) [[DOI](https://doi.org/10.1007/JHEP01(2021)153)] (2020)
    * [Finding New Physics without learning about it: Anomaly Detection as a tool for Searches at Colliders](https://arxiv.org/abs/2006.05432) [[DOI](https://doi.org/10.1140/epjc/s10052-020-08807-w)] (2020)
    * [Learning the latent structure of collider events](https://arxiv.org/abs/2005.12319) [[DOI](https://doi.org/10.1007/JHEP10(2020)206)] (2020)
    * [Dijet resonance search with weak supervision using 13 TeV pp collisions in the ATLAS detector](https://arxiv.org/abs/2005.02983) [[DOI](https://doi.org/10.1103/PhysRevLett.125.131801)] (2020)
    * [Adversarially Learned Anomaly Detection on CMS Open Data: re-discovering the top quark](https://arxiv.org/abs/2005.01598) [[DOI](https://doi.org/10.1140/epjp/s13360-021-01109-4)] (2020)
    * [Use of a Generalized Energy Mover's Distance in the Search for Rare Phenomena at Colliders](https://arxiv.org/abs/2004.09360) [[DOI](https://doi.org/10.1140/epjc/s10052-021-08891-6)] (2020)
    * [Transferability of Deep Learning Models in Searches for New Physics at Colliders](https://arxiv.org/abs/1912.04220) [[DOI](https://doi.org/10.1103/PhysRevD.101.035042)] (2019)
    * [A generic anti-QCD jet tagger](https://arxiv.org/abs/1709.01087) [[DOI](https://doi.org/10.1007/JHEP11(2017)163)] (2017)
    * [Anomaly Detection with Density Estimation](https://arxiv.org/abs/2001.04990) [[DOI](https://doi.org/10.1103/PhysRevD.101.075042)] (2020)
    * [Simulation Assisted Likelihood-free Anomaly Detection](https://arxiv.org/abs/2001.05001) [[DOI](https://doi.org/10.1103/PhysRevD.101.095004)] (2020)
    * [Uncovering latent jet substructure](https://arxiv.org/abs/1904.04200) [[DOI](https://doi.org/10.1103/PhysRevD.100.056002)] (2019)
    * [Nonparametric semisupervised classification for signal detection in high energy physics](https://arxiv.org/abs/1809.02977) (2018)
    * [Does SUSY have friends? A new approach for LHC event analysis](https://arxiv.org/abs/1912.10625) [[DOI](https://doi.org/10.1007/JHEP02(2021)160)] (2019)
    * [Guiding New Physics Searches with Unsupervised Learning](https://arxiv.org/abs/1807.06038) [[DOI](https://doi.org/10.1140/epjc/s10052-019-6787-3)] (2018)
    * [Novelty Detection Meets Collider Physics](https://arxiv.org/abs/1807.10261) [[DOI](https://doi.org/10.1103/PhysRevD.101.076015)] (2018)
    * [Adversarially-trained autoencoders for robust unsupervised new physics searches](https://arxiv.org/abs/1905.10384) [[DOI](https://doi.org/10.1007/JHEP10(2019)047)] (2019)
    * [Variational Autoencoders for New Physics Mining at the Large Hadron Collider](https://arxiv.org/abs/1811.10276) [[DOI](https://doi.org/10.1007/JHEP05(2019)036)] (2018)
    * [A robust anomaly finder based on autoencoder](https://arxiv.org/abs/1903.02032) (2019)
    * [QCD or What?](https://arxiv.org/abs/1808.08979) [[DOI](https://doi.org/10.21468/SciPostPhys.6.3.030)] (2018)
    * [Searching for New Physics with Deep Autoencoders](https://arxiv.org/abs/1808.08992) [[DOI](https://doi.org/10.1103/PhysRevD.101.075021)] (2018)
    * [Learning Multivariate New Physics](https://arxiv.org/abs/1912.12155) [[DOI](https://doi.org/10.1140/epjc/s10052-021-08853-y)] (2019)
    * [Extending the search for new resonances with machine learning](https://arxiv.org/abs/1902.02634) [[DOI](https://doi.org/10.1103/PhysRevD.99.014038)] (2019)
    * [Anomaly Detection for Resonant New Physics with Machine Learning](https://arxiv.org/abs/1805.02664) [[DOI](https://doi.org/10.1103/PhysRevLett.121.241803)] (2018)
    * [Learning New Physics from a Machine](https://arxiv.org/abs/1806.02350) [[DOI](https://doi.org/10.1103/PhysRevD.99.015014)] (2018)

##  Foundation Models, LLMs.


??? example "Foundation Models, LLMs."

    * [Is Tokenization Needed for Masked Particle Modelling?](https://arxiv.org/abs/2409.12589) (2024)
    * [OmniLearn: A Method to Simultaneously Facilitate All Jet Physics Tasks](https://arxiv.org/abs/2404.16091) (2024)
    * [Xiwu: A Basis Flexible and Learnable LLM for High Energy Physics](https://arxiv.org/abs/2404.08001) (2024)
    * [Physics Event Classification Using Large Language Models](https://arxiv.org/abs/2404.05752) [[DOI](https://doi.org/10.1088/1748-0221/19/07/C07011)] (2024)
    * [Re-Simulation-based Self-Supervised Learning for Pre-Training Foundation Models](https://arxiv.org/abs/2403.07066) (2024)
    * [OmniJet-$\alpha$: The first cross-task foundation model for particle physics](https://arxiv.org/abs/2403.05618) [[DOI](https://doi.org/10.1088/2632-2153/ad66ad)] (2024)
    * [Finetuning Foundation Models for Joint Analysis Optimization](https://arxiv.org/abs/2401.13536) [[DOI](https://doi.org/10.1088/2632-2153/ad55a3)] (2024)

##  Simulation-based (`likelihood-free') Inference

??? example "Parameter estimation"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Parameter estimation
    </div>

    * [Profile Likelihoods on ML-Steroids](https://arxiv.org/abs/2411.00942) (2024)
    * [Optimal Equivariant Architectures from the Symmetries of Matrix-Element Likelihoods](https://arxiv.org/abs/2410.18553) (2024)
    * [Advancing Tools for Simulation-Based Inference](https://arxiv.org/abs/2410.07315) (2024)
    * [Bayesian Inference analysis of jet quenching using inclusive jet and hadron suppression measurements](https://arxiv.org/abs/2408.08247) (2024)
    * [Constraining the Higgs Potential with Neural Simulation-based Inference for Di-Higgs Production](https://arxiv.org/abs/2405.15847) [[DOI](https://doi.org/10.1103/PhysRevD.110.056004)] (2024)
    * [Bayesian Active Search on Parameter Space: a 95 GeV Spin-0 Resonance in the ($B-L$)SSM](https://arxiv.org/abs/2404.18653) (2024)
    * [Improvement and generalization of ABCD method with Bayesian inference](https://arxiv.org/abs/2402.08001) [[DOI](https://doi.org/10.21468/SciPostPhysCore.7.3.043)] (2024)
    * [Rotation-equivariant graph neural network for learning hadronic SMEFT effects](https://arxiv.org/abs/2401.10323) [[DOI](https://doi.org/10.1103/PhysRevD.109.076012)] (2024)
    * [From Optimal Observables to Machine Learning: an Effective-Field-Theory Analysis of $e^+e^- \to W^+W^-$ at Future Lepton Colliders](https://arxiv.org/abs/2401.02474) [[DOI](https://doi.org/10.1007/JHEP05(2024)292)] (2024)
    * [Precision-Machine Learning for the Matrix Element Method](https://arxiv.org/abs/2310.07752) (2023)
    * [Scaling MadMiner with a deployment on REANA](https://arxiv.org/abs/2304.05814) (2023)
    * [Simulation-based inference in the search for CP violation in leptonic WH production](https://arxiv.org/abs/2308.02882) [[DOI](https://doi.org/10.1007/JHEP04(2024)014)] (2023)
    * [Reconstructing axion-like particles from beam dumps with simulation-based inference](https://arxiv.org/abs/2308.01353) [[DOI](https://doi.org/10.1140/epjc/s10052-024-12557-4)] (2023)
    * [Machine Learning and Kalman Filtering for Nanomechanical Mass Spectrometry](https://arxiv.org/abs/2306.00563) [[DOI](https://doi.org/10.1109/JSEN.2024.3350730)] (2023)
    * [Emulator-based Bayesian Inference on Non-Proportional Scintillation Models by Compton-Edge Probing](https://arxiv.org/abs/2302.05641) [[DOI](https://doi.org/10.1038/s41467-023-42574-y)] (2023)
    * [Hierarchical Neural Simulation-Based Inference Over Event Ensembles](https://arxiv.org/abs/2306.12584) (2023)
    * [Learning Likelihood Ratios with Neural Network Classifiers](https://arxiv.org/abs/2305.10500) [[DOI](https://doi.org/10.1007/JHEP02(2024)136)] (2023)
    * [Deep Learning for the Matrix Element Method](https://arxiv.org/abs/2211.11910) [[DOI](https://doi.org/10.22323/1.414.0246)] (2022)
    * [Two Invertible Networks for the Matrix Element Method](https://arxiv.org/abs/2210.00019) [[DOI](https://doi.org/10.21468/SciPostPhys.15.3.094)] (2022)
    * [Machine-Learned Exclusion Limits without Binning](https://arxiv.org/abs/2211.04806) [[DOI](https://doi.org/10.1140/epjc/s10052-023-12314-z)] (2022)
    * [New Machine Learning Techniques for Simulation-Based Inference: InferoStatic Nets, Kernel Score Estimation, and Kernel Likelihood Ratio Estimation](https://arxiv.org/abs/2210.01680) (2022)
    * [A method for approximating optimal statistical significances with machine-learned likelihoods](https://arxiv.org/abs/2205.05952) [[DOI](https://doi.org/10.1140/epjc/s10052-022-10944-3)] (2022)
    * [Constraining CP-violation in the Higgs-top-quark interaction using machine-learning-based inference](https://arxiv.org/abs/2110.10177) [[DOI](https://doi.org/10.1007/JHEP03(2022)017)] (2021)
    * [Machine Learning the Higgs-Top CP Phase](https://arxiv.org/abs/2110.07635) [[DOI](https://doi.org/10.1103/PhysRevD.105.035023)] (2021)
    * [A neural simulation-based inference approach for characterizing the Galactic Center $\gamma$-ray excess](https://arxiv.org/abs/2110.06931) [[DOI](https://doi.org/10.1103/PhysRevD.105.063017)] (2021)
    * [Black-Box Optimization with Local Generative Surrogates](https://arxiv.org/abs/2002.04632) [[url](https://proceedings.neurips.cc/paper/2020/hash/a878dbebc902328b41dbf02aa87abb58-Abstract.html)] (2020)
    * [Tree boosting for learning EFT parameters](https://arxiv.org/abs/2107.10859) [[DOI](https://doi.org/10.1016/j.cpc.2022.108385)] (2021)
    * [E Pluribus Unum Ex Machina: Learning from Many Collider Events at Once](https://arxiv.org/abs/2101.07263) [[DOI](https://doi.org/10.1103/PhysRevD.103.116013)] (2021)
    * [Measuring QCD Splittings with Invertible Networks](https://arxiv.org/abs/2012.09873) [[DOI](https://doi.org/10.21468/SciPostPhys.10.6.126)] (2020)
    * [Parameter Inference from Event Ensembles and the Top-Quark Mass](https://arxiv.org/abs/2011.04666) [[DOI](https://doi.org/10.1007/JHEP09(2021)058)] (2020)
    * [Targeted Likelihood-Free Inference of Dark Matter Substructure in Strongly-Lensed Galaxies](https://arxiv.org/abs/2010.07032) (2020)
    * [Parameter Estimation using Neural Networks in the Presence of Detector Effects](https://arxiv.org/abs/2010.03569) [[DOI](https://doi.org/10.1103/PhysRevD.103.036001)] (2020)
    * [Approximating Likelihood Ratios with Calibrated Discriminative  Classifiers](https://arxiv.org/abs/1506.02169) (2015)
    * [Mining gold from implicit models to improve likelihood-free inference](https://arxiv.org/abs/1805.12244) [[DOI](https://doi.org/10.1073/pnas.1915980117)] (2018)
    * [MadMiner: Machine learning-based inference for particle physics](https://arxiv.org/abs/1907.10621) [[DOI](https://doi.org/10.1007/s41781-020-0035-2)] (2019)
    * [A Guide to Constraining Effective Field Theories with Machine Learning](https://arxiv.org/abs/1805.00020) [[DOI](https://doi.org/10.1103/PhysRevD.98.052004)] (2018)
    * [Constraining Effective Field Theories with Machine Learning](https://arxiv.org/abs/1805.00013) [[DOI](https://doi.org/10.1103/PhysRevLett.121.111801)] (2018)
    * [Resonance Searches with Machine Learned Likelihood Ratios](https://arxiv.org/abs/2002.04699) (2020)
    * [Likelihood-free inference with an improved cross-entropy estimator](https://arxiv.org/abs/1808.00973) (2018)
    * [Neural Networks for Full Phase-space Reweighting and Parameter Tuning](https://arxiv.org/abs/1907.08209) [[DOI](https://doi.org/10.1103/PhysRevD.101.091901)] (2019)


??? example "Unfolding"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Unfolding
    </div>

    * [Generative Unfolding with Distribution Mapping](https://arxiv.org/abs/2411.02495) (2024)
    * [Novel machine learning applications at the LHC](https://arxiv.org/abs/2409.20413) (2024)
    * [Multidimensional Deconvolution with Profiling](https://arxiv.org/abs/2409.10421) (2024)
    * [Moment Unfolding](https://arxiv.org/abs/2407.11284) (2024)
    * [The Landscape of Unfolding with Machine Learning](https://arxiv.org/abs/2404.18807) (2024)
    * [Full Event Particle-Level Unfolding with Variable-Length Latent Variational Diffusion](https://arxiv.org/abs/2404.14332) (2024)
    * [End-To-End Latent Variational Diffusion Models for Inverse Problems in High Energy Physics](https://arxiv.org/abs/2305.10399) (2023)
    * [Unbinned Profiled Unfolding](https://arxiv.org/abs/2302.05390) [[DOI](https://doi.org/10.1103/PhysRevD.108.016002)] (2023)
    * [An unfolding method based on conditional Invertible Neural Networks (cINN) using iterative training](https://arxiv.org/abs/2212.08674) [[DOI](https://doi.org/10.21468/scipostphyscore.7.1.007)] (2022)
    * [Optimizing Observables with Machine Learning for Better Unfolding](https://arxiv.org/abs/2203.16722) [[DOI](https://doi.org/10.1088/1748-0221/17/07/P07009)] (2022)
    * [Feed-forward neural network unfolding](https://arxiv.org/abs/2112.08180) (2021)
    * [Presenting Unbinned Differential Cross Section Results](https://arxiv.org/abs/2109.13243) [[DOI](https://doi.org/10.1088/1748-0221/17/01/P01024)] (2021)
    * [Measurement of lepton-jet correlation in deep-inelastic scattering with the H1 detector using machine learning for unfolding](https://arxiv.org/abs/2108.12376) [[DOI](https://doi.org/10.1103/PhysRevLett.128.132002)] (2021)
    * [Preserving New Physics while Simultaneously Unfolding All Observables](https://arxiv.org/abs/2105.09923) [[DOI](https://doi.org/10.1103/PhysRevD.104.076027)] (2021)
    * [Scaffolding Simulations with Deep Learning for High-dimensional Deconvolution](https://arxiv.org/abs/2105.04448) (2021)
    * [Comparison of Machine Learning Approach to other Unfolding Methods](https://arxiv.org/abs/2104.03036) [[DOI](https://doi.org/10.5506/APhysPolB.52.863)] (2021)
    * [Foundations of a Fast, Data-Driven, Machine-Learned Simulator](https://arxiv.org/abs/2101.08944) [[DOI](https://doi.org/10.1038/s41598-022-10966-7)] (2021)
    * [Neural Empirical Bayes: Source Distribution Estimation and its Applications to Simulation-Based Inference](https://arxiv.org/abs/2011.05836) [[url](https://proceedings.mlr.press/v130/vandegar21a.html)] (2020)
    * [Invertible Networks or Partons to Detector and Back Again](https://arxiv.org/abs/2006.06685) [[DOI](https://doi.org/10.21468/SciPostPhys.9.5.074)] (2020)
    * Binning-Free Unfolding Based on Monte Carlo Migration (2003)
    * [Unfolding by weighting Monte Carlo events](https://doi.org/10.1016/0168-9002(94)01067-6) (1995)
    * [Advanced event reweighting using multivariate analysis](https://doi.org/10.1088/1742-6596/368/1/012028) (2012)
    * [Machine learning as an instrument for data unfolding](https://arxiv.org/abs/1712.01814) (2017)
    * [Machine learning approach to inverse problem and unfolding procedure](https://arxiv.org/abs/1004.2006) (2010)
    * [How to GAN away Detector Effects](https://arxiv.org/abs/1912.00477) [[DOI](https://doi.org/10.21468/SciPostPhys.8.4.070)] (2019)
    * [Unfolding with Generative Adversarial Networks](https://arxiv.org/abs/1806.00433) (2018)
    * [OmniFold: A Method to Simultaneously Unfold All Observables](https://arxiv.org/abs/1911.09107) [[DOI](https://doi.org/10.1103/PhysRevLett.124.182001)] (2019)
    * [DeepEfficiency - optimal efficiency inversion in higher dimensions at the LHC](https://arxiv.org/abs/1809.06101) (2018)


??? example "Domain adaptation"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Domain adaptation
    </div>

    * [Converting sWeights to Probabilities with Density Ratios](https://arxiv.org/abs/2409.08183) (2024)
    * [Normalizing Flows for Domain Adaptation when Identifying $\Lambda$ Hyperon Events](https://arxiv.org/abs/2403.14804) [[DOI](https://doi.org/10.1088/1748-0221/19/06/C06020)] (2024)
    * [Improving $\Lambda$ Signal Extraction with Domain Adaptation via Normalizing Flows](https://arxiv.org/abs/2403.14076) [[DOI](https://doi.org/10.22323/1.456.0043)] (2024)
    * [Peak finding algorithm for cluster counting with domain adaptation](https://arxiv.org/abs/2402.16270) [[DOI](https://doi.org/10.1016/j.cpc.2024.109208)] (2024)
    * [Flow Away your Differences: Conditional Normalizing Flows as an Improvement to Reweighting](https://arxiv.org/abs/2304.14963) (2023)
    * [Mimicking non-ideal instrument behavior for hologram processing using neural style translation](https://arxiv.org/abs/2301.02757) [[DOI](https://doi.org/10.1364/OE.486741)] (2023)
    * [Model independent measurements of Standard Model cross sections with Domain Adaptation](https://arxiv.org/abs/2207.09293) [[DOI](https://doi.org/10.1140/epjc/s10052-022-10871-3)] (2022)
    * [Neural Conditional Reweighting](https://arxiv.org/abs/2107.08979) [[DOI](https://doi.org/10.1103/PhysRevD.105.076015)] (2021)
    * [DCTRGAN: Improving the Precision of Generative Models with Reweighting](https://arxiv.org/abs/2009.03796) [[DOI](https://doi.org/10.1088/1748-0221/15/11/P11004)] (2020)
    * [Approximating Likelihood Ratios with Calibrated Discriminative  Classifiers](https://arxiv.org/abs/1506.02169) (2015)
    * [Neural Networks for Full Phase-space Reweighting and Parameter Tuning](https://arxiv.org/abs/1907.08209) [[DOI](https://doi.org/10.1103/PhysRevD.101.091901)] (2019)
    * [Reweighting with Boosted Decision Trees](https://arxiv.org/abs/1608.05806) [[DOI](https://doi.org/10.1088/1742-6596/762/1/012036)] (2016)


??? example "BSM"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  BSM
    </div>

    * [Profile Likelihoods on ML-Steroids](https://arxiv.org/abs/2411.00942) (2024)
    * [Machine Learning Electroweakino Production](https://arxiv.org/abs/2411.00093) (2024)
    * [A novel quantum machine learning classifier to search for new physics](https://arxiv.org/abs/2410.18847) (2024)
    * [Probing Light Scalars and Vector-like Quarks at the High-Luminosity LHC](https://arxiv.org/abs/2410.17854) (2024)
    * [Signal model parameter scan using Normalizing Flow](https://arxiv.org/abs/2409.13201) [[DOI](https://doi.org/10.22323/1.458.0017)] (2024)
    * [Refinable modeling for unbinned SMEFT analyses](https://arxiv.org/abs/2406.19076) (2024)
    * [Exploring Exotic Decays of the Higgs Boson to Multi-Photons at the LHC via Multimodal Learning Approaches](https://arxiv.org/abs/2405.18834) [[DOI](https://doi.org/10.1007/JHEP09(2024)166)] (2024)
    * [Magnetic Monopole Phenomenology at Future Hadron Colliders](https://arxiv.org/abs/2404.10871) (2024)
    * [Boosted four-top production at the LHC : a window to Randall-Sundrum or extended color symmetry](https://arxiv.org/abs/2404.04409) [[DOI](https://doi.org/10.1103/PhysRevD.110.075020)] (2024)
    * [Probing intractable beyond-standard-model parameter spaces armed with Machine Learning](https://arxiv.org/abs/2404.02698) [[DOI](https://doi.org/10.1140/epjs/s11734-024-01236-w)] (2024)
    * [Probing Heavy Charged Higgs Boson Using Multivariate Technique at Gamma-Gamma Collider](https://arxiv.org/abs/2403.20293) (2024)
    * [Dark Matter-induced electron excitations in silicon and germanium with Deep Learning](https://arxiv.org/abs/2403.07053) (2024)
    * [Higgs couplings in SMEFT via Zh production at the HL-LHC](https://arxiv.org/abs/2403.03001) (2024)
    * [The impact of CP-violating phases on DM observables in the cpMSSM](https://arxiv.org/abs/2402.08814) (2024)
    * [Current status of the light neutralino thermal dark matter in the phenomenological MSSM](https://arxiv.org/abs/2402.07991) (2024)
    * [Combining evolutionary strategies and novelty detection to go beyond the alignment limit of the Z3 3HDM](https://arxiv.org/abs/2402.07661) [[DOI](https://doi.org/10.1103/PhysRevD.109.095040)] (2024)
    * [LHC Study of Third-Generation Scalar Leptoquarks with Machine-Learned Likelihoods](https://arxiv.org/abs/2309.05407) [[DOI](https://doi.org/10.1103/PhysRevD.109.055032)] (2023)
    * [Tip of the Red Giant Branch Bounds on the Neutrino Magnetic Dipole Moment Revisited](https://arxiv.org/abs/2307.13050) (2023)
    * [Pinning down the leptophobic $Z^\prime$ in leptonic final states with Deep Learning](https://arxiv.org/abs/2307.01118) [[DOI](https://doi.org/10.1016/j.physletb.2023.138417)] (2023)
    * [Autoencoders for Real-Time SUEP Detection](https://arxiv.org/abs/2306.13595) [[DOI](https://doi.org/10.1140/epjp/s13360-024-05028-y)] (2023)
    * [Simple, but not simplified: A new approach for optimising beyond-Standard Model physics searches at the Large Hadron Collider](https://arxiv.org/abs/2305.01835) (2023)
    * [Tip of the Red Giant Branch Bounds on the Axion-Electron Coupling Revisited](https://arxiv.org/abs/2305.03113) (2023)
    * [On the BSM reach of four top production at the LHC](https://arxiv.org/abs/2302.08281) [[DOI](https://doi.org/10.1103/PhysRevD.108.035001)] (2023)
    * [LHC EFT WG Report: Experimental Measurements and Observables](https://arxiv.org/abs/2211.08353) (2022)
    * [Unbinned multivariate observables for global SMEFT analyses from machine learning](https://arxiv.org/abs/2211.02058) [[DOI](https://doi.org/10.1007/JHEP03(2023)033)] (2022)
    * [Exploring Parameter Spaces with Artificial Intelligence and Machine Learning Black-Box Optimisation Algorithms](https://arxiv.org/abs/2206.09223) [[DOI](https://doi.org/10.1103/PhysRevD.107.035004)] (2022)
    * [Use of a Generalized Energy Mover's Distance in the Search for Rare Phenomena at Colliders](https://arxiv.org/abs/2004.09360) [[DOI](https://doi.org/10.1140/epjc/s10052-021-08891-6)] (2020)
    * [MadMiner: Machine learning-based inference for particle physics](https://arxiv.org/abs/1907.10621) [[DOI](https://doi.org/10.1007/s41781-020-0035-2)] (2019)
    * [Mining gold from implicit models to improve likelihood-free inference](https://arxiv.org/abs/1805.12244) [[DOI](https://doi.org/10.1073/pnas.1915980117)] (2018)
    * [A Guide to Constraining Effective Field Theories with Machine Learning](https://arxiv.org/abs/1805.00020) [[DOI](https://doi.org/10.1103/PhysRevD.98.052004)] (2018)
    * [Constraining Effective Field Theories with Machine Learning](https://arxiv.org/abs/1805.00013) [[DOI](https://doi.org/10.1103/PhysRevLett.121.111801)] (2018)
    * [Resonance Searches with Machine Learned Likelihood Ratios](https://arxiv.org/abs/2002.04699) (2020)
    * [Simulation Assisted Likelihood-free Anomaly Detection](https://arxiv.org/abs/2001.05001) [[DOI](https://doi.org/10.1103/PhysRevD.101.095004)] (2020)


??? example "Differentiable Simulation"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Differentiable Simulation
    </div>

    * [Rejection Sampling with Autodifferentiation -- Case study: Fitting a Hadronization Model](https://arxiv.org/abs/2411.02194) (2024)
    * [Full Detector Simulation of a Projective Dual-Readout Segmented Crystal Electromagnetic Calorimeter with Precision Timing](https://arxiv.org/abs/2408.11027) (2024)
    * [Differentiable MadNIS-Lite](https://arxiv.org/abs/2408.01486) (2024)
    * [Differentiable nuclear deexcitation simulation for low energy neutrino physics](https://arxiv.org/abs/2404.00180) (2024)
    * [Differentiable Vertex Fitting for Jet Flavour Tagging](https://arxiv.org/abs/2310.12804) [[DOI](https://doi.org/10.1103/PhysRevD.110.052010)] (2023)
    * [Progress in End-to-End Optimization of Detectors for Fundamental Physics with Differentiable Programming](https://arxiv.org/abs/2310.05673) (2023)
    * [Branches of a Tree: Taking Derivatives of Programs with Discrete and Branching Randomness in High Energy Physics](https://arxiv.org/abs/2308.16680) (2023)
    * [Differentiable Earth Mover's Distance for Data Compression at the High-Luminosity LHC](https://arxiv.org/abs/2306.04712) [[DOI](https://doi.org/10.1088/2632-2153/ad1139)] (2023)
    * [Novel Machine Learning and Differentiable Programming Techniques applied to the VIP-2 Underground Experiment](https://arxiv.org/abs/2305.17153) [[DOI](https://doi.org/10.1088/1361-6501/ad080a)] (2023)
    * [Implicit Neural Representation as a Differentiable Surrogate for Photon Propagation in a Monolithic Neutrino Detector](https://arxiv.org/abs/2211.01505) (2022)
    * [Morphing parton showers with event derivatives](https://arxiv.org/abs/2208.02274) (2022)
    * [Toward the end-to-end optimization of particle physics instruments with differentiable programming](https://arxiv.org/abs/2203.13818) [[DOI](https://doi.org/10.1016/j.revip.2023.100085)] (2022)
    * [Differentiable Matrix Elements with MadJax](https://arxiv.org/abs/2203.00057) [[DOI](https://doi.org/10.1088/1742-6596/2438/1/012137)] (2022)

##  Uncertainty Quantification

??? example "Interpretability"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Interpretability
    </div>

    * [Explainable AI classification for parton density theory](https://arxiv.org/abs/2407.03411) (2024)
    * [Interpretable machine learning approach for electron antineutrino selection in a large liquid scintillator detector](https://arxiv.org/abs/2406.12901) (2024)
    * [Statistical divergences in high-dimensional hypothesis testing and a modern technique for estimating them](https://arxiv.org/abs/2405.06397) (2024)
    * [Interpretable deep learning models for the inference and classification of LHC data](https://arxiv.org/abs/2312.12330) [[DOI](https://doi.org/10.1007/JHEP05(2024)004)] (2023)
    * [Interpretable Machine Learning Methods Applied to Jet Background Subtraction in Heavy Ion Collisions](https://arxiv.org/abs/2303.08275) [[DOI](https://doi.org/10.1103/PhysRevC.108.L021901)] (2023)
    * [Interpretability of an Interaction Network for identifying $H \rightarrow b\bar{b}$ jets](https://arxiv.org/abs/2211.12770) [[DOI](https://doi.org/10.22323/1.414.0223)] (2022)
    * [A Detailed Study of Interpretability of Deep Neural Network based Top Taggers](https://arxiv.org/abs/2210.04371) [[DOI](https://doi.org/10.1088/2632-2153/ace0a1)] (2022)
    * [Lessons on interpretable machine learning from particle physics](https://arxiv.org/abs/2203.08021) [[DOI](https://doi.org/10.1038/s42254-022-00456-0)] (2022)
    * [Improving Parametric Neural Networks for High-Energy Physics (and Beyond)](https://arxiv.org/abs/2202.00424) [[DOI](https://doi.org/10.1088/2632-2153/ac917c)] (2022)
    * [Creating Simple, Interpretable Anomaly Detectors for New Physics in Jet Substructure](https://arxiv.org/abs/2203.01343) [[DOI](https://doi.org/10.1103/PhysRevD.106.035014)] (2022)
    * [Explaining machine-learned particle-flow reconstruction](https://arxiv.org/abs/2111.12840) (2021)
    * [An Exploration of Learnt Representations of W Jets](https://arxiv.org/abs/2109.10919) (2021)
    * [Safety of Quark/Gluon Jet Classification](https://arxiv.org/abs/2103.09103) (2021)
    * [Resurrecting $b\bar{b}h$ with kinematic shapes](https://arxiv.org/abs/2011.13945) [[DOI](https://doi.org/10.1007/JHEP04(2021)139)] (2020)
    * [Explainable AI for ML jet taggers using expert variables and layerwise relevance propagation](https://arxiv.org/abs/2011.13466) [[DOI](https://doi.org/10.1007/JHEP05(2021)208)] (2020)
    * [CapsNets Continuing the Convolutional Quest](https://arxiv.org/abs/1906.11265) [[DOI](https://doi.org/10.21468/SciPostPhys.8.2.023)] (2019)
    * [What is the Machine Learning?](https://arxiv.org/abs/1709.10106) [[DOI](https://doi.org/10.1103/PhysRevD.97.056009)] (2017)
    * [Jet-images — deep learning edition](https://arxiv.org/abs/1511.05190) [[DOI](https://doi.org/10.1007/JHEP07(2016)069)] (2015)


??? example "Estimation"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Estimation
    </div>

    * [Modelling parametric uncertainty in PDEs models via Physics-Informed Neural Networks](https://arxiv.org/abs/2408.04690) (2024)
    * [Calibrating Bayesian Generative Machine Learning for Bayesiamplification](https://arxiv.org/abs/2408.00838) (2024)
    * [Smartpixels: Towards on-sensor inference of charged particle track parameters and uncertainties](https://arxiv.org/abs/2312.11676) (2023)
    * [The DL Advocate: Playing the devil's advocate with hidden systematic uncertainties](https://arxiv.org/abs/2303.15956) [[DOI](https://doi.org/10.1140/epjc/s10052-023-11925-w)] (2023)
    * [Deep Neural Network Uncertainty Quantification for LArTPC Reconstruction](https://arxiv.org/abs/2302.03787) [[DOI](https://doi.org/10.1088/1748-0221/18/12/P12013)] (2023)
    * [Exploring the Universality of Hadronic Jet Classification](https://arxiv.org/abs/2204.03812) [[DOI](https://doi.org/10.1140/epjc/s10052-022-11084-4)] (2022)
    * [Understanding Event-Generation Networks via Uncertainties](https://arxiv.org/abs/2104.04543) [[DOI](https://doi.org/10.21468/SciPostPhys.13.1.003)] (2021)
    * [Parton Shower Uncertainties in Jet Substructure Analyses with Deep Neural Networks](https://arxiv.org/abs/1609.00607) [[DOI](https://doi.org/10.1103/PhysRevD.95.014018)] (2016)
    * [AI Safety for High Energy Physics](https://arxiv.org/abs/1910.08606) (2019)
    * [A guide for deploying Deep Learning in LHC searches: How to achieve optimality and account for uncertainty](https://arxiv.org/abs/1909.03081) [[DOI](https://doi.org/10.21468/SciPostPhys.8.6.090)] (2019)


??? example "Mitigation"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Mitigation
    </div>

    * [Improving robustness of jet tagging algorithms with adversarial training](https://arxiv.org/abs/2203.13890) [[DOI](https://doi.org/10.1007/s41781-022-00087-1)] (2022)
    * [Combine and Conquer: Event Reconstruction with Bayesian Ensemble Neural Networks](https://arxiv.org/abs/2102.01078) [[DOI](https://doi.org/10.1007/JHEP04(2021)296)] (2021)
    * [Learning to Pivot with Adversarial Networks](https://arxiv.org/abs/1611.01046) [[url](https://papers.nips.cc/paper/2017/hash/48ab2f9b45957ab574cf005eb8a76760-Abstract.html)] (2016)
    * [Machine Learning Uncertainties with Adversarial Neural Networks](https://arxiv.org/abs/1807.08763) [[DOI](https://doi.org/10.1140/epjc/s10052-018-6511-8)] (2018)
    * [Adversarial learning to eliminate systematic errors: a case study in High Energy Physics](https://dl4physicalsciences.github.io/files/nips_dlps_2017_1.pdf) (2017)


??? example "Uncertainty- and inference-aware learning"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Uncertainty- and inference-aware learning
    </div>

    * [Application of Inferno to a Top Pair Cross Section Measurement with CMS Open Data](https://arxiv.org/abs/2301.10358) (2023)
    * [neos: End-to-End-Optimised Summary Statistics for High Energy Physics](https://arxiv.org/abs/2203.05570) [[DOI](https://doi.org/10.48550/arXiv.2203.05570)] (2022)
    * [Punzi-loss: A non-differentiable metric approximation for sensitivity optimisation in the search for new particles](https://arxiv.org/abs/2110.00810) [[DOI](https://doi.org/10.1140/epjc/s10052-022-10070-0)] (2021)
    * [Uncertainty Aware Learning for High Energy Physics](https://arxiv.org/abs/2105.08742) [[DOI](https://doi.org/10.1103/PhysRevD.104.056026)] (2021)
    * [Optimal statistical inference in the presence of systematic uncertainties using neural network optimization based on binned Poisson likelihoods with nuisance parameters](https://arxiv.org/abs/2003.07186) [[DOI](https://doi.org/10.1007/s41781-020-00049-5)] (2020)
    * [INFERNO: Inference-Aware Neural Optimisation](https://arxiv.org/abs/1806.04743) [[DOI](https://doi.org/10.1016/j.cpc.2019.06.007)] (2018)
    * [Deep-Learning Jets with Uncertainties and More](https://arxiv.org/abs/1904.10004) [[DOI](https://doi.org/10.21468/SciPostPhys.8.1.006)] (2019)
    * [Constraining the Parameters of High-Dimensional Models with Active Learning](https://arxiv.org/abs/1905.08628) [[DOI](https://doi.org/10.1140/epjc/s10052-019-7437-5)] (2019)

##  Formal Theory and ML

??? example "Theory and physics for ML"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Theory and physics for ML
    </div>

    * [Neural Scaling Laws From Large-N Field Theory: Solvable Model Beyond the Ridgeless Limit](https://arxiv.org/abs/2405.19398) (2024)
    * [Metric Flows with Neural Networks](https://arxiv.org/abs/2310.19870) [[DOI](https://doi.org/10.1088/2632-2153/ad8533)] (2023)
    * [Neural Network Field Theories: Non-Gaussianity, Actions, and Locality](https://arxiv.org/abs/2307.03223) [[DOI](https://doi.org/10.1088/2632-2153/ad17d3)] (2023)
    * [Black holes and the loss landscape in machine learning](https://arxiv.org/abs/2306.14817) [[DOI](https://doi.org/10.1007/JHEP10(2023)107)] (2023)
    * [A Correspondence Between Deep Boltzmann Machines and p-Adic Statistical Field Theories](https://arxiv.org/abs/2306.03751) [[DOI](https://doi.org/10.4310/atmp.240914023328)] (2023)
    * [Structures of Neural Network Effective Theories](https://arxiv.org/abs/2305.02334) [[DOI](https://doi.org/10.1103/PhysRevD.109.105007)] (2023)
    * [p-Adic statistical field theory and convolutional deep Boltzmann machines](https://arxiv.org/abs/2302.03817) [[DOI](https://doi.org/10.1093/ptep/ptad061)] (2023)
    * [Renormalization in the neural network-quantum field theory correspondence](https://arxiv.org/abs/2212.11811) (2022)


??? example "ML for theory"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  ML for theory
    </div>

    * [Truth, beauty, and goodness in grand unification: a machine learning approach](https://arxiv.org/abs/2411.06718) (2024)
    * [cymyc -- Calabi-Yau Metrics, Yukawas, and Curvature](https://arxiv.org/abs/2410.19728) (2024)
    * [Calabi-Yau metrics through Grassmannian learning and Donaldson's algorithm](https://arxiv.org/abs/2410.11284) (2024)
    * [Bootstrapping string models with entanglement minimization and Machine-Learning](https://arxiv.org/abs/2409.18259) (2024)
    * [Machine Learning Toric Duality in Brane Tilings](https://arxiv.org/abs/2409.15251) (2024)
    * [Conformal Fields from Neural Networks](https://arxiv.org/abs/2409.12222) (2024)
    * [Variational Monte Carlo with Neural Network Quantum States for Yang-Mills Matrix Model](https://arxiv.org/abs/2409.00398) (2024)
    * [Learning the Simplicity of Scattering Amplitudes](https://arxiv.org/abs/2408.04720) (2024)
    * [Deep Learning Calabi-Yau four folds with hybrid and recurrent neural network architectures](https://arxiv.org/abs/2405.17406) (2024)
    * [Learning BPS Spectra and the Gap Conjecture](https://arxiv.org/abs/2405.09993) [[DOI](https://doi.org/10.1103/PhysRevD.110.046016)] (2024)
    * [Classical integrability in the presence of a cosmological constant: analytic and machine learning results](https://arxiv.org/abs/2404.18247) (2024)
    * [On Machine Learning Complete Intersection Calabi-Yau 3-folds](https://arxiv.org/abs/2404.11710) (2024)
    * [Feynman Diagrams as Computational Graphs](https://arxiv.org/abs/2403.18840) (2024)
    * [Predicting Feynman periods in $\phi^4$-theory](https://arxiv.org/abs/2403.16217) (2024)
    * [Gravitational Duals from Equations of State](https://arxiv.org/abs/2403.14763) [[DOI](https://doi.org/10.1007/JHEP07(2024)087)] (2024)
    * [Quantum chaos in the sparse SYK model](https://arxiv.org/abs/2403.13884) (2024)
    * [Neural network representation of quantum systems](https://arxiv.org/abs/2403.11420) (2024)
    * [Neural Network Learning and Quantum Gravity](https://arxiv.org/abs/2403.03245) [[DOI](https://doi.org/10.1007/JHEP07(2024)105)] (2024)
    * [Rigor with machine learning from field theory to the Poincar\'e conjecture](https://arxiv.org/abs/2402.13321) [[DOI](https://doi.org/10.1038/s42254-024-00709-0)] (2024)
    * [NCoder -- A Quantum Field Theory approach to encoding data](https://arxiv.org/abs/2402.00944) (2024)
    * [Computation of Quark Masses from String Theory](https://arxiv.org/abs/2402.01615) (2024)
    * [Autoencoder-Driven Clustering of Intersecting D-brane Models via Tadpole Charge](https://arxiv.org/abs/2312.07181) [[DOI](https://doi.org/10.1007/JHEP08(2024)133)] (2023)
    * [Calabi-Yau Four/Five/Six-folds as $\mathbb{P}^n_\textbf{w}$ Hypersurfaces: Machine Learning, Approximation, and Generation](https://arxiv.org/abs/2311.17146) [[DOI](https://doi.org/10.1103/PhysRevD.109.106006)] (2023)
    * [Deep learning complete intersection Calabi-Yau manifolds](https://arxiv.org/abs/2311.11847) [[DOI](https://doi.org/10.1142/9781800613706_0005)] (2023)
    * [Machine learning the breakdown of tame effective theories](https://arxiv.org/abs/2311.03437) [[DOI](https://doi.org/10.1140/epjc/s10052-024-12988-z)] (2023)
    * [Seeking Truth and Beauty in Flavor Physics with Machine Learning](https://arxiv.org/abs/2311.00087) (2023)
    * [Metric Flows with Neural Networks](https://arxiv.org/abs/2310.19870) [[DOI](https://doi.org/10.1088/2632-2153/ad8533)] (2023)
    * [Machine Learning Regularization for the Minimum Volume Formula of Toric Calabi-Yau 3-folds](https://arxiv.org/abs/2310.19276) [[DOI](https://doi.org/10.1103/PhysRevD.109.046015)] (2023)
    * [Constructing and Machine Learning Calabi-Yau Five-folds](https://arxiv.org/abs/2310.15966) [[DOI](https://doi.org/10.1002/prop.202300262)] (2023)
    * [BFBrain: Scalar Bounded-From-Below Conditions from Bayesian Active Learning](https://arxiv.org/abs/2309.10959) [[DOI](https://doi.org/10.1103/PhysRevD.109.095018)] (2023)
    * [Unsupervised Machine Learning Techniques for Exploring Tropical Coamoeba, Brane Tilings and Seiberg Duality](https://arxiv.org/abs/2309.05702) [[DOI](https://doi.org/10.1103/PhysRevD.108.106009)] (2023)
    * [Distilling the essential elements of nuclear binding via neural-network quantum states](https://arxiv.org/abs/2308.16266) [[DOI](https://doi.org/10.1103/PhysRevLett.133.142501)] (2023)
    * [Scattering with Neural Operators](https://arxiv.org/abs/2308.14789) [[DOI](https://doi.org/10.1103/PhysRevD.108.L101701)] (2023)
    * [Renormalizing Diffusion Models](https://arxiv.org/abs/2308.12355) (2023)
    * [Reconstructing $S$-matrix Phases with Machine Learning](https://arxiv.org/abs/2308.09451) [[DOI](https://doi.org/10.1007/JHEP05(2024)200)] (2023)
    * [Accelerated Discovery of Machine-Learned Symmetries: Deriving the Exceptional Lie Groups G2, F4 and E6](https://arxiv.org/abs/2307.04891) [[DOI](https://doi.org/10.1016/j.physletb.2023.138266)] (2023)
    * [Macroscopic Dynamics of Entangled 3+1-Dimensional Systems: A Novel Investigation Into Why My MacBook Cable Tangles in My Backpack Every Single Day](https://arxiv.org/abs/2304.00220) (2023)
    * [The R-mAtrIx Net](https://arxiv.org/abs/2304.07247) [[DOI](https://doi.org/10.1088/2632-2153/ad56f9)] (2023)
    * [Machine Learning in Physics and Geometry](https://arxiv.org/abs/2303.12626) (2023)
    * [Clustering Cluster Algebras with Clusters](https://arxiv.org/abs/2212.09771) [[DOI](https://doi.org/10.4310/ATMP.2023.v27.n3.a5)] (2022)
    * [Mahler Measuring the Genetic Code of Amoebae](https://arxiv.org/abs/2212.06553) [[DOI](https://doi.org/10.4310/ATMP.2023.v27.n5.a3)] (2022)
    * [Autoencoding heterotic orbifolds with arbitrary geometry](https://arxiv.org/abs/2212.00821) [[DOI](https://doi.org/10.1088/2399-6528/ad246f)] (2022)
    * [CYJAX: A package for Calabi-Yau metrics with JAX](https://arxiv.org/abs/2211.12520) [[DOI](https://doi.org/10.1088/2632-2153/acdc84)] (2022)
    * [Characterizing 4-string contact interaction using machine learning](https://arxiv.org/abs/2211.09129) [[DOI](https://doi.org/10.1007/JHEP04(2024)016)] (2022)
    * [Machine Learned Calabi-Yau Metrics and Curvature](https://arxiv.org/abs/2211.09801) [[DOI](https://doi.org/10.4310/ATMP.2023.v27.n4.a3)] (2022)

##  Experimental results.
 *This section is incomplete as there are many results that directly and indirectly (e.g. via flavor tagging) use modern machine learning techniques.  We will try to highlight experimental results that use deep learning in a critical way for the final analysis sensitivity.*


??? example "Performance studies"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Performance studies
    </div>

    * [A Search for Leptonic Photon, $Z_{l}$, at All Three CLIC Energy Stages by Using Artificial Neural Networks (ANN)](https://arxiv.org/abs/2406.10097) [[DOI](https://doi.org/10.5506/APhysPolB.55.6-A4)] (2024)
    * [Particle identification with machine learning from incomplete data in the ALICE experiment](https://arxiv.org/abs/2403.17436) [[DOI](https://doi.org/10.1088/1748-0221/19/07/C07013)] (2024)
    * [Neural Network Applications to Improve Drift Chamber Track Position Measurements](https://arxiv.org/abs/2311.15541) [[DOI](https://doi.org/10.1016/j.nima.2024.169404)] (2023)
    * [Simultaneous energy and mass calibration of large-radius jets with the ATLAS detector using a deep neural network](https://arxiv.org/abs/2311.08885) [[DOI](https://doi.org/10.1088/2632-2153/ad611e)] (2023)
    * [Automated visual inspection of CMS HGCAL silicon sensor surface using an ensemble of a deep convolutional autoencoder and classifier](https://arxiv.org/abs/2303.15319) [[DOI](https://doi.org/10.1088/2632-2153/aced7e)] (2023)
    * [Deep machine learning for the PANDA software trigger](https://arxiv.org/abs/2211.15390) [[DOI](https://doi.org/10.1140/epjc/s10052-023-11494-y)] (2022)
    * [Pulse shape discrimination using a convolutional neural network for organic liquid scintillator signals](https://arxiv.org/abs/2211.07892) [[DOI](https://doi.org/10.1088/1748-0221/18/03/P03003)] (2022)
    * [A feasibility study of multi-electrode high-purity germanium detector for $^{76}$Ge neutrinoless double beta decay searching](https://arxiv.org/abs/2211.06180) [[DOI](https://doi.org/10.1088/1748-0221/18/05/P05025)] (2022)
    * [Identification of hadronic tau lepton decays using a deep neural network](https://arxiv.org/abs/2201.08458) [[DOI](https://doi.org/10.1088/1748-0221/17/07/P07023)] (2022)


??? example "Searches and measurements where ML reconstruction is a core component"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Searches and measurements where ML reconstruction is a core component
    </div>

    * [Search for vector-like leptons coupling to first- and second-generation Standard Model leptons in $pp$ collisions at $\sqrt{s}](https://arxiv.org/abs/2411.07143) (2024)
    * [Observation of a rare beta decay of the charmed baryon with a Graph Neural Network](https://arxiv.org/abs/2410.13515) (2024)
    * [Search for light long-lived particles decaying to displaced jets in proton-proton collisions at $\sqrt{s}$](https://arxiv.org/abs/2409.10806) (2024)
    * [Accuracy versus precision in boosted top tagging with the ATLAS detector](https://arxiv.org/abs/2407.20127) [[DOI](https://doi.org/10.1088/1748-0221/19/08/P08018)] (2024)
    * [Measurement of boosted Higgs bosons produced via vector boson fusion or gluon fusion in the H $\to$$\mathrm{b\bar{b}}$ decay mode using LHC proton-proton collision data at $\sqrt{s}$](https://arxiv.org/abs/2407.08012) (2024)
    * [Shower Separation in Five Dimensions for Highly Granular Calorimeters using Machine Learning](https://arxiv.org/abs/2407.00178) (2024)
    * [Improving neutrino energy estimation of charged-current interaction events with recurrent neural networks in MicroBooNE](https://arxiv.org/abs/2406.10123) (2024)
    * [A simultaneous unbinned differential cross section measurement of twenty-four $Z$+jets kinematic observables with the ATLAS detector](https://arxiv.org/abs/2405.20041) (2024)
    * [Dark sector searches with the CMS experiment](https://arxiv.org/abs/2405.13778) (2024)
    * [Test of light-lepton universality in $\tau$ decays with the Belle II experiment](https://arxiv.org/abs/2405.14625) [[DOI](https://doi.org/10.1007/JHEP08(2024)205)] (2024)
    * [ATLAS searches for additional scalars and exotic Higgs boson decays with the LHC Run 2 dataset](https://arxiv.org/abs/2405.04914) (2024)
    * [Search for new resonances decaying to pairs of merged diphotons in proton-proton collisions at $\sqrt{s}$](https://arxiv.org/abs/2405.00834) (2024)
    * [Search for a resonance decaying into a scalar particle and a Higgs boson in the final state with two bottom quarks and two photons in proton-proton collisions at a center of mass energy of 13 TeV with the ATLAS detector](https://arxiv.org/abs/2404.12915) (2024)
    * [Search for Higgs Boson Pair Production with One Associated Vector Boson in Proton-Proton Collisions at $\sqrt{s}$](https://arxiv.org/abs/2404.08462) [[DOI](https://doi.org/10.1007/JHEP10(2024)061)] (2024)
    * [Exploration at the high-energy frontier: ATLAS Run 2 searches investigating the exotic jungle beyond the Standard Model](https://arxiv.org/abs/2403.09292) (2024)
    * [Observation of electroweak production of $W^+W^-$ in association with jets in proton-proton collisions at $\sqrt{s}](https://arxiv.org/abs/2403.04869) [[DOI](https://doi.org/10.1007/JHEP07(2024)254)] (2024)
    * [Search for long-lived particles using displaced vertices and missing transverse momentum in proton-proton collisions at $\sqrt{s}$](https://arxiv.org/abs/2402.15804) [[DOI](https://doi.org/10.1103/PhysRevD.109.112005)] (2024)
    * [Search for new phenomena with top-quark pairs and large missing transverse momentum using 140 fb$^{-1}$ of pp collision data at $ \sqrt{s} $](https://arxiv.org/abs/2401.13430) [[DOI](https://doi.org/10.1007/JHEP03(2024)139)] (2024)
    * [CMS highlights on searches for new physics in final states with jets](https://arxiv.org/abs/2401.07172) [[DOI](https://doi.org/10.22323/1.450.0162)] (2024)
    * [Novel techniques for alpha/beta pulse shape discrimination in Borexino](https://arxiv.org/abs/2310.11826) [[DOI](https://doi.org/10.1103/PhysRevD.109.112014)] (2023)
    * [Advances in developing deep neural networks for finding primary vertices in proton-proton collisions at the LHC](https://arxiv.org/abs/2309.12417) [[DOI](https://doi.org/10.1051/epjconf/202429509003)] (2023)
    * [Suppression of Neutron Background using Deep Neural Network and Fourier Frequency Analysis at the KOTO Experiment](https://arxiv.org/abs/2309.12063) [[DOI](https://doi.org/10.1016/j.nima.2023.169010)] (2023)
    * [Boosting dark matter searches at muon colliders with Machine Learning: the mono-Higgs channel as a case study](https://arxiv.org/abs/2309.11241) [[DOI](https://doi.org/10.1093/ptep/ptad144)] (2023)
    * [Applying Machine Learning Techniques to Searches for Lepton-Partner Pair-Production with Intermediate Mass Gaps at the Large Hadron Collider](https://arxiv.org/abs/2309.10197) [[DOI](https://doi.org/10.1103/PhysRevD.109.075018)] (2023)
    * [Searches for supersymmetric particles with prompt decays with the ATLAS detector](https://arxiv.org/abs/2306.15014) (2023)
    * [Measurement of \ensuremath{\nu}\ensuremath{\mu} charged-current inclusive \ensuremath{\pi}0 production in the NOvA near detector](https://arxiv.org/abs/2306.04028) [[DOI](https://doi.org/10.1103/PhysRevD.107.112008)] (2023)
    * [Evidence of off-shell Higgs boson production from $ZZ$ leptonic decay channels and constraints on its total width with the ATLAS detector](https://arxiv.org/abs/2304.01532) [[DOI](https://doi.org/10.1016/j.physletb.2023.138223)] (2023)
    * [Search for third-generation vector-like leptons in $pp$ collisions at $\sqrt{s}](https://arxiv.org/abs/2303.05441) [[DOI](https://doi.org/10.1007/JHEP07(2023)118)] (2023)
    * [Search for a light charged Higgs boson in $t \rightarrow H^{\pm}b$ decays, with $H^{\pm} \rightarrow cb$, in the lepton+jets final state in proton-proton collisions at $\sqrt{s}](https://arxiv.org/abs/2302.11739) [[DOI](https://doi.org/10.1007/JHEP09(2023)004)] (2023)
    * [Observation of single-top-quark production in association with a photon using the ATLAS detector](https://arxiv.org/abs/2302.01283) [[DOI](https://doi.org/10.1103/PhysRevLett.131.181901)] (2023)
    * [Search for a new Z' gauge boson in $4\mu$ events with the ATLAS experiment](https://arxiv.org/abs/2301.09342) [[DOI](https://doi.org/10.1007/JHEP07(2023)090)] (2023)
    * [Search for periodic signals in the dielectron and diphoton invariant mass spectra using 139 fb$^{-1}$ of $pp$ collisions at $\sqrt{s}](https://arxiv.org/abs/2305.10894) [[DOI](https://doi.org/10.1007/JHEP10(2023)079)] (2023)
    * [Search for a new scalar resonance in flavour-changing neutral-current top-quark decays $t \rightarrow qX$ ($q](https://arxiv.org/abs/2301.03902) [[DOI](https://doi.org/10.1007/JHEP07(2023)199)] (2023)
    * [Search for long-lived particles using out-of-time trackless jets in proton-proton collisions at $ \sqrt{s} $](https://arxiv.org/abs/2212.06695) [[DOI](https://doi.org/10.1007/JHEP07(2023)210)] (2022)
    * [Evidence for Four-Top Quark Production at the LHC](https://arxiv.org/abs/2212.06075) (2022)
    * [Measurement of the cross section of top quark-antiquark pair production in association with a W boson in proton-proton collisions at $\sqrt{s}](https://arxiv.org/abs/2212.03770) (2022)
    * [Reconstruction of the event vertex in the PandaX-III experiment with convolution neural network](https://arxiv.org/abs/2211.14992) [[DOI](https://doi.org/10.1007/JHEP05(2023)200)] (2022)
    * [Search for Higgs Boson and Observation of Z Boson through their Decay into a Charm Quark-Antiquark Pair in Boosted Topologies in Proton-Proton Collisions at s](https://arxiv.org/abs/2211.14181) [[DOI](https://doi.org/10.1103/PhysRevLett.131.041801)] (2022)
    * [Search for supersymmetry in final states with a single electron or muon using angular correlations and heavy-object identification in proton-proton collisions at $\sqrt{s}$](https://arxiv.org/abs/2211.08476) [[DOI](https://doi.org/10.1007/JHEP09(2023)149)] (2022)
    * [Search for supersymmetry in final states with missing transverse momentum and three or more b-jets in 139 fb$^{-1}$ of proton\textendash{}proton collisions at $\sqrt{s}](https://arxiv.org/abs/2211.08028) [[DOI](https://doi.org/10.1140/epjc/s10052-023-11543-6)] (2022)
    * [Search for an anomalous excess of charged-current quasi-elastic $\nu_e$ interactions with the MicroBooNE experiment using Deep-Learning-based reconstruction](https://arxiv.org/abs/2110.14080) [[DOI](https://doi.org/10.1103/PhysRevD.105.112003)] (2021)
    * [Search for an anomalous excess of inclusive charged-current $\nu_e$ interactions in the MicroBooNE experiment using Wire-Cell reconstruction](https://arxiv.org/abs/2110.13978) [[DOI](https://doi.org/10.1103/PhysRevD.105.112005)] (2021)
    * [A deep neural network to search for new long-lived particles decaying to jets](https://arxiv.org/abs/1912.12238) [[DOI](https://doi.org/10.1088/2632-2153/ab9023)] (2019)
    * [The Full Event Interpretation}: {An Exclusive Tagging Algorithm for the Belle II Experiment](https://arxiv.org/abs/1807.08680) [[DOI](https://doi.org/10.1007/s41781-019-0021-8)] (2018)


??? example "Final analysis discriminate for searches"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Final analysis discriminate for searches
    </div>

    * [Evidence for Four-Top Quark Production at the LHC](https://arxiv.org/abs/2212.06075) (2022)
    * [Inclusive search for highly boosted Higgs bosons decaying to bottom quark-antiquark pairs in proton-proton collisions at $\sqrt{s}](https://arxiv.org/abs/2006.13251) [[DOI](https://doi.org/10.1007/JHEP12(2020)085)] (2020)
    * [Dijet resonance search with weak supervision using 13 TeV pp collisions in the ATLAS detector](https://arxiv.org/abs/2005.02983) [[DOI](https://doi.org/10.1103/PhysRevLett.125.131801)] (2020)
    * [Search for Higgs boson decays into a $Z$ boson and a light hadronically decaying resonance using 13 TeV $pp$ collision data from the ATLAS detector](https://arxiv.org/abs/2004.01678) [[DOI](https://doi.org/10.1103/PhysRevLett.125.221802)] (2020)
    * [Search for non-resonant Higgs boson pair production in the $bb\ell\nu\ell\nu$ final state with the ATLAS detector in $pp$ collisions at $\sqrt{s}](https://arxiv.org/abs/1908.06765) [[DOI](https://doi.org/10.1016/j.physletb.2019.135145)] (2019)


??? example "Measurements using deep learning directly (not through object reconstruction)"
    <div class="meta_for_parser tablespecs"
    style="font-size: 1pt;visibility:hidden" markdown>
    ###  Measurements using deep learning directly (not through object reconstruction)
    </div>

    * [Unbinned Deep Learning Jet Substructure Measurement in High $Q^2$ ep collisions at HERA](https://arxiv.org/abs/2303.13620) [[DOI](https://doi.org/10.1016/j.physletb.2023.138101)] (2023)
    * [Measurement of lepton-jet correlation in deep-inelastic scattering with the H1 detector using machine learning for unfolding](https://arxiv.org/abs/2108.12376) [[DOI](https://doi.org/10.1103/PhysRevLett.128.132002)] (2021)

