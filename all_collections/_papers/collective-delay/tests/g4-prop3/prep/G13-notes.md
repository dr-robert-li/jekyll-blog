# G13 preparer notes (private; coders never see this)

Case: Ofqual 2020 standardisation algorithm for A-level and GCSE grades, England.
Adoption anchor: A+0 = 2020 (Secretary of State direction to Ofqual, 31 March 2020, following exam cancellation on 18 March 2020; Ofqual consultation outcome on the standardisation approach in spring 2020). Fractions: July 2020 ~A+0.3; 13-17 Aug 2020 ~A+0.35-0.37; 2 Sep ~A+0.4; 16 Sep ~A+0.45; Dec 2020 ~A+0.7; 2 Mar 2021 ~A+0.95; Oct 2025 ~A+5.5.

## Token key
- [MODEL] = Ofqual 2020 standardisation model ("the algorithm", Direct Centre Performance model)
- [OPERATOR] = Ofqual (Office of Qualifications and Examinations Regulation)
- [AGENCY-1] = Department for Education; "the minister" = Gavin Williamson, Secretary of State for Education
- [AGENCY-2] = Office for Statistics Regulation (OSR)
- [AGENCY-3] = Information Commissioner's Office (ICO)
- [COMMITTEE-1] = House of Commons Education Select Committee (chair Robert Halfon); inquiry "The impact of COVID-19 on education and children's services"; report HC 617 "Getting the grades they've earned" (published 11 July 2020)
- [COURT-1] = High Court of England and Wales (Administrative Court)
- [PLAINTIFF-1] = Curtis Parfitt-Ford
- [ORG-1] = Foxglove
- [ORG-2] = Leigh Day
- [ORG-3] = Good Law Project
- [INQUIRY-1] = UK Covid-19 Inquiry (Module 8, children and young people; module number not verified from a primary source)
- [STATUTE-1] = Apprenticeships, Skills, Children and Learning Act 2009 (Ofqual's statutory objectives)
- [STATUTE-2] = UK GDPR / Data Protection Act 2018 (incl. Art. 22)
- [STATUTE-3] = Equality Act 2010
- [COUNTRY-A] = England; [REGION-B] = Scotland (SQA episode, context only)
- "former head of government" = Boris Johnson; regulator's chair = Roger Taylor; head of regulator who resigned = Sally Collier; senior civil servant = Jonathan Slater.
- Upper-secondary = A level; lower-secondary = GCSE; vocational body = Pearson (BTEC).

## Sources
- S1 Leigh Day, "Government announces u-turn over A-level grading" (Aug 2020). https://www.leighday.co.uk/news/news/2020-news/government-announces-u-turn-over-a-level-grading
- S2 Foxglove, statement on Ofqual challenge, 17 Aug 2020. https://www.foxglove.org.uk/?p=573
- S3 Cornerstone Barristers, "U-turn on A-level algorithm in wake of JR threats". https://cornerstonebarristers.com/u-turn-level-algorithm-wake-jr-threats/
- S4 Landmark Chambers, "A-level results system: systemic judicial review brought by Good Law Project ... against Ofqual", 17 Aug 2020. https://www.landmarkchambers.co.uk/a-level-results-system-systemic-judicial-review-brought-by-good-law-project-and-landmark-barristers-against-ofqual/
- S5 CrowdJustice, "Justice for A Level Students" (GLP crowdfunder; ~GBP 76.7k pledged; update 17 Aug 2020). https://www.crowdjustice.com/case/justice-for-a-level-students
- S6 ITV News, 16 Aug 2020, "Students taking legal action against exam regulator Ofqual". https://www.itv.com/news/2020-08-16/students-taking-legal-action-against-ofqual-amid-a-level-results-anger
- S7 Schools Week, "Ofqual removes mock exam appeals policy just hours after publication", 15 Aug 2020. https://schoolsweek.co.uk/ofqual-removes-mock-exam-appeals-policy-just-hours-after-publication/
- S8 Express & Star (PA), "Ofqual suspends policy on A-level mock exam appeals", 15 Aug 2020. https://www.expressandstar.com/uk-news/ofqual-suspends-policy-on-a-level-mock-exam-appeals-6028254
- S9 Wikipedia, "2020 United Kingdom school exam grading controversy" (used as locator/timeline only). https://en.wikipedia.org/wiki/2020_United_Kingdom_school_exam_grading_controversy
- S10 House of Commons Education Committee, "Getting the grades they've earned", HC 617, 11 July 2020. https://committees.parliament.uk/publications/1834/documents/17976/default/ (fetch blocked; findings taken from S11 and press coverage)
- S11 Tes, "MPs warn of 2020 GCSE and A-level grading bias" (July 2020). https://www.tes.com/magazine/archive/mps-warn-2020-gcse-and-level-grading-bias ; also HEPI 14 July 2020 https://www.hepi.ac.uk/2020/07/14/halfon-is-right-ofqual-has-more-to-do/
- S12 PublicTechnology, 3 Sep 2020, on Roger Taylor's evidence of 2 Sep 2020. https://www.publictechnology.net/2020/09/03/education-and-skills/williamson-made-fundamental-mistake-algorithms-says-ofqual-chair/ ; also chair stepping down: https://www.publictechnology.net/2020/12/18/education-and-skills/chair-exam-regulator-points-very-difficult-summer-resignation/
- S13 Education Committee oral evidence transcript (Ofqual session). https://committees.parliament.uk/oralevidence/790/pdf
- S14 Civil Service World, 17 Sep 2020, on Williamson's evidence of 16 Sep 2020. https://www.civilserviceworld.com/news/article/education-secretary-fails-to-back-officials-over-exam-scandal
- S15 Schools Week, "Williamson suggests he didn't analyse Ofqual algorithm until after it was published". https://schoolsweek.co.uk/williamson-suggests-he-didnt-analyse-ofqual-algorithm-until-after-it-was-published/
- S16 OSR, "Learning lessons from the approach to developing models for awarding grades in the UK in 2020" / "Ensuring statistical models command public confidence", 2 Mar 2021. https://osr.statisticsauthority.gov.uk/publication/ensuring-statistical-models-command-public-confidence
- S17 FE Week, "Watchdog fears public bodies will avoid statistical models following exam grading backlash", Mar 2021. https://feweek.co.uk/watchdog-fears-public-bodies-will-avoid-statistical-models-following-exam-grading-backlash/
- S18 The Scotsman, "'Homicidal' Johnson considered sacking Williamson over 2020 exam results fiasco" (Covid Inquiry evidence, autumn 2025). https://mp.scotsman.com/uk-news/homicidal-johnson-considered-sacking-williamson-over-2020-exam-results-fiasco-5660368
- S19 Pinsent Masons Out-Law, "Exam results put reliance on algorithms in the spotlight" (reports ICO statement). https://www.pinsentmasons.com/out-law/news/exam-results-put-reliance-on-algorithms-in-the-spotlight
- S20 Monckton Chambers, "Challenge to Ofqual's exam algorithm: Ciar McAndrew acts in proposed judicial review". https://www.monckton.com/challenge-to-ofquals-exam-algorithm-ciar-mcandrew-acts-in-proposed-judicial-review/

## Preparer remarks
- Neither JR (Foxglove/Leigh Day; GLP/Landmark) was issued; both overtaken by the 17 Aug U-turn. No record found of formal withdrawal or costs.
- ICO: only a public statement; no investigation/decision found, so placed in context.
- Education Committee report (pre-results) and the two post-results hearings belong to one inquiry; packaged as one episode (E1).
- Mock-appeal criteria withdrawal (15 Aug) included as a regulator decision about the appeal route against model outputs (E2).
- Covid Inquiry: exam grading was examined within Module 8 hearings (Sep–Oct 2025, per press); no report found by 31 Dec 2025. Included as E7 since it is an official inquiry touching the model; coders may judge.
- Not found: any issued court proceedings, any NAO/PAC review, any Ofqual internal published review specific to the model.
- Scottish SQA episode kept as context only, per instruction. Welsh (Qualifications Wales) and NI (CCEA) parallels omitted (different models).
