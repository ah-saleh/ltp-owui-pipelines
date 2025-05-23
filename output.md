See discussions, stats, and author profiles for this publication at: https://www.researchgate.net/publication/343341533

Improving picking performance at a large retailer warehouse by combining
probabilistic simulation, optimization, and discrete‐event simulation

Article  in  International Transactions in Operational Research · July 2020

DOI: 10.1111/itor.12852

CITATIONS
10

4 authors:

Mário Amorim Lopes

University of Porto

22 PUBLICATIONS   304 CITATIONS   

SEE PROFILE

João Alves

University of Porto

1 PUBLICATION   10 CITATIONS   

SEE PROFILE

Some of the authors of this publication are also working on these related projects:

Knowlogis — An intelligent dashboard for hospital logistics View project

RANCARE Action: Missed nursing care (EU COST Action) View project

READS
810

Luis Guimarães

University of Porto

20 PUBLICATIONS   438 CITATIONS   

SEE PROFILE

Bernardo Almada-Lobo

University of Porto

111 PUBLICATIONS   3,169 CITATIONS   

SEE PROFILE

All content following this page was uploaded by Mário Amorim Lopes on 04 August 2020.

The user has requested enhancement of the downloaded file.

Intl. Trans. in Op. Res. 00 (2020) 1–29
DOI: 10.1111/itor.12852

INTERNATIONAL
TRANSACTIONS
IN OPERATIONAL
RESEARCH

Improving picking performance at a large retailer
warehouse by combining probabilistic simulation,
optimization, and discrete-event simulation

Mário Amorim-Lopesa,b,∗

, Luís Guimarãesa, João Alvesc

and Bernardo Almada-Loboa

aFaculdade de Engenharia, INESC-TEC, Universidade do Porto, Porto 4099-002, Portugal
bCatólica Porto Business School, Porto 4169-005, Portugal
cLTP Labs, Porto 4149-008, Portugal
E-mail: mario.lopes@fe.up.pt [Amorim-Lopes]; lguimaraes@fe.up.pt [Guimarães]; joao.alves@ltplabs.com [Alves];
almada.lobo@fe.up.pt [Almada-Lobo]

Received 18 March 2019; received in revised form 10 July 2020; accepted 11 July 2020

Abstract

Distribution warehouses are a critical part of supply chains, representing a nonnegligible share of the op-
erating costs. This is especially true for unautomated, labor-intensive warehouses, partially due to time-
consuming activities such as picking up items or traveling. Inventory categorization techniques, as well as
zone storage assignment policies, may help in improving operations, but may also be short-sighted. This work
presents a three-step methodology that uses probabilistic simulation, optimization, and event-based simula-
tion (SOS) to analyze and experiment with layout and storage assignment policies to improve the picking
performance. In the ﬁrst stage, picking performance is estimated under diﬀerent storage assignment policies
and zone conﬁgurations using a probabilistic model. In the second stage, a mixed integer optimization model
deﬁnes the overall warehouse layout by selecting the conﬁguration and storage assignment policy for each
zone. Finally, the optimized layout solution is tested under demand uncertainty in the third, ﬁnal simulation
phase, through a discrete-event simulation model. The SOS methodology was validated with three months
of operational data from a large retailer’s warehouse, successfully illustrating how it may be successfully used
for improving the performance of a distribution warehouse.

Keywords: warehouse design; storage assignment policies; picking performance; discrete-event simulation; mixed integer
programming; simulation-optimization

∗Corresponding author.

© 2020 The Authors.
International Transactions in Operational Research © 2020 International Federation of Operational Research Societies
Published by John Wiley & Sons Ltd, 9600 Garsington Road, Oxford OX4 2DQ, UK and 350 Main St, Malden, MA02148,
USA.

2

M. Amorim-Lopes et al. / Intl. Trans. in Op. Res. 00 (2020) 1–29

1. Introduction

Warehouses are a critical component of modern supply chains, storing and buﬀering goods that
arrive from suppliers located all over the world—sometimes continents apart—in single point,
from which they are then sent to other locations, usually retail stores. Ideally, goods would be
shipped just in time directly to the stores, or at least in such a way that stocks would be kept
to a bare minimum, while keeping service levels at a satisfactory level. In practice, however,
shipping times and transportation costs turn this option impracticable, or at least too expen-
sive. Furthermore, they make it hard to deal with demand uncertainty, potentially leading to
stockouts.

Arguably, the most labor-intensive and costly activity in a warehouse is order picking (de Koster
et al., 2007; Rushton et al., 2014), which involves retrieving the requested items from storage to
satisfy client orders. Drilling down the underlying tasks of order picking, Tompkins et al. (2010)
estimate that roughly 50% of the order-picking time is spent traveling through the storage locations,
20% is spent searching for the item, 15% is spent for actually picking the item and moving it to the
car or basket, and 15% for setup and other tasks. In addition, some authors estimate that order
picking accounts for 60–70% of warehousing costs (Chen et al., 2015).

Although warehouse operations are technically simple to execute, improving warehouse eﬃ-
ciency entails many nontrivial decision-related issues. The warehouse manager faces many options
regarding operational and tactical decisions when it comes to setting up a warehouse (de Koster
et al., 2007). To name but a few, a diligent warehouse manager has to decide on the layout design for
the warehouse and for each storage area (Sprock et al., 2017); deﬁne storage assignment policies,
namely where items should be stored; consider picking policies, elaborating a list of which items
and how many items to pick; implement routing policies, as the route taken may increase signiﬁ-
cantly the order retrieval time, especially in large and sparse warehouses; and so on (Davarzani and
Norrman, 2015). Moreover, the warehouse manager needs to solve these problems while striving to
minimize the travel distance/time and order throughput times (Grosse et al., 2017).

Addressing each of the said issues individually is already a diﬃcult task, and even more so when
we consider the integrated problem, as the impact of each of these policies is interdependent (van
Gils et al., 2018b). For instance, no matter how optimized a picking policy is, if the layout design
is ﬂawed, it may compromise the picking performance, and vice versa. Moreover, and according
to the literature, it is clear that there is not a single, one-size-ﬁts-all solution exists; hence, optimal
solutions can only be applied to very speciﬁc settings, and therefore, they are nongeneralizable.
When all the degrees of freedom for arranging a warehouse are added up, the problem becomes
increasingly complex. This is especially true given the onset of e-commerce, which has caused
the stock-keeping unit (SKU) assortment to increase considerably (de Koster et al., 2017). There-
fore, it is even more relevant to address warehouse problems in an integrated way (van Gils et al.,
2018a).

This paper presents a three-stage methodology anchored on simulation and optimization that
incorporates both zone layout design and storage assignment policies as warehouse management
levers. Each phase solves a diﬀerent part of the problem: the ﬁrst ﬁnds the best storage assign-
ment policy for each zone; the second considers the warehouse as a whole, and ﬁnds the best
location for each zone with regard to throughput; and ﬁnally, stage three subjects the model to
demand uncertainty. The model was tested on a picker-to-parts warehouse of a large distribution

© 2020 The Authors.
International Transactions in Operational Research © 2020 International Federation of Operational Research Societies

M. Amorim-Lopes et al. / Intl. Trans. in Op. Res. 00 (2020) 1–29

3

company, achieving signiﬁcant eﬃciency gains by decreasing the travel distance, as well as the order
retrieval time.

The main contribution of this paper rests on the methodology hereby presented, and speciﬁ-
cally on its ability to help designing a warehouse, or implementing storage assignment and picking
policies. The methodology also encloses the following contributions: (a) we introduce a probabilis-
tic simulation model to capture the travel time of diﬀerent order sizes in a picker-to-parts ware-
house with unidirectional aisles and (b) we introduce a novel mixed integer mathematical model
to simultaneously deﬁne the conﬁguration, location, and storage assignment policy in a multizone
warehouse. Given the nature of the methodology, it can be easily extended to also study routing
policies or other warehouse decision related problems, and can also be adapted to other multizone
warehouses realities, by introducing the required changes to each phase without losing the method-
ological structure. The use of simulation facilitates subjecting the model to uncertainty, in this case
to demand (order) uncertainty.

The remainder of the paper is organized as follows. Section 2 reviews the state of the art on
warehouse science and order picking, while Section 3 presents the case study, along with rel-
evant information. Section 4 explains the methodology employed, Section 5 presents the vali-
dation and the results obtained, and Section 7 concludes with a short discussion and further
work.

2. Overview of warehouse decision problems

Warehouses are a sprocket of modern supply chains, helping to balance supply with uncertain de-
mand (Gu et al., 2007). In an interconnected marketplace that serves customers from all over the
world, surges in demand may happen frequently, with warehouses acting as a safety buﬀer (de
Koster et al., 2007). Also, warehouses come as a compromise between transportation and opera-
tional costs, decreasing the ﬁrst, but increasing the second, ideally in an uneven way. According to
ELA/AT Kearney (2004), it is estimated that warehouses add about 20% to logistic costs, in return
for the savings obtained in the transportation costs.

These fulﬁllment centers are essentially a “pass through” for the goods, an intermediary stage
between procurement and distribution. The four main activities carried out at a warehouse are (a)
receiving the goods, (b) putting away the goods either on buﬀers or storage locations, (c) order
picking, and (d) shipping. The ﬁrst two activities are inbound processes, while the two last are out-
bound processes (Bartholdi and Hackman, 2011). Order picking is arguably the most demanding
and labor-intensive, especially in nonautomated, picker-to-part systems. In fact, most of the re-
search on improving warehouse performance invariably rests on enhancing picker performance (de
Koster et al., 2007).

In order to improve picking eﬃciency, warehouse managers typically face four tactical and op-
erational decision related problems: (a) layout design, (b) picking policies, (c) storage assignment
policies, and (d) routing policies (Chan and Chan, 2011). Layout design focuses on the disposition
of the order-picking system, but also with the layout of the entire facility, including input and out-
put (I/O) points, marshaling positions, proximity to cross-docks, etc. Picking policies deﬁne if and
how orders are to be grouped into picking tours. Storage assignment policies specify how to store
items through the warehouse. Finally, routing policies indicate the sequence of items to be picked.

© 2020 The Authors.
International Transactions in Operational Research © 2020 International Federation of Operational Research Societies

4

M. Amorim-Lopes et al. / Intl. Trans. in Op. Res. 00 (2020) 1–29

