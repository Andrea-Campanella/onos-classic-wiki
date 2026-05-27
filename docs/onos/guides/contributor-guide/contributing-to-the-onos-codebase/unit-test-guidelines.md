# Unit Test Guidelines

Unit tests for ONOS are built using the [JUnit](http://junit.org/) framework, version 4.12. Unit tests are used to verify correctness of implementations and are run as part of every full build of ONOS. The nightly SonarQube build runs all of the unit tests and produces coverage data that can be seen [here](https://sonar.onosproject.org/).

# How to Write Good Tests

Unit tests should be as short, fast, and reliable as they can be.  Every developer on the project will be running your tests, they should be easy to run and produce accurate results. Here are some key ways to write tests that are not brittle:

* Avoid using sleep() whenever possible, since it often leads to brittle tests.  If you find that you have to wait for an event or wait for some work to be done by another thread, prefer latches or thread notifications to sleeps.
* Try to keep individual tests small, and only test one thing per test.
* Use mocking when you need to include a complicated service to satisfy dependencies. ONOS uses the [EasyMock framework](http://easymock.org/), version 3.4.
* Bazel may choose to run multiple tests in the same Java virtual machine.  If you use static variables in classes, be sure to reset them to known starting values before each test runs.
* Do not use local resources like files, ports, or IP Addresses in tests.

# Basic Tests

If you add a class, consider adding the following basic tests for it first:

## Use EqualsTester for equality and string conversion tests

Any class that defines equals(), hashCode(), or toString() must test these methods.  The [Google Guava EqualsTester](http://guava-libraries.googlecode.com/svn-history/r144/trunk/javadoc/com/google/common/testing/EqualsTester.html) class provides full coverage for these methods:

**Using EqualsTester**

```
final FlowId flowId1 = FlowId.valueOf(1);
final FlowId sameAsFlowId1 = FlowId.valueOf(1);
final FlowId flowId2 = FlowId.valueOf(2);


/**
* Checks the operation of equals(), hashCode() and toString() methods.
*/
@Test
public void testEquals() {
   new EqualsTester()
      .addEqualityGroup(flowId1, sameAsFlowId1)
      .addEqualityGroup(flowId2)
      .testEquals();
}
```

## Testing immutable classes and utility classes

Utility test methods are provided to check that classes are properly defined immutable classes, immutable base classes or utility classes.  Using these methods will assure that other developers don't make changes to your classes that violate your assumptions.

### Immutable Classes

**Immutable Class Check**

```
import static org.onlab.junit.ImmutableClassChecker.assertThatClassIsImmutable;
 
/**
  * Checks that the FlowId class is immutable.
  */
@Test
public void testImmutability() {
    assertThatClassIsImmutable(FlowId.class);
}
```

### Immutable Base Classes

**Immutable Base Class Check**

```
import static org.onlab.junit.ImmutableClassChecker.assertThatClassIsImmutableBaseClass;
 
/**
  * Checks that the DefaultFlowRule class is immutable but can be inherited
  * from.
  */
@Test
public void testImmutability() {
    assertThatClassIsImmutableBaseClass(DefaultFlowRule.class);
}
```

### Utility Classes

**Utility Class Check**

```
import static org.onlab.junit.UtilityClassChecker.assertThatClassIsUtility;
 
/**
  * Check that the Criteria class is a valid utility class.
  */
@Test
public void testCriteriaUtility() {
    assertThatClassIsUtility(Criteria.class);
}
```

## Construction and Retrieval Tests

A basic test for each one of your constructors and a check for the values returned by data access methods should always be included.

**Constructor and Accessor Check**

```
    /**
     * Checks the construction of a FlowId object.
     */
    @Test
    public void testConstruction() {
        final long flowIdValue = 7777L;
        final FlowId flowId = FlowId.valueOf(flowIdValue);
        assertThat(flowId, is(notNullValue()));
        assertThat(flowId.value(), is(flowIdValue));
    }
```

## Referencing Private Data

Sometimes when writing a test, you'll need to access data from a class that does not have a public API to access the data.  In ONOS, we try to not add interfaces only used by test code.  Instead, we have utility methods that use the Java reflection API to access this private data. In this example, the test verifies that the contents of the private `intentsByLink`  member are correct using the `TestUtils.getField()` method to access the member.

**Accessing Private Data in a Test**

```
import org.onlab.junit.TestUtils;
 
    @Test
    public void testLeaderEvents() throws Exception {
        final ObjectiveTracker tracker = new ObjectiveTracker();

        final SetMultimap<LinkKey, IntentId> intentsByLink =
                TestUtils.getField(tracker, "intentsByLink");
        assertThat(intentsByLink.size(), is(0));
    }
```

# Mocking

Mocking is a useful strategy for limiting the interaction between your code under test and other modules that are required to satisfy dependencies.  There are several strategies that may be used for mocking, two that are used inside of ONOS are described here.

## EasyMock Mocking Framework

[EasyMock](http://easymock.org/) allows a test to create a mocked object directly from an interface, without having to define a class and mock every method defined by the API.  The test writer can define only the methods that are required to execute the test. In this example, a mock is created for the HostService API which is passed in to the HostToHostIntentCompiler class.

**EasyMock Example**

```
import static org.easymock.EasyMock.*;
 
    private HostService mockHostService;
 
    private static final String HOST_ONE_MAC = "00:00:00:00:00:01";
    private static final String HOST_TWO_MAC = "00:00:00:00:00:02";
    private static final String HOST_ONE_VLAN = "-1";
    private static final String HOST_TWO_VLAN = "-1";
    private static final String HOST_ONE = HOST_ONE_MAC + "/" + HOST_ONE_VLAN;
    private static final String HOST_TWO = HOST_TWO_MAC + "/" + HOST_TWO_VLAN;
    private HostId hostOneId = HostId.hostId(HOST_ONE);
    private HostId hostTwoId = HostId.hostId(HOST_TWO);
 
    @Test
    public void testHostToHostIntentCompiler() throws Exception {
        mockHostService = EasyMock.createMock(HostService.class);
        expect(mockHostService.getHost(eq(hostOneId))).andReturn(hostOne).anyTimes();
        expect(mockHostService.getHost(eq(hostTwoId))).andReturn(hostTwo).anyTimes();
        replay(mockHostService);
 
        final HostToHostIntentCompiler compiler = new HostToHostIntentCompiler();
		compiler.hostService = mockHostService;

        final Intent intent = new HostToHostIntent(APPID, hid(oneIdString), hid(twoIdString),
                                                   selector, treatment);
 
        final List<Intent> result = compiler.compile(intent, null, null);
        assertThat(result, is(Matchers.notNullValue()));
        assertThat(result, hasSize(2));
    }
 
 
```

## Custom Mocks

Sometimes a test writer will want to implement their own complete mocked implementation of an API rather than use the mocking framework. This can be accomplished by creating a class that implements the API interface, and then implementing the methods to do whatever the test requires.

**Custom Mock Example**

```
   private static class TestIntentCompilerError implements IntentCompiler<Intent> {
        @Override
        public List<Intent> compile(Intent intent, List<Intent> installable,
                                    Set<LinkResourceAllocations> resources) {
            throw new IntentCompilationException("Compilation always fails");
        }
    }
 
    /**
     * Tests for proper behavior of installation of an intent that triggers
     * a compilation error.
     */
    @Test
    public void errorIntentCompile() {
        final TestIntentCompilerError errorCompiler = new TestIntentCompilerError();
        final IntentManager intentManager = new IntentManager();
        final IntentExtensionService extensionService = intentManager;
        final IntentService intentService = intentManager;

        extensionService.registerCompiler(MyIntent.class, errorCompiler);
        MyIntent intent = new MyIntent();
 
		// Invoke the error compiler
		intentService.submit(myIntent);
    }
```

# Hamcrest

[Hamcrest](http://hamcrest.org/JavaHamcrest/) is a powerful framework for defining matchers for data values in tests. ONOS uses version 1.3 of Hamcrest. Contributors are encouraged to learn about and use the Hamcrest framework, particularly when working with arrays and collections. Hamcrest also gives you the ability to write your own matchers, which will make your tests easier to read and easier to extend by other developers.

Here is an example of a custom Hamcrest matcher, that matches a Criterion type in a TrafficSelector object:

**Hamcrest Matcher for Criterion Type**

```
    /**
     * Hamcrest matcher to check that a selector contains a
     * Criterion with the specified type.
     */
    public static final class CriterionExistsMatcher
           extends TypeSafeMatcher<TrafficSelector> {
        private final Criterion.Type type;
        /**
         * Constructs a matcher for the given criterion type.
         *
         * @param typeValue criterion type to match
         */
        public CriterionExistsMatcher(Criterion.Type typeValue) {
            type = typeValue;
        }
        @Override
        public boolean matchesSafely(TrafficSelector selector) {
            final Set<Criterion> criteria = selector.criteria();
            return notNullValue().matches(criteria) &&
                   hasSize(1).matches(criteria) &&
                   notNullValue().matches(selector.getCriterion(type));
        }
        @Override
        public void describeTo(Description description) {
            description.appendText("a criterion with type \" ").
                    appendText(type.toString()).
                    appendText("\"");
        }
    }

    /**
     * Creates a criterion type matcher.  Returns a matcher
     * for a criterion with the given type.
     *
     * @param type type of Criterion to match
     * @return Matcher object
     */
    @Factory
    public static Matcher<TrafficSelector> hasCriterionWithType(Criterion.Type type) {
        return new CriterionExistsMatcher(type);
    }
 
   /**
     * Tests the builder functions that add specific criteria.
     */
    @Test
    public void testCriteriaCreation() {
        TrafficSelector selector;

        selector = DefaultTrafficSelector.builder()
                .matchInport(PortNumber.portNumber(11)).build();
        assertThat(selector, hasCriterionWithType(Type.IN_PORT));
    }
```

# Add library for Unit Test

If you are using a library for Unit Test other than the above, please add the library to the build path. You can modify the `lib/deps.json` file where we keep track of external libraries:

**Modify the lib/deps.json file**

```
vi lib/deps.json
```

**lib/deps.json**

```
{
 "libraries": {
・・・
,
    "TEST": [
      "[new library name]",
      "junit",
      "easymock",
      "hamcrest-all",
      "hamcrest-optional",
      "guava-testlib",
      "//utils/junit:onlab-junit"
    ],
・・・
 },


 "artifacts": {
・・・
    "jsch":"mvn:com.jcraft:jsch:0.1.53",
    "[new library name]":"mvn:[new library path]:[new library version]",
    "junit":"mvn:junit:junit:4.12",
    "junit-dep":"mvn:junit:junit:4.10",
・・・
 }
}
```

...and then run `onos-lib-gen` tool to re-generate the Bazel workspace file.

**Re-generate Bazel workspace**

```
tools/build/onos-lib-gen
```

---

[Home : Contributing to the ONOS Codebase](../contributing-to-the-onos-codebase.md)

---
