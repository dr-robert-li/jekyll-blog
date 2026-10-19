# Coder: fable — evidence

Scoring conventions I applied throughout (from the codebook):
- challenger `unclear` whenever an individual/private party's funding is "not reported"; `lone` only when the packet says self-funded/self-represented or one firm acting alone; institutions, groups, orgs, operators and governments acting on their own mandate are `organised`.
- success `0` for inquiries/audits/studies that produced findings or recommendations with no reported acceptance or action; `1` where the packet says recommendations were accepted/implemented, legislation was enacted, rules adopted, or the actor's own decision took effect. Aggregated episodes with outcomes "not reported" score `0`.
- content_reopen `1` only where the packet says the model/its use was withdrawn, suspended, declared unlawful/invalid in general, materially revised under a binding requirement, or independently re-estimated with public results; case-by-case relief, disclosure orders, warnings and party-only settlements score `0`.
- ground `unclear` for settlements with no stated basis and for executive acts with no model-related reason.

## G01
Probe G01: I think this is the COMPAS tool (Northpointe/equivant) and the Wisconsin v. Loomis decision; the A+4 newsroom analysis is ProPublica's. recognised=1. Scored only from the packet.
- G01 E1 challenger organised: "Brought by: [AGENCY-1], the state's criminal-justice services agency. Funded or run by: [AGENCY-1] research office." target model (tested the scale generally); success 0: "no relief sought"; content_reopen 0: a validation study tested accuracy, it did not re-estimate the judgements or change them.
- G01 E2 challenger unclear: "Funded or run by: not reported." target own-case: "Sought: resentencing or sentence modification"; success 0: "judgment and postconviction order affirmed"; content_reopen 0.
- G01 E3 challenger unclear: "Funded or run by: not reported." target own-case: "Sought: resentencing"; success 0: "unanimously affirmed", "the defendant's sentence was upheld"; content_reopen 0: the general relief was a "written advisement warning judges", which the codebook excludes ("only warnings or caveats added").
- G01 E4 challenger organised: "[AGENCY-2], the state auditor". target model: "validate [MODEL]". success 0: recommendation "only partially implemented... [MODEL] had not" been validated; content_reopen 0.

## G02
Probe G02: I think this is Houston ISD's use of SAS EVAAS and the Houston Federation of Teachers v. HISD ruling. recognised=1. Scored only from the packet.
- G02 E1 challenger organised: "the local teachers' union, together with several individual teachers"; fees paid to the union affiliate. supported 0 (union is a party). target model: "relief against [OPERATOR]'s use of [MODEL] scores in teacher appraisal and in terminating teachers". success 1: summary judgment refused on due process; settlement "agreed not to use value-added scores... to terminate any teacher". ground procedural: "teachers had no meaningful way to make sure their own scores were correctly calculated... denied them a fair chance to contest". content_reopen 1, scope class: "settlement bars termination on unverifiable value-added scores district-wide".
- G02 E2 challenger organised: "[OPERATOR]'s elected board of trustees". target model (contract for the scores). success 1 (decision took effect: "the district stopped obtaining [MODEL] scores"). ground substantive: "about five years of use had not improved performance". content_reopen 1 (withdrawn), scope class: "all district teachers (scores no longer produced)".