Usually, items are sorted to ensure a single-pass retrieval, but exceptions exist. Each of the four
decision problems is detailed next.

2.1. Layout design

Two decision problems occur when addressing the layout design (de Koster et al., 2007). First, how
to design the facilities, including deﬁning areas for loading and unloading docks, cross-docking,
buﬀers, storage areas, marshaling positions (if any), etc. Second, how to deﬁne the layout within the
order-picking designated area, also known as internal layout design or aisle conﬁguration problem.
Changes to the facility layout are outside the scope of this paper, and so we are mostly concerned
with changes to storage areas. In this regard, Caron et al. (2000) presented an analytical approach
for designing the picking area in low-level picker-to-part systems using a particular storage as-
signment metric, the cube per order index (COI), which takes into account the ratio between the
product’s total required space and the number of trips required to satisfy its demand per period.
Petersen (2002) uses simulation to measure the eﬀect of aisle length and the number of aisles on
total travel time. Also, Larson et al. (1997) suggest a heuristic for assigning classes to locations,
thus reducing the travel distance between I/O locations and aisle spots for the top-picked products.
In a more recent work, Horta et al. (2016) propose a min–max mathematical programming model
to assign stores to locations in order to minimize the distance traveled. The model is tested on a
fruits and vegetables warehouse from a large retail chain.

2.2. Picking policies

In terms of options involving picking policies, the most common is a picker-to-part system, where
the order picker walks or drives along the storage aisles to retrieve the items. Within this picking
model, the decision over how to split and combine orders also matters, as it may severely aﬀect the
picking performance. For large orders with diverse products, each order can be handled individu-
ally, with each task giving origin to one picking tour. Alternatively, when orders are small, travel
time may be reduced if diﬀerent orders are grouped into one picking tour. The former is known as
single order-picking policy, while the last is known as batching (de Koster et al., 2007). Clearly, single
order-picking policy is administratively simpler, as no additional eﬀort is required to split a batch
and consolidate the items per customer order. Additionally, accumulation/sorting (A/S) processes
are very prone to errors, especially when handled manually. Changes to picking policies are outside
the scope of this work; therefore, we will skip a detailed review of this topic. The interested readers
can refer to de Koster et al. (2007) for an extensive discussion on this subproblem.

2.3. Storage assignment policies

As regards storage assignment policies, alternatives abound, and they are known to inﬂuence sig-
niﬁcantly the distance traveled to complete an order. In general, it has been shown that nonran-
domized, dedicated storage helps to maximize system throughput, while random storage is more

© 2020 The Authors.
International Transactions in Operational Research © 2020 International Federation of Operational Research Societies

M. Amorim-Lopes et al. / Intl. Trans. in Op. Res. 00 (2020) 1–29

5

adequate when the goal is to maximize the utilization of storage space (Mansuri, 1997). Prior to
actually deﬁning where to assign products, space has to be allocated. One way of allocating the
space within the storage area is the forward-reserve system. In this setup, the bulk stock (reserve
area) is put on a place apart from the pick stock (forward area), thus reducing the picking area (de
Koster et al., 2007). Holding everything else constant, the smaller the area, the lower the average
travel times will be. However, dividing the inventory will require internal replenishments from the
reserve to the forward area, and therefore a trade-oﬀ emerges. In van den Berg et al. (1998), the
authors provide a model adapted from the knapsack problem to minimize the expected amount of
labor during the picking period by optimizing replenishments. Öztürko˘glu (2020) proposed a biob-
jective mathematical model for allocating products in block staking warehouses. In this particular
case, storage assignment targets two objectives: reducing travel distance and maximizing average
storage usage.

With the picking and reserve locations well deﬁned, the next decision concerns assigning prod-
ucts to particular aisles. The most common assignment policies are random storage, closest open
location storage, dedicated storage, full turnover, and class-based storage (de Koster et al., 2007).
Random storage consists in assigning a position that is selected randomly (i.e., with equal proba-
bility) from a set of eligible positions. This policy is known to promote high space utilization at the
expense of increased travel distance, and is the method of choice for many of Amazon’s distribution
warehouses of low-volume SKUs (Weidinger, 2018). It also has the additional beneﬁt of simplify-
ing business rules. In a recent work, Ballestín et al. (2020) show how a multistage heuristic can be
used for solving storage and retrieval problems in a random allocation setup, while taking into ac-
count congestion issues. For an evaluation of heuristics and exact methods in random assignment
environments, refer to Petersen (1997).

In a similar fashion, the closest open location policy assigns items to the ﬁrst available location.
The nuance introduced in this method comparatively to the random assignment policy is concen-
trating the products next to the pick-up/drop-oﬀ areas, usually where the pickers start their tasks.
This usually creates an uneven concentration of items next to I/O, which does not happen in the
random assignment policy, except by pure chance.

On the contrary, nonrandomized policies, such as dedicated storage, assign products to ﬁxed lo-
cations. This improves the picker’s space awareness, as they become familiar with positions, while
also improving their performance. However, space utilization is considerably lower, especially if
there are many out-of-stock items. Full-turnover storage is a slight adaptation of dedicated storage,
using the product turnover to assign items to the closest locations, while slow-moving products are
stored in more distant locations. COI is frequently used as the proxy metric to turnover, and the
rule consists of putting the lowest COI items closest to I/O locations (Heskett, 1963, 1964). If sea-
sonality is removed from the equation, full-turnover storage would not diﬀer much from dedicated
storage. However, seasonal trends may cause products to change positions often during the year.
The additional eﬀort required to classify items is also not negligible, although modern information
systems facilitate this process.

Finally, class-based storage divides products into classes according to a Pareto 20/80 distribu-
tion, ensuring that the fast-moving class contains about 20% of the products, but generating over
80% of the turnover. Methods such as ABC or COI-based class storage are common. The ﬁrst
method groups items into A-, B- and C-items, where A-items are the ones that generate about 80%
of the turnover. B-items usually sit on the 80–95% range, and C-items are the remaining ones. The

© 2020 The Authors.
International Transactions in Operational Research © 2020 International Federation of Operational Research Societies

6

M. Amorim-Lopes et al. / Intl. Trans. in Op. Res. 00 (2020) 1–29

particular nature of a warehouse warrants a discussion regarding the metric to use. Turnover may
not fully convey the operational complexity added to picking, since very expensive, but seldom
ordered items, may have high turnover, but do not generate many picking tasks. By occupying pre-
mium locations, they are taking out prime space that could be used instead for fast rotating items.
Therefore, COI or pick volume is often used, as it translates turnover to demand frequency and
picking eﬀort more accurately. Either way, what follows is a discussion on how to position A-, B-
and C-areas in low-level picker-to-part systems. Two possibilities are discussed in Jarvis and Mc-
Dowell (1991). Regardless of the method chosen, the main idea is to bring these positions close to
the depot points to minimize the tour’s length.

Also worth pointing out is a subbranch of class-based storage methods that use the product
family, or any other product properties to group together similar items. This area has evolved sig-
niﬁcantly in recent years, especially with the improvement in data mining methods. Perhaps the
simplest method is to compare the statistical correlation between items, as proposed by Frazele
and Sharp (1989) and applied, for instance, by Liu (1999), where it is shown that it can actually im-
prove the eﬃciency of order picking. Several enhancements have then been proposed. Wutthisirisart
et al. (2015) suggest an item-order relationship, using both order frequency and order size to gen-
erate an allocation algorithm to group together items. Zhang (2016) proposes several methods for
this new branch of research called correlated storage assignment strategies. Two are sum-seed and
static-seed clustering algorithms, and four other methods are sequencing algorithms for ﬁnding
item sets. Following this strand of research, Battini et al. (2015) develop a multinominal proba-
bility model to deﬁne storage assignment policies at the microlevel, and warehouse design rules at
the macrolevel.

2.4. Routing policies

The routing problem a warehouse manager faces inherits most of its properties from the travel-
ing salesman problem, although certain singularities apply. First, congestion may be a problem
(Bahrami et al., 2017), as too many pickers traveling through a corridor may hamper order re-
trieval time. But most importantly, there are thousands of picking locations, and as orders grow
in size, so do the locations to visit. Consequently, exact methods grow exponentially in size, and
are rendered useless as they cannot be solved in an acceptable time frame. For this reason, routing
heuristics are used instead in practice (de Koster et al., 2007). Even though they may not guarantee
optimality, they may generate solutions good enough to be used in practice in a reasonable time.
By running multiple numerical experiments, Petersen (1997) estimates the best heuristic has a 5%
gap from the optimal solution for a large number of instances.

Roodbergen (2001) provides an extensive review of the available heuristics. S-shape or traversal
is one of the simplest and requires the picker operators to traverse the whole aisle in case there is
one pick to be performed in that corridor. This leads to a serpentine-like path, with pickers moving
back and forth along the aisles. In the return method, in contrast, the picker is allowed to make a
U-turn and reverse his way. The midpoint method divides the storage into two, with front and back
positions being accessed in two passes. Hall (1993) has shown that the midpoint method performs
better when the number of picks per aisle is small (i.e., one pick on average), which depends not
only on the size of the warehouse but also on the product assignment policy in use. The largest gap

© 2020 The Authors.
International Transactions in Operational Research © 2020 International Federation of Operational Research Societies

M. Amorim-Lopes et al. / Intl. Trans. in Op. Res. 00 (2020) 1–29

7

policy does not diﬀer much from the midpoint, except that pickers move as far on the aisle as the
largest gap goes, meaning that they may cross the midpoint if required; moreover, and it has been
shown that it always outperforms the midpoint policy (Hall, 1993). Finally, the combined heuristic
uses a mix of S-shape routes and the largest gap.

In a more recent work, Lu et al. (2016) developed a dynamic routing algorithm with an extremely
low running time that continuously reviews the best route and changes accordingly. The model is
able to signiﬁcantly reduce the order completion time.

3. Problem description

