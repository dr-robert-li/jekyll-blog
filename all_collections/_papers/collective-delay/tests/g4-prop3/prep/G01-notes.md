# G01 preparer notes (PRIVATE - coders never see this)

Case: COMPAS recidivism risk assessment, Wisconsin.

## A+0 definition
A+0 = 2012: Wisconsin Department of Corrections adopted COMPAS statewide (DOC Council on Offender Reentry minutes, Mar 2017, say COMPAS was procured "about five years ago"; Wikipedia and case summaries give 2012). Year conversions: 2011 = A-1, 2012 = A+0, 2013 = A+1, 2014 = A+2, 2015 = A+3, 2016 = A+4, 2017 = A+5, 2018 = A+6, 2019 = A+7, 2023 = A+11.

## Token key
- [MODEL] = COMPAS (Correctional Offender Management Profiling for Alternative Sanctions)
- [VENDOR] = Northpointe, Inc. (now equivant)
- [OPERATOR] = Wisconsin Department of Corrections
- [STATE-A] = Wisconsin; [STATE-B] = New York; [STATE-C] = California
- [COURT-2 (appellate)] = Wisconsin Court of Appeals
- [COURT-3] = Wisconsin Supreme Court
- [COURT-4] = Supreme Court of the United States
- [AGENCY-1] = New York State Division of Criminal Justice Services (DCJS), Office of Justice Research and Performance (author Sharon Lansing)
- [AGENCY-2] = California State Auditor
- [APPELLANT-1] = Jordan Samsa
- [APPELLANT-2] = Eric L. Loomis
- federal government's chief appellate lawyer = US Solicitor General (amicus at Court's invitation, May 2017)
- [ORG-1] = ProPublica ("Machine Bias", May 2016)

