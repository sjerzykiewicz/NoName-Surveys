lint:
	golangci-lint run

lint-fix:
	golangci-lint run --fix

build:
	go generate main.go
	go build -v -o bin/main main.go

run: build
	go run main.go

test:
	go test -v -count=1 ./...

tidy:
	go mod tidy

check-swagger:
	go get -u github.com/go-swagger/go-swagger/cmd/swagger

create-swagger: check-swagger
	swagger generate spec -o ./static/swagger.yaml --scan-models

swagger: create-swagger tidy # we do not need packages added by swagger (tidy or reset manually)