Our motivation comes from a distribution warehouse of one of the biggest Iberian nonfood retail-
ers, aiming at improving overall operations eﬃciency, but also at optimizing the space being used,
thus potentially avoiding, or at least delaying, an extra investment to move to a larger warehouse.
This warehouse in particular features over 70,000 SKUs, mainly of sports and fashion goods, dis-
tributed through two diﬀerent areas. In the ﬁrst area, known as “Racks” there are ﬁve-level pallet
racking systems, with ground-level locations being used for picking, and all the above locations
assigned as reserve positions. The aisles may be visited by car only, and they are one way only,
although shortcuts exist. The second area, labeled “Mezzanine,” is used for storing small items in
cases of 50 cm × 50 cm. Picking is done manually, with operators walking around while carrying a
box. Overall, including part- and full-time equivalents, there are around 120 professionals, working
in eight-hour shifts, which is a small part of the 500 people in total who work at the distribution
warehouse, with a signiﬁcant number being assigned to administrative tasks.

Our work will focus on the “Racks” section, which currently features ﬁve diﬀerent zones or
business units (BUs). These zones contain articles ranging from sports footwear, sports clothing
and equipment, nursery and clothing packs of multiple sizes, but also large and unusual formats
such as treadmills. On an average day, the distance traveled by each picker on their cars is around 50
km. Considering that 120 pickers work at the warehouse, the total distance traveled over a period
of 24 hours amounts to 3600 km.

Although the BUs share administrative resources as well as loading and unloading docks, the
picking is actually performed by individual teams, and the orders never cross more than one zone.
In fact, if it were not for the economies of scale gained from sharing administrative resources and
loading docks, each BU could be located on separate warehouses. Order picking is fulﬁlled by a
picking by store policy, meaning that picking orders are not aggregated to increase the quantity
retrieved, except for some products that are picked on a batch and then delivered to an automatic
sorter. Changing the picking policy was outside the scope of this project, and was therefore not
considered, the same being true for the few SKUs picked as a batch and sent to the sorter.

Figure 1 illustrates the “Racks” section, as well as how the ﬁve diﬀerent zones were initially dis-
tributed in the warehouse. Zones S1–S3 store sports department items, while zones F1 and F2 store
fashion items. There are three ﬁxed input/output (I/O) areas that work as drop-oﬀ points. Each
zone has its own exclusive area, and they are not interchangeable. dSD serves zones S1 and S2, dF D
is assigned to zone F1, and ﬁnally zones S3 and F2 use dS as their drop-oﬀ point. Since thousands
of picking tasks are performed each day, the distance traveled within the BU, or inner distance,
may be as critical as the distance traveled back and forth to the drop-oﬀ points, or outer distance.

© 2020 The Authors.
International Transactions in Operational Research © 2020 International Federation of Operational Research Societies

8

M. Amorim-Lopes et al. / Intl. Trans. in Op. Res. 00 (2020) 1–29

Fig. 1. Initial disposition of the ﬁve zones of the “Racks” section in the warehouse.

Finally, the “Reserved” section contains nonconformity items, such as treadmills or dumbbells,
which are seldom ordered, and for which special picking guidelines exist. This section was excluded
from the analysis.

The ﬂow through each corridor is unidirectional and one way only, either north, that is, from
downward to upward, or south, that is, from upward to downward, thus avoiding traﬃc jams
caused by pickers traveling in diﬀerent directions. Nonetheless, there are shortcuts that the pick-
ers may take to cross the corridors without having to take the longest path. The BUs only deﬁne
virtual areas for which a particular set of items is assigned.

The main challenge consisted in increasing productivity and reducing operational costs. Con-
sidering that about 50% of the order-picking time is spent on traveling between picking positions
and drop-oﬀ points (Chan and Chan, 2011), and that no other changes (e.g., adding more drop-oﬀ
points, building a new warehouse, changing the picking strategy, etc.) were to be considered, the
approach would arguably require minimizing the distance traveled, both within the BUs, and from
and to the drop-oﬀ points.

Therefore, the method to be devised for reducing the travel time spent on satisfying orders needs
to address two separate, yet complementary problems: (a) within each BU, what is the best product
assignment policy, that is, the one that minimizes the distance traveled to satisfy the orders placed;
(b) considering that diﬀerent BUs operate on the same warehouse, what is the best layout to accom-
modate the varying stress each BU generates? For the ﬁrst question, we considered experimenting
with diﬀerent storage assignment policies, such as ABC-based, COI-based ABC, or random. With
regard to the second question, the disposition and proximity to drop-oﬀ points of each BU had to
be considered.

Our starting point is slightly diﬀerent from the one usually reported in the literature, where 50%
of the order-picking time is spent on traveling (Chan and Chan, 2011). In our case, we have found
that 32% of the time is spent on traveling, and 68% on picking. If taken at face value, this could
suggest that traveling time is already quite optimized or that picking is fairly ineﬃcient, at least
compared to the literature. In any case, only travel time will be considered as a performance metric
to be improved. Additionally, we only report the work developed on the “Racks” section, without
any loss of generality to the reader, since the methodology was also applied to the “Mezzanine”
section quite similarly.

© 2020 The Authors.
International Transactions in Operational Research © 2020 International Federation of Operational Research Societies

M. Amorim-Lopes et al. / Intl. Trans. in Op. Res. 00 (2020) 1–29

9

4. Methodology

This distribution warehouse serves several business areas with diﬀerent product types and demands,
subject to diﬀerent seasonal cycles and with diﬀerent teams operating independently. Notwith-
standing, the warehouse operates as one single unit with some parts shared by all business areas,
such as the docking stations and marshaling points, and cannot be managed separately. In fact,
sometimes diﬀerent business areas may serve the same retail shop, although operations at the dis-
tribution warehouse are managed separately until the pallets are loaded into a marshaling point,
and then onto a truck. This adds an additional layer of complexity to the problem and requires a
methodology that can decompose the problem at two diﬀerent levels: (a) the BU area or zone level,
considering its layout and storage assignment policy impact on the distance traveled within each
zone; (b) the whole warehouse operation, and the impact of the warehouse layout design on the
distance traveled between BUs and drop-oﬀ points.

Given these requirements, we devised a three-stage methodology called simulation–
optimization–simulation (SOS) that explores both simulation and optimization to improve picking
performance, namely by suggesting changes to the layout or to assignment policies. Considering
the ﬁrst (S), we use a probabilistic model to simulate diﬀerent conﬁgurations for each BU. We con-
sider the disposition (horizontal or vertical positioning), the picking ﬂow, and storage assignment
strategies (closest open position, random, ABC, COI-based ABC). Based on this, we estimate, for
an increasing number of order lines, the time required to fulﬁll orders considering diﬀerent setups
(see column “Avg. inner distance traveled” in Table 3 for an example of the outputs of Stage 1). In
the second phase (O), we feed the best results obtained in the ﬁrst (S) to a mixed integer program-
ming (MIP) model that builds the overall racks area layout by selecting a conﬁguration, for each
BU, in order to minimize the distance traveled at the warehouse level. This includes the distance
that was not considered in the prior stage, such as moving from base to the BU area, and from the
BU to the I/O points. Since some BUs are more solicited than others and put a diﬀerent stress on
the warehouse, the optimizer explores this trade-oﬀ to provide an optimal warehouse layout. As an
output of this stage, we obtain diﬀerent layouts ranked according to the overall distance traveled.
Finally, the third simulation process (S) analyses both randomness and potential operational prob-
lems that had not been considered before, such as traﬃc jams in the corridors that are one way only.
This model is a discrete-event simulation (DES) that replicates real operations of the warehouse,
providing visual guidance while performing sensitivity analysis. Moreover, it simpliﬁes the veriﬁca-
tion and validation of the methodology. We apply this model to the two best layouts obtained in
the previous stage in order to see which one copes better with uncertainty.

Figure 2 illustrates how the SOS methodology is iteratively applied to construct new layouts and
storage assignment policies. The ﬁrst model uses the probabilistic simulation model to evaluate
diﬀerent ﬂows, conﬁgurations, and storage assignment policies for each BU. Since each BU acts
independently from all others, with their own particularities, a one-size-ﬁts-all solution would be
suboptimal. Expected travel distances and order retrieval times are estimated for a set of possible
combinations of layout and storage assignment policies. Next, this information is passed onto the
MIP model. The optimal conﬁguration at the BU level can be suboptimal at the warehouse level,
thus we need to consider the trade-oﬀ between sacriﬁcing individual BU’s performance and max-
imizing the overall warehouse throughput. The optimizer balances the level of importance each
BU puts on the warehouse, and runs accordingly. Finally, the warehouse layout needs to be tested

© 2020 The Authors.
International Transactions in Operational Research © 2020 International Federation of Operational Research Societies

10

M. Amorim-Lopes et al. / Intl. Trans. in Op. Res. 00 (2020) 1–29

Fig. 2. How the SOS methodology can be applied to generate new layouts and storage assignment
policies for a warehouse.

under uncertainty factors—that due to their complexity were not included in the previous steps.
The DES model runs through several weeks’ worth of real data, as well as virtually generated data,
to ensure the suggested warehouse layout and storage assignment policies perform as needed. If
a particular BU disposition is found to be unfeasible or inadequate, we remove it from the list of
available dispositions and run the optimization model again to redo the layouts. This feedback loop
reduces the set of feasible layouts. We detail each of the stages next.

4.1. Notation

For the purpose of introducing our methodology, we start by describing the notation used through-
out the paper. Consider Fig. 3 that depicts a 2D top view of one BU possible storage area. The
layout is divided vertically into corridors and horizontally into levels. We index corridors using
c = {1, . . . , C} from left to right and levels using k = {1, . . . , K} from top to bottom. Each corridor
can only be crossed in one direction, either from top to bottom or otherwise. In the interception
between a corridor and a level, we have an aisle a ∈ {1, . . . , A} which are numbered from left to
right and following the corridor direction. Considering the corridor’s direction, we can deﬁne that
set D comprehending the aisles in corridors crossed from top to bottom, and set I composed of
the aisles in corridors crossed tin at the opposite direction. Each aisle’s length is l and the distance
between the center of two adjacent corridors is e (as depicted in Fig. 3).

4.2. First stage: simulate the business unit

As mentioned before, the warehouse layout is split between several BUs or storage areas, each
having its own independent team of pickers, with orders and teams of operators never crossing more

© 2020 The Authors.
International Transactions in Operational Research © 2020 International Federation of Operational Research Societies

M. Amorim-Lopes et al. / Intl. Trans. in Op. Res. 00 (2020) 1–29

11

Fig. 3. A typical business area containing four levels and six corridors.

