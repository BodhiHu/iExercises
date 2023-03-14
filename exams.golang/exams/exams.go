package exams

import "github.com/gofiber/fiber/v2"

func Foo(c *fiber.Ctx) error {
	return c.SendString("foo")
}

func ReplaceSpace(c *fiber.Ctx) error {
	s := new(string)
	if err := c.BodyParser(s); err != nil {
		return err
	}

	return c.JSON(s)
}
