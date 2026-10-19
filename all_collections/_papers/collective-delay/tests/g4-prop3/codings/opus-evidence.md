# Coder opus: evidence

Decision rules I applied throughout (from codebook, made explicit for consistency):
- Institutions (legislatures, regulators, auditors, inquiries, operators acting on their own) = `organised`, supported 0.
- Named individual with "Funded or run by: not reported" and no sign of an organisation = `unclear` challenger (the packet does not say who paid). Self-funded / private solicitors / no advocates funded = `lone`.
- For reviews, inquiries and executive acts, "relief" = relief from the model's judgements: success 1 when the episode produced adverse findings, recommendations or binding action against the model; success 0 when the review endorsed the model, failed, or produced nothing.
- content_reopen 1 only for withdrawal/suspension, general invalidity, binding revision of model outputs (incl. jurisdiction-wide floors), or a published independent re-estimate by a body with standing. Disclosure, conduct/conflict rules, warnings, compensation-only schemes = 0.
- Settlements with no stated basis = ground `unclear`.

## G01
Probe G01: I think this is COMPAS (Northpointe) in Wisconsin, State v. Loomis, with the ProPublica analysis in context. Recognised = 1.
- G01 E1: "Brought by: [AGENCY-1], the state's criminal-justice services agency"; "found the scale predicted rearrest with accuracy it described as satisfactory"; "Relief applied to: none (no relief sought)". Organised, model, success 0; a validation test, not a re-estimate, so content_reopen 0.
- G01 E2: "[APPELLANT-1], a defendant ... Funded or run by: not reported" -> unclear; "Sought: resentencing" -> own-case; "judgment and postconviction order affirmed" -> success 0.
- G01 E3: "[APPELLANT-2] ... Funded or run by: not reported" (federal brief filed only at the court's invitation) -> unclear; "Sought: resentencing" -> own-case; "the defendant's sentence was upheld" -> success 0. The general limits and "written advisement" are caveats added to outputs, so content_reopen 0.
- G01 E4: "[AGENCY-2], the state auditor"; "recommended that the department validate [MODEL]"; "[MODEL] had not [been validated]". Organised, model, success 1 (recommendation), substantive ("had not validated [MODEL]"), content_reopen 0 (no change ordered).

## G02
Probe G02: I think this is Houston ISD's EVAAS (SAS) and Houston Federation of Teachers v. HISD. Recognised = 1.
- G02 E1: "[PLAINTIFF-1], the local teachers' union, together with several individual teachers"; fees paid to "the union's state affiliate" -> organised. "Sought: relief against [OPERATOR]'s use of [MODEL] scores" -> model. Settlement: "agreed not to use value-added scores ... to terminate any teacher" -> success 1; use suspended for "all [OPERATOR] teachers going forward" -> content_reopen 1, class. Ground procedural: "teachers had no meaningful way to make sure their own scores were correctly calculated ... denied them a fair chance to contest".
- G02 E2: "[OPERATOR]'s elected board of trustees"; "the contract was not renewed and the district stopped obtaining [MODEL] scores"; "Relief applied to: all district teachers". Organised, model, success 1 (relief from the model), content_reopen 1 class (withdrawn). Ground unclear: "No official written reasons located."

## G03
Probe G03: I think this is the credit-rating-agency structured-finance crisis (S&P, Moody's, Fitch; CRA Reform Act, Dodd-Frank, DOJ v S&P, Cheyne SIV / Abu Dhabi Commercial Bank, Bathurst council case in Australia). Recognised = 1.
- G03 E1: "Brought by: [LEGISLATURE-1]"; enacted registration scheme; "barred the regulator from regulating the methods". Organised, model, success 1, content_reopen 0; ground procedural ("transparency, competition and conflicts of interest").
- G03 E2: "[BODY-1] ... recommended that agencies disclose more"; reason "flaws in rating agencies' assessments". Organised, model, success 1, cr 0, substantive.
- G03 E3: "[ORG-2], an international body of national authorities"; "recommended that agencies improve the quality of ratings"; reason "poor performance ... weaknesses in the agencies' models". Organised, model, 1, 0, substantive.
- G03 E4: "[ORG-1] ... code revised"; "voluntary"; reasons "performed poorly and ... conflict and quality concerns". Organised, model, 1, 0, mixed.
- G03 E5: "[AG-1] ... agencies agreed to charge for initial reviews ... disclose information"; reason "issuer-pays model and 'rating shopping'". Organised, model, 1, 0 (no rating revised), procedural.
- G03 E6: "[REGULATOR-1] staff"; "Agencies were asked to take remedial steps; no enforcement"; findings on disclosure, documentation, conflicts. Organised, model, 1, 0, procedural.
- G03 E7: "[COMMITTEE-2]"; "no formal report or sanction"; "Relief applied to: none". Organised, model, success 0.
- G03 E8: "[REGULATOR-1] ... rules adopted"; conflicts and disclosure rules; reason "conflicts of interest and lack of transparency". Organised, model, 1, 0, procedural.
- G03 E9: "a foreign bank, and other institutional investors (14 plaintiffs)" -> organised (group); "damages for losses" -> own-case; "all defendants settled" -> success 1; "Relief applied to: the plaintiff investors only" -> cr 0; settlement terms and basis not given -> ground unclear.
- G03 E10: "[PLAINTIFF-2], a local government ... and other investors" -> organised; damages -> own-case; "refused to dismiss; final outcome not reported" -> success 0.
- G03 E11: "pension and union funds as lead plaintiffs" (class sought) -> organised; damages -> own-case; "remaining claims were then settled" -> success 1; reasons "not reported" -> unclear; cr 0.
- G03 E12: "five state pension and investment funds ... with the state attorney general's office" -> organised; damages -> own-case; "dismissed ... affirmed" -> 0.
- G03 E13: "[PLAINTIFF-3], a large state public employees' pension fund ... Funded or run by: the fund" -> lone (one firm, own case); damages -> own-case; "[AGENCY-A] settled ... [AGENCY-B] settled later" -> 1; "plaintiff fund only" -> cr 0; settlement basis -> unclear.
- G03 E14: "[REGULATOR-1] enforcement staff"; "issued a public report instead of an enforcement action ... warned agencies"; model error "raised the ratings" and committee declined to downgrade. Organised, model, success 1 (adverse public findings), cr 0, mixed (model error + control failures).
- G03 E15: "[LEGISLATURE-1]"; enacted; "required every federal agency to remove references to and reliance on credit ratings from its regulations". Organised, model, success 1; regulatory use withdrawn for all -> cr 1, class; reason "ratings ... had proved inaccurate" -> substantive.
- G03 E16: "[COMMISSION-1]"; found "models relied on flawed and outdated assumptions ... pressure from issuers"; "Relief applied to: none (findings only)". Organised, model, 1, 0, mixed.
- G03 E17: "[COMMITTEE-1]"; found "models that relied on limited and outdated data ... conflicts"; recommendations. Organised, model, 1, 0, mixed.
- G03 E18: "investors ... pension funds as lead plaintiffs" -> organised; damages -> own-case; "dismissal affirmed" -> 0.
- G03 E19: "attorneys general of more than a dozen states" -> organised; penalties for misrepresenting independence -> model; resolved in E22/E27 settlements -> success 1; cr 0; ground mixed per E22/E27 reasons.
- G03 E20: "[PLAINTIFF-5], a group of about a dozen local government councils" -> organised; damages -> own-case; "found [AGENCY-A] liable ... appeals ... dismissed" -> 1; "plaintiff councils only" -> cr 0; "the top rating had no reasonable basis" -> substantive.
- G03 E21: "[REGULATOR-1], as required by [STATUTE-2]"; "recommended a public roundtable rather than adopting an assignment system"; "Relief applied to: none". Organised, model, 0.
- G03 E22: "[AGENCY-1] ... Funded or run by: federal government"; "agreed to pay over a billion dollars"; reasons "delayed or adjusted updates to its debt-obligation model ... competitive ... pressure". Organised, model, 1, cr 0 (payments only), mixed.
- G03 E23: "[REGULATOR-1], with parallel actions"; "paid tens of millions ... barred for one year from rating one type"; reasons method misdescribed and control failures. Organised, model, 1, cr 0 (sanction on agency; existing ratings not withdrawn), mixed.
- G03 E24: "legislature of [BLOC-1]"; "reduce sole or mechanical reliance ... civil-liability claim ... rotation"; reason "overreliance on ratings and conflicts". Organised, model, 1, 0 (reduce, not withdraw), procedural.
- G03 E25: "[REGULATOR-1] ... adopted rules requiring internal control structures ... disclosure"; Organised, model, 1, 0, procedural.
- G03 E26: "annual staff reports identifying deficiencies ... in model governance and in following stated methods". Organised, model, 1, 0, procedural.
- G03 E27: "[AGENCY-B] ... paid hundreds of millions"; reasons "did not follow its own rating standards, used more lenient standards ... conflicts". Organised, model, 1, 0, mixed.
- G03 E28: "[REGULATOR-1]"; "lacked effective controls to detect errors in a model ... later corrected hundreds of ratings"; "Relief applied to: the agency (sanctions and remediation of ratings)". Organised, model, 1, cr 1 (binding remediation of the affected ratings), scope group (that agency's RMBS ratings only), mixed.

## G04
Probe G04: I think this is the Basel II internal-ratings-based (IRB) approach, through to Basel III "endgame" / output floor. Recognised = 1.
All G04 episodes are brought by regulators, legislatures, standard setters or government inquiries -> organised, supported 0, target model. Where an episode imposes a binding floor/add-on/remediation on model outputs in one jurisdiction I code content_reopen 1, scope group (one jurisdiction's banks, not everyone using the model); the international standard revision is class.
- G04 E1: "[AGENCY-3] ... delayed their proposed rule after their impact study showed large drops"; success 1; not yet in use domestically so nothing withdrawn -> cr 0; substantive ("size and spread of the capital reductions").
- G04 E2: "final rule ... imposed transitional floors limiting how far model-based capital could fall"; 1, cr 1 group, substantive ("uncertainty about how far model estimates could reduce capital").
- G04 E3: "enacted; banks using [MODEL] may not hold less capital than the generally applicable ... requirements"; 1, cr 1 group, substantive.
- G04 E4: "a material part came from differences in bank and supervisory practice"; "Relief applied to: none directly"; 1 (adverse findings), cr 0, substantive.
- G04 E5: "a substantial share of differences in risk weights could not be explained by differences in portfolio risk"; recommendations; 1, 0, substantive.
- G04 E6: "floor of 15% set ... raised to 25%"; "model-based mortgage risk weights were judged too low"; 1, 1 group, substantive.
- G04 E7: "15% floor introduced"; 1, 1 group, substantive.
- G04 E8: "a 5 percentage-point add-on to risk weights produced by [MODEL]"; 1, 1 group, substantive.
- G04 E9: "capital shortfall ... from applying more prudent risk weights than banks' own calculations; banks were required to submit plans"; 1, 1 group, substantive.
- G04 E10: "criticised reliance on banks' internal risk-weight models ... recommended"; "none directly"; 1, 0, substantive.
- G04 E11: "set out a programme of policy options"; "none directly"; 1, 0, substantive ("variability not explained by risk").
- G04 E12: "recommended that the supervisor raise average mortgage risk weights"; 1, 0, substantive.
- G04 E13: "loss-given-default floor ... raised from 10% to 20% ... minimum average risk weight of 20%"; 1, 1 group, substantive.
- G04 E14: "required banks using [MODEL] to raise average mortgage risk weights from about 17% to at least 25%"; 1, 1 group, substantive.
- G04 E15: "recurring reports ... identifying dispersion ... national supervisors required to assess outliers"; 1, cr 0 (assessment, not revision), substantive.
- G04 E16: "found differences in bank practices"; "none directly"; 1, 0, substantive ("as in E4").
- G04 E17: "removed the most advanced form of [MODEL] for exposures to large corporates ... input floors ... output floor ... 72.5%"; applies to "all internationally active banks"; 1, 1 class, substantive.
- G04 E18: "binding measures requiring remediation ... risk-weighted assets ... rose by roughly a tenth"; 1, 1 group (significant banks in [REGION-1]), substantive ("non-compliant modelling practices").
- G04 E19: "issued technical standards ... guidelines on estimating default and loss parameters"; 1, 1 group, substantive.
- G04 E20: "15% floor for banks using [MODEL]"; 1, 1 group, substantive.
- G04 E21: "floor introduced, set by loan-to-value bands"; 1, 1 group, substantive.
- G04 E22: "not finalised by the end of A+21"; 0, 0.
- G04 E23: "enacted, introducing the output floor ... and input floors and restricting [MODEL]"; 1, 1 group, substantive.
- G04 E24: "rules restricting [MODEL] ... input floors and an output floor"; 1, 1 group, substantive.

## G05
Probe G05: I think this is Florida hurricane catastrophe models, the Florida Commission on Hurricane Loss Projection Methodology, the Florida Public Hurricane Loss Model, RMS's near-term model, and State Farm Florida's rate fights. Recognised = 1.
- G05 E1: "[STATE-A] legislature"; "created [AGENCY-1] ... to adopt standards"; access requirement for regulator and consumer advocate. Organised, model, 1, cr 0 (insurers "may" use; no output revised), procedural.
- G05 E2: "[AGENCY-1] ... three principal vendors' models were accepted". Organised, model, success 0 (models endorsed), cr 0.
- G05 E3: "funded and contracted" public model; reason "commercial models are proprietary ... not open to the regulator". Organised, model, 1, cr 0 (not yet built), procedural.
- G05 E4: "two members of the state house"; "did not become law". Organised, model, 0.
- G05 E5: "enacted ... required insurers to give the regulator ... access to all assumptions"; Organised, model, 1, 0, procedural.
- G05 E6: Commission review (vendor submission; I treat the commission's review as the challenge): "did not meet several standards ... the vendor withdrew it"; insurers had "began using it in filings" (Context A+13). Organised, model, 1, cr 1 class (version withdrawn), substantive ("standards required the long-run historical storm record").
- G05 E7: "[AGENCY-3] on filings by [INSURER-1]'s group"; "notices of intent to disapprove"; "Relief applied to: the insurer group's policyholders". Organised, own-case (one insurer's filings), 1, 0, substantive ("rates did not pass on savings"; reliance on unaccepted adjustments).
- G05 E8: "[AGENCY-3] (subpoenas and ... suspending the insurer's licences)"; "held that the commissioner had not exceeded his authority"; "Relief applied to: [INSURER-1]'s group". Organised, own-case, 1, 0, procedural ("documents were needed to review its filings").
- G05 E9: "insurers must use methods and models found accurate ... may not modify or adjust their outputs"; reasons "not reported". Organised, model, 1, cr 0 (outputs themselves not revised), unclear.
- G05 E10: regulator "disapproved"; settlement "increase of roughly 15%" versus 47% sought; "[INSURER-2]'s policyholders". Organised (regulator), own-case, 1, 0, substantive ("averaging three models did not produce a reliable answer"; rates not shown not excessive).
- G05 E11: "not accepted, because the commissioners present split evenly on a meteorological question". Organised, model, 1; version not yet in use -> cr 0; substantive.
- G05 E12: "acceptance suspended"; "a software implementation error was found in the accepted version"; "insurers relying on that version". Organised, model, 1, cr 1 class, substantive.

## G06
Probe G06: I think this is the Harvard Six Cities and American Cancer Society cohort studies behind the 1997 PM2.5 NAAQS, Whitman v. American Trucking, the HEI reanalysis, the Shelby amendment, the Secret Science/HONEST Act bills and the 2021 EPA transparency rule vacatur. Recognised = 1.
- G06 E1: "[PLAINTIFF-1] (a trucking trade association) ... Funded or run by: industry trade associations"; "to set aside the fine-particle standard"; final: "upheld the fine-particle standards"; "none for petitioners". Organised, model, 0.
- G06 E2: "[ORG-1] (an independent research institute ...) at the request of [AGENCY-1] ..."; "independent reanalysis of both studies"; "original results could be reproduced ... associations ... robust". Organised, model, success 0 (no relief from the model; it was confirmed), but cr 1 class: published independent re-estimate by a commissioned body with standing.
- G06 E3: "[LEGISLATURE-1], by a rider"; "make data from federally funded research available on request"; "Whether it reached [MODEL]'s existing data is not reported". Organised, model, 1, cr 0 (disclosure only), procedural.
- G06 E4: "several states and public-health groups" (and industry); "remanded the annual fine-particle standard ... without vacating"; reason "had not adequately explained". Organised, model, 1, cr 0 (remand to reconsider, nothing revised yet), procedural (failure to explain).
- G06 E5: "[ORG-1] ... extended follow-up and spatial analysis of [STUDY-2]"; "report confirmed associations". Organised, model, 0; cr 1 class (published independent re-estimate).
- G06 E6: committee subpoena; "did not produce the confidential participant-level data"; "Relief applied to: none". Organised, model, 0.
- G06 E7: "[PLAINTIFF-3] ... business associations"; "petitions denied; standard upheld". Organised, model, 0.
- G06 E8: "passed the lower chamber ... not enacted". Organised, model, 0.
- G06 E9: "passed the lower chamber; not enacted". Organised, model, 0.
- G06 E10: "passed the lower chamber; not enacted". Organised, model, 0.
- G06 E11: "[AGENCY-1] under a new administration"; rule "finalised ... made effective on publication; vacated within weeks"; critics: "would exclude studies, such as [MODEL]". Organised, model, success 1 (briefly in force), cr 0 (never applied to withdraw [MODEL]'s estimates), procedural ("transparency and reproducibility").
- G06 E12: "[PLAINTIFF-4] (an environmental organisation) ... Funded or run by: the plaintiff organisations"; sought to set aside the transparency rule (which defends rather than attacks the model) -> target unclear; "vacated and remanded the rule" -> success 1; reason "could not be issued under the housekeeping statute" -> procedural; cr 0.
- G06 E13: "several states and public-health and environmental groups"; "held in abeyance ... the agency later lowered the standard". Organised, model, success 1 (relief via official action), cr 0, substantive ("evidence called for a lower standard").
- G06 E14: "pending at the end of A+28". Organised, model, 0.

## G07
Probe G07: I think this is Imperial College's CovidSim (Ferguson, Report 9), the CODECHECK certificate, the Rice et al. BMJ reanalysis (Edinburgh), Dolan v Secretary of State, the Commons committee inquiries and the UK Covid-19 Inquiry Module 2. Recognised = 1.
- G07 E1: "a university neuroscientist acting for [ORG-2], an open code-checking initiative ... Funded or run by: [ORG-2]" -> organised; "key results reproducible" -> success 0; a re-run of the same computation, not an independent re-estimate -> cr 0.
- G07 E2: "four researchers at [ORG-1] ... Funded or run by: not reported" -> unclear; "reproduced the qualitative results"; operator called it "independent confirmation" -> success 0; uncommissioned academics, not a body with standing -> cr 0.
- G07 E3: "[PLAINTIFF-1] (a businessman) and two co-claimants ... private solicitors acted" -> lone (paying own private lawyers, no organisation); "declarations that the restriction regulations ... were unlawful" -> model (use for everyone); "dismissed ... refused" -> 0.
- G07 E4: "[COMMITTEE-1] ... on its own initiative"; found "public understanding and scrutiny ... hampered by lack of transparency"; recommendations. Organised, model, 1, 0, procedural.
- G07 E5: joint committees; "Whether the report examined [MODEL] specifically was not verified" -> target unclear; findings on "lacked transparency ... structured challenge" -> success 1, procedural, cr 0.
- G07 E6: "[INQUIRY-1] ... relying on evidence from the head of [OPERATOR]'s team" to estimate effect of earlier action -> it used rather than challenged the model; organised, model, success 0, cr 0.

## G08
Probe G08: I think this is the Post Office Horizon scandal (Fujitsu; Wolstenholme, Castleton, Second Sight, Swift review, Bates v Post Office, CCRC, Hamilton, the Post Office (Horizon System) Offences Act). Recognised = 1.
- G08 E1: "[PLAINTIFF-1], a former branch operator ... Funded or run by: not reported" -> unclear; counterclaim on her own dismissal -> own-case; "settled by [OPERATOR] before trial" -> 1; "[PLAINTIFF-1] only" -> cr 0; expert said equipment "clearly defective" -> substantive.
- G08 E2: "defended without a lawyer ... defendant self-funded" -> lone; own-case; "judgment for [OPERATOR]; counterclaim dismissed" -> 0.
- G08 E3: "[OPERATOR] appointed [ORG-1] ... at the request of members of parliament and a branch operators' campaign group" -> organised; investigate system complaints -> model; "identified two software anomalies"; some settlements -> 1; no general re-estimate -> cr 0; substantive.
- G08 E4: "two senior barristers ... Funded or run by: [OPERATOR]"; "reported no evidence of a system-wide problem"; "Relief applied to: none" -> organised, model, 0.
- G08 E5: "over five hundred branch operators under a group litigation order. Funded or run by: a commercial litigation funder" -> organised; damages for the group -> own-case (named set); settled -> 1; "the group claimants only" -> cr 0; found "numerous bugs, errors and defects" -> substantive.
- G08 E6: "[AGENCY-1] (a large police force)"; target is individuals' conduct -> unclear; "no charging decision" -> 0.
- G08 E7: "[AGENCY-2] (statutory, government-funded)" -> organised; referral of individual convictions -> own-case; "39 convictions referred" -> 1; "the referred individuals" -> cr 0; "abuse of process ... failures in ... disclosure" -> procedural.
- G08 E8: "six former branch operators on [AGENCY-2] referral" -> organised (referral body; group), supported 0; "all six convictions quashed" -> 1; own-case; procedural (as E7).
- G08 E9: "42 appellants (39 on [AGENCY-2] referral...)" -> organised; "39 convictions quashed" -> 1; own-case; "a fair trial was not possible ... failed to investigate or disclose" -> procedural (abuse of process).
- G08 E10: further appellants by referral or direct appeal -> organised; "further convictions quashed"; "the individual appellants" -> own-case, 1, 0, procedural.
- G08 E11: "[OPERATOR] (with government oversight)" -> organised; compensation to "eligible applicants" -> own-case (a defined set), 1; compensation, not withdrawal of the model's judgements -> cr 0; "redress following the group-litigation findings" -> substantive.
- G08 E12: "[INQUIRY-1] ... Funded or run by: government"; found staff "knew or should have known the system was capable of errors"; recommendations -> organised, model, 1, 0, substantive.
- G08 E13: "[COMMITTEE-2]"; compensation for group claimants -> own-case (named set); led to E14 -> 1; reasons about exclusion from scheme -> unclear; cr 0.
- G08 E14: "the responsible government department"; "compensate the group claimants" -> organised, own-case, 1, 0, unclear.
- G08 E15: "[AGENCY-3] (that jurisdiction's criminal cases review body)"; "quashed the convictions ... after the prosecution conceded" -> organised, own-case, 1, 0, unclear (concessions).
- G08 E16: "the government, as a statute"; power to pay "eligible branch operators" -> organised, own-case, 1, 0, unclear ("not reported beyond the Act's purpose").
- G08 E17: Acts "to quash, in bulk, convictions ... while the system was in use"; "hundreds of convictions quashed"; "all convictions meeting the statutory criteria" -> organised, model, 1, cr 1 class (outcomes resting on the system withdrawn in general), unclear ground ("the scale of unsafe convictions and the time individual appeals would take").
- G08 E18: "[COMMITTEE-3]"; "found redress had been a complete failure"; redress schemes -> own-case; 1 (adverse findings/recommendations), 0, procedural ("delays and low offers").

## G09
Probe G09: I think this is Australia's Robodebt (Online Compliance Intervention): AAT decisions, Ombudsman reports, Senate inquiries, Amato, Prygodicz class action, Royal Commission, NACC. Recognised = 1.
- G09 E1: "mostly self-represented or assisted by community legal centres; not reported in aggregate" -> unclear; individual debts -> own-case; "several hundred decisions ... set aside or varied the debts" -> 1; "each appellant only" -> cr 0; "annual income figure spread evenly ... did not establish the actual income" -> substantive.
- G09 E2: "[AGENCY-2] (national ombudsman)"; "eight recommendations, all accepted"; "problems of usability and transparency" -> organised, model, 1, 0, procedural.
- G09 E3: "[COMMITTEE-1]"; "recommendations (detail not verified) ... The programme continued" -> organised, model, success 0 (no relief shown), cr 0.
- G09 E4: "represented by [ORG-1] (a state legal aid commission) as a test case" -> organised, supported 1; her debt -> own-case; "wiped the debt" -> 1; "[PLAINTIFF-1] only" -> cr 0; "recalculated the debt using information" -> substantive.
- G09 E5: ombudsman follow-up; "four further recommendations" -> organised, model, 1, 0, procedural.
- G09 E6: "[COMMITTEE-1]"; "recommendation to end the programme immediately was rejected" -> organised, model, 0.
- G09 E7: "represented by [ORG-1] as a test case" -> organised, supported 1; her debt -> own-case; "government conceded ... unlawful" -> 1; "[PLAINTIFF-2] only (by the orders)" -> cr 0; "averaged annual income does not show what was earned" -> substantive.
- G09 E8: "the responsible minister/[AGENCY-1]"; "halt debt raising ... that relied on income averaging" -> organised, model, 1, cr 1 class (suspended for everyone), substantive (unlawful calculation).
- G09 E9: "lead applicants for a group of hundreds of thousands ... Funded or run by: [ORG-2] (a plaintiff law firm)" -> organised; "declarations that the debts were invalid" -> model; "court declared that debt decisions based on income averaging ... were invalid" -> 1, cr 1 class; substantive.
- G09 E10: "refund debts raised wholly or partly by income averaging"; "everyone with an averaging-based debt" -> organised, model, 1, 1 class, substantive.
- G09 E11: royal commission; "neither fair nor lawful ... income averaging was a central flaw ... failed to act" -> organised, model, 1, 0, mixed.
- G09 E12: anti-corruption commission; target individuals -> unclear; reconsideration led to "began investigating the six" -> 1; reasons "not published" -> unclear; cr 0.
- G09 E13: "[AGENCY-5] (public service commissioner)"; "12 were found to have breached the code" -> organised, unclear target, 1, 0, unclear.
- G09 E14: "two group members of E9, represented by [ORG-2]. Funded or run by: [ORG-2]" -> organised, supported 1; for "eligible group members" -> own-case; "agreed to pay a further several hundred million" -> 1; compensation only -> cr 0; "lacked important evidence" -> procedural.

## G10
Probe G10: I think this is SyRI (Systeem Risico Indicatie) in the Netherlands, the NJCM et al. v. State judgment of The Hague district court, with the UN special rapporteur's amicus. Recognised = 1.
- G10 E1: "several civil-society bodies ... coordinated by a public-interest litigation project" -> organised; "statutory provision and decree ... declared non-binding" -> model, 1, cr 1 class ("everyone; the legal basis ... ceased to bind"); "insufficiently transparent and verifiable ... insufficient safeguards" -> procedural.
- G10 E2: "the mayor of [CITY-1]"; "stopped using [MODEL] in two neighbourhoods" -> organised, model, 1, cr 1 group (residents of two neighbourhoods), procedural ("too unclear whether the system complied with privacy law").
- G10 E3: "the junior minister ... did not appeal ... no new projects would start"; "everyone; all use of the instrument ended" -> organised, model, 1, 1 class, procedural (accepted E1).
- G10 E4: "placed in public consultation ... adoption ... not confirmed" -> organised, model, 0.

## G11
Probe G11: I think this is the Dutch childcare benefits scandal (toeslagenaffaire) and the Belastingdienst risk-classification model, Raad van State 2019 rulings, Autoriteit Persoonsgegevens fines, the Van Dam POK and Rutte III resignation. Recognised = 1.
- G11 E1: "individual parents. Funded or run by: not reported" -> unclear; annulment of their decisions -> own-case; [COURT-1] "set it aside in about a fifth" -> 1 (some relief); "case by case" -> cr 0; ground for successful appeals not given -> unclear.
- G11 E2: "[OMBUDS-1], after complaints"; about the families of one agency -> own-case (named set); "disproportionate reaction"; recommendations accepted -> 1, cr 0, procedural ("without enough regard for the individual parent's position").
- G11 E3: "individual parents (appellants). Funded or run by: not reported" -> unclear; own-case; "abandoned the all-or-nothing line" -> 1; concerns recovery rule, not [MODEL] -> cr 0; "statute leaves room for a proportionate setting" -> substantive.
- G11 E4: government advisory committee; advice on handling parents -> target unclear; "recommended compensation" -> 1, cr 0, ground unclear.
- G11 E5: "[AUDITOR-1]"; "established that dual nationality had been used as a criterion" -> organised, model, 1, 0, mixed.
- G11 E6: "[AGENCY-1], on its own investigation"; "using nationality as an indicator in the risk-scoring model ... was unlawful and discriminatory"; fine; "all applicants" -> organised, model, 1, cr 1 class (declared unlawful in general), substantive (unlawful in what it calculates).
- G11 E7: "management team of [OPERATOR]"; "permanently stopped"; "all future applicants" -> organised, model, 1, 1 class; "did not meet the requirements of the regional data-protection regulation" -> procedural.
- G11 E8: "the lower house of parliament"; childcare-allowance implementation generally -> target unclear; "basic rule-of-law principles had been violated" -> 1, 0, mixed.
- G11 E9: "the cabinet"; flat sum "to every parent found harmed" -> organised, own-case, 1, 0, unclear ("to do justice to parents faster").
- G11 E10: cabinet resignation; not relief -> organised, unclear, 0.
- G11 E11: "about twenty parents, later joined by several dozen more, through a lawyer" -> organised (group); prosecution of ministers -> unclear; "advised against" -> 0.
- G11 E12: "individual parents. Funded or run by: not reported" -> unclear; own-case; first tests done, compensation -> 1, 0, unclear ("per individual case").
- G11 E13: judiciary working group; "recommended that judges actively examine the facts" -> organised, unclear, 1, 0, procedural.
- G11 E14: "[INTL-1]"; "shortcomings ... serious and systemic"; recommendations -> organised, unclear, 1, 0, procedural.
- G11 E15: "[COURT-1]"; "regretted returning too late from its strict line" -> organised, unclear, 1, 0, substantive (accepted all-or-nothing "without enough attention to proportionality").
- G11 E16: DPA fine on "[SYSTEM-2]" (not [MODEL]) -> organised, target unclear, 1; register already off, not [MODEL] -> cr 0; "no legal basis ... incorrect and outdated data" -> mixed.
- G11 E17: "defence counsel ... Funded or run by: not reported" -> unclear; own-case; "rejected; the accused were convicted" -> 0.
- G11 E18: "the junior finance minister"; "an age-related identifier indicator also had a discriminatory effect" -> organised, model, 1; ministry analysis, not independent -> cr 0; substantive.
- G11 E19: "a large number of parents" -> organised; prosecution -> unclear; "refused" -> 0.
- G11 E20: statute on redress; "parents who registered and were found harmed" -> organised, own-case, 1, 0, unclear.
- G11 E21: external audit firm; "did not directly lead to corrections or stopped allowances" -> organised, model, 0.
- G11 E22: parliamentary inquiry; "inadequate technical set-up, indicators lacking statistical relevance ... breaches of the rights" -> organised, model, 1, 0, mixed.
- G11 E23: "parents, through a lawyer" -> organised; prosecution of officials -> unclear; "refused" -> 0.
- G11 E24: benefits service study; "no indication that handling after selection by the model was harsher" -> organised, model, 0.

## G12
Probe G12: I think this is Michigan's MiDAS unemployment fraud system (UIA; Zynch v Ardis, Bauserman v UIA, Cahoo v SAS). Recognised = 1.
- G12 E1: "individual claimants ... Funded or run by: not reported" -> unclear; own-case; "the agency's position was upheld in under a tenth" -> 1; "individual appellants" -> cr 0; "per case; not reported" -> unclear.
- G12 E2: "[AGENCY-2], which oversees state unemployment programmes"; "found the practice violated federal regulations" -> organised, model, 1; re-adjudication only "advised" -> cr 0; "require individual investigation and an opportunity to rebut" -> procedural.
- G12 E3: "individual claimants, a national industrial labour union ([ORG-2]) and a non-profit law centre ([ORG-1])" -> organised; "an order stopping fraud determinations" -> model; "agreed to suspend collections tied to the automated determinations and reviewed earlier determinations" -> 1, cr 1 class ("all claimants subject to ... fraud determinations"); due process -> procedural.
- G12 E4: "class action ... a private plaintiffs' law firm" -> organised; "money damages" -> own-case; settled "about twenty million dollars" -> 1; damages only -> cr 0; "state constitution's due process guarantee" -> procedural.
- G12 E5: auditor general; findings on reversals and that agency should "better explain" and "gather better information" -> organised, model, 1, 0, mixed.
- G12 E6: "[OPERATOR] and its parent state agency"; "reversing tens of thousands of fraud findings and refunding"; "persons with determinations in the reviewed period" -> organised, model, 1, cr 1 class, substantive ("most were wrong").
- G12 E7: statute: "may not determine ... fraud unless a state employee verifies it; this codified the agency's change made at A+2" -> organised, model, 1; the automated function had already been switched off, so this episode did not itself withdraw anything -> cr 0; mistaken accusations plus human verification -> mixed.
- G12 E8: "five named claimants, filed as a proposed class action" -> organised (class action); damages -> own-case; "no relief reported" -> 0.
- G12 E9: statute "reduced the maximum penalty multipliers" -> organised, model (consequences for all), 1, cr 0 (determinations not revised), substantive ("response to the agency's false fraud findings").
- G12 E10: auditor general; "undercalculated penalties in about half of cases" -> organised, model, 1, 0, substantive.

## G13
Probe G13: I think this is the 2020 Ofqual A-level/GCSE standardisation algorithm in England (Foxglove/Curtis Parfitt-Ford; Good Law Project; U-turn to centre-assessed grades; OSR review). Recognised = 1.
- G13 E1: "[COMMITTEE-1], a standing committee"; called to publish the model, warned of unfairness and bias; "no binding relief" -> organised, model, 1 (adverse findings/recommendations), 0, mixed (transparency + anchoring unfairness).
- G13 E2: "[OPERATOR] itself"; criteria published "then withdrew them within hours" -> organised, model, 0.
- G13 E3: "[PLAINTIFF-1], a student ... through the law firm [ORG-2] and the technology-justice group [ORG-1]. Funded or run by: [ORG-1] and [ORG-2]" -> organised, supported 1; asked that "students be graded on their own merits" -> model; "Three days after the letter, the government ... replaced model grades" -> 1, cr 1 class; "no court ruling" -> ground unclear.
- G13 E4: "several students (reported as six) ... with ... [ORG-3]. Funded or run by: [ORG-3]" -> organised, supported 0 (group of students); "review and revision of the scheme" -> model; "overtaken by E5" -> 1, cr 1 class; unclear (no ruling).
- G13 E5: minister and [OPERATOR]; "received the higher of their teacher-estimated grade and their model grade"; "all students" -> organised, model, 1, 1 class; "fairness achieved was not felt to be acceptable" / evidence of outcomes -> substantive.
- G13 E6: "[AGENCY-2], the national statistics regulator"; "limits and uncertainty ... not fully communicated"; "none binding" -> organised, model, 1, 0, procedural.
- G13 E7: inquiry hearings; "No report findings on this topic" -> organised, model, 0.

## G14
Probe G14: I think this is Arkansas ARChoices / the RUGs home-care algorithm (Legal Aid of Arkansas; Bradley Ledgerwood case; InterRAI). Recognised = 1.
- G14 E1: "mostly self-represented; [ORG-1] assisted about a hundred people" -> unclear (mixed, not reported in aggregate); own-case; "aggregate numbers and outcomes not reported" -> 0.
- G14 E2: "[PLAINTIFF-1] ... Funded or run by: [ORG-1], a legal aid nonprofit" -> organised, supported 1; "restoration of hours and adequate notice" -> own-case; "ruled for the plaintiff" -> 1; notice fix is not a revision of outputs -> cr 0; "did not give adequate notice" -> procedural.
- G14 E3: "seven severely physically disabled recipients ... Funded or run by: [ORG-1]" -> organised, supported 0 (group); "an order barring use of [MODEL]" -> model; "permanent injunction barring use of [MODEL] ... applied to all programme recipients" -> 1, cr 1 class; "rested on how the method was adopted, not on whether its outputs were correct" -> procedural.
- G14 E4: "[AGENCY-1], seeking approval of an emergency rule to keep using [MODEL]" -> organised, model; no relief from the model (it continued it) -> 0, cr 0.
- G14 E5: "rules dropped [MODEL] and its resource-utilisation groups"; "all programme recipients" -> organised, model, 1, cr 1 class; reasons "more flexibility" and spending -> unclear.

## G15
Probe G15: I think this is Idaho's developmental-disability budget tool, K.W. v. Armstrong (ACLU of Idaho). Recognised = 1.
- G15 E1: "individual participants ... often helped by unpaid service coordinators; [AGENCY-1] did not fund advocates" -> lone; "higher individual budgets" -> own-case; "about three-fifths of budgets reviewed were increased" -> 1; "individual appellants only" -> cr 0; "not reported in aggregate" -> unclear.
- G15 E2: "Funded or run by: [ORG-1], a civil liberties organisation"; class action -> organised; "a lawful budget method" -> model; injunction "restored budgets" and "extended ... to all of them"; tool held to violate due process -> 1, cr 1 class; reasons "notice inadequate; tool unreliable and untested" -> mixed.