than one BU. Consequently, diﬀerent storage assignment policies may coexist within the warehouse,
and thus each BU can be analyzed individually.

Although picking tasks usually start with administrative and processing time, most of the time
is spent on actually traveling between pick locations, and therefore improving picking eﬃciency re-
quires minimizing the total picking time. Since we are leaving changes to the picking policy outside
the scope of analysis, eﬃciency gains have to stem from reducing travel time between picking loca-
tions.

For this purpose, the BU’s layout (i.e., number, size, and orientation of picking aisles) may be
reconﬁgured, but also operating (i.e., sequencing items in the order list) and storage policies (i.e.,
item location in the storage area) may be changed. Changes to the physical disposition of aisles were
outside the scope of the intervention, and the scope of analysis. However, the actual disposition of
the storage area was considered, including the number of aisles and orientation (i.e., whether it
expands horizontally or vertically).

In addition, storage policies were also questioned. We investigate the use of three alternative
storage assignment policies: (a) closet open position, (b) random assignment, and (c) COI-based
ABC categorization. The ﬁrst in case distance correlated highly with order patterns, the last in case
products were ordered randomly, with the beneﬁt of avoiding congestion.

Considering these requirements, we developed a probabilistic simulation model, following the
work of Caron et al. (2000). The model estimates the expected picking time inside each BU based
on the order size (the number of SKUs), storage assignment policy, and BU conﬁguration. The
objective is to estimate the expected picking tour length E[L] associated with a given task t, which
can be written as

E[L] =

A(cid:2)

a=1

E[La],

(1)

© 2020 The Authors.
International Transactions in Operational Research © 2020 International Federation of Operational Research Societies

12

M. Amorim-Lopes et al. / Intl. Trans. in Op. Res. 00 (2020) 1–29

where E[La] is the expected contribution of aisle a to the total tour length. The total time can then
be calculated using

E[time] = E[L]
v

+ nt · pick,

(2)

which adds up the time spent traveling between aisles, assuming pickers travel at an average speed
of v, with the average time spent actually picking up the item (pick) multiplied by the total number
of items nt to be picked to complete the order-picking task t.

Let us suppose that there is an order to pick two items located on aisles a2 and a4 of Fig. 3. Using
Equation (1) we compute the individual contribution of all aisles involved in the tour, which are a1
through a4, plus a5–a8 since the picker has to return to the I/O point. For the remaining ones not
crossed, we ﬂag them with a zero, thus providing a null contribution to the total tour length.

The expected contribution of any aisle depends on two factors: (a) its length and width; and (b)
whether it has to be crossed or not. In the previous example, only aisles a1 through a8 have to be
crossed; therefore, the chances of visiting other aisles are nil. The contribution of each aisle, E[La],
can be computed easily by adding up its length, l, and the distance between corridors, e, or in
mathematical notation (l + e). In the model implementation, these parameters are constant, as all
aisles’ and corridors’ distance is the same. We can generalize this and deﬁne it as follows:

E[La] = (l + e) · p(Sa).

(3)

The complicated part is computing p(Sa), the probability of visiting aisle a, and therefore being
part of the tour. There are only two reasons why aisle a needs to be crossed, and they are mutually
exclusive: at least one item has to be picked from that aisle, which can be represented as Ea; no
items have to be picked from aisle a, despite being part of the route, which we can denote as Va.
In such case, p(Sa) can be expressed as an arithmetic sum of the individual probabilities p(Ea) and
p(Va):

p(Sa) = p(Ea) + p(Va).

(4)

Considering that a given task t has N items to be collected, we can deﬁne the probability of aisle

a containing at least one item to be retrieved as follows:

p(Ea) = 1 − [1 − p(Pa)]N,

(5)

where p(Pa) is the probability that a pick addresses aisle a. With p(Ea) well deﬁned, we now need
to calculate the odds of visiting aisle a even when no items have to be picked, p(Va). We can start
by analyzing the case when the picker does not need to visit other aisles, that is, p(Va) = 0, before
reaching the next picking location. Such case only occurs when there is a direct move between the
current picking position a and the next, a(cid:4). This is more common when the next aisle is positioned
right after the current one (for instance, when an item has to be picked from aisle a3 and then from

© 2020 The Authors.
International Transactions in Operational Research © 2020 International Federation of Operational Research Societies

M. Amorim-Lopes et al. / Intl. Trans. in Op. Res. 00 (2020) 1–29

13

Fig. 4. Illustration of all the instances when a given aisle a needs to be visited on the way to the next picking location
(for aisles belonging to domain D).

aisle a4). We can provide a general expression for calculating the probability of going directly from
aisle a to aisle a(cid:4) without having to perform a picking task in between
(cid:9)

(cid:7)

N−1

p(Ea, Ea(cid:4) ) =

⎧
⎪⎪⎪⎨
⎪⎪⎪⎩

1 −

0,

a(cid:4)−1(cid:8)

j=a+1

p(Pj )

· p(Ea(cid:4) ),

if a < a(cid:4)

otherwise.

(6)

Shortcuts complicate matters further. Consider Fig. 3, where it is clear to see that aisle a7 can be
reached from a2 by taking a shortcut. There are three cases in total that have to be addressed for
calculating p(Va) when the visiting aisle is on an odd corridor (D):

p(Va) = p(Vdd ) + p(Vid ) + p(Vsd ),

∀a ∈ D.

(7)

The ﬁrst case we need to address (Vdd ) is represented in Fig. 4a, and the purpose is to explore the
cases when the next aisle in the corridor, for instance aisle a11, may need to be visited, even though
no picking takes place. If the picker is currently at aisle a10 and the next aisle is a20, he can take a
shortcut and go directly two levels up. The picker has not left domain D (aisles in odd levels). Now
consider that the next item is on aisle a13. Since the corridors are one way only, the picker cannot
take a shortcut, and has to cross aisle a11. In this case, it changes both domain (to I) and level.
After generalizing, we obtain Equation (8). c(cid:4) and k(cid:4) will refer to the corridor and level of the next
aisle to be visited:

(cid:2)

(cid:2)

p(Vdd ) =

p(Em) ·

p(Em, E j ).

(8)

m∈D: m<a
k(cid:4)<k
c=c(cid:4)

j∈D ∧ k(cid:4)>k ∧ c(cid:4)≥c
∨
j∈I ∧ k(cid:4)≥k ∧ c(cid:4)>c

The next case encompasses all instances when the next item to be picked is sitting on a corridor
from domain D on the same level or above, or it is sitting on a corridor from domain I on the same

© 2020 The Authors.
International Transactions in Operational Research © 2020 International Federation of Operational Research Societies

14

M. Amorim-Lopes et al. / Intl. Trans. in Op. Res. 00 (2020) 1–29

level or below (Vid ). Figure 4b illustrates this case. Suppose the picker is currently at aisle a15, and
the picker’s next assignment is at a19. In such case, the next aisle in the corridor, a16, does not need
to be visited, since the operator can take a shortcut, but will have to pass through aisle a18, as this
aisle stands in the way. The same goes if the next item in line is on aisle a23 or any level below, in
which case the picker also crosses aisle a18. In any other case, the picker does not have to go through
this aisle. The following Equation (9) generalizes these cases:

p(Vid ) =

(cid:2)

m∈I: m<a
k(cid:4)≤k
c(cid:4)=c−1

(cid:2)

p(Em) ·

p(Em, E j ).

j∈D ∧ k(cid:4)>k ∧ c=c(cid:4)
∨
j∈I ∧ k(cid:4)≥k ∧ c(cid:4)=c+1

(9)

Finally, we need to address the case when the picking task has just started, and the picker leaves
from the I/O location (Vsd ). Such case is illustrated in Fig. 4c. If the picker has to retrieve an item
from aisle a3 or from aisle a7, he must visit aisle a2 as well. This occurs when the next item is on
the same corridor, c, but one or more levels above (k(cid:4) > k), or when it is on the same level or above
(k(cid:4) ≥ k) but on the next corridor (c(cid:4) = c + 1). Generalizing, we obtain Equation (10):

(cid:2)

p(Vsd ) =

p(E0, E j ).

j∈I ∧ k(cid:4)≥k ∧ c(cid:4)=c+1
∨
j∈D ∧ k(cid:4)>k ∧ c=c(cid:4)

(10)

These three options cover all possible cases that imply crossing aisle a on the way to the next
pick when the picker is currently on an aisle in the set D. We can now compute the probabilities of
visiting aisles on domain I in a similar fashion. First, the probability of visiting aisle a on the way
to the next picking position is generically given by

p(Va) = p(Vii) + p(Vdi) + p(Vie),

∀a ∈ I.

(11)

Figure 5 illustrates the three cases when a given aisle a needs to be visited on the way to the next

picking location, and the starting position is on an even corridor (I).

In the ﬁrst case (Vii), depicted in Fig. 5a, the picker has to visit aisle a6 on the way to the next
picking location, situated in the same corridor, but on a level below, or when it is in the next cor-
ridor, also on a level below. We cover these instances using the following expression, which is an
adaptation of Equation (8):

p(Vii) =

(cid:2)

m∈I: m<a
k(cid:4)>k
c=c(cid:4)

(cid:2)

p(Em) ·

p(Em, E j ).

j∈D ∧ k(cid:4)≤k ∧ c(cid:4)>c
∨
j∈I ∧ k(cid:4)<k ∧ c(cid:4)≥c

(12)

The second instance (Vdi), represented in Fig. 5b, covers the case when the current corridor is a
direct corridor. As the illustration shows, if an operator is currently at aisle a15 and wants to reach
an aisle on the next corridor, and on a level below (k(cid:4) ≤ k) or two corridors away on the same level

© 2020 The Authors.
International Transactions in Operational Research © 2020 International Federation of Operational Research Societies

M. Amorim-Lopes et al. / Intl. Trans. in Op. Res. 00 (2020) 1–29

15

Fig. 5. Illustration of all the instances when a given aisle a needs to be visited on the way to the next picking location for
aisles belonging to set I.

or lower level, then the operator has to cross aisle a18 on its way to the next aisle. We can generalize
this using the following expression:
(cid:2)

(cid:2)

(13)

p(Vdi) =

p(Em)

m∈D: m<a
k(cid:4)≥k
c(cid:4)=c−1

