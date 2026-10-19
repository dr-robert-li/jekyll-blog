# G07 preparer notes (PRIVATE - coders never see)

Case: Imperial College London CovidSim model; Report 9 ("Impact of non-pharmaceutical interventions (NPIs) to reduce COVID-19 mortality and healthcare demand", 16 March 2020). A+0 = March 2020.

## Token key
- [MODEL] = CovidSim (Imperial/Ferguson individual-based model)
- [OPERATOR] = Imperial College London COVID-19 Response Team / MRC Centre for Global Infectious Disease Analysis (lead: Prof Neil Ferguson)
- [ORG-1] = University of Edinburgh (Rice, Wynne, Martin, Ackland)
- [ORG-2] = CODECHECK (codecheck.org.uk); reviewer Dr Stephen Eglen
- [ORG-3] = University of Cambridge
- [PLAINTIFF-1] = Simon Dolan (Simon Dolan & Ors; co-claimants as named in judgment)
- [COURT-1] = High Court (Administrative Court), Lewis J, 6 July 2020
- [COURT-2 (appellate)] = Court of Appeal (Civil Division), Lord Burnett CJ, King LJ, Singh LJ
- [STATUTE-1] = Public Health (Control of Disease) Act 1984 (as amended by Health and Social Care Act 2008)
- [COMMITTEE-1] = House of Commons Science and Technology Committee
- [COMMITTEE-2] = House of Commons Health and Social Care Committee
- [INQUIRY-1] = UK Covid-19 Inquiry (Baroness Hallett), Module 2/2A/2B/2C
- "four national governments" = UK, Scotland, Wales, Northern Ireland; "one nation" = England

## Dates (calendar -> relative)
- Report 9: 16 Mar 2020 (A+0); lockdown 23 Mar 2020
- CODECHECK certificate: early June 2020 (A+0.2)
- Rice et al. BMJ 2020;371:m3588, 7 Oct 2020 (A+0.6)
- Dolan CA judgment: 1 Dec 2020, [2020] EWCA Civ 1605 (A+0.7)
- STC HC 136 "The UK response to covid-19: use of scientific advice": published 8 Jan 2021 (A+0.8); govt response May 2021 (CP 432)
- HSCC/STC joint "Coronavirus: lessons learned to date" (HC 92): 12 Oct 2021 (A+1.6); govt response June 2022 (CP 690)
- Covid Inquiry Module 2 report: 20 Nov 2025 (A+5.7)
- OSR letter on Module 2 modelling presentation: 19 Feb 2026 (outside window; context only)

## Sources
- S1: Rice K, Wynne B, Martin V, Ackland GJ. Effect of school closures on mortality from coronavirus disease 2019: old and new predictions. BMJ 2020;371:m3588. https://dx.doi.org/10.1136/bmj.m3588 ; Science Media Centre expert reaction (Woolhouse comment): https://www.sciencemediacentre.org/expert-reaction-to-reanalysis-of-model-used-for-imperial-report-9-and-impact-of-school-closures/ ; Univ. Edinburgh release: https://www.ed.ac.uk/news/2020/shutting-schools-increases-covid-19-deaths-study-f
- S2: Cambridge news, "Codecheck confirms reproducibility of COVID-19 model results": https://www.cam.ac.uk/research/news/codecheck-confirms-reproducibility-of-covid-19-model-results ; certificate DOI 10.5281/zenodo.3865491
- S3: Imperial College news 197875: https://www.imperial.ac.uk/news/197875/codecheck-confirms-reproducibility-covid-19-model-results ; Software Sustainability Institute: https://www.software.ac.uk/news/institute-fellow-stephen-eglens-codecheck-initiative-confirms-reproducibility-covid-19-model
- S4: House of Commons Science and Technology Committee, The UK response to covid-19: use of scientific advice, HC 136, 8 Jan 2021 (paras 71, 86, 87, 92-93, conclusions 11, 12, 18). Parliament page: https://api.parliament.uk/committees/publications/4165 ; text read from PDF copy at https://dera.ioe.ac.uk//37110/1/download%20%285%29.pdf ; oral evidence 25 Mar 2020 https://committees.parliament.uk/oralevidence/237/pdf ; 10 Jun 2020 https://committees.parliament.uk/oralevidence/539/html ; govt response: https://www.gov.uk/government/publications/use-of-scientific-advice-in-the-uk-response-to-covid-19-government-response-to-science-and-technology-committee-report
- S5: Imperial news "BMJ study confirms Imperial COVID-19 projections": https://www.imperial.ac.uk/news/206213/bmj-study-confirms-imperial-covid-19-projections/
- S6: R (Dolan & Ors) v Secretary of State for Health and Social Care [2020] EWCA Civ 1605: https://caselaw.nationalarchives.gov.uk/ewca/civ/2020/1605 (paras 82(a), 83, 89, 97, 115). Funding of claim not stated in judgment (press reported self-funding/crowdfunding; not used).
- S7: HSCC & STC, Coronavirus: lessons learned to date, 12 Oct 2021 (summary paras 2, 5, 6, 7): copy at https://bsswebsite.me.uk/Coronavirus/report.html ; Parliament: https://committees.parliament.uk/publications/7496/documents/78687/default/ ; Inquiry exhibit: https://www.covid19.public-inquiry.uk/documents/inq000075336_0055-extract-of-report-from-health-and-social-care-and-science-and-technology-committees-titled-coronavirus-lessons-learned-to-date-dated-12-10-2021/
- S8: Government response CP 690: https://www.gov.uk/government/publications/coronavirus-lessons-learned-to-date-report-government-response/the-governments-response-to-the-health-and-social-care-committee-and-science-and-technology-committee-joint-report-coronavirus-lessons-learned-to-d
- S9: UK Covid-19 Inquiry, Module 2 report publication release: https://covid19.public-inquiry.uk/?p=54437 ; reports page https://covid19.public-inquiry.uk/reports/ ; gov.uk https://www.gov.uk/government/publications/uk-covid-19-inquiry-core-decision-making-and-political-governance-modules-2-2a-2b-2c-report
- S10: OSR / Inquiry correspondence (used only for what the executive summary stated and its reliance on Ferguson evidence and Knock et al.): https://osr.statisticsauthority.gov.uk/correspondence/presentation-of-modelling-in-the-module-2-report-of-the-uk-covid-19-inquiry ; https://osr.statisticsauthority.gov.uk/wp-content/uploads/2026/02/2026-02-19-Letter-Ben-Connah-to-Ed-Humpherson-FINAL.pdf
- S11: Harper Macleod summary of Module 2 report: https://www.harpermacleod.co.uk/insights/uk-covid-inquiry-module-2-report/

## Search log / judgement calls
- Searched for: Royal Society RAMP review of CovidSim, other formal reanalyses, other litigation citing the model, regulator decisions. None found that fit the definition. Other lockdown challenges (e.g. R (Hussain), Philip v Scottish Ministers) did not, on available sources, rest on the model, so not included.
- Dolan included because the judgment records the claimants arguing the unreliability of the Ferguson/Imperial evidence and the court's answer.
- E5: could not retrieve the full lessons-learned report text (parliament.uk returned 403). Only its summary paragraphs were verified; whether it discusses CovidSim/Report 9 by name is unverified. Included because it examined the scientific/modelling advice behind lockdown timing.
- STC "Reproducibility and research integrity" inquiry (HC 101, May 2023): Ferguson gave evidence Dec 2021, but no source found linking the report's conclusions to CovidSim; not included.
- Code release on GitHub (May 2020) by the operator is not a challenge episode; mentioned as context.
- OSR letter (19 Feb 2026) is outside the window.