## G03
Probe G03: I think this is the US credit rating agencies (S&P, Moody's, Fitch) and the subprime RMBS/CDO ratings crisis, Dodd-Frank, the DOJ FIRREA suit, and the Australian Bathurst councils case. recognised=1. Scored only from the packet.
- G03 E1 organised ("[LEGISLATURE-1]"); model (registration/oversight of all agencies); success 1 ("enacted"); content_reopen 0 ("barred the regulator from regulating the methods"); ground unclear ("concern about limited competition and accountability").
- G03 E2 organised ([BODY-1]); model; success 0 (recommendations only); content_reopen 0.
- G03 E3 organised ([ORG-2]); model; success 0 (recommendations); content_reopen 0.
- G03 E4 organised ([ORG-1]); model; success 1 ("code revised"); ground mixed ("performed poorly" and "conflict and quality concerns"); content_reopen 0 (voluntary code).
- G03 E5 organised ([AG-1]); model ("all mortgage-backed deals rated by the three agencies"); success 1 ("agencies agreed to..."); ground procedural ("issuer-pays model and 'rating shopping'"); content_reopen 0 (process changes, no revision of ratings).
- G03 E6 organised ([REGULATOR-1] staff); model; success 0 ("no enforcement action", findings only); content_reopen 0.
- G03 E7 organised ([COMMITTEE-2]); model; success 0 ("no formal report or sanction"); content_reopen 0.
- G03 E8 organised ([REGULATOR-1]); model ("all recognised agencies"); success 1 ("rules adopted"); ground procedural ("conflicts of interest and lack of transparency"); content_reopen 0.
- G03 E9 organised (14 institutional plaintiffs, a group); own-case ("damages for losses"); success 1 ("all defendants settled"); ground unclear (settlement, amount/basis not reported); content_reopen 0 ("the plaintiff investors only").
- G03 E10 organised (local government "and other investors"); own-case; success 0 ("final outcome not reported"; refusal to dismiss is not relief); content_reopen 0.
- G03 E11 organised ("pension and union funds as lead plaintiffs"); target unclear (share-price misstatement claim, not relief from ratings); success 1 ("remaining claims were then settled"); ground unclear; content_reopen 0.
- G03 E12 organised ("five state pension and investment funds"); own-case; success 0 ("dismissed... affirmed"); content_reopen 0.
- G03 E13 lone ("a large state public employees' pension fund... Funded or run by: the fund"); own-case; success 1 ("[AGENCY-A] settled... for over a hundred million"); ground unclear (settlement); content_reopen 0 ("the plaintiff fund only").
- G03 E14 organised ([REGULATOR-1] enforcement staff); model; success 0 ("public report instead of an enforcement action"); content_reopen 0.
- G03 E15 organised ([LEGISLATURE-1]); model; success 1 ("Enacted"); ground mixed ("ratings... had proved inaccurate" plus oversight/disclosure); content_reopen 1, scope class: "required every federal agency to remove references to and reliance on credit ratings from its regulations" (withdrawal of the model's regulatory use for all).
- G03 E16 organised ([COMMISSION-1]); model; success 0 ("findings only"); content_reopen 0.
- G03 E17 organised ([COMMITTEE-1]); model; success 0 ("findings and recommendations"); content_reopen 0.
- G03 E18 organised ("pension funds as lead plaintiffs"); own-case; success 0 ("dismissal affirmed"); content_reopen 0.
- G03 E19 organised (state attorneys general); model (enforcement over ratings practice generally); success 1 ("resolved in the joint settlement"); ground mixed (per E22/E27: departed from published methods and adjusted models under business pressure); content_reopen 0.
- G03 E20 organised ("a group of about a dozen local government councils"); own-case; success 1 ("found [AGENCY-A] liable"); ground substantive ("the top rating had no reasonable basis... unjustified assumption"); content_reopen 0 ("the plaintiff councils only").
- G03 E21 organised ([REGULATOR-1]); model; success 0 ("recommended a public roundtable"); content_reopen 0.
- G03 E22 organised ([AGENCY-1]); model; success 1 ("agreed to pay over a billion dollars"); ground mixed ("delayed or adjusted updates to its debt-obligation model... in response to competitive and market-share pressure"); content_reopen 0 ("payments to the federal and state governments").
- G03 E23 organised ([REGULATOR-1] and two states); model; success 1 ("settled; [AGENCY-A] paid"); ground mixed ("publicly described one method... but used a different" one; "assumption that made ratings less conservative"); content_reopen 0 (sanctions).
- G03 E24 organised (legislature of [BLOC-1]); model; success 1 ("adopted"); ground mixed ("overreliance on ratings and conflicts of interest"); content_reopen 0 (reduce reliance, liability, rotation; ratings not revised/withdrawn).
- G03 E25 organised ([REGULATOR-1]); model; success 1 ("adopted rules"); ground procedural ("conflicts and the quality and transparency"); content_reopen 0.
- G03 E26 organised ([REGULATOR-1]); model; success 0 (annual findings and recommendations); content_reopen 0.
- G03 E27 organised ([AGENCY-1] and states); model; success 1 ("paid hundreds of millions"); ground mixed ("did not follow its own rating standards, used more lenient standards than it published"); content_reopen 0.
- G03 E28 organised ([REGULATOR-1]); model; success 1 ("settled... paid over ten million"); ground mixed ("lacked effective controls to detect errors in a model"); content_reopen 1, scope group: "it later corrected hundreds of ratings covering tens of billions of dollars" (remediation of ratings of one type).

## G04
Probe G04: I think this is the Basel II internal-ratings-based (IRB) approach and the Basel III/"Basel IV" output floor, with the Collins amendment, EBA benchmarking, ECB TRIM, and national mortgage risk-weight floors. recognised=1. Scored only from the packet.
- G04 E1 organised ([AGENCY-3]); model; success 1 ("the agencies delayed their proposed rule"); ground substantive ("large drops in minimum required capital and wide spread in results"); content_reopen 0 (delay of adoption, no judgements yet revised).
- G04 E2 organised; model; success 1 ("final rule adopted"); ground substantive ("uncertainty about how far model estimates could reduce capital"); content_reopen 1, scope group: "transitional floors limiting how far model-based capital could fall" for "banks in [COUNTRY-A]".
- G04 E3 organised (legislature); model; success 1 ("enacted"); ground substantive ("to stop large banks' model-based requirements falling below those applied to other banks"); content_reopen 1, scope group ("all banks in [COUNTRY-A] using [MODEL]").
- G04 E4 organised ([ORG-1]); model; success 0 ("Policy options were to be developed"); content_reopen 0 (a dispersion study, not a re-estimate; "none directly").
- G04 E5 organised ([AGENCY-2]); model; success 0 ("recommended more supervisory consistency"); content_reopen 0.
- G04 E6 organised ([AGENCY-4]); model; success 1 ("floor of 15% set"); ground substantive ("model-based mortgage risk weights were judged too low"); content_reopen 1, scope group ("banks using [MODEL] for domestic mortgages in [COUNTRY-B]").
- G04 E7 organised ([AGENCY-5]); model; success 1 ("15% floor introduced"); ground substantive ("hold more capital... than their models produced"); content_reopen 1, scope group.
- G04 E8 organised ([AGENCY-6]); model; success 1 ("5 percentage-point add-on"); ground substantive ("model risk weights were low relative to real-estate risks"); content_reopen 1, scope group.
- G04 E9 organised (macroprudential committee / [AGENCY-7]); model; success 1 ("banks were required to submit plans"); ground substantive ("applying more prudent risk weights than banks' own calculations"); content_reopen 1 (independent re-estimate by a body with standing, result published as a shortfall), scope group ("the major banks of [COUNTRY-E]").
- G04 E10 organised (parliamentary commission); model; success 0 ("recommendations to government and supervisor"); content_reopen 0.
- G04 E11 organised ([ORG-1]); model; success 0 ("set out a programme of policy options"); content_reopen 0.
- G04 E12 organised (government inquiry); model; success 0 ("recommendation to supervisor"); content_reopen 0.
- G04 E13 organised ([AGENCY-8] and finance ministry); model; success 1 ("floor... raised", "minimum average risk weight of 20%"); ground substantive ("model risk weights were too low"); content_reopen 1, scope group.
- G04 E14 organised ([AGENCY-9]); model; success 1 ("required banks... to raise average mortgage risk weights"); ground substantive ("to narrow the gap with standardised risk weights"); content_reopen 1, scope group.
- G04 E15 organised ([AGENCY-2]); model; success 0 (recurring reports identifying outliers); content_reopen 0.
- G04 E16 organised ([ORG-1]); model; success 0 ("described sound practice"); content_reopen 0.
- G04 E17 organised ([ORG-1]); model; success 1 ("final standard removed the most advanced form of [MODEL]... introduced an aggregate output floor"); ground substantive ("excessive variability in risk weights not explained by risk; low-default portfolios could not be modelled robustly"); content_reopen 1, scope class ("all internationally active banks using [MODEL] in member jurisdictions").
- G04 E18 organised ([AGENCY-1]); model; success 1 ("binding measures requiring remediation"); ground substantive ("inconsistent and in some cases non-compliant modelling practices"); content_reopen 1 (materially revised under binding requirement: "risk-weighted assets for the investigated models rose by roughly a tenth"), scope group ("significant banks in [REGION-1]").
- G04 E19 organised ([AGENCY-2]); model; success 1 ("issued technical standards... guidelines"); ground substantive ("reduce variability in risk parameters arising from differences in practice"); content_reopen 1 (binding standards on how estimates are built), scope group.
- G04 E20 organised ([AGENCY-10]); model; success 1 ("15% floor"); ground substantive ("risks not fully captured in model risk weights"); content_reopen 1, scope group.
- G04 E21 organised ([AGENCY-11]); model; success 1 ("floor introduced"); ground substantive ("low model risk weights"); content_reopen 1, scope group.
- G04 E22 organised ([AGENCY-3]); model; success 0 ("not finalised"); content_reopen 0.
- G04 E23 organised (regional legislature); model; success 1 ("enacted"); ground substantive ("restore credibility of risk weights"); content_reopen 1 (output and input floors, restrictions), scope group ("banks in [REGION-1]").
- G04 E24 organised ([AGENCY-7]); model; success 1 ("rules restricting [MODEL]... output floor"); ground substantive ("as in E17"); content_reopen 1, scope group ("banks in [COUNTRY-E]").

## G05
Probe G05: I think this is Florida's hurricane catastrophe models, the Florida Commission on Hurricane Loss Projection Methodology, the public model, and the State Farm Florida rate dispute. recognised=1. Scored only from the packet.
- G05 E1 organised (legislature); model; success 1 ("enacted; created [AGENCY-1]"); ground mixed (standards on accuracy plus "access to all the assumptions and factors behind the model"); content_reopen 0 (review regime created; no model withdrawn/revised).
- G05 E2 organised ([AGENCY-1] with state-funded professional team); model; success 1 ("the three principal vendors' models were accepted"); ground substantive ("compliance with published standards, verified by on-site audit"); content_reopen 0 (acceptance, no withdrawal/revision/re-estimate).
- G05 E3 organised (legislature and [AGENCY-2]); model (a public check on all filings); success 1 ("funded and contracted"); ground procedural ("commercial models are proprietary and their inner workings not open"); content_reopen 0 (model not yet built).
- G05 E4 organised (two members of the state house); model; success 0 ("did not become law"); content_reopen 0.
- G05 E5 organised (legislature); model; success 1 ("enacted"); ground procedural ("regulator needed an independent check on proprietary model outputs"; access to assumptions); content_reopen 0 (access/disclosure only).
- G05 E6 lone ("Brought by: [VENDOR-3] (submission for acceptance)", one firm); model; success 0 ("the vendor withdrew it and did not seek a second audit"); content_reopen 1, scope group: the short-term version that "insurers began using... in filings" (context) was withdrawn after the audit, affecting "insurers that would have used the short-term version".
- G05 E7 organised ([AGENCY-3]); own-case (one insurer group's filings); success 1 ("notices of intent to disapprove all the filings"); ground mixed ("did not pass on savings" and "relied on short-term adjustments... that [AGENCY-1] had not accepted"); content_reopen 0.
- G05 E8 organised ([AGENCY-3]); own-case ([INSURER-1]'s group); success 1 ("held that the commissioner had not exceeded his authority"); ground procedural ("documents were needed to review its filings"); content_reopen 0.
- G05 E9 organised (legislature); model ("all residential insurers"); success 1 ("enacted"); ground unclear ("not reported in sources reviewed"); content_reopen 0 (binds use to accepted models; no withdrawal/revision).
- G05 E10 organised ([AGENCY-3] disapproval); own-case ([INSURER-2]); success 1 (recommended order denying increases; settlement at ~15%); ground substantive ("averaging three models did not produce a reliable answer"; not shown rates were not excessive); content_reopen 0.
- G05 E11 lone ([VENDOR-3]); model; success 0 ("not accepted"); content_reopen 0 (new version never in use).
- G05 E12 organised ([AGENCY-1]); model; success 1 ("acceptance suspended"); ground substantive ("a software implementation error was found"); content_reopen 1 (suspended), scope group ("insurers relying on that version").

## G06
Probe G06: I think this is the US EPA PM2.5 NAAQS and the Harvard Six Cities / ACS cohort studies, with American Trucking Associations v. EPA / Whitman v. ATA, the Shelby amendment, the HEI reanalysis, and the EPA "secret science" rule. recognised=1. Scored only from the packet.
- G06 E1 organised ("industry trade associations"); model ("to set aside the fine-particle standard"); success 0 ("none for petitioners; standard remained in force"); content_reopen 0.
- G06 E2 organised ([ORG-1], independent institute); model; success 1 (audit and reanalysis done); ground procedural ("to answer criticism that the data and analyses had not been open to independent checking"); content_reopen 1 (independent re-estimate by a body with standing, public), scope class.
- G06 E3 organised ([LEGISLATURE-1]); model (access to the data behind federally funded research); success 1 ("enacted"); ground procedural ("public should be able to see data"); content_reopen 0 (disclosure only).
- G06 E4 organised ("farm and industry groups" and "several states and public-health groups"); model; success 1 ("remanded the annual fine-particle standard"); ground procedural ("had not adequately explained"); content_reopen 0 (remand to reconsider; model not revised/withdrawn).
- G06 E5 organised ([ORG-1]); model; success 1 (extension completed); ground substantive ("to update and test the robustness of the earlier findings"); content_reopen 1 (independent re-estimate, public), scope class.
- G06 E6 organised (committee); model (data); success 0 ("did not produce the confidential participant-level data"); content_reopen 0.
- G06 E7 organised ("business associations"); model; success 0 ("petitions denied"); content_reopen 0.
- G06 E8 organised (committee members); model; success 0 ("not enacted"); content_reopen 0.
- G06 E9 organised; model; success 0 ("not enacted"); content_reopen 0.
- G06 E10 organised; model; success 0 ("not enacted"); content_reopen 0.
- G06 E11 organised ([AGENCY-1]); model (weighting of studies such as [MODEL]); success 1 ("finalised... made effective on publication"); ground procedural ("transparency and reproducibility"); content_reopen 0 (vacated within weeks; no judgement reopened).
- G06 E12 organised ("the plaintiff organisations"); model (general rule on the model's use); success 1 ("vacated and remanded the rule"); ground procedural ("could not be issued under the housekeeping statute... without the usual waiting period"); content_reopen 0.
- G06 E13 organised ("several states and public-health and environmental groups"); model; success 1 ("the agency later lowered the standard"); ground unclear (agency reasons not given); content_reopen 0 (standard changed, model's estimates not reopened).
- G06 E14 organised ([STATE-GROUP-1] and business associations); model; success 0 ("pending"); content_reopen 0.

## G07
Probe G07: I think this is the Imperial College COVID-19 "Report 9" model (Ferguson et al.), the Codecheck certificate, the Edinburgh BMJ reanalysis, Dolan v Secretary of State, and the UK Covid Inquiry. recognised=1. Scored only from the packet.
- G07 E1 organised ("acting for [ORG-2], an open code-checking initiative... Funded or run by: [ORG-2]"); model; success 0 ("no relief sought... verification only"); content_reopen 1 (independent re-run: "re-ran all the simulations and found the key results reproducible", certificate published), scope class.
- G07 E2 organised ("four researchers at [ORG-1] (a university)"); model; success 0 ("Relief applied to: none"); content_reopen 1 (independent reanalysis re-running the model, "Published"), scope class.
- G07 E3 unclear ("Funded or run by: not reported in the judgment; private solicitors acted"); model ("declarations that the restriction regulations... were unlawful"); success 0 ("dismissed... permission was refused"); content_reopen 0.
- G07 E4 organised ([COMMITTEE-1]); model; success 0 ("recommendations addressed to government"); content_reopen 0.
- G07 E5 organised (joint committees); model; success 0 (recommendations); content_reopen 0.
- G07 E6 organised ([INQUIRY-1]); model; success 0 ("recommendations to governments generally"); content_reopen 0.

## G08
Probe G08: I think this is the UK Post Office Horizon IT system (Fujitsu), Bates v Post Office, the Second Sight review, Hamilton v Post Office, and the Post Office Horizon IT Inquiry. recognised=1. Scored only from the packet.
- G08 E1 unclear ("Funded or run by: not reported"); own-case (counterclaim re her dismissal and shortfall); success 1 ("settled by [OPERATOR] before trial"); ground substantive ("equipment installed at the branch was clearly defective"); content_reopen 0 ("[PLAINTIFF-1] only").
- G08 E2 lone ("defended without a lawyer... defendant self-funded"); own-case; success 0 ("judgment for [OPERATOR]; counterclaim dismissed"); content_reopen 0.
- G08 E3 organised ("[OPERATOR] appointed [ORG-1]... [OPERATOR] funded both"); model ("investigate complaints that the system caused unexplained losses"); success 1 (review done, scheme ran, some settlements); ground substantive ("identified two software anomalies (bugs)"); content_reopen 1 (independent forensic review, report "published"), scope class.
- G08 E4 organised ([OPERATOR]); model; success 0 ("not disclosed... not published"); content_reopen 0.
- G08 E5 organised ("a commercial litigation funder ([ORG-3]), led by a branch operators' campaign group"); model (sought "findings that the system was not reliable" generally); success 1 ("Settled in mediation for tens of millions"); ground mixed ("could not simply treat system figures as a debt" and "numerous bugs, errors and defects"); content_reopen 1 (judicial finding that the system was "far from robust" — invalid in general), scope group ("the group claimants only").
- G08 E6 organised ([AGENCY-1], police); target unclear (perjury investigation); success 0 ("no charging decision"); content_reopen 0.
- G08 E7 organised ("Funded or run by: [AGENCY-2] (statutory, government-funded)"); supported 1 (body referred named individuals' convictions); own-case; success 1 ("39 convictions referred"); ground mixed ("depended on the system's evidence" and "failures in [OPERATOR]'s investigation and disclosure"); content_reopen 0 ("the referred individuals").
- G08 E8 organised ("on [AGENCY-2] referral"); supported 1; own-case; success 1 ("all six convictions quashed"); ground mixed ("as in E7"); content_reopen 0.
- G08 E9 organised (39 on referral); supported 1; own-case; success 1 ("39 convictions quashed"); ground mixed ("a fair trial was not possible", "knew of serious questions about the system's reliability yet failed to investigate or disclose"); content_reopen 0 ("the 39 successful appellants").
- G08 E10 organised (referral or direct); supported 1; own-case; success 1 ("further convictions quashed"); ground mixed ("same reasoning as E9"); content_reopen 0.
- G08 E11 organised ([OPERATOR] with government oversight); own-case (compensation for a defined set); success 1 ("thousands of settlement offers made... most accepted"); ground substantive ("redress following the group-litigation findings"); content_reopen 0.
- G08 E12 organised (government statutory inquiry); model; success 0 ("recommendations to government"); content_reopen 0.
- G08 E13 organised (parliament); own-case (compensation groups); success 0 ("recommendations to government"); content_reopen 0.
- G08 E14 organised (government department); own-case ("the group claimants"); success 1 ("funding announced... full scheme details"); ground unclear ("had received little after costs"); content_reopen 0.
- G08 E15 organised ([AGENCY-3]); supported 1; own-case; success 1 ("quashed the convictions referred"); ground unclear ("the prosecution conceded"); content_reopen 0.
- G08 E16 organised (government statute); own-case (compensation payments); success 1 ("enacted"); ground unclear ("not reported beyond the Act's purpose"); content_reopen 0.
- G08 E17 organised (governments); own-case (a defined set of convictions); success 1 ("both enacted; hundreds of convictions quashed"); ground mixed ("the scale of unsafe convictions and the time individual appeals would take"); content_reopen 1 (judgements invalidated in bulk by statute, not case by case), scope group ("all convictions meeting the statutory criteria (hundreds of people)").
- G08 E18 organised (parliament); own-case (redress schemes); success 0 ("The government rejected the transfer"); content_reopen 0.

## G09
Probe G09: I think this is Australia's Robodebt scheme (Centrelink income averaging), Amato, Prygodicz v Commonwealth, and the Royal Commission. recognised=1. Scored only from the packet.
- G09 E1 unclear ("mostly self-represented or assisted by community legal centres; not reported in aggregate"); own-case; success 1 ("several hundred decisions... set aside or varied the debts"); ground substantive ("annual income figure spread evenly... did not establish the actual income"); content_reopen 0 ("each appellant only").
- G09 E2 organised ([AGENCY-2]); model; success 1 ("eight recommendations, all accepted"); ground procedural ("problems of usability and transparency"); content_reopen 0 (non-binding recommendations; programme continued).
- G09 E3 organised (parliament); model; success 0 ("The programme continued"); content_reopen 0.
- G09 E4 organised ("[ORG-1] (a state legal aid commission) as a test case"); supported 1; own-case ("a debt raised by income averaging"); success 1 ("wiped the debt"); ground substantive ("recalculated the debt"); content_reopen 0 ("[PLAINTIFF-1] only").
- G09 E5 organised ([AGENCY-2]); model; success 1 ("implemented its recommendation... significant progress"); ground procedural; content_reopen 0.
- G09 E6 organised (parliament); model; success 0 ("recommendation to end the programme immediately was rejected"); content_reopen 0.
- G09 E7 organised ("represented by [ORG-1] as a test case"); supported 1; own-case ("her averaged debt"); success 1 ("consent orders; the court declared..."); ground substantive ("averaged annual income does not show what was earned in each fortnight"); content_reopen 1 (general declaration that averaged data "was not capable of satisfying a decision-maker that a debt existed" — invalid in general), scope own ("[PLAINTIFF-2] only (by the orders)").
- G09 E8 organised (minister/[AGENCY-1]); model; success 1 ("announced"); ground substantive ("advised that the practice was unlawful"); content_reopen 1 (suspended), scope class ("future debt decisions").
- G09 E9 organised ("[ORG-2] (a plaintiff law firm)" running a class action); model (declarations that the debts were invalid for hundreds of thousands); success 1 ("settled... approved"); ground substantive ("no proper legal basis for debts"); content_reopen 1 ("the court declared that debt decisions based on income averaging... were invalid"), scope class ("all group members (hundreds of thousands)").
- G09 E10 organised (minister); model; success 1 ("to be refunded"); ground substantive ("could not rely on averaging to establish debts"); content_reopen 1 (withdrawn), scope class ("everyone with an averaging-based debt").
- G09 E11 organised (royal commission); model; success 0 ("recommendations to government"); content_reopen 0.
- G09 E12 organised ([AGENCY-4] on referrals); target unclear (individual conduct); success 1 ("[AGENCY-4] began investigating the six"); ground unclear ("reconsideration reasons not published"); content_reopen 0.
- G09 E13 organised ([AGENCY-5]); target unclear (individual officials); success 1 ("12 were found to have breached the code... sanctioned"); ground unclear ("detailed reasons not verified"); content_reopen 0.
- G09 E14 organised ("Funded or run by: [ORG-2]"); supported 1 (two named group members); own-case (group settlement); success 1 ("agreed to pay a further several hundred million"); ground procedural ("lacked important evidence"); content_reopen 0.

## G10
Probe G10: I think this is the Dutch SyRI (Systeem Risico Indicatie) case, NJCM v the Netherlands, in The Hague District Court. recognised=1. Scored only from the packet.
- G10 E1 organised ("several civil-society bodies... coordinated by a public-interest litigation project"); model ("declared non-binding"); success 1 ("the court held that the legislation breached the right to private life"); ground procedural ("insufficiently transparent and verifiable, gave no information on the risk model... insufficient safeguards"); content_reopen 1 ("declared the statutory provision and the decree chapter non-binding"), scope class ("everyone").
- G10 E2 organised (mayor and executive of [CITY-1]); model (the city's use); success 1 ("the city stopped using [MODEL] in two neighbourhoods"); ground unclear ("too unclear whether the system complied with privacy law; limited inspection capacity"); content_reopen 1 (use halted), scope group ("residents of the two project neighbourhoods").
- G10 E3 organised (junior minister); model; success 1 ("no new projects would start"); ground procedural ("accepted the court's judgment" — the E1 grounds); content_reopen 1 (withdrawn), scope class ("everyone; all use of the instrument ended").
- G10 E4 organised (ministry); model; success 0 ("adoption and publication not confirmed"); content_reopen 0.

## G11
Probe G11: I think this is the Dutch childcare benefits scandal (toeslagenaffaire) at the Belastingdienst/Toeslagen, with the Autoriteit Persoonsgegevens fines, the parliamentary interrogation committee and the Rutte III cabinet resignation. recognised=1. Scored only from the packet.
- G11 E1 unclear ("individual parents. Funded or run by: not reported"); own-case; success 0 ("upheld the district court in most appeals"; all-or-nothing line applied); content_reopen 0.
- G11 E2 organised ([OMBUDS-1]); own-case ("the families of that agency"); success 1 ("The junior finance minister accepted that the balance had tipped too far"); ground mixed ("disproportionate reaction" and "without enough regard for the individual parent's position"); content_reopen 0.
- G11 E3 unclear ("Funded or run by: not reported"); own-case; success 1 ("the court abandoned the all-or-nothing line"); ground substantive ("the statute leaves room for a proportionate setting"); content_reopen 0 (concerns the recovery rule, not the risk-scoring model).
- G11 E4 organised (government committee); own-case (handling of affected parents); success 0 (advice; acceptance not reported here); content_reopen 0.
- G11 E5 organised ([AUDITOR-1]); own-case (a set of fraud-team cases); success 0 ("formed the basis for a later external re-assessment" — findings only); content_reopen 0.
- G11 E6 organised ([AGENCY-1]); model; success 1 ("fined the finance minister"); ground substantive ("processing them in the model was discriminatory and so unfair"; "not necessary"); content_reopen 1 ("using nationality as an indicator in the risk-scoring model... was unlawful"), scope class ("all applicants").
- G11 E7 organised (management team of [OPERATOR]); model; success 1 ("permanently stopped"); ground unclear ("did not meet the requirements of the regional data-protection regulation"); content_reopen 1 (withdrawn), scope class ("all future applicants").
- G11 E8 organised (lower house); model; success 1 ("the cabinet... announced apologies and measures"); ground mixed ("basic rule-of-law principles had been violated"; "applied without proportionality"); content_reopen 0.
- G11 E9 organised (cabinet); own-case (payments to harmed parents); success 1 ("formalised by ministerial decrees"); ground unclear ("to do justice to parents faster"); content_reopen 0.
- G11 E10 organised (cabinet); target unclear (resignation); success 1 ("offered its resignation"); ground unclear; content_reopen 0.
- G11 E11 unclear ("through a lawyer. Funded or run by: not reported"); target unclear (criminal investigation of ministers); success 0 ("advised against a criminal investigation"); content_reopen 0.
- G11 E12 unclear ("individual parents. Funded or run by: not reported"); own-case; success 0 (outcomes "not reported in the sources consulted"); content_reopen 0.
- G11 E13 organised ([JUDICIAL-COUNCIL-1]); target unclear (judicial practice); success 0 (recommendations); content_reopen 0.
- G11 E14 organised ([INTL-1]); target unclear; success 0 (recommendations); content_reopen 0.
- G11 E15 organised ([COURT-1]); target unclear; success 0 (self-review statement); content_reopen 0.
- G11 E16 organised ([AGENCY-1]); target unclear (the fraud-signal register [SYSTEM-2], not [MODEL]); success 1 ("a fine of a few million"); ground mixed ("no legal basis" and "incorrect and outdated data"); content_reopen 0 (register already switched off; not the model).
- G11 E17 unclear ("defence counsel... Funded or run by: not reported"); own-case; success 0 ("rejected; the accused were convicted"); content_reopen 0.
- G11 E18 organised (finance ministry); model; success 0 ("not applicable" relief; findings only); content_reopen 0 (self-analysis by the operator's ministry, not independent).
- G11 E19 unclear ("Funded or run by: not reported"); target unclear (prosecution order); success 0 ("refused"); content_reopen 0.
- G11 E20 organised (government/parliament); own-case ("parents who registered and were found harmed"); success 1 ("entered into force"); ground unclear ("legal basis for redress"); content_reopen 0.
- G11 E21 organised (ministry commissioning [FIRM-1]); model; success 0 (findings); content_reopen 0.
- G11 E22 organised (lower house); model; success 0 (recommendations); content_reopen 0.
- G11 E23 unclear ("Funded or run by: not reported"); target unclear; success 0 ("refused"); content_reopen 0.
- G11 E24 organised (benefits service/finance ministry); model; success 0 ("decision on compensation pending"); content_reopen 0.

## G12
Probe G12: I think this is Michigan's MiDAS unemployment-insurance system, with Cahoo v. SAS, Zynda v. Arrington, and Bauserman v. UIA. recognised=1. Scored only from the packet.
- G12 E1 unclear ("Funded or run by: not reported"); own-case; success 1 ("the rest were reversed, dismissed, modified or remanded" — agency upheld "in under a tenth"); ground unclear ("per case; not reported in aggregate"); content_reopen 0.
- G12 E2 organised ([AGENCY-2]); model; success 1 ("monitoring report... found the practice violated federal regulations"); ground procedural ("require individual investigation and an opportunity to rebut"); content_reopen 1 ("advised [OPERATOR] to re-adjudicate all fraud cases"; "Relief applied to: all claimants (policy direction)"), scope class.
- G12 E3 organised ("individual claimants, a national industrial labour union ([ORG-2]) and a non-profit law centre ([ORG-1])... run by [ORG-1]"); supported 0 (orgs are parties); model ("stopping fraud determinations and collections made without adequate notice"); success 1 ("agreement... included safeguards"); ground procedural (notice and time to respond); content_reopen 1 ("suspend collections tied to the automated determinations and reviewed earlier determinations"), scope class ("all claimants subject to [OPERATOR] fraud determinations").
- G12 E4 organised ("a private plaintiffs' law firm ([FIRM-1])" running a class action); own-case ("money damages"); success 1 ("settled... for about twenty million dollars"); ground unclear (settlement basis not stated); content_reopen 0.
- G12 E5 organised ([AGENCY-1]); model; success 1 ("[OPERATOR] agreed with most findings"); ground mixed ("approved and paid benefits and then reversed" plus "better explain to people why they are accused"); content_reopen 0.
- G12 E6 organised ([OPERATOR] and parent agency); model; success 1 ("reversing tens of thousands of fraud findings and refunding"); ground substantive ("most were wrong (over nine in ten)"); content_reopen 1 (mass review and reversal of the system's determinations), scope class ("persons with determinations in the reviewed period").
- G12 E7 organised (legislature); model; success 1 ("enacted"); ground procedural ("unless a state employee verifies it"); content_reopen 1 (automated determinations withdrawn for all), scope class ("all future claimants").
- G12 E8 unclear ("five named claimants... Funded or run by: not reported"); own-case (damages); success 0 ("no relief reported"); content_reopen 0.
- G12 E9 organised (legislature); model; success 1 ("enacted"); ground substantive ("response to the agency's false fraud findings"); content_reopen 0 (penalty levels; judgements not reopened).
- G12 E10 organised ([AGENCY-1]); model; success 0 (findings; "not applicable"); content_reopen 0.

## G13
Probe G13: I think this is the UK 2020 A-level/GCSE Ofqual standardisation algorithm, with Foxglove/Good Law Project threatened judicial reviews, the Education Committee, and the OSR review. recognised=1. Scored only from the packet.
- G13 E1 organised ([COMMITTEE-1]); model; success 0 ("no binding relief"; "[OPERATOR] did not publish the model until results day"); content_reopen 0.
- G13 E2 organised ([OPERATOR] board); model (appeal route for all); success 0 ("withdrew them within hours"); content_reopen 0.
- G13 E3 organised ("[ORG-1] and [ORG-2] ran the challenge"); supported 1 (named student, orgs ran it); model ("students be graded on their own merits rather than their school's history"); success 1 ("Three days after the letter, the government and [OPERATOR] replaced model grades"; "less than a day before the claim was due"); ground substantive (per E5: "evidence... showing the model's outcomes"; "fairness... not... acceptable"); content_reopen 1 (model grades withdrawn), scope class ("applied to all affected students").
- G13 E4 organised ("[ORG-3], via public crowdfunding"); supported 1 (six named students); model ("review and revision of the scheme"); success 1 ("overtaken by E5, announced the day the claim was publicised"); ground substantive (as E5); content_reopen 1, scope class.
- G13 E5 organised (minister and [OPERATOR]); model; success 1 ("received the higher of their teacher-estimated grade and their model grade"); ground substantive ("evidence... showing the model's outcomes"; "level of fairness achieved was not felt to be acceptable"); content_reopen 1 (withdrawn/reissued), scope class ("all students awarded grades that year").
- G13 E6 organised ([AGENCY-2]); model; success 0 ("none binding; recommendations"); content_reopen 0.
- G13 E7 organised ([INQUIRY-1]); model; success 0 ("No report findings on this topic"); content_reopen 0.

## G14
Probe G14: I think this is Arkansas DHS's use of the RUGs algorithm in the ARChoices home-care programme, litigated by Legal Aid of Arkansas (Ledgerwood v. Arkansas DHS). recognised=1. Scored only from the packet.
- G14 E1 unclear ("mostly self-represented; [ORG-1] assisted about a hundred"); own-case; success 0 ("aggregate numbers and outcomes not reported"); content_reopen 0.
- G14 E2 organised ("[ORG-1], a legal aid nonprofit"); supported 1 (named individual); own-case ("restoration of hours and adequate notice"); success 1 ("the judge ruled for the plaintiff"); ground procedural ("did not give adequate notice of how hours were determined"); content_reopen 0 (notice fix only; "only... warnings or caveats"/disclosure-type relief).
- G14 E3 organised ([ORG-1]); supported 1 (seven named recipients); model ("an order barring use of [MODEL] to set hours"); success 1 ("permanent injunction barring use of [MODEL]"); ground procedural ("failed to give adequate public notice before adopting the method... not on whether its outputs were correct"); content_reopen 1 (use suspended), scope class ("the permanent injunction applied to all programme recipients").
- G14 E4 organised ([AGENCY-1]); model (continue using [MODEL]); success 1 ("approved the emergency rule"; "later held its adoption was not contempt"); ground unclear ("needed continuity... federal waiver required the algorithm"); content_reopen 0.
- G14 E5 organised ([AGENCY-1]); model; success 1 ("approved... The rules dropped [MODEL]"); ground substantive ("allowed more flexibility for individual needs"); content_reopen 1 (withdrawn), scope class ("all programme recipients").

## G15
Probe G15: I think this is Idaho's developmental-disability budget tool, K.W. v. Armstrong, brought by the ACLU of Idaho. recognised=1. Scored only from the packet.
- G15 E1 lone ("participants, often helped by unpaid service coordinators; [AGENCY-1] did not fund advocates"); own-case ("higher individual budgets"); success 1 ("about three-fifths of budgets reviewed were increased"); ground unclear ("not reported in aggregate"); content_reopen 0 ("individual appellants only").
- G15 E2 organised ("Funded or run by: [ORG-1], a civil liberties organisation"); supported 1 (named representatives); model ("a lawful budget method"; disclosure; notice); success 1 ("the court blocked the reductions"; summary judgment that "the tool's unreliability arbitrarily deprived participants of their property"); ground mixed ("notice inadequate; tool unreliable and untested"); content_reopen 1 (budgets restored class-wide and the tool held unreliable with a binding order to replace it), scope class ("all participants in and applicants to the programme statewide").
