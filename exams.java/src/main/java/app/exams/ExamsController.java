package app.exams;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.function.Predicate;
import java.util.stream.Stream;

import org.springframework.util.StringUtils;
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

	/** find duplicate numbers from array */
	@PostMapping(path = "/findDupNumbers")
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

	/** find if number exists in given 2D matrix:
	
	{
		"matrix": [
		  [1,   4,  7, 11, 15],
		  [2,   5,  8, 12, 19],
		  [3,   6,  9, 16, 22],
		  [10, 13, 14, 17, 24],
		  [18, 21, 23, 26, 30]
		],
		"num": 51
	}
	*/
	@PostMapping(path = "/findNumberIn2DArray")
	public Mono<Boolean> findNumberIn2DArray(@RequestBody MatrixNumerBody body) {
		for (int[] nums: body.matrix) {
			for (int n : nums) {
				if (body.num == n) {
					return Mono.just(true);
				}
			}
		}

		return Mono.just(false);
	}

	@PostMapping(path = "/string/replaceSpace")
	public Mono<String> replaceSpace(@RequestBody String s) {
		if (StringUtils.hasLength(s)) {
			s = s.replaceAll("\\s", "%20");
		}

		return Mono.just(s);
	}

	@PostMapping(path = "/array/moveZeroes")
	public Mono<int[]> moveZeroes(@RequestBody int[] nums) {
		ArrayExam.moveZeroes(nums, nums.length);
		return Mono.just(nums);
	}
}
