# ONOS Application Permissions

|  |  |  |  |
| --- | --- | --- | --- |
| **TYPE** | **Description** | **SERVICES** | **APIs** |
| **APP\_READ** | Permission to read various information about installed applications | Application Service | getApplication(s)  getState  getId  getPermissions |
| Core Service | version  getAppId(s)  getIdGenerator |
| **APP\_WRITE** | Permission to register new application | Core Service | registerApplication |
| **APP\_EVENT** | Permission to receive application lifecycle events | Application Service | addListener  removeListener |
| **CONFIG\_READ** | Permission to read configuration properties | Component Config Service | getComponentNames  getProperties |
| Network Config Service | getSubjectClasees  getSubjectFactory  getConfigClass  getSubjects  getConfig |
| **CONFIG\_WRITE** | Permission to write configuration properties | Component Config Service | registerProperties  unregisterProperties  setProperty  unsetProperty  preSetProperty |
| Network Config Service | addConfig  applyConfig  removeConfig |
| **CODEC\_READ** | Permission to read codec information | Codec Service | getCodec(s) |
| **CODEC\_WRITE** | Permission to add/remove entityclass from codecs | Codec Service | registerCodec  unregisterCodec |
| **CLOCK\_WRITE** | Permission to write clock properties | Logical Clock Service | getTimestamp |
| **CLUSTER\_READ** | Permission to read cluster information | Cluster Service | getLocalNode  getNode(s)  getState  getLastUpdated |
| Cluster Metadata Service | getClusterMetadata  getLocalNode |
| MastershipTermService | getMastershipTerm |
| Leadership Service | getLeader  getLeadership  ownedTopics  getLeaderboard  getCandidates |
| Mastership Service | getLocalRole  getMasterFor  getNodesFor  getDevicesOf |
| **CLUSTER\_WRITE** | Permission to modify the cluster | Leadership Service | runForLeadership  withdraw |
| Mastership Service | requestRoleFor  relinquishMastership |
| **CLUSTER\_EVENT** | Permission receive cluster events | Cluster Service | addListener  removeListener |
| Leadership Service | addListener  removeListener |
| Mastership Service | addListener  removeListener |
| **DEVICE\_READ** | Permission to read device information | Device Service | getDeviceCount  getDevices  getAvailableDevices  getDevice  getRole  getPort(s)  getPortStatistics  isAvailable  getPortdeltaStatistics |
| Device Clock Service | isTimestampAvailable  getTimestamp |
| **DEVICE\_EVENT** | Permission receive device events | Device Service | addListener  removeListener |
| **DRIVER\_READ** | Permission to get driver instances | Driver Service | getDriver(s) |
| **DRIVER\_WRITE** | Permission to create a new driver handler | Driver Service | createHandler |
| **DEVICE\_KEY\_READ** | Permission to read device key | Device Key Service | getDeviceKey(s) |
| **EVENT\_READ** | Permission to read event properties | Event Delivery Service | getDispatchTimeLimit |
| **EVENT\_WRITE** | Permission to write event properties | Event Delivery Service | setDispatchTimeLimit |
| **FLOWRULE\_READ** | Permission to read flow rule information | Flow Rule Service | getFlowRuleCount  getFlowEntries  getFlowRulesById  getFlowRulesByGroupId  getFlowTableStatistics |
| **FLOWRULE\_WRITE** | Permission to add/remove flow rules | Flow Rule Service | applyFlowRules  removeFlowRules  removeFlowRulesById  apply |
| FlowObjectiveService | filter  forward  next  allocateNextId  initPolicy |
| **FLOWRULE\_EVENT** | Permission receive flow rule events | Flow Rule Service | addListener  removeListener |
| **GROUP\_READ** | Permission to read group information | Group Service | getGroup(s) |
| **GROUP\_WRITE** | Permission to modify groups | Group Service | addGroup  addBucketsToGroup  removeBucketsFromGroup  removeGroup |
| **GROUP\_EVENT** | Permission to receive group events |  | addListener  removeListener |
| **HOST\_READ** | Permission to read host information | Host Service | getHostCount  getHosts  getHost  getHostByVlan  getHostsByMac  getHostsByIP  getConnectedHosts  getAddressBindings  getAddressBindingsForPort |
| Host Clock Service | getTimestemp |
| **HOST\_WRITE** | Permission to modify host | Host Service | requestMac |
| **HOST\_EVENT** | Permission receive host events | Host Service | startMonitoringIp  stopMonitoringIp  addListener  removeListener |
| **INTENT\_READ** | Permission to read intent information | Intent Service | getIntent(s)  getIntentCount  getIntentState  getInstallableIntents  isLocal  getPending  getIntentData |
| Intent Extention Service | getCompilers |
| Intent Partition Service | isMine  getLeader |
| Partition Service | isMine  getLeader |
| Intent Clock Service | getTimestamp |
| **INTENT\_WRITE** | Permission to add/remove intents | Intent Service | submit  withdraw  purge |
| Intent Extention Service | registerCompiler  unregisterCompiler |
| **INTENT\_EVENT** | Permission receive intent events | Intent Service | addListener  removeListener |
| Intent Partition Service | adListener  removeListener |
| **LINK\_READ** | Permission to read link information | Link Service | getLinkCount  getLink(s)  getActiveLinks  getDeviceLinks  getDeviceEgressLinks  getEgressLinks  getDeviceIngressLinks  getIngressLinks |
| Link Resource Service | getAllocation(s)  getAvailableResources |
| Label Resource Service | isDevicePoolFull  isGlobalPoolFull  getFreeNumOfDevicePool  getFreeNumOfGlobalPool  getDeviceLabelResourcePool  getGlobalLabelResourcePool |
| **LINK\_WRITE** | Permission to modify link information | Link Resource Service | requestResources  releaseResources  updateResources |
| Label Resource Service | applyFromDevicePool  applyFromGlobalPool  releaseToDevicePool  releaseToGlobalPool |
| **LINK\_EVENT** | Permission receive link events | Link Service | addListener  removeListener |
| Link Resource Service | addListener  removeListener |
| Label Resource Service | addListener  removeListener |
| ****MUTE**X\_WRITE** | Permission to execute mutex task | Mutex Excusion Service | execute |
| **PACKET\_READ** | Permission to read packet information | Packet Context | time  inPacket  outPacket  treatmentBuilder  isHandled |
| Packet Service | requestPackets  getProcessors  cancelPackets  getRequests |
| ProxyArpService | isKnown |
| **PACKET\_WRITE** | Permission to send/block packet | Packet Context | send  block |
| Packet Service | emit |
| ProxyArpService | reply  forward  handlePacket |
| Edge Port Service | emitPacket |
| **PACKET\_EVENT** | Permission to handle packet events | Packet Service | addProcessor  removeProcessor |
| **PARTITION\_READ** | Permission to read partition information | Partition Service | getNumberOfPartitions  getConfiguredMembers  getActiveMembersNumbers  getAllPartitionIds  getDistributedPrimitiveCreator |
| **PARTITION\_EVENT** | Permission to handle partition events | Partition Service | addListener  removeListener |
| **PERSISTENCE\_WRITE** | Permission to create persistent builder | Persistence Service | persistentSetBuilder  persistentMapBuilder |
| **REGION\_READ** | Permission to read region information | Region Service | getRegion(s)  getRegionForDevice(s) |
| **RESOURCE\_READ** | Permission to read resource information | Resource Service | getResourceAllocations  getAvailableResources  getAvailableResourceValues  getRegisterdResources  isAvailalble |
| **RESOURCE\_WRITE** | Permission to allocate/release resource | Resource Service | allocate  release |
| **RESOURCE\_EVENT** | Permission to handle resource events | Resource Service | addListener  removeListener |
| **STATISTIC\_READ** | Permission to access flow statistic information | Statistic Service | load  max  min  highesthitter |
| Flow Statistics Service | loadSummary  loadAllByType  loadTopnByType |
| **TOPOLOGY\_READ** | Permission to read path and topology information | Path Service | getPaths  getDisjointPaths |
| Topology Service | currentTopology  isLatest  getGraph  getCluster(s)  getClusterDevices  getClusterLinks  getPaths  isInfrastructure  isBroadcastPoint  getDisjointPaths |
| Edge Port Service | isEdgePoint  getEdgePoints |
| **TOPOLOGY\_EVENT** | Permission to handle topology events | Topology Service | addListener  removeListener |
| **TUNNEL\_READ** | Permission to read tunnel information | Tunnel Service | getTunnelCount  getTunnel(s) |
| **TUNNEL\_WRITE** | Permission to create tunnels | Tunnel Service | requestTunnel |
| **TUNNEL\_EVENT** | Permission to receive tunnel events | Tunnel Service | addListener  removeListener |
| **UI\_READ** | Permission to read UI information | Ui Extension Service | getExtentions  getViewExtention |
| **UI\_WRITE** | Permission to create/remove UI service | Ui Extension Service | register  unregister |
| **STORAGE\_WRITE** | Permission to create stores | Storage Service | eventuallyConsistentMapBuilder  consistentMapBuilder  setBuilder  atomicCounterBuilder  queueBuilder  atomicValueBuilder  leaderElectorBuilder |
