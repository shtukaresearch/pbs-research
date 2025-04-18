# Builder multiplexing in PBS

*Andrew W. Macpherson, Shtuka Research.*
*Supported by PBS Foundation through Research Grant R9.*

This post is an abridged version of an extended report of the same title. The full report, which contains the details of our model and scenario analysis, is published [here]().  The author is grateful to the PBS Foundation for supporting this work.

## Background

Concentration and exclusive "backroom deals" in Ethereum's PBS builder markets has long been a concern of the Ethereum blockspace community. Concentration is regarded as an unwanted pathway to monopoly, centralisation, and all of the inefficiencies that entails. Unfortunately, it appears to be an inevitable consequence of the present structure of the blockspace supply chain that builders can only achieve edge by privately negotiated exclusive arrangements. Worse than being simply opaque, exclusive arrangements are extremely hard to come by for new entrants and hence present an apparently insurmountable barrier to entry, severely limiting the competitiveness of builder markets. Moreover, the exclusivity of these links fragments the market, reducing reliability.

In this work, we attempt to illuminate these issues by introducing an incentive model of builders and what we call*multiplexers* or *muxers*, that is, entities who forward transaction items to one or more builders together with a request for partial rebate. The incentive model quantifies the tradeoff between the reliability of multiplexing to many builders and the possibility of obtaining a larger rebate from the edge that a single builder gains through an exclusive arrangement. This builds on a body of previous work by quantifying at the model level:
* *why* order flow sources (OFS) might enter into risky exclusive arrangements, and 
* the conditions that make an OFS "pivotal"'" to a builder in the sense that its presence or absence decides the outcome of the PBS auction.

Finally, we wish to emphasise that our model assumes complete trust in the execution of the PBS auction. The frictions we identify would therefore persist even if the well-known issue of trust in the relay were resolved.

### Key findings

Our model predicts that PBS markets are dominated by builders with persistent edge, regardless of auction structure or profitability, and that the key sources of edge are OFS with high-value bundles and relatively high risk tolerance who may choose an exclusive forwarding strategy for its higher expected returns. We find conditions under which exclusive flow can materialise even in the absence of a formal integration or "backroom deal" governing the relationship between the OFS and the builder.

Significantly, the model shows that this state of affairs — already well known to be the case in the PBS market today — is not due to the idiosyncracies of the present incumbents, the PBS auction rules, or the current reliance on trust in the execution of those rules. Rather, it is an inevitable consequence of the single item auction structure of PBS and the existence of major OFS with certain risk preferences.

In more detail:
1. We describe the source of *contention* between transaction items as a set of "safety rules" governing block construction. As well as consensus rules, safety rules can be inherited from commitments further up the OF supply chain such as execution guarantees and bundle compatibility.
   By definition, contentious transactions are those for which inclusion into the optimal block depends on the other transactions in a builder's mempool. It is therefore difficult to get strong upstream assurances about whether such items will be included.
   
2.  Builder muxing with nonzero rebate is a way for a builder to maintain edge at the same time as derisking by sharing flow.  Based on the current market layout, it appears that this edge is much smaller than those associated to exclusive flow.
3.  Market dominance in the current structure requires only consistent edge. The size of the edge doesn't affect the amount of dominance. To allow builders with weaker edge to acquire non-trivial market share, a new market structure — probably one with multiple sellers and multiple items — is necessary. Simply changing the auction format, as suggested by (Öz, 2024), isn't good enough.
4.  We identify two major theoretical sources of edge: originating contentious items (searcher-builder), and a preferential relationship on pivotal flows. In the pivotal flows case, an exclusive forwarding strategy sometimes dominates even without a formal "backroom deal" or contention. Even under conditions of complete trust in the PBS relay, these sources of edge are only available to builders with specific structural advantages or under specific builder market conditions.
5.  Once a builder has achieved market dominance, he can substantially increase his profit margins by making decisions on additional contentious items, including those where the contention is idiosyncratic to that builder (for example because of jurisdictional issues). This single point of control over allocation is an efficiency and censorship threat.

### Recommendations for future research

We call on the Ethereum research and business communities to intensify research into the following areas:

