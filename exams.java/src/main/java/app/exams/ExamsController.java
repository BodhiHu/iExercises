package app.exams;

import java.util.Arrays;
import java.util.List;
import java.util.function.Predicate;
import java.util.stream.Stream;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Mono;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@RestController
@RequestMapping("/exams")
public class ExamsController {

  static Logger logger = LoggerFactory.getLogger(ExamsController.class);

	@PostMapping(path = "/find-dup-nums")
	public Mono<Integer[]> findDupNumbers(@RequestBody Integer[] nums) {
		Integer[] ret = new Integer[]{};

		if (nums != null && nums.length > 0) {
			List<Integer> numsArr = Arrays.asList(nums);
			ret = Stream.of(nums).filter(new Predicate<Integer>() {
				@Override
				public boolean test(Integer n) {
					return numsArr.indexOf(n) != numsArr.lastIndexOf(n);
				};
			}).distinct().toArray(Integer[]::new);
			logger.info("dup nums count =" + ret.length);
		}

		return Mono.just(ret);
	}
}