j∈D ∧ k(cid:4)≤k ∧ c(cid:4)=c+1
∨
j∈I ∧ k(cid:4)<k ∧ c=c(cid:4)

p(Em, E j ).

Finally, we adapt Equation (10) to cover the cases when an aisle a needs to be visited and the
task is about to ﬁnish, which is represented in Fig. 5c (a24 is the last aisle). Suppose the operator is
currently next to aisle a19 or next to the adjacent aisle, in this case aisle a22. Hence, the operator has
to go through aisle a23 to complete the task. In general, this happens when the last pick was on a
D-aisle on the same or an higher level, or when it is in the same corridor and also on a higher level.
The following expression translates these cases:

(cid:2)

p(Vie) =

p(E j, E0).

j∈D ∧ k(cid:4)≥k ∧ c(cid:4)=c−1
∨
j∈I ∧ k(cid:4)>k ∧ c=c(cid:4)

(14)

4.3. Second stage: optimizing the warehouse layout

As mentioned before, the warehouse comprises diﬀerent BUs that operate separately, each having
its own team of pickers and serving separate orders. For each BU, we have considered two levers for
adjusting picking performance in terms of inner distance traveled: inner zone layouts (horizontal
and vertical) and product assignment policies (ABC, COI-based ABC, random, etc.). The simula-
tion model was helpful for obtaining key performance metrics for each BU, but each BU puts a
diﬀerent stress on the overall warehouse operations. Some BUs receive more orders than others,
and the size of the teams also varies. Intuitively, it makes sense to privilege BUs more critical to

© 2020 The Authors.
International Transactions in Operational Research © 2020 International Federation of Operational Research Societies

16

M. Amorim-Lopes et al. / Intl. Trans. in Op. Res. 00 (2020) 1–29

operations, when compared to those that put a lower burden on the operations, and bring them
closer to I/O points, as movements back and forth drop-oﬀ points constitute a signiﬁcant share of
the travel time.

However, given the size of the warehouse, the possible combination of inner zone layouts and
product assignment policies, and the number of BUs currently operating, the problem easily grows
exponential in complexity. Back-of-the-envelope calculations are therefore pointless, with the prob-
lem requiring a more structured approach. In this sense, we developed an MIP model that tries to
optimize the entire warehouse layout. It selects the best trade-oﬀ between minimizing the inner
distance traveled inside each BU and the outer distance traveled to reach the I/O points. Obvi-
ously, this depends on the expected number of picking tasks each BU has, concerning the goal of
minimizing the total travel distance of all the order pickers within the warehouse.

, yend
z

, ystart
z

z

