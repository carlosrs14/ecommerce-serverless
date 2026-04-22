.PHONY: build build-GetOrdersFunction clean

build:
	CGO_ENABLED=0 go build -o bootstrap main.go
	cp bootstrap $(ARTIFACTS_DIR)/bootstrap

build-GetOrdersFunction:
	CGO_ENABLED=0 go build -o bootstrap main.go
	cp bootstrap $(ARTIFACTS_DIR)/bootstrap

clean:
	rm -f bootstrap