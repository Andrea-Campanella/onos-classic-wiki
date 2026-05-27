# Interface changes

**OpenFlowSwitch** Expand source

```
public interface OpenFlowSwitch {


	....
 
	/**
	 * Send FlowRule to the driver.
	 *
	 * @param flowRule the FlowRule to be sent
	 */
	public void sendFlowRule(FlowRule flowRule);


	/**
	 * Send a FlowRule list to the driver.
	 *
	 * @param flowRules a list of FlowRule to be sent
	 */
	public void sendFlowRules(List<FlowRule> flowRules);

	....
}
```

**FlowRule** Expand source

```
public interface FlowRule extends BatchOperationTarget {
	
	/**
 	* The FlowRule type is used to determine in which table the flow rule
 	* needs to be put for multi-table support switch.
 	* For single table switch, Default is used.
 	*/
	public static enum FlowRuleType {
    	/* Default type - used in flow rule for single table switch */
    	Default,
    	/* Used in flow entry for IP table */
    	IP,
    	/* Used in flow entry for MPLS table */
    	MPLS,
    	/* Used in flow entry for ACL table */
    	ACL
	}
 
    ......
 
	/**
	 * Returns the flow rule type.
	 *
	 * @return flow rule type
 	*/
	FlowRuleType type();
 
	.......
 
}
```