1. *Quantitative analysis of sources of builder edge.* If the largest sources of edge were smaller, minor sources of edge like priority sharing could become viable routes to entry, improving market access. To understand how these sources can be broken up and shared, we need a deeper, quantitative understanding of why exclusive arrangements of the two types identified are attractive for the OF sources. This objective could be pursued with more detailed scenario analysis, gathering case studies, and statistical analysis of labelled data to fit the model parameters.
2. *Costs and returns of reliability guarantees.* As far as we know there are currently no muxer services that offer a concrete guarantee on transaction landing rate (though Flashbots Protect does at least [report](https://dune.com/flashbots/flashbots-protect) theirs). For classes of items where contention is limited, more effort should be made into modelling landing rate with a goal of underwriting such a guarantee. Part of the work involved would be to explicitly identify the relevant low-contention classes. Statistical research into the demand for improved reliability would illuminate the value of such constructions to the Ethereum business community.
3. *Novel market structures for full blocks.* The single change that we think would have the widest impact on the current bottlenecks of the PBS market would be to move from a single seller to multiple seller market for blocks, breaking the proposer monopoly on the single slot timescale. Some movement in this direction is already under way, with partial block construction being factored out to other markets (via preconf protocols) or in-protocol committees (via FOCIL).   
   Making this change for the full block, particularly the part of the block containing the highest value contentious items, would need either widespread community support for a consensus upgrade or a large fraction of validators signing up for an external commitment market. We therefore expect this line of research to play out over a longer time scale than the previous two directions.

## Model description and discussion

For details, see the [full report]().


## Pathways to impact

How can we leverage our model to influence how the Ethereum community builds? We couch the discussion in terms of what we believe to be three core concerns: *transparency*, *centralisation vectors*, and *reliability*.

### Prior work
To understand where to go from here, we first review the state of the art.

* In (Öz, 2024) the authors perform extensive labelling of OFS, present visualisations on the breakdown of builder gross revenue, and computes Spearman correlations between profit margin and various OFS features.  The paper provides no opinion on methods to reduce the pivotal nature of exclusive as opposed to shared private orderflow.
* In (Gupta, 2023), a statistical model is used to find a relationship between price volatility, used as a proxy for CEX/DEX arbitrage opportunities, and dominance of so-called "HFT builders." Other OFS sources or features and alternative builder strategies are not considered. Our model quantifies Remark 1 of *op. cit*.
* The article (Titan, 2023), authored by what is today one of the major block builders, uses a private dataset to illustrate the prevalence of multiplexing among searchers.
* (Yang, 2024) identifies the concept of pivotal flow. The approach is combinatorial, focusing on identifying OFS whose inclusion or exclusion decides the game outcome, rather than quantitative. However, the authors' proposed solution involves a centralised entity running a TEE, which is rather unsatisfactory from the perspective of resilience or censorship-resistance.

### Transparency

Publishing and disseminating insights into the structure and flows of the Ethereum blockspace supply chain improves trust and usability for broadcasters and builders alike. Transparency lowers barriers to entry that have the form of information asymmetry. Smaller builders or broadcasters may enter the market with greater confidence about the competitive landscape, increasing competitiveness and hence improving services, diversity, and efficiency.

So far, the community has been successful in illuminating many facets of the PBS landscape:

* The structure and cash flows of a subset of the OFA/muxer and builder relationships (excluding muxer-builders);
* The extent to which volatility, as a proxy for CEX/DEX arb value, drives builder profits;
* The breakdown of block revenue into components originating from various labelled OFS;
* Case studies and combinatorics of pivotal OFS in the current market;
* Partial data on transaction landing rates.

However, there is much more we could be doing via a combination of theory, publicly available data, and encouraging the publication of summaries of proprietary data:

* Further illuminate the strategy space. Further exploration of the strategies of long tail and emerging "midfield" builders. A model-based approach can identify strategies that are not currently being explored or exist under counterfactual scenarios. In-depth study of entry strategies and complementarity (muxer-builder, searcher-builder). 
* Identify common factors of the components that drive builder market share ranking, for example the relation to volatility to labelled OFS features. Investigate the extent to which these factors drive builder *net* revenue.
* Further studies on landing rate and reliability, beyond Flashbots Protect. Can we uncover data on failures in exclusive flow strategies?

### Builder centralisation

The concerns of the community about concentration and entrenchment in the builder market can be understood in terms of multiple threats:

* Monopolistic practices such as artificial scarcity and price hikes;
* Censorship;
* Other economic inefficiencies such as lack of investment into service improvements.

What does our model tell us about the severity of these threats and possible paths to resolution?

1.  Does builder market concentration really cause these issues? How centralised is too centralised? How about not centralised enough?
   By analogy with the model of (Chitra, 2024), entry costs are likely to be important drivers of the welfare-maximising answers to these questions. As we have seen, entry costs are downstream of sources of edge and the risk appetites of OFS, so a model of these should help us understand the welfare of different concentration levels.
2. Can we isolate centralisation threats by taking some responsibilities away from the builder? For example, on a multi-block timescale, inclusion lists in Ethereum offload some allocation responsibility to a committee of validators. On the single-block timescale, preconfirmation and similar commitment protocols may be able to do the same.
   To understand this we need a solid model of transaction contention and which types of flow it is feasible to push upstream.
3. How can anyone lower the barriers to entry to become a full block builder? Under the current market structure, we have seen that these barriers are driven by risk-tolerant, high value OFS. Thus understanding the incentives of these sources is crucial to an investigation of what other structures might draw them away from exclusive builder arrangements.
   A more fundamental approach is to change the market structure of PBS by introducing multiple sellers. Note that simply changing the *auction format*, as proposed in (Öz, 2024), does not solve this problem — it is intrinsic to the single item, single seller auction.

*Remark. (A threat).* Any approach the community takes to "democratise" or otherwise curtail specific sources of builder edge must be taken extremely carefully, for fear of collapsing the market into an even more fragile state. For example, adopt the stylised model of the current market that Titan Builder's main source of edge is Telegram bot flow while beaverbuild's main edge is an integrated CEX/DEX arb searcher. If the market structure changes in such a way as to break one of these sources of edge but not the other, the surviving builder could easily become a monopoly — a far worse outcome than an apparently competitive duopoly.

### Reliability

A primary concern for the usability of Ethereum is its capacity to offer reliable assurances of inclusion and execution within specified time frames. For reasons illustrated by our model, the current system of builders and exclusive flow is not well-suited to provide that. Transaction originators wishing to avoid the public mempool must manage connection to multiple builders or delegate this responsibility to a downstream muxer. No one is in a position to uphold a strong SLA for contentious items.

While much of the conversation around the problems facing the PBS market has focused on contention, there is much to be said for improving the reliability of Ethereum's handling of non-contentious, ordinary items. Important examples of low or no contention items are bridge locks and unlocks, rollup state root updates, and blobs. It's likely that these services can be improved substantially even without solving the harder issues.

How can the system deliver reliable service without breaching centralisation limits?

1. Understand the rates at which contentious transactions land. Estimate the cost of landing transactions at different chance bounds on a per use case basis.
2. Study mechanisms for coordinating acceptance decisions between builders for items falling under given constraints.
3. Understand how important landing rate is to OFS. Study the relation between landing rate per service against demand growth.

## Bibliography

* Chitra, T., Kulkarni, K., Pai, M., & Diamandis, T. (2024). *An Analysis of Intent-Based Markets* (No. arXiv:2403.02525). arXiv. https://doi.org/10.48550/arXiv.2403.02525
* Gupta, T., Pai, M. M., & Resnick, M. (2023). The Centralizing Effects of Private Order Flow on Proposer-Builder Separation. In J. Bonneau & S. M. Weinberg (Eds.), *5th Conference on Advances in Financial Technologies (AFT 2023)* (Vol. 282, p. 20:1-20:15). Schloss Dagstuhl – Leibniz-Zentrum für Informatik. https://doi.org/10.4230/LIPIcs.AFT.2023.20
* Öz, B., Sui, D., Thiery, T., & Matthes, F. (2024). Who Wins Ethereum Block Building Auctions and Why? In R. Böhme & L. Kiffer (Eds.), *6th Conference on Advances in Financial Technologies (AFT 2024)* (Vol. 316, p. 22:1-22:25). Schloss Dagstuhl – Leibniz-Zentrum für Informatik. https://doi.org/10.4230/LIPIcs.AFT.2024.22
* Titan. (2023, June 13). *Builder Dominance and Searcher Dependence*. Builder Dominance and Searcher Dependence. https://frontier.tech/builder-dominance-and-searcher-dependence
* Yang, S., Nayak, K., & Zhang, F. (2024). *Decentralization of Ethereum’s Builder Market* (No. arXiv:2405.01329). arXiv. https://doi.org/10.48550/arXiv.2405.01329
