# FAQ

### 

## General

### Can I add questions and answers to this document?

**Yes!** If there are questions and answers you think should be added here please do.  This is a wiki and you're welcome to [register for an account](http://onosproject.org/register/) and start editing.

### What does "ONOS" stand for?

ONOS stands for "Open Network Operating System". We realize it's a bit confusing, considering ON.Lab stands for "Open *Networking* Laboratory"!

### Which platforms and Java versions does ONOS support?

We currently actively support Ubuntu, CentOS, and OS X. ONOS works with Oracle Java 1.8, but OpenJDK should work as well.

### When will ONOS do X/support Y?

Please check our [Jira](http://jira.onosproject.org) to see what's in progress. If what you are looking for isn't there, you can always help by contributing!

### How can I contribute to ONOS?

Thank you for your interest! The [Contributor Guide](guides/contributor-guide.md) should give you the details of what's involved.

### Where can I find ONOS documentation, tutorials and sample code?

You can find the latest documentation on the [ONOS Documentation homepage](guides.md). The tutorials and sample code can be found in [Tutorials](tutorials.md).

### How can I get help with ONOS?

You're already off to a good start by reading this FAQ! First make sure you've read the FAQ and documentation on this wiki. Then you should check the archives for the [mailing lists](community-information/mailing-lists.md) (particularly `onos-discuss`) to see if someone else has run into a similar issue or has a similar question. If you still have questions, consider posting to `onos-discuss` or slack. Also, you may be able to find people within your organization who can help you with ONOS.

## ONOS Wiki

### I renamed a page, and now I get sent to a redirection page when I follow the old URL!

Confluence generates URLs based on a page's name, so renaming it changes its URL. Sadly, Confluence doesn't do automatic redirects from the old URLmbut luckily it automatically updates the links *within* the wiki, so you don't have to worry about links within the wiki breaking.

For linking to a page from emails, blogs, etc., Confluence **recommends using a page's shortened URL**, which remains stable across name changes. **Press "k" on any page to bring up its shortened URL**.

Why should I used shortened URLs for links to this wiki from external sites?

As noted above, **Confluence just isn't as smart as other wiki software** and it doesn't automatically redirect links to pages whose names have changed!!

Iff you used a shortened URL, then the link will continue to work even after the page is renamed.

Although shortened URLs aren't as easy to read, they are shorter and can be easier to type than lengthy paths based on page titles.

### How do I get a shortened URL for a wiki page?

Go to the **Tools dropdown** and select**Link to this Page...**. A window should pop up with both a regular and a shortened URL. For example, for this page:

* regular URL: [https://wiki.onosproject.org/display/ONOS/FAQ](https://wiki.onosproject.org/display/ONOS/FAQs)
* shortened URL: <https://wiki.onosproject.org/x/TQAQ>.

Of course, the result is more dramatic and useful for pages with longer names.

### I can't delete my page!

Currently, pages can only be deleted by ONOS wiki administrators. For the time being, you can move your page under the [Trashbin](../trashbin-9832277.md) and then drop a line in the [#onos-docs](https://onosproject.slack.com/messages/onos-docs) channel or [onos-discuss](https://groups.google.com/a/onosproject.org/forum/#!forum/onos-discuss) to have your page removed.

### How do I change a page's location?

Drag it to a new location using **[Browse>Space Operations>Pages>Tree View](https://wiki.onosproject.org/pages/listpages-dirview.action?key=ONOS)**.

## Troubleshooting

### What is the default username/password for the ONOS GUI/CLI?

The default username/password is `karaf`/`karaf`.

### Why do I see "Service not found" when running CLI commands?

This usually means ONOS did not start up properly, so the ONOS services are not available even though the CLI commands are loaded. Try looking in the ONOS log for exceptions or errors that may indicate why ONOS did not start up.

### **Why are flows stuck in PENDING\_ADD state?**

Please first read the [Flow Rule Subsystem](guides/architecture-and-internals-guide/flow-rule-subsystem.md) page to understand how flows are managed in ONOS. The reason flows are stuck in PENDING\_ADD state is because ONOS is unable to confirm that the flow is present on the dataplane.

If you are using OpenFlow, the provider periodically sends FLOW\_STATS\_REQUEST messages to the device and expects FLOW\_STATS\_REPLY messages in return. One possible reason for flows being in PENDING\_ADD state is the device doesn’t properly support sending FLOW\_STATS\_REPLY messages doesn’t send the right information in the FLOW\_STATS\_REPLY.

Another possible reason could be that ONOS simply can’t match the flows in the FLOW\_STATS\_REPLY with the state in the flow store. The OpenFlow provider uses the FlowModBuilder to map ONOS constructs to OpenFlow, and the FlowEntryBuilder to map OpenFlow constructs back to ONOS constructs. Often flows being stuck in PENDING\_ADD means that these mappings are not properly symmetric, i.e. the FlowEntryBuilder doesn’t map the flow stats to the same FlowRule object that was installed. This could be because a new criterion/instruction was added, or a bug in the existing mappings.

### Why does ONOS periodically reinstall flows that are already installed?

This is generally a different symptom of the same problem as above (flows stuck in PENDING\_ADD). If ONOS can’t match the returned flow stats with flow rules in the store, it will remove what it considers to be an extraneous flow and install the flow in the store again. The solution to this problem is to ensure that ONOS can match observed flows with its internal flow store.

### Why do I see extra hosts in the CLI or GUI?

ONOS' dynamic host discovery works by observing packets sent by hosts on the dataplane that come up to the controller (e.g. OpenFlow devices send packets to the controller by using packet-ins). It looks at the source MAC address of the packets and creates host entries for these MAC addresses. In some situations, packets may be observed by ONOS that are not sent by real hosts in the network. In particular, when using Mininet to emulate a network, sometimes extra hosts will be observed apart from the real hosts in the Mininet network. This is simply an artifact of the way Mininet uses Linux to create networks - it is creating interfaces in Linux which the OS is sending packets out of, and these packets are observed by ONOS and appear as hosts. It is usually safe to simply ignore the extra hosts.

### Where can I find the ONOS log?

The ONOS log is located on disk at `<KARAF_ROOT>/data/log/karaf.log` (e.g. this usually means it can be found at `/opt/onos/karaf/data/log/karaf.log`).

If you run ONOS locally using `onos-karaf` you can use the tool `onos-local-log` to follow the log.

If you run ONOS remotely using `onos-install`, you can use the tool `onos-log <instance>` (e.g. `onos-log $OC1`) to follow the log.

If you are using `onos.py`, the log is also linked to `/tmp/onos1/log` (replace `onos1` with the name of the ONOS instance whose log you wish to view)

If you are running multi instance onos cluster, you can fetch log files from all instances by `onos-fetch-logs --cell.`

You can also view the ONOS log in the ONOS/karaf console by using commands such as `log:display`.

### How can I tell if ONOS encountered an error at runtime?

Often errors can be found in the log if something goes wrong. You can either find the log file on disk and look in there (see above question) or from the ONOS shell you can view the log using `log:display`.

`log:exception-display` will show the last exception in the log.

`log:display | grep ERROR` will show any errors in the log.
