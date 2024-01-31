package exams

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"

	"github.com/gofiber/fiber/v2"

	linked_list "exams.golang/exams/linked-list"
	"exams.golang/exams/tree"
)

func Init(app *fiber.App) {
	examsApi := app.Group("/exams")
	examsApi.Get("/foo", Foo)
	examsApi.Post("/replaceSpace", ReplaceSpace)
	examsApi.Post("/reverseLinkedListToValues", ReverseLinkedListToValues)
	examsApi.Post("/buildTree", tree.BuildTree)
}

func Foo(c *fiber.Ctx) error {
	return c.SendString("foo")
}

/** Replace space in string */
func ReplaceSpace(c *fiber.Ctx) error {
	s := new(string)
	if err := c.BodyParser(s); err != nil {
		return err
	}

	re := regexp.MustCompile(`\s`)
	ret := re.ReplaceAllString(*s, "%20")

	ret2 := strings.ReplaceAll(*s, " ", "%20")

	return c.JSON(ret + "  <:>  " + ret2)
}

/** Reverse linked list to values array */
func ReverseLinkedListToValues(c *fiber.Ctx) error {
	return linked_list.ReverseLinkedListToValues(c)
}

func foo() any {
	s := "abc" + "def"
	fmt.Println(s)

	fs := fmt.Sprintf("eg: %s, %d, %f", "123", 456, 234.5)
	fmt.Println(fs)

	sArr := []string{"s1", "s2", "s2"}
	fmt.Println(strings.Join(sArr, ", "))

	r := []int32("Hello, 菩提")
	fmt.Printf("%s,%s,%s", string(r[0:5]), string(r[6:]), ".")

	defer func() {
		fmt.Printf("defered function")
	}()

	n, err := strconv.Atoi("42")
	n2, err2 := strconv.ParseInt("123", 0, 0)
	fmt.Printf("%d, %d, %s, %s", n, n2, err, err2)

	return nil
}
