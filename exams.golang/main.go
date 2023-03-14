package main

import (
	"log"

	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/middleware/cors"
	"github.com/gofiber/fiber/v2/middleware/recover"

	"exams.golang/exams"
)

func main() {
	app := fiber.New()
	app.Use(cors.New())
	app.Use(recover.New())

	app.Get("/", func(c *fiber.Ctx) error {
		return c.SendString("Hello, World!")
	})

	// API /exams ------------------------------------
	examsApi := app.Group("/exams")
	examsApi.Get("/foo", exams.Foo)
	examsApi.Post("replaceSpace", exams.ReplaceSpace)

	log.Fatal(app.Listen(":3000"))
}
