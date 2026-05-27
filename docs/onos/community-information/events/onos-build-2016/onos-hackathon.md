# ONOS Hackathon

## **ORGANIZER**: [Ali Al-Shabibi](https://www.linkedin.com/in/alialshabibi) (ON.Lab) - ali AT onlab DOT us

## **SCHEDULE**: Thursday Nov 3 (14:00 - 23:00) and Friday Nov 4 (11:00 - 15:30)

## **LOCATION**: **Room C**

## **REGISTRATION**: [onosproject.org/hackathon](http://onosproject.org/hackathon)

---

### What is the ONOS Hackathon?

The ONOS Hackathon at ONOS Build 2016 will be an event spanning the length of the conference where participants will develop a new feature into ONOS. The new feature could be as simple as a new small application on ONOS or a new subsystem within ONOS.

### **What is the goal of the hackathon?**

The idea is to encourage developers to build new applications or new features into ONOS and continue collaborating with them long after the event. 

### How will the hackathon be run?

Each team will be composed of *at least two people* and up to a *maximum of four people*. Each team will be led by a Team Captain and will come with an idea of what to build for ONOS. We will also propose some ideas for those teams that lack some inspiration ;). Teams will build their feature over the duration of the event and then teams will be expected to present their work to the conference during the closing session. All participants of the conference will vote for the best projects.

### Who can participate (ie. what basic technical expertise do you need)?

Anyone can participate. Of course, if you are interested in networking technology and can write code, that's even better but the hackathon is definitely not limited to coders. It is up to the Team Captain to select and build his/her team, so if the Team Captain decides that he needs a circus juggler or salsa dancer on his team to get the work done and win the top prize, then that's totally fine!

### What is a Team Captain?

Eachteam is led by a Team Captain who is responsible for forming his/her team and overseeing his/her team's project from the beginning of the Hackathon until the very end. The Team Captain is also responsible for reaching unanimous agreement with his/her team on how to share their prize should his/her team win a prize.

### What is the maximum number of participants per team?

Each team should be composed at least 2 people and up to 4 people. 

### What are the prizes ?

The tentative prizes are: 

1st prize: $1,500 USD\*

2nd prize: $500 USD\*

3rd prize: Customised ONOS polo shirt for each team member

### How can I register for the hackathon?

To register, please follow this link: [onosproject.org/hackathon](http://onosproject.org/hackathon)

### Hackathon Teams

| Team Name | Project Idea | Team Members |
| --- | --- | --- |
| **Schnappi!** | Want to make using ONOS even easier? Want to make ONOS even more secure? Then I want YOU to join this team. We will create an ONOS snap with Snapcraft (<http://snapcraft.io/>), put it in an actual app store, and if we're really a crack team we'll also design and implement new snapd interfaces for IPC in/out of ONOS! | * Loïc Minier (Team Captain) * Viswanath Kumar Skand Priya * Maybe YOU! |
| **YANG** | As part of YANG Hackathon we are planning to do the following.  1)      YANG tools integration in BUCK.  2)      Adapting Device and Link subsystem’s interface using YANG (NBI)  3)      Adapting flow objective behavior to configure the device using YANG (SBI) | * Vinod Kumar S. (Team Captain) * Fetia Bannour |
| **PCE** | PCE Calendering - Extensions needed to the Path Computation Element (PCE) communication Protocol (PCEP), so as to enable Labeled switched Path (LSP) scheduling for path computation and LSP setup/deletion based on the actual network resource usage duration of a traffic service in a centralized network environment. A scheduled LSP can be setup at its starting time and deleted after its usage duration such that LSPs for the other traffic services can take over these network resources beyond that period | * Satish Karunanithi (Team Captain) * Vinod Selvaraj |
| **Love CORDing** | A network monitor feature in ONOS which could check the latency between any two switches. | * Jian-Hao Chen (Team Captain) * Tim Chen |
| **Roll the Control** | We want to enable the provision of an intent through a domain, so that ONOS is able to communicate with other sub-domains e.g., vendor-specific controller (ACINO and GEANT use cases), SDN domains (ICONA use case).   We would provide an extension of the Intent Framework to produce, as a compilation result, a high-level description of the policy to be applied in the network (i.e., intent), so that ONOS provides not only the installation of flowrule-specific and flowobjective-specific intent, but also the installation of "intent-specific intent". The flowrule-specific and flowobjective-specific intent are installed by generating multiple requests for each device. At the contrary, the intent-specific intent is installed as a single request for the entire domain.   An alternative strategy is to leverage on the tunnel subsystems and to carry out failure discovery of the tunnels outside the ONOS core.   If the TST vision is aligned with the former solution and willing to adopt it within the ONOS core, we would definitely prefer to develop that one. Otherwise, the second solution would be preferable, since it can be implemented within an application/provider, thus avoiding any consistency issue with future releases of the code base. | * Michele Santuari * Andreas Papazois * Thomas Szyrkowiec * Francesco Lucrezia |
| **LISP SBI** | Locator/Identifier Separation Protocol (LISP) is "map-and-encapsulate" protocol which is developed by IETF LISP working group. The underlying idea of LISP is to separate two IP roles which are routing locator and identifiers in two different spaces. During the hackathon, we are planning to realize LISP SBI support in a way to make ONOS to handle Map-Register message from egress tunnel router, and acknowledge with Map-Notify message. We also consider to handle Map-Request message from ingress tunnel router, and reply with Map-Reply message. With those features, we can fully manage the mapping information of LISP tunnel router from ONOS controller. | * Jian Li (Team Captain) * Chi Dung PHUNG * Matthieu Coudron |

(\*) 1st and 2nd prizes will be in the form of Amazon gift vouchers