z

) and (xend

To introduce our MIP model, let (xstart

) denote the input and output point
coordinates for each BU indexed by z = {1, . . . , Z} and let T (n)z be the expected total number of
tasks having size n for BU z in the planning horizon. For each of these BU, the ﬁrst-stage simulation
model deﬁnes a set of possible conﬁgurations denoted by Fz. A conﬁguration f can be described
by the following parameters: h f the height in aisles, l f the length in aisles, D(n)in
f the expected
inner distance of a task of size n, the expected entering (x(n)start
), and exiting position
(x(n)end
) of a task of size n measured from the center of the upper left aisle of the layout.
These conﬁgurations can also be grouped into two disjoint sets: (a) whose ﬁrst aisle is a direct aisle
(F D) and (b) the ones with an indirect aisle as the ﬁrst (F I ).

, y(n)start

, y(n)end

f

f

f

f

To deﬁne an optimal layout for the warehouse, we introduce the binary placement decision vari-
ables Wf a that are equal to 1 if the upper left aisle of conﬁguration f is to be placed at aisle a, 0
otherwise. We also introduce the assignment decision variables Z f a that are equal to 1 if the aisle
a is assigned to conﬁguration f , 0 otherwise. To correctly estimate the outer traveled distance, we
ﬁrst need to obtain the ﬁnal entering and exiting position considering the arranged warehouse lay-
out. To do so, let X (n)start
be auxiliary variables that capture the
expected entering and exiting position of a task of size n of BU z having into account the proposed
layout. The outer distance traveled is then calculated by estimating the Euclidean distance between
the entering and exiting point of the BU and its I/O point. Since the order pickers are unable to
walk freely due to the aisle layout, this distance can be estimated by the sum of the diﬀerences
in the x- and y-axis of the entering and existing points to the I/O of the BU. Decision variables
Dx(n)start
are introduced
z
to capture the distance between the I/O and the entering (superscript start) and existing (super-
script end) points. The complete MIP model reads as follows:

, and Y (n)end

, Dx(n)start

, Dy(n)start

, Dy(n)start

, Dx(n)end

, Dx(n)end

, Dy(n)end

, Dy(n)end

, Y (n)start

, X (n)end

z

z

z

z

z

z

z

z

z

z

z

min

+

+

(cid:2)

z,n
(cid:2)

z,n
(cid:2)

z,n

T (n)z · (Dx(n)start

z

+ Dx(n)start

z

+ Dy(n)start

z

+ Dy(n)start

z

)

T (n)z · (Dx(n)end

z

+ Dx(n)end

z

+ Dy(n)end

z

+ Dy(n)end

z

)

T (n)z ·

(cid:2)

z, f ∈Fz,a

D(n)in
f

· Wf a

(15)

© 2020 The Authors.
International Transactions in Operational Research © 2020 International Federation of Operational Research Societies

s.t.

(cid:2)

f ∈Fz, a
(cid:2)

M. Amorim-Lopes et al. / Intl. Trans. in Op. Res. 00 (2020) 1–29

Wf a = 1 ∀ z

Z f a(cid:4) ≤ K · C · Wf a ∀ f , a

a(cid:4): k(cid:4)∈{1,...,K}
c(cid:4)∈{1,...,c−1}
(cid:2)

a(cid:4): k(cid:4)∈{1,...,k−1}
c(cid:4)∈{c,...,C}
(cid:2)

Z f a(cid:4) ≤ K · C · Wf a ∀ f , a

Z f a(cid:4) ≤ K · C · Wf a ∀ f , a

a(cid:4): k(cid:4)∈{k+h f ,...,K}
c(cid:4)∈{c,...,C}
(cid:2)

Z f a(cid:4) ≤ K · C · Wf a ∀ f , a

a(cid:4): k(cid:4)∈{k,...,K}
c(cid:4)∈{c+l f ,...,C}
(cid:2)

Z f a(cid:4) ≥ h f · l f ·

a(cid:4)
(cid:2)

f

Z f a ≤ 1 ∀ a

(cid:2)

a

Wf a ∀ f

(cid:2)

(cid:10)

X (n)start
z

=

(xa + x(n)start

f

) · Wf a

∀ z, n

(cid:11)

Y (n)start
z

=

X (n)end

z

=

Y (n)end

z

=

f ∈Fz, a
(cid:2)

(cid:10)

(ya + y(n)start

f

) · Wf a

∀ z, n

(cid:11)

f ∈Fz, a
(cid:10)
(cid:2)

(xa + x(n)end

f

) · Wf a

∀ z, n

(cid:11)

f ∈Fz, a
(cid:2)

(cid:10)

f ∈Fz, a

(ya + y(n)end

f

) · Wf a

∀ z, n

(cid:11)

Dx(n)start

z

− Dx(n)start

z

= xstart
z

− X (n)start

z

∀ z, n

Dy(n)start

z

− Dy(n)start

z

= ystart
z

− Y (n)start

z

∀ z, n

Dx(n)end

z

− Dx(n)end

z

= xend
z

− X (n)end

z

∀ z, n

Dy(n)end

z

− Dy(n)end

z

= yend
z

− Y (n)end

z

∀ z, n

X, Y, Dx, Dy, Dx, Dy ≥ 0, W, Z ∈ {0, 1}.

17

(16)

(17)

(18)

(19)

(20)

(21)

(22)

(23)

(24)

(25)

(26)

(27)

(28)

(29)

(30)

(31)

© 2020 The Authors.
International Transactions in Operational Research © 2020 International Federation of Operational Research Societies

18

M. Amorim-Lopes et al. / Intl. Trans. in Op. Res. 00 (2020) 1–29

The objective function (15) aims at minimizing the total expected traveled distance at the ware-
house level, presenting the sum of three terms: the outer distance traveled from the input point to
the start of the BU area, the outer distance traveled from the end of the BU area to the output point
and the inner distance traveled, respectively. Hence, the total expected traveled distance results from
multiplying then total expected tour length (sum of outer and inner distances) of each order size,
at each BU, by the number of expected tasks having such size. Constraints (16) ensure that exactly
one conﬁguration is selected for each BU from the potential candidates. The link between the BU
conﬁguration placement and the aisle assignment is guaranteed by constraints (17)–(20). The ﬁrst
two sets of constraints ensure that no aisle to the left (constraints (17)), nor above (constraints(18))
the upper left aisle selected, is assigned to the conﬁguration. Similarly, the following two sets of con-
straints replicate the same logic to the right (constraints (20)) and bottom (constraints (19)), but
having into account the size of the conﬁguration. Constraints (21) ensure that the number of aisles
assigned to the BU follow the selected conﬁguration size and constraints (22), avoiding overlap be-
tween diﬀerent BUs by not allowing the same aisle to be assigned to two diﬀerent conﬁgurations.
Constraints (23)–(26) calculate the coordinates of the expected entering and existing points for each
BU depending on the task size. Finally, the constraint sets (27)–(30) estimate the outer traveled dis-
tance. Both constraints (27) and (28) estimate the outer distance in the x- and y-axis until the order
picker enters the BU area, while constraints (29) and (30) estimate the distance traveled in these two
axis after the order picker leaves the BU area. Note that two distinct variable sets are introduced to
deﬁne positive (e.g., Dx(n)start
) diﬀerences between the input/output
point and the entering/existing of the BU area.

) and negative (e.g., Dx(n)start

z

z

4.4. Third stage: simulate the warehouse operation

The ﬁrst stage dealt with the simulation at the BU level, generating estimates for the expected dis-
tance to be traveled when fulﬁlling an order for each possible conﬁguration. In a second stage, the
optimizer tries to combine all the possible conﬁgurations of inner layouts and product assignment
policies for the diﬀerent BUs, using the estimates obtained previously as inputs. This step is neces-
sary since optimal solutions at the BU level may not generate optimal layouts at the warehouse level.
Some BUs receive more orders than others, leading to diﬀerent levels of stress to the warehouse op-
erations. The optimizer takes into consideration this trade-oﬀ between sacriﬁcing eﬃciency at the
unit level but improving the overall result when generating a layout.

The third stage consists of a fully ﬂedged discrete-event model that simulates actual picking
orders in the layout suggested by the optimizer. The simulation model replicates the warehouse
put-away and picking activities as close to reality as possible. There are pickers driving picking cars
with speeds adjusted to match recorded speeds that fulﬁll orders in the exact same sequence as in
real life. When completed or when the car is full, they drop the items at the assigned drop-oﬀ point,
which may be a marshaling area or an automated belt. When the order is complete the operators
return to I/O and are ready to fulﬁll another order. Otherwise, they go back to the BU and pick
the missing items until the order is completed.

Three main activities had to be implemented in the DES model in order to reproduce the pick-
ing operations at the warehouse, along with other routine and setup operations, including drawing
the layout or loading the SKUs from the database. The ﬁrst activity concerns the logic behind

© 2020 The Authors.
International Transactions in Operational Research © 2020 International Federation of Operational Research Societies

M. Amorim-Lopes et al. / Intl. Trans. in Op. Res. 00 (2020) 1–29

19

Fig. 6. State chart containing the order-picking sequence of steps.

Fig. 7. State chart implementing the logic for creating picking routes.

order-picking tasks. The state chart depicted in Fig. 6 captures the steps necessary to successfully
complete an order-picking task. The process is considerably simple since the complexity rests on
sequencing the items to pick, which depends on the picking policy. Since the picking policy cur-
rently in place is not to be changed, the item list is retrieved directly from the information system’s
database. Hence, picking the items is a matter of moving the operator between picking locations
until all items are retrieved from the order.

Ordering the items to be picked also requires devising a logical mechanism to guide the virtual
operators, which we represent in Fig. 7. Since pickers follow S-shaped routes, the items can be
ordered from the front to the rear of the BU according to the direction of the aisles, starting at the
closest location to the I/O location. The task stops if either all items in the order are included in the
item list or if picker capacity has been surpassed, in which case a new task will have to be created.
Finally, items arriving at the unloading docks need to be stored away. As it currently stands, items
are assigned to the ﬁrst available location. However, class-based storage has been introduced, and
the state chart also takes into account that aspect. In case a picking location is already assigned,
the newly arrived items go to reserve locations, which stand in positions above the ground level, in
order to meet internal replenishment orders.

With all the logic in place, the DES starts by loading all the items and assigning them the exact
same locations as in the real warehouse. Model parameters are deﬁned at start up, and are listed
in Table 1. Parameters regarding average picking time and average speed were manually derived
from direct observation and measurement. Tasks are then initiated until all work for the day is
completed, while simultaneously, items arriving through the unloading docks are put away. The
model is then used to experiment with diﬀerent inner layouts and storage assignment policies.

BUs are assigned in the warehouse, including orientation and direction of picking ﬂows (corri-
dors are one way only). The simulator then reproduces all the orders received within a time frame
of several months and benchmarks it against the current layout. To do so, it assigns tasks to pickers
following exactly the same rules used in the real warehouse, and tracks the distance traveled. In
this stage, we can capture the impact of potential operational problems, such as traﬃc jams in the
corridors. This is critical to guarantee a smooth operation, and may indeed require changes to the
unit-level conﬁguration, to the warehouse layout or to both, in a manual feedback process.

© 2020 The Authors.
International Transactions in Operational Research © 2020 International Federation of Operational Research Societies

20

M. Amorim-Lopes et al. / Intl. Trans. in Op. Res. 00 (2020) 1–29

Table 1
Parameters and variables used in the discrete-event simulation model

Input

Characteristics

Frequency

Value

Storage assignment

Class of products that should go to

Startup

First free position, ABC

each aisle

Relevant characteristics of each

Startup

Dimensions, weight, category,

policy
Products

Drop point
Average speed
Picking time

product

Place where the picking tasks end
Speed at which each picker travels
Time to retrieve an item from a

position

Number of pickers
Initial stock
SKUs received

Quantity of order pickers
SKUs and initial stored quantity
SKUs that were stored on a given

day

Startup
Startup
Startup

Startup
Startup
Daily

type, etc.
dSD, dF D, dS
3 km/h
0.75–2.5 seconds

120
70k SKUs
10–400

Orders

SKU and quantities ordered by each

Daily

300–1000 orders, 11k–30k units

client

Finally, we study demand variability by simulating the warehouse operations for over 50 days of
24/7 work. The time period the data report to was chosen to be as variable as possible, including
both periods of low activity (weekends), but also periods of extreme activity (one Black Friday).
During these 50 days, the number of picks processed in the warehouse was 20.000, on average and
on a daily basis, while the number of tasks was approximately 670 per day. However, there were
peaks of 34.000 boxes and 1.091 tasks, almost twice the average processing throughput. In the
same period, there were also slow days with 2.339 boxes collected and 100 tasks per days.

5. Results and discussion

In this section, we ﬁrst validate the probabilistic simulation model and the DES based on a data
sample composed of the real picking operations. Next, we show the application of the SOS method-
ology and identify the potential gains obtained using our suggested warehouse layout and storage
assignment policies.

5.1. Model validation

Each step of the SOS method was validated independently, comparing simulated and actual data.
Real data are very accurate, since picking operators wear a headset that connects to a voice picking
system that informs the picker on the next position to visit, tracking every movement until the
task is completed. The system is also used by management to obtain labor productivity metrics,
including distance traveled and total time to complete a task.

For the probabilistic simulation model, we compared the expected time to complete a task by
varying the number of picking operations. To do so, the model was run with several parameters,
including number of groups of aisles and levels, aisle length, distance between groups of aisles,

© 2020 The Authors.
International Transactions in Operational Research © 2020 International Federation of Operational Research Societies

M. Amorim-Lopes et al. / Intl. Trans. in Op. Res. 00 (2020) 1–29

21

Fig. 8. Simulated versus actual data of the expected time to complete a task, depending on the number
of picking operations.

average picker speed, and average picking time, all in accordance to the real warehouse setup. The
size of the task (i.e., the number of items to pick) is then changed iteratively, and the expected time
is compared with an average of the real order retrieval times.

Figure 8a presents the actual data against the times predicted by the probabilistic model. Using
a standard measure to estimate the disparity between real and simulated values such as the mean
absolute percentage error (MAPE), we can get an idea of how the model fares in estimating the
time required to complete a picking order. In this particular case, MAPE is about 15.75%.

This average deviation may be explained by the fact that, in real life, picker cars may stop work-
ing, congestion occurs (we have not considered congestion in this model), pickers may let items
drop to the ﬂoor, and so on. These delays could very well explain why the probabilistic model
slightly undershoots the expected time to complete a task for orders up to 40–50 items. For larger
orders, the model is more pessimistic. Visual inspection suggests that sometimes pickers cross aisles
walking, particularly if the items to be picked are close to the end and to the beginning of the aisles,
respectively. After a large number of picks such time diﬀerence accrues, reducing the picking time.
The DES model was validated using two diﬀerent, but complementary strategies, typically used
in simulation: veriﬁcation and validation. First, we ensure that the model represents accurately the
business processes in place in the warehouse, and that all relevant activities are executed as intended
and match the speciﬁcations. For instance, we simulate one single agent fulﬁlling an order to verify
if the proper sequence is followed; all the items are picked; and whether the items are dropped at
the right drop point. This is performed for all the simulated operational activities of the warehouse.
Validation, on the other hand, determines the degree to which the simulation model and the
data are an accurate representation of actual operations at the warehouse. In this sense, we validate
the simulator by reproducing 50 straight days of real, nonrandomly generated tasks on the current
warehouse layout, and compare those with the real statistics collected by the warehouse IT system.
In Fig. 8b, we present one month of accumulated time for completing all the tasks in BU S2, which
contains sports footwear, against the simulated time in the DES model. The MAPE is about 12.6%.

© 2020 The Authors.
International Transactions in Operational Research © 2020 International Federation of Operational Research Societies

22

M. Amorim-Lopes et al. / Intl. Trans. in Op. Res. 00 (2020) 1–29

Table 2
Real and simulated times for 50 straight days of work in ﬁve diﬀerent business units

Business unit

Real time (minutes)

Simulated time (minutes)

WMAPE (%)

F1
F2
S1
S2
S3

Total

93,811
123,886
43,673
199,148
155,439
615,957

91,333
126,247
41,746
183,343
142,312
584,982

12.3
14.0
20.2
12.6
12.3
13.2

The S2 area is the most demanding BU of the warehouse, as it deals with a considerable number
of SKUs and picking orders. Nevertheless, other BUs also put stress on the warehouse operations.
Table 2 provides an account of both real and simulated times for all BUs, as well as the deviation.
The average weighted MAPE (WMAPE) is approximately 13.2%. The worst result obtained, 20.2%,
represents a small BU that corresponds to approximately 7% of the warehouse picking time, and
consists of picking very large items that are often diﬃcult to place in the picking car.

5.2. Application of the SOS methodology

As a starting point, the probabilistic simulation model was to be used to generate the expected travel
distance and order-picking time for all combinations of ﬂows, layout conﬁgurations, and storage
assignment policies (random, ABC, ABC COI-based, etc.). However, preliminary results showed
that the COI-based ABC storage assignment policy Pareto-dominates all other policies, concerning
all BUs. A detailed analysis of the data—after a data mining classiﬁcation method—showed that
a lot of items are frequently ordered together, and that seasonality is also a strong factor at play.
These are strong points in favor of a nonrandom storage assignment policy, and more so toward a
class-based policy, such as COI-based ABC.

Although this result cannot be generalized to all warehouses, it can be used to signiﬁcantly re-
duce the number of combinations that need to be generated, thus reducing the solution space sig-
niﬁcantly, as only combinations of ﬂow and layout disposition need now to be generated. Figure 9
shows the comparison between COI-based ABC and random assignment for one BU (same re-
sults apply to all others), the policy currently in place, with signiﬁcant savings in terms of order
retrieval time. For picking tasks containing between 10 and 30 items, up to 25% in time savings can
be obtained using a COI-based ABC storage assignment policy. There is no task size for which a
COI-based policy performs worse, so COI-based ABC is Pareto-dominant in the case under study.
Considering this, we have then generated all feasible combinations of ﬂows and layout, which
will lead to an optimal solution. For each BU, we have tried diﬀerent feasible—not all BUs may
be rotated, since the warehouse is rectangular—layout dispositions. We also experimented with
diﬀerent ﬂows, including whether the operator enters the BU downward (N) or upward (S). This is
required since the corridors are one way only, and therefore operators can only circulate downward
and upward throughout the corridors, but it is possible to deﬁne the starting point of the path,
forcing the person to start from the bottom or from the topmost position. For instance, a ﬂow
“S-N” means that the operator enters the BU from the position closest to the South, and therefore

© 2020 The Authors.
International Transactions in Operational Research © 2020 International Federation of Operational Research Societies

M. Amorim-Lopes et al. / Intl. Trans. in Op. Res. 00 (2020) 1–29

23

Fig. 9. Expected time to complete a task for one BU changing the storage assignment policy.

Fig. 10. Optimal layout that minimizes the total distance traveled, including inner distance (inside each BU) and outer
distance (from and to I/O points).

moves upward; and that he or she leaves the BU from the uppermost position, moving upward.
Finally, we have selected a task size for each BU that best represents the typical order-picking task
by calculating a yearly average. Table 3 lists all the combinations that were simulated using the
probabilistic model, and subsequently used as inputs in the MIP model.

Ideally, the best solution would be for each individual BU to be selected. However, such combi-
nation may not be feasible, as all BUs have to ﬁt inside the current space available at the warehouse,
causing a 2D packing problem. Moreover, the outer distance is also a strong factor at play (the
most signiﬁcant in this particular case, indeed), and therefore not all BUs may stay close to the
I/O points. At that point, the MIP model that equates these trade-oﬀs, and gives the optimal so-
lution considering all constraints. It also takes into account the distance between each BU and the
drop-oﬀ points, as well as the stress each BU puts on the warehouse. Figure 10 provides a graphical
overview of the prescribed layout for our case study.

© 2020 The Authors.
International Transactions in Operational Research © 2020 International Federation of Operational Research Societies

24

M. Amorim-Lopes et al. / Intl. Trans. in Op. Res. 00 (2020) 1–29

Table 3
Results obtained by running the probabilistic simulation model on a set of possible combinations

Business
unit
S1∗
S1+
S1
S1
S2+
S2
S2
S2∗
S3+
S3
S3
S3
S3
S3∗
F1+
F1
F1
F1
F1∗
F1
F2
F2+
F2
F2
F2∗
F2

Conﬁguration
(levels vs. corridors)

Flow
(in, out)

Avg. task
size

Avg. inner distance
traveled (m)

3 × 2
3 × 2
2 × 3
2 × 3
11 × 2
11 × 2
7 × 3
7 × 3
8 × 2
8 × 2
16 × 1
16 × 1
6 × 3
6 × 3
9 × 1
9 × 1
5 × 2
5 × 2
3 × 3
3 × 3
12 × 1
12 × 1
6 × 2
6 × 2
4 × 3
4 × 3

S–N
N–S
S–S
N–N
N–S
S–N
S–N
N–S
S–S
N–N
S–S
N–N
S–S
N–N
N–S
S–N
N–S
S–N
N–S
S–N
S–S
N–N
S–S
N–N
S–S
N–N

28
28
28
28
80
80
80
80
70
70
70
70
70
70
26
26
26
26
26
26
22
22
22
22
22
22

349.5
280.2
308.3
464.9
783.1
839.8
911.8
798.9
542.6
574.7
506.0
496.3
616.4
717.5
285.6
306.5
346.8
395.5
373.2
474.8
267.5
263.8
321.5
333.7
370.4
420.9

Note: The current layout dispositions are marked with a +. The layout selected in the ﬁnal optimized warehouse layout is marked
with a ∗.

As expected, the optimizer proceeded by favoring BUs that put a higher stress on the warehouse
(i.e., more tasks per day), moving them closer to the I/O points. In fact, all the inner layouts chosen
by the optimizer perform worse in terms of average inner distance traveled when compared with
the current conﬁguration (cf. Table 3), but signiﬁcantly better in terms of outer distance. Overall,
the vertical layout improves overall performance (i.e., traveling time and picking time) by 5.6%,
reducing traveling time by 18.8%. Although the impact in terms of traveling time is signiﬁcant, its
contribution to the total order-picking time is considerably smaller than the time spent picking up
the items. Table 4 presents the results for each BU. With the exception of F1, for which no gains
were obtained, all other BUs present signiﬁcant gains in terms of traveling time.

However, more gains can be expected from also changing the storage assignment policy. Using
again the DES model, we have tested the new layout conﬁguration that the optimizer provided
along with a COI-based ABC policy, and the improvement in terms of expected time of travel
is slightly bigger. Table 4 shows the results obtained for each BU and for the whole warehouse
operation in terms of time traveled and picking time. Figure 11 provides a heat map generated

© 2020 The Authors.
International Transactions in Operational Research © 2020 International Federation of Operational Research Societies

M. Amorim-Lopes et al. / Intl. Trans. in Op. Res. 00 (2020) 1–29

25

Table 4
Impact of the change to the layout disposition of the warehouse

Traveling time (minutes)
Current Alternative (cid:2)

Picking time (minutes)

Total

(cid:2) (%) Current Alternative (cid:2)

(cid:2) (%) Current Alternative (cid:2)

(cid:2) (%)

Horizontal layout with COI-based ABC storage assignment

S1
S2
S3
F1
F2

112
1284
913
403
764

104
970
815
403
529

8
314
98
0
235

7
24
11
0
31

663
2216
1407
1452
1556

Total 3476

2822

654

18.8

7293

663
2217
1406
1452
1555

7293

Vertical layout with COI-based ABC storage assignment

S1
S2
S3
F1
F2

112
1284
913
403
764

100
939
582
403
515

12
345
330
0
249

11
27
36
0
33

663
2216
1407
1452
1556

Total 3476

2539

937

26.9

7294

663
2216
1407
1452
1555

7294

0
−1
1
0
1

0
0
0
0
0

775
3501
2319
1803
2319

767
3187
2221
1856
2084

8
314
98

1
9
4
−53 −3
10
235

0.6 0

10,718

10,114

603

5.6

0
0
0
0
1

1

0
0
0
0
0

0

775
3501
2319
1856
2319

10,718

763
3156
1990
1856
2070

9835

8
345
330
0
249

883

2
10
14
0
11

8.2

Note: Although the vertical layout provides gains (approx. 2.6 percentage points over the horizontal (original) disposition), it
requires a signiﬁcant eﬀort and operations downtime).

