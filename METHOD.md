# Method and evidence

Associated paper: [Would You Imagine Yourself Negotiating With a Robot, Jennifer? Why Not?](https://doi.org/10.1109/THMS.2021.3121664).

## Scientific contract

TSBT or BABT between groups, with within-participant gesture conditions and the notification protocol.

Five-minute practice; two ten-minute main sessions; fifteen-minute break; nine-point questionnaire after both sessions. Point profiles are assigned by session position.

The machine-readable [paper map](paper-map.json) links selected manuscript labels,
source hashes and locations to implementation, independent tests, configurations
and result targets. Only the selected active LaTeX entry was used. Manuscript
working files, inactive drafts and reviewer correspondence are not redistributed.


## Interaction and presentation

The Ready → human offer → agent response → Accept/Reject → Ready handshake is
implemented. Notifications and rejections are protocol events, not formal bids.
A stale offer reference cannot reject a newer offer. The human-share perspective
is the same in structured input, text parsing, spoken proposal and utility tests.

The paper mood priority is selectable per condition. The templates expose an
illustrative warning fraction `.8` and BABT mild multiplier `.95`; numerical
historical confirmation and the original argument/gesture corpus are preflight
gaps. Generated plain-language proposals do not claim to recreate those corpora.
Gesture-disabled conditions suppress gesture commands while retaining speech.

## Utility, targets and game scores

A bid always states the human share. Agent utility uses the complementary allocation.
Utility is computed at full precision; rendering multiplies by 100 for display.
A target score is distinct from a reservation constraint. In the fruit papers,
a human agreement below 40 points is permitted but earns zero game points;
raw utility and game payoff remain separate logged fields. The Jennifer papers'
30-point goal is not silently turned into a prohibition on lower agreements.
The short Solver and Appearance examples do not claim those fruit reward rules.

## Remaining evidence gaps

The inspected historical mood controller uses a .7 warning and a .3 Offended
threshold, while its BABT wrapper uses .9 for the mild multiplier. The templates'
.8/.95 values are illustrative. A zero hard reservation currently also gives the
paper mood adapter a zero Offended threshold. In addition, BABT's maintained
nearest-utility selector differs from the legacy expanding-interval random choice.
These behavior differences need method/configuration decisions independently of
participant-data availability.

- Original practice profiles, questionnaire wording and gesture/argument corpus.
- Numerical warning and BABT mood threshold with historical provenance.
- Exact inclusion/exclusion mapping and permitted paired participant records.

Unknown inputs are not filled with simulated participants or invented historical
constants. The existing templates are inspectable, but their published-protocol
preflight prevents starting before required evidence is supplied and reviewed.
A custom study has its own declared configuration and cannot inherit a reproduction
claim merely by using the same strategy name.

## Relationship to the research series

Preserves tactic groups and within-person gesture comparisons; later centroid reuse is code/asset provenance, not the same experiment.

The common engine owns utility, lifecycle, logs, GUI, shared methods and device
contracts. This repository owns paper-specific profiles, protocol choices, analysis
rules, reproduction targets and tests. [framework.json](framework.json) pins the
engine; [NOTICE](NOTICE) preserves original source attribution.
