package playground

type Cake = struct {
	Name  string `json:name`
	Maker string `json:maker`
}

type Methods interface {
	Make() (any, error)
	Make2(ingredients *[]string, tp string)
}

const (
	_  = iota
	KB = 1 << (10 * iota)
	MB
	GB
	TB
)

func foo() {
	var a int = 10

	switch a {
	case 1:
		println("1")
		break
	default:
		println("default")
		break
	}

	switch {
	case a < 10:
		println("a < 10")
		break
	default:
		println("a >= 10")
		break
	}

	var x interface{}
	switch x.(type) {
	case nil:
		break
	case int:
		break
	default:
		break
	}
}