Fig. 11. A heatmap emphasizing aisles that were frequently and seldom visited (the darker the tone, the more visits). A
COI-based ABC storage assignment policy concentrates picking on the region closest to the I/O point.

using the current storage assignment policy and simulated using a COI-based ABC policy for one
of the BUs. As one can observe, a class-based storage policy concentrates frequently ordered items
on the same space, which can be stored closer to the drop-oﬀ points. This reduces both the inner
distance traveled, as C-items are less frequently picked, but also the outer distance, since pickers do
not need to cross the whole BU and can leave anytime.

According to the results obtained, up to 26.9% can be gained in terms of traveling time from
implementing a vertical layout along with a COI-based ABC storage assignment policy. Except for
BU F1, for which there are no discernible improvements in the time traveled (similar to the previous
case), all other BUs show strong gains in terms of picking performance. Its impact on the overall

© 2020 The Authors.
International Transactions in Operational Research © 2020 International Federation of Operational Research Societies

26

M. Amorim-Lopes et al. / Intl. Trans. in Op. Res. 00 (2020) 1–29

operation is mitigated by the fact that traveling only accounts for 32% of the total order-picking
time. As such, 68% of the time is spent on picking up the items and putting them in the car. Hence,
the overall improvement is about 8.2%, which is still signiﬁcant.

The SOS methodology allowed testing each of the changes, and involving the decision maker in
the process by also providing a DES model where real-life operations can be tested. In fact, this
has shown to be very important in earning the stakeholder’s conﬁdence. The case study illustrated
its application in practice, and the results obtained show that it is a great tool to experiment new
warehouse policies without having to disrupt operations.

6. Managerial insights

The SOS framework was the result of a consultancy-based research project that took place at one
of the largest sports and fashion Iberian retailers. In addition to providing a real-case problem in
which to test the model, the project was also a source of real data for validation. The distribution
warehouse in which it was tested deals with over 70,000 SKUs, ﬁve diﬀerent and independent BUs,
and performs approximately 1000 picking tasks per day, amounting to thousands of picking lines.
Although the two scenarios that were presented to the steering committee originated savings,
one required a sizeable downtime in the operations to be implemented. In the ﬁrst scenario, the
savings were estimated to be of around 5.6%, and required only the change of the assignment
storage policy to a COI-based ABC. In the second scenario, which could lead to potential savings
of 8.2%, it required a complete redeﬁnition of the macro layout, which meant a downtime period
of several weeks. These savings can also be converted into FTEs—which did not imply downsizing
the workforce, in the particular case of this retailer, but rather a reallocation to other activities. The
ﬁrst scenario allowed for a reduction of 2.1 FTEs, while the second scenario could lead to savings
equivalent to 3.1 FTEs.

Overall, the savings in terms of traveling time are much higher (18.8% for the ﬁrst scenario and
26.9% for the second), but crossing picking locations amounts to no more than 32% of the total
order-picking time in this warehouse, with the remaining time being spent on actually picking up
the items. In fact, our results deviate considerably from the values reported in the literature, which
typically report traveling as taking over 50% of the time Tompkins et al. (2010). If this were the
case, the savings would be much higher.

As a result of this work, one of the ﬁrst actions adopted by the warehouse managers was to
implement the heat map, which provided them with a simple tool to measure the picking density
over the warehouse and identify potential traﬃc jams. Most signiﬁcantly, the ﬁrm went through
with the COI-based ABC policy in the largest BU the one containing the footwear and the results
gave conﬁdence to the managers for scaling-up COI-based ABC to all BUs. Figure 12 illustrates
actual results of the implementation of the COI-based ABC policy.

