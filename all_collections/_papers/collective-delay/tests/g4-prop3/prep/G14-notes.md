# G14 preparer notes (private; coders never see this)

Case: Arkansas Department of Human Services, RUGs-based algorithm for ARChoices in-home attendant-care hours.
Adoption anchor: A+0 = January 2016 (ARChoices began 1 Jan 2016, merging ElderChoices and AAPD; hours set by RUGs from ArPath assessment). Fractions: Oct 2016 A+0.8; Jan 2017 A+1.0; Feb 2017 A+1.1; Jul 2017 A+1.5; Nov 2017 A+1.9; Apr 2018 A+2.3; 14/18/23 May 2018 A+2.4; 20–21 Dec 2018 / 1 Jan 2019 A+3; 11 Apr 2019 A+3.3; May 2019 A+3.4; Feb 2020 A+4.1.

## Token key
- [MODEL] = RUGs (Resource Utilization Groups) algorithm applied to ArPath (interRAI-based) assessment
- [AGENCY-1] = Arkansas Department of Human Services (DHS), Division of Aging and Adult Services; secretary Cindy Gillespie
- [VENDOR] = third-party software vendor implementing the algorithm (not named in sources used); RUGs system founder = Brant Fries
- [STATE-A] = Arkansas
- [COURT-1] = U.S. District Court, Eastern District of Arkansas (Judge D. Price Marshall Jr.)
- [COURT-2] = Pulaski County Circuit Court (Judge Wendell Griffen)
- [COURT-3] = Arkansas Supreme Court
- [LEGISLATURE-1 committee] = Arkansas Legislative Council and its Administrative Rules and Regulations Subcommittee
- [STATUTE-1] = Arkansas Administrative Procedure Act
- [ORG-1] = Legal Aid of Arkansas (attorney Kevin De Liban)
- Would-be intervenor = Disability Rights Arkansas
- [PLAINTIFF-1] = Ethel Jacobs (Jacobs v. Gillespie, E.D. Ark., 2016)
- [PLAINTIFF-2] = Bradley Ledgerwood (Ark. Dep't of Human Servs. v. Ledgerwood, 2017 Ark. 308, 530 S.W.3d 336; and 2019 Ark. 100, 571 S.W.3d 1)
- Successor assessment: Optum Government Solutions independent assessment (ARIA), from Jan 2019.

## Sources
- S1 Legal Aid of Arkansas, "Federal judge orders DHS to stop benefit cuts", 2 Nov 2016. https://arlegalaid.org/news-events/newsroom.html/article/2016/11/02/federal-judge-orders-dhs-to-stop-benefit-cuts
- S2 Arkansas Democrat-Gazette, "Attorney fees awarded in Medicaid-hours suit", 18 Jul 2017. https://www.arkansasonline.com/news/2017/jul/18/attorney-fees-awarded-in-medicaid-hours/
- S3 Legal Aid of Arkansas, "Seven individuals with disabilities continue the legal fight against secretive Medicaid home care cuts", Jan 2017. https://arlegalaid.org/news-events/newsroom.html/article/2017/01/30/seven-individuals-with-disabilities-continue-the-legal-fight-against-secretive-medicaid-home-care-cuts
- S4 Arkansas Democrat-Gazette, "Group's request in Medicaid suit tossed by Arkansas judge", 20 Apr 2018. https://www.arkansasonline.com/news/2018/apr/20/group-s-request-in-medicaid-suit-tossed-1/
- S5 Legal Aid of Arkansas fact sheet, "ARChoices—Fighting the 4,000 Cuts" (2017; advocacy document, reports DHS testimony and court admissions). https://arlegalaid.org/file_download/84e2dd5a-0889-47b6-901e-dd3e300878d4
- S6 Arkansas Nonprofit News Network / KARK (Benjamin Hardy), on the May 2018 injunction and contempt. https://digital-release.kark.com/?p=113376
- S7 Arkansas Democrat-Gazette, "DHS to appeal ban on formula; algorithm pared home-based care", 12 Jun 2018. https://www.arkansasonline.com/news/2018/jun/12/dhs-to-appeal-ban-on-formula-20180612-1/ ; also NWA Democrat-Gazette "Care-hours algorithm favored", 18 May 2018. https://www.nwaonline.com/news/2018/may/18/care-hours-algorithm-favored-20180518/
- S8 Arkansas Democrat-Gazette, "In-home care changes OK'd by lawmakers", 22 Dec 2018. https://www.arkansasonline.com/news/2018/dec/22/in-home-care-changes-ok-d-by-lawmakers-/ ; aging committees' review of Optum contract: https://www.arkansasonline.com/news/2019/jun/03/gauge-cuts-medicaid-assisted-living-eligibility-ro/
- S9 Arkansas Democrat-Gazette, "2nd suit filed over in-home care cuts", 26 Feb 2020. https://www.arkansasonline.com/news/2020/feb/26/2nd-suit-filed-over-in-home-care-cuts-2/
- S10 Ark. Dep't of Human Servs. v. Ledgerwood, 2017 Ark. 308, 530 S.W.3d 336 (affirming TRO). https://case-law.vlex.com/vid/ark-dep-t-of-894108726
- S11 Ark. Dep't of Human Servs. v. Ledgerwood, 2019 Ark. 100, 571 S.W.3d 1 (11 Apr 2019; contempt reversed, appeal dismissed as moot). https://leagle.com/decision/inarco20190411009 ; Justia summary https://arkansassupremecourtopinions.justia.com/category/government-administrative-law/page/8 ; news: https://www.arkansasonline.com/news/2019/apr/19/justices-overturn-contempt-of-court-ord-1/
- S12 Reporting of the coding error (diabetes, cerebral palsy) found during litigation: The Conversation/IPS/TheNextWeb, "Can a robot decide my medical treatment?", Jun 2020. https://ipsnews.net/business/2020/06/03/can-a-robot-decide-my-medical-treatment/?amp=1 ; originally reported by The Verge (Colin Lecher, Mar 2018) https://www.theverge.com/2018/3/21/17144260/healthcare-medicaid-algorithm-arkansas-cerebral-palsy (fetch blocked; not directly verified).
- S13 Cornell LII, Ark. Code R. 016.06.18-009 (ARChoices manual update 2018). https://www.law.cornell.edu/regulations/arkansas/016-06-18-Ark-Code-R-009

## Preparer remarks
- Jacobs v. Gillespie caption confirmed only by press search snippets; Legal Aid release names Jacobs and Judge Marshall.
- Coding-error finding is from secondary reporting (not a court document); the number affected is given only as "hundreds". Placed inside E2 since it surfaced in that litigation.
- Arkansas Supreme Court 2019 disposition: Justia says the mooted appeal was the TRO appeal; Leagle excerpt says the permanent-injunction appeal. Packet says "remaining appeal ... moot".
- Administrative fair hearings (E5): only the Legal Aid fact sheet documents the route and Legal Aid's ~100 clients; no aggregate official data found. Weakly sourced; coders may judge.
- Whether Disability Rights Arkansas filed a separate action was not found.
- 2019 and 2020 federal suits (Dearmore etc.) concern the successor Optum assessment and appeal handling, so kept as context.
