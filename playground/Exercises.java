import java.io.Serializable;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.Callable;
import java.util.concurrent.FutureTask;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.Iterator;

public class Exercises implements Serializable {

  public Exercises() {
    char ch = 'a';
    Character CH = 'A';
  }

  public foo() {
    Matcher matcher;
    matcher.results();
    String s = "abc";
    Pattern p = Pattern.compile("a");
    p.matcher("abcs").find();

    List<Integer> l = new ArrayList<>();
    l.toArray();
    l.stream().map((Integer v, int i) -> {
      return v;
    });

    Map m = new HashMap<>();

    Object o = new Object();
    Thread.sleep(1000);
    o.notify();
    o.notifyAll();
    o.wait(500);

    Thread thread = new Thread(new FutureTask<>(
      new Callable<Object>() {
        @Override
        public Object call() {
          Object o = new Object();
          o.wait(1000);
          return o;
        };
      }
    ));
    // Syncronized run
    thread.run();
    // Concurrently run
    thread.start();

    synchronized (o) {
      System.out.println("s");
    }
  }

  public foo2() {
    List<Integer> list = new ArrayList<>(3);
    list.sort();

    List<Integer> list2;
    list2.clear();

    String str = "1 2 3 4 5";
    String[] nums = str.split(" ");
    Math.ceil(123.123);

    System.out.printf(str);

    Function<Object, Object> func = (String str1) -> str1;
  }

  public interface Withable {
    default void enter() {
      // ...
    }
    default void exit(Exception exc) {
      // ...
    }
    default void call() {
      Exception exc;
      this.enter();
      try {
        // ...
      } catch(Exception e) {
        exc = e;
      }
      this.exit(exc);
    }

    public static void with(Withable thing) {
      thing.call();
    }
  }
}