The second scenario, however, was put on hold until the next warehouse overhaul takes places,
and this carries important lessons in terms of change management. Despite the promising results
arising from the COI-based ABC storage assignment policy with the vertical layout, changing the
actual layout of the warehouse meant bringing it to a full halt, in order to move the goods around
and reorganize the pallet racking system. This downtime would incur in heavy costs to the organi-
zation, and a potential hit on the service level to the stores. When fully accounting for the beneﬁts

© 2020 The Authors.
International Transactions in Operational Research © 2020 International Federation of Operational Research Societies

M. Amorim-Lopes et al. / Intl. Trans. in Op. Res. 00 (2020) 1–29

27

Fig. 12. Heat map of the footwear business unit before and after the implementation of the COI-based ABC storage
assignment policy.

and the costs, the ﬁrm decided to wait for an opportunity to shut down the warehouse, and then
proceed with the layout change.

7. Conclusion

Warehouse managers face many decisions, including the layout, policies related to storage assign-
ment and picking, zoning, and also routing. When multiple BUs exist inside the same warehouse,
decision makers face two levels of optimization, and hence an optimal solution at the lower, BU
level may be suboptimal at the warehouse level. In such cases, an integrated approach to warehouse
design and planning is advisable.

Considering this, our work proposes a novel SOS framework that provides insights at both micro-
and the macrolevel, eﬀectively assisting the decision maker in the planning of the warehouse. The
three stages work as follows: ﬁrst, a probabilistic simulation model estimates travel time inside each
BU for diﬀerent layouts; second, an optimization model uses the outputs of the probabilistic model
for building the 2D packing layout, that is, combining the diﬀerent BUs in order to minimize the
travel distance of the overall operation; ﬁnally, a DES model is used to subject the new layout to a
stochastic demand, observing whether the proposed conﬁguration can cope with uncertainty. The
SOS methodology can be used to guide the process of the warehouse design at the micro- and the
macrolevel, even when no empirical data exists to estimate traveling time (one can use our ﬁrst
probabilistic simulation model to extrapolate times).

Although the policy levers considered only enacted changes to the conﬁguration of each BU and
to storage assignment policies, the SOS framework also makes it possible to test diﬀerent picking
and routing policies, requiring only slight changes to the DES model. For instance, the warehouse
currently operates on a pick-by-store policy, but aggregated picking could also be put to the test
using the simulator. This last stage is also useful for submitting the warehouse to diﬀerent stressing
conditions, including restocks and orders arriving at a random, stochastic order. This sensitivity
analysis is crucial for ﬁnding an optimal layout that has an additional slack to cope with an array

© 2020 The Authors.
International Transactions in Operational Research © 2020 International Federation of Operational Research Societies

28

M. Amorim-Lopes et al. / Intl. Trans. in Op. Res. 00 (2020) 1–29

of unanticipated situations. Finally, the DES model was very helpful for visually mapping solutions,
thus helping decision makers understand the proposed changes and observe their impact.

As future work, changes to picking policies could also be pondered and incorporated in SOS. For
instance, aggregate picking could be adopted instead of a pick-by-store policy. Such option would
require, however, a place for sorting out the items through the diﬀerent orders. The automatic sorter
cannot be used for all items, so it would have to be a manual process, so far excluded. Two-level
picking could also be considered. The four positions of the racks other than the ground level are
used for reserve locations, but the ﬁrst one could be assigned also for picking. Such option could
reduce signiﬁcantly the picking times, especially if frequently ordered times are grouped together.
However, there are strong ergonomic restrictions to this option, since not all pickers have the height
to reach higher levels, and some could actually injure themselves doing so. Either way, the SOS is
extendable at any point, and can be used to study further enhancements to the warehouse.

References

Bahrami, B., Aghezzaf, E.H., Limere, V., 2017. Using simulation to analyze picker blocking in manual order picking

systems. Procedia Manufacturing 11, 1798–1808.

Ballestín, F., Pérez, Á., Quintanilla, S., 2020. A multistage heuristic for storage and retrieval problems in a warehouse

with random storage. International Transactions in Operational Research 27, 3, 1699–1728.

Bartholdi, J.J., Hackman, S.T., 2011. Warehouse & Distribution Science. School of Industrial and Systems Engineering,

Georgia Institute of Technology, Atlanta, GA.

Battini, D., Calzavara, M., Persona, A., Sgarbossa, F., 2015. Order picking system design: the storage assignment and
travel distance estimation (SA&TDE) joint method. International Journal of Production Research 53, 4, 1077–1093.
Caron, F., Marchet, G., Perego, A., 2000. Optimal layout in low-level picker-to-part systems. International Journal of

Production Research 38, 1, 101–117.

Chan, F.T.S., Chan, H.K., 2011. Improving the productivity of order picking of a manual-pick and multi-level rack
distribution warehouse through the implementation of class-based storage. Expert Systems with Applications 38, 3,
2686–2700.

Chen, T.L., Cheng, C.Y., Chen, Y.Y., Chan, L.K., 2015. An eﬃcient hybrid algorithm for integrated order batching,

sequencing and routing problem. International Journal of Production Economics 159, 158–167.

Davarzani, H., Norrman, A., 2015. Toward a relevant agenda for warehousing research: literature review and practition-

ers’ input. Logistics Research 8, 1, 1.

de Koster, R., 2008. Warehouse assessment in a single tour. In Lahmar, M. (ed.) Facility Logistics. Approaches and

Solutions to Next Generation Challenges. Auerbach: New York, pp. 39–60.

de Koster, R., Le-Duc, T., Roodbergen, K.J., 2007. Design and control of warehouse order picking: a literature review.

European Journal of Operational Research 182, 2, 481–501.

de Koster, R.B.M., Johnson, A.L., Roy, D., 2017. Warehouse design and management. International Journal of Production

Research 55, 21, 6327–6330.

ELA/AT Kearney, 2004. Diﬀerentiation for performance. Excellence in Logistics 2004. ELA, Brussels.
Frazele, E.A., Sharp, G.P., 1989. Correlated assignment strategy can improve any order-picking operation. Industrial

Engineering 21, 4, 33–37.

Grosse, E.H., Glock, C.H., Neumann, W.P., 2017. Human factors in order picking: a content analysis of the literature.

International Journal of Production Research 55, 5, 1260–1276.

Gu, J., Goetschalckx, M., McGinnis, L.F., 2007. Research on warehouse operation: a comprehensive review. European

Journal of Operational Research 177, 1, 1–21.

Hall, R.W., 1993. Distance approximations for routing manual pickers in a warehouse. IIE Transactions 25, 4, 76–87.
Heskett, J.L., 1963. Cube-per-order index—a key to warehouse stock location. Transportation and Distribution Manage-

ment 3, 1, 27–31.

© 2020 The Authors.
International Transactions in Operational Research © 2020 International Federation of Operational Research Societies

M. Amorim-Lopes et al. / Intl. Trans. in Op. Res. 00 (2020) 1–29

29

Heskett, J.L., 1964. Putting the cube-per-order index to work in warehouse layout. Transportation and Distribution Man-

agement 4, 8, 23–30.

Horta, M., Coelho, F., Relvas, S., 2016. Layout design modelling for a real world just-in-time warehouse. Computers &

Industrial Engineering 101, 1–9.

Jarvis, J.M., McDowell, E.D., 1991. Optimal product layout in an order picking warehouse. IIE Transactions 23, 1, 93–

102.

Larson, T.N., March, H., Kusik, A., 1997. A heuristic approach to warehouse layout with class-based storage. IIE Trans-

actions 29, 4, 337–348.

Liu, C.M., 1999. Clustering techniques for stock location and order-picking in a distribution center. Computers & Oper-

ations Research 26, 10, 989–1002.

Lu, W., McFarlane, D., Giannikas, V., Zhang, Q., 2016. An algorithm for dynamic order-picking in warehouse operations.

European Journal of Operational Research 248, 1, 107–122.

Mansuri, M., 1997. Cycle-time computation, and dedicated storage assignment, for As/R systems. Computers & Indus-

trial Engineering 33, 1, 307–310.

Öztürko˘glu, Ö., 2020. A bi-objective mathematical model for product allocation in block stacking warehouses. Interna-

tional Transactions in Operational Research 27, 4, 2184–2210.

Petersen, C.G., 1997. An evaluation of order picking routing policies. International Journal of Operations & Production

Management 17, 11, 1098–1111.

Petersen, C.G., 2002. Considerations in order picking zone conﬁguration. International Journal of Operations & Produc-

tion Management 22, 7, 793–805.

Roodbergen, K.J., 2001. Layout and routing methods for warehouses. PhD thesis, Erasmus University Rotterdam, Rot-

terdam.

Rushton, A., Croucher, P., Baker, P., 2014. The Handbook of Logistics and Distribution Management: Understanding the

Supply Chain. Kogan Page, London.

Sprock, T., Murrenhoﬀ, A., McGinnis, L.F., 2017. A hierarchical approach to warehouse design. International Journal of

Production Research 55, 21, 6331–6343.

Tompkins, J., White, J., Bozer, Y., Tanchoco, J., 2010. Facilities Planning. Wiley, Hoboken, NJ.
van den Berg, J.P., Sharp, G.P., Gademann, A., Pochet, Y., 1998. Forward-reserve allocation in a warehouse with unit-load

replenishments. European Journal of Operational Research 111, 1, 98–113.

van Gils, T., Ramaekers, K., Braekers, K., Depaire, B., Caris, A., 2018a. Increasing order picking eﬃciency by integrating
storage, batching, zone picking, and routing policy decisions. International Journal of Production Economics 197,
243–261.

van Gils, T., Ramaekers, K., Caris, A., de Koster, R.B., 2018b. Designing eﬃcient order picking systems by combining
planning problems: state-of-the-art classiﬁcation and review. European Journal of Operational Research 267, 1, 1–15.
Weidinger, F., 2018. Picker routing in rectangular mixed shelves warehouses. Computers & Operations Research 95, 139–

150.

Wutthisirisart, P., Noble, J.S., Chang, C.A., 2015. A two-phased heuristic for relation-based item location. Computers &

Industrial Engineering 82, 94–102.

Zhang, Y., 2016. Correlated storage assignment strategy to reduce travel distance in order picking. IFAC-PapersOnLine

49, 2, 30–35.

© 2020 The Authors.
International Transactions in Operational Research © 2020 International Federation of Operational Research Societies

View publication stats

