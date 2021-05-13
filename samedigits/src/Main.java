
import java.lang.Math;
import java.util.*;

public class Main {

    public static void main(String[] args) {

        Map<Integer, Boolean> testValues = new HashMap<Integer, Boolean>();

        testValues.put(1, true);
        testValues.put(10, true);
        testValues.put(251894, true);
        testValues.put(251895, false);

        for (Map.Entry<Integer, Boolean> entry: testValues.entrySet()) {
            var result = n3SameDigits(entry.getKey());

            if (result != entry.getValue())
                System.out.println(String.format("Got incorrect result for:%s", entry.getKey()));
        }

    }

    private static boolean n3SameDigits(int number) {
        final var EXPONENT = 3;

        var powerString =  String.valueOf((long)Math.pow(number, EXPONENT));
        Set<String> powerSet = new HashSet<>();
        powerSet.addAll(Arrays.asList(powerString.split("")));

        Set<String> inputSet = new HashSet<>();
        inputSet.addAll(Arrays.asList(String.valueOf(number).split("")));


        return powerSet.equals(inputSet);

    }
}
