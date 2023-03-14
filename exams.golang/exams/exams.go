package exams

import (
	"regexp"
	"strings"

	"github.com/gofiber/fiber/v2"
)

func Foo(c *fiber.Ctx) error {
	return c.SendString("foo")
}

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
