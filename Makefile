build:
	docker build -t "encoding-converter:latest" .

convert:
	./convert.sh $(INPUT_FILE) $(OUTPUT_FILE)