## Sources
- S1: State v. Loomis, 2016 WI 68, 371 Wis. 2d 235, 881 N.W.2d 749 (decided 13 July 2016). Text: https://caselaw.findlaw.com/wi-supreme-court/1742124.html ; WI State Public Defender summary: https://www.wispd.gov/2016/07/scow-upholds-use-of-compas-at-sentencing/ ; ProPublica report on ruling: https://www.propublica.org/article/wisconsin-court-warning-labels-needed-scores-rating-risk-future-crime
- S2: Court of Appeals certification in State v. Loomis, No. 2015AP157-CR (Sept 2015): https://www.wispd.gov/2015/09/court-of-appeals-certifies-issues-challenging-use-of-compas-assessments-at-sentencing/ ; docket documents https://acefiling.wicourts.gov/document/eFiled/2015AP000157/156725
- S3: State v. Samsa, 2015 WI App 6, 359 Wis. 2d 580 (filed 16 Dec 2014): https://www.wispd.gov/2014/12/sentencing-judge-didnt-err-in-its-interpretation-or-application-of-compas-report/ ; https://www.michbar.org/file/news/releases/archives17/State-v-Samsa.pdf
- S4: Loomis v. Wisconsin, No. 16-6387, cert. denied 26 June 2017 (137 S. Ct. 2290); SG amicus brief: https://www.scotusblog.com/cases/case-files/loomis-v-wisconsin ; https://www.wispd.gov/2017/06/solicitor-general-files-amicus-brief-regarding-compas-in-wisconsin-v-loomis/
- S5: Lansing, S. (Sept 2012). New York State COMPAS-Probation Risk and Need Assessment Study: Examining the Recidivism Scale's Effectiveness and Predictive Accuracy. NYS DCJS. https://www.criminaljustice.ny.gov/crimnet/ojsa/opca/compas_probation_report_2012.pdf (returned 404 on 2026-10-19; abstract at https://ojp.gov/ncjrs/virtual-library/abstracts/new-york-state-compas-probation-risk-and-need-assessment-study , NCJ 247345)
- S6: Wisconsin DOC Council on Offender Reentry minutes, 15 Mar 2017: https://doc.wi.gov/Documents/AboutDOC/PublicNotices/MeetingMinutes/031517CouncilOffenderReentryMinutes.pdf ; https://en.wikipedia.org/wiki/COMPAS_(software) (locator only). Vendor bill-of-sale norming caveat: WI SPD On Point blog 2016 (secondary).
- S7: California State Auditor Report 2010-124 (Sept 2011), "CDCR: The Benefits of Its Correctional Offender Management Profiling for Alternative Sanctions Program Are Uncertain": https://information.auditor.ca.gov/pdfs/reports/2010-124.pdf ; recommendation status: https://information.auditor.ca.gov/reports/responses/2010-124/2
- S8: California State Auditor Report 2018-113 (Jan 2019), "CDCR: Several Poor Administrative Practices Have Hindered Reductions in Recidivism ...", Recommendation 1 and follow-ups to Oct 2023: https://information.auditor.ca.gov/reports/responses/2018-113/1
- S9: NY Appellate Division, Third Dept: Matter of Garfield v Evans, 108 AD3d 830 (2013) https://www.nycourts.gov/REPORTER/3dseries/2013/2013_05029.htm ; Matter of Malerba v Evans, 109 AD3d 1067 (2013) https://www.nycourts.gov/REPORTER/3dseries/2013/2013_06052.htm ; Matter of Adams v NYS Bd of Parole, 110 AD3d 1338 (2013) https://www.nycourts.gov/REPORTER/3dseries/2013/2013_06929.htm ; Matter of Linares v Evans, 112 AD3d 1056 (2013) https://www.nycourts.gov/reporter/3dseries/2013/2013_08189.htm ; Second Dept: Matter of Symes v NYS Bd of Parole (2014) https://nycourts.gov/REPORTER/3dseries/2014/2014_03693.htm . (nycourts.gov returned 403 to fetch; details from search snippets.)
- S10: Angwin et al., "Machine Bias", ProPublica, 23 May 2016: https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing (media; context only)
- S11: Flores, Bechtel & Lowenkamp (2016), "False Positives, False Negatives, and False Analyses", Federal Probation 80(2); Dressel & Farid (2018), "The accuracy, fairness, and limits of predicting recidivism", Science Advances 4(1), doi:10.1126/sciadv.aao5580.

## Decisions and caveats
- NY parole cases (S9) placed in Context, not Episodes: they sought to compel use of COMPAS under Executive Law 259-c(4), not to challenge its outputs or use. There are many more such NY Article 78 decisions (dozens) including later "departure" cases (e.g., trial-level Green v. Towns, re 2022 denial) that challenge the Board for departing from low COMPAS scores without explanation; these too enforce the tool rather than challenge it. Coordinator may wish to revisit.
- California 2011 audit (S7) predates A+0 so put in Context; its follow-ups to 2015/2016 overlap A+0..A+4 but are status reviews of a pre-adoption audit.
- Peer-reviewed academic reanalyses (S11) and ProPublica placed in Context as informal academic criticism/media; neither was commissioned by a body with standing. Flag for coordinator: S11 papers are peer-reviewed and could be argued to be "formal reanalyses".
- NY DCJS 2012 study (E1) included as an official review by a state agency (different state from operator). It is an operator-side validation, not a challenge, but fits "official audits, inquiries and reviews".
- Loomis counted once at highest decided level (Wisconsin Supreme Court, with cert denial noted). Loomis's sentence details (6 years initial confinement + 5 extended supervision) paraphrased as "several years".
- Searched without success: federal habeas by Loomis; any Wisconsin Legislative Audit Bureau review; any Michigan/federal appellate COMPAS due-process ruling; a W.D. Wis. equal-protection suit (Henderson v. Stensberg) that I could not confirm exists. Unpublished Wisconsin Court of Appeals decisions applying Loomis likely exist (numerous) but were not located individually.
- Funding of Loomis and Samsa appeals not reported in sources consulted.
