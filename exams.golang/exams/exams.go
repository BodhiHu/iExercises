package exams

import (
	"regexp"
	"strings"

	"github.com/gofiber/fiber/v2"

	linked_list "exams.golang/exams/linked-list"
)

func Init(app *fiber.App) {
	examsApi := app.Group("/exams")
	examsApi.Get("/foo", Foo)
	examsApi.Post("/replaceSpace", ReplaceSpace)
	examsApi.Post("/reverseLinkedListToValues", ReverseLinkedListToValues)
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